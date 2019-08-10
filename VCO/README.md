# Digital VCO
---

## Inputs
* Pitch CV
* Sync CV
* PWM CV

## Outputs
* Signal out

## User interface
* Pitch knob
* Pulse width knob
* Rotary selector switch - waveform select

## How it works
* Core: DDS (maybe [AD9833](https://www.analog.com/media/en/technical-documentation/data-sheets/AD9833.pdf)): generates sine, triangle, and square waves. [Here](https://www.allaboutcircuits.com/projects/how-to-DIY-waveform-generator-analog-devices-ad9833-ATmega328p/) is an example project.
* Can implement ramp wave with square wave and integrator
* Can implement PWM with ramp wave and a comparator
* [Achieving hard sync with the AD9833](https://www.muffwiggler.com/forum/viewtopic.php?p=2815552#2815552)
