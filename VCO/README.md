# Digital VCO
---

## Inputs
* Pitch CV
* Sync CV
* PWM CV

## Outputs
* Signal out

## User interface
* 16x2 LCD display (w/ backlight) - use an MCP23008 "backpack" to conserve MCU pins
* Rotary encoder


## How it works
* Core: DDS (maybe [AD9833](https://www.analog.com/media/en/technical-documentation/data-sheets/AD9833.pdf)): generates sine, ramp, and square waves
* Can implement PWM with ramp wave and a comparator
* [Achieving hard sync with the AD9833](https://www.muffwiggler.com/forum/viewtopic.php?p=2815552#2815552)
