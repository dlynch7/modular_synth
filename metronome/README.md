# Metronome
---
## Inputs
None

## Outputs
Clock CV xN (4?)

## User interface
* Rotary encoder
* 8x LED (display tempo in binary)
* 4x LED (display BPM multiplier in binary, w/ offset of 1)
* Toggle switch (toggle between set-tempo and set-multiplier)

## How it works
* User turns rotary encoder to set tempo (BPM) and BPM multiplier (1 = quarter note, 4 = 16th note, etc), LEDs display tempo and multiplier
* Clock CV is a square wave oscillating between 0 V and 5 V.
* Other modules can be set to trigger on rising or falling clock edge
* Multiple clock CV outputs, but how many?
