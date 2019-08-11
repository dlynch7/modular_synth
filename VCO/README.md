# Digital VCO
---

## Inputs
* 1V/octave pitch CV
* Sync CV
* PWM CV

## Outputs
Waveform select switch (see User Interface) to choose between:
* Sine out
* Square out
* Triangle out
* Ramp out

## User interface
* Tune knobs (coarse and fine)
* Pulse width knob
* Waveform select switch (w/ LEDs?)

## How it works
### Function generator
* Core: digital sine wave generator (maybe [AD9833](https://www.analog.com/media/en/technical-documentation/data-sheets/AD9833.pdf)): generates sine, triangle, and square waves. [Here](https://www.allaboutcircuits.com/projects/how-to-DIY-waveform-generator-analog-devices-ad9833-ATmega328p/) is an example project.
* [Example](https://www.edn.com/design/test-and-measurement/4333929/DDS-device-produces-sawtooth-waveform) of two DDS chips working together to create a sawtooth wave
* Can implement PWM directly with the PIC, using a timer and an output compare module.
* [A cool DDS-based function generator by Herptronix](https://github.com/herptronix/tiny-DDS)
* [Achieving hard sync with the AD9833](https://www.muffwiggler.com/forum/viewtopic.php?p=2815552#2815552)

### 1V/octave pitch CV
The more-or-less-agreed-upon standard for pitch CV is 1V per octave.
With 12 semitones per octave, this standard results in 0.083333 V or 83.333 mV per semitone.

Analog VCOs require a circuit to convert 1V/octave pitch CV signals to exponential voltages, but because this VCO has a digital core, the linear-to-exponential conversion can be done in software (TODO: determine whether this conversion should be done with math or with a lookup table).

On the flip side, because this VCO has a digital core, it requires an ADC to process the 1V/octave pitch CV signal, and the resolution of the ADC is critical.
I wrote a [simple Python script](/VCO/math/calculate_ADC_resolution.py) to calculate the resolution in cents per ADC count, given a 0-12V pitch CV signal and the ADC's input range (V) and resolution (bits)

| Resolution (bits) | Resolution (cents/count)  |
| ----------        | -------------             |
| 8                 | 56.25                     |
| 10                | 14.06                     |
| 12                | 3.52                      |
| 14                | 0.88                      |
| 16                | 0.22                      |

If I'm using an ADC with a small input range (3.3V or 5V for example), I need a way to scale down the 1V/octave CV signal so it fits in that input range.
My naive approach is to use a voltage divider (followed by a unity gain buffer):
* 12 V to 3.3 V: gain of 0.2750
* 12 V to 5 V:   gain of 0.4167

Yet another problem to consider is noise: there's no point using a 16-bit ADC instead of a 12-bit ADC when the extra resolution only serves to convert noise on the 1V/octact CV input.

At the moment I'm considering [the MCP3201, a 12-bit ADC from Microchip](http://ww1.microchip.com/downloads/en/DeviceDoc/21290F.pdf), setting `V_REF` = 5 V.
[The MAX1416, a 16-bit ADC from Maxim Integrated](https://datasheets.maximintegrated.com/en/ds/MAX1415-MAX1416.pdf) is a higher-resolution (and higher-cost) alternative;
it also has a much lower samping rate compared to the MCP3201: 500 samples per second versus 100 ksps.
On the other hand, the MAX1416 has a differential input, whereas the MCP3201 only has a pseudo-differential input.
