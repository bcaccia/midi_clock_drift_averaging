# midi_clock_drift_averaging
Measures the amount of drift in a MIDI arp or MIDI clock over a period of events.

## Dependencies

The following dependencies must be installed using `pip install` for midi-blaster to run.

* pygame

## Usage:

To launch the application:
`python midi_clock_drift_averaging.py`

1. Choose your MIDI input. 
1. Enter the number of MIDI events that you want to analyze.
1. Start the arpeggiator or clock on your device. Send Note On's at 1/4 resolution, 120bpm
1. Press Enter. Once the amount of MIDI events have been received, an average is displayed. 

## Known Issues:

* Robust exception handling has not yet been implemented. You can crash it.
* It's difficult to get pygame to install on a Mac. If you get it installed, you'll run into crashes when attempting to load MIDI data from an external file. 
* There is no graceful way to abort sending MIDI other than to force quit the app or quit the console.