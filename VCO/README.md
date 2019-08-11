# Digital VCO
---

## Inputs
* 1V/octave pitch CV
* Sync CV
* PWM CV

## Outputs
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
Analog VCOs require a circuit to convert 1V/octave pitch CV signals to exponential voltages, but because this VCO has a digital core, the linear-to-exponential conversion can be done in software.

TODO: determine whether this conversion should be done with math or with a lookup table.

On the flip side, because this VCO has a digital core, it requires an ADC to process the 1V/octave pitch CV signal, and the resolution of the ADC is critical.
I wrote a [simple Python script](/math/calculate_ADC_resolution.py) to calculate the resolution in cents per ADC count, given the input volgate range and resolution in bits.

| Input range (V)   | Resolution (bits) | Resolution (cents/count)  |
| --------------    | ----------        | -------------             |
| 3.3               | 8                 | 15.47                     |
|                   | 10                | 3.87                      |
|                   | 12                | 0.97                      |
|                   | 14                | 0.24                      |
|                   | 16                | 0.06                      |
| 5.0               | 8                 | 23.44                     |
|                   | 10                | 5.86                      |
|                   | 12                | 1.46                      |
|                   | 14                | 0.36                      |
|                   | 16                | 0.09                      |
| 12.0              | 8                 | 56.25                     |
|                   | 10                | 14.06                     |
|                   | 12                | 3.52                      |
|                   | 14                | 0.88                      |
|                   | 16                | 0.22                      |
