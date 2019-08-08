# Sequencer
---

## Inputs
* Metronome clock

## Outputs
1. Pitch CV
2. Velocity CV
3. Gate
4. Trigger

## User interface
* 16x2 LCD screen
* Rotary encoder
* 2x momentary pushbutton
* 2x LEDs (one per pushbutton)
* Power switch
* Power LED

## How it works
### Array representation of a sequence
A "sequence" is simply an array of pitch, velocity, and duration information.
For example, a 64-note sequence might look like this

```
uint8_t sequence[64][3] = {
    {0, 127, 256},
    {1, 63, 256},
    {2, 127, 127},
    {3, 63, 127},
    ...
    };
```
The first column represents pitch, the second column represents velocity, and the third column represents duration (256 means the note sustains until the next note, 127 means the note sustains for half that time, etc.).

To compose a sequence, the user needs to enter the pitch, velocity, and duration for each note as well as the sequence length (total number of notes in the sequence).

### Stepping through a sequence
On each tick from the metronome clock input, the sequencer advances to the next step, wrapping around to the beginning after reaching the user-defined sequence length.
Pitch and velocity will be sent to a dual-DAC, and duration will be converted into digital gate and trigger signals.

### Storing a sequence
The user should have the option to store a sequence in flash memory so it can be retrieved later.

### Erasing the current sequence
The user should be able to erase the current sequence, in which case the `sequence` array is reset to some default.
