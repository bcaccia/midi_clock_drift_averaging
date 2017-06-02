#Author: Benjamin Caccia
#Year: 2014
#Listed below are common averages for stable products. The samples were taken
#by sending Note On's at 1/4 resolution, 120bpm. These are averaged from 1000 midi events.
#Max 25 - 0.503ms
#MPK 225 - 0.499ms
#Trigger Finger Pro - 0.291ms
#Rhythm Wolf - 0.499ms

import sys, pygame, pygame.midi
 
# set up pygame
pygame.init()
pygame.midi.init()
 
# list all midi devices
for x in range( 0, pygame.midi.get_count() ):
		print x + 1, pygame.midi.get_device_info(x)[1:]

		
# get user input and make it match the printed list by subtracting from the user entered value.		
midiInput = int(raw_input('\nChoose your MIDI input: '))
midiInput = midiInput - 1
 
# open a specific midi device
inp = pygame.midi.Input(midiInput)

# get user input for amount of MIDI to receive before calculating results.
testSamples = int(raw_input('\nEnter the amount of MIDI note on samples you want to analyze: '))

newMIDI = []
allMIDI = []
i = 0
# run the event loop
while i < testSamples:
    if inp.poll():
         # no way to find number of messages in queue
         # so we just specify a high max value
        newMIDI.append(inp.read(1000))
		
	
	# checks to see if the incoming MIDI value is equal to 144 DEC. If so, it will be appended to the MIDI list.
	if newMIDI[0][0][0][0] == 144 or newMIDI[0][0][0][0] == 154:
		allMIDI.append(newMIDI)
		
		#pulls timestamp from incoming MIDI data	
		#print "First timestamp: ", allMIDI[0][0][1]
		print "Number of MIDI events analyzed: ",len(allMIDI)
		
		
		#This is only hear to debug and see what MIDI is being captured. Leave commented out.
		#print newMIDI[0][0]
		#print newMIDI[0][0][1]
		#stop = raw_input()
		
		# wait 10ms - this is arbitrary, but wait(0) still resulted
		# in 100% cpu utilization
		i += 1 
		pygame.time.wait(10)
		#resets container for MIDI.
		newMIDI = []

	else:
		#resets container for MIDI.
		newMIDI = []
	


#slices and separates the time stamps
tally = []
count = 0
holding = []
e = 0

#This is only hear to debug and see what MIDI is being captured. Leave commented out.
#print allMIDI[0][0][0][1]
#stop = raw_input()

for e in range(len(allMIDI)):
	tally.append(allMIDI[e][0][0][1])
	
	

count = len(tally) - 2


	
total = []
t = 0	
while t < count:
	holding = tally[t+1] - tally[t]
	total.append(holding)
	t += 1

#converts to milliseconds	
final_sum = sum(total) / len(total)
final_sum_adjusted = float(final_sum) / 1000
print "The average is: ", final_sum_adjusted, "ms"
nothing = raw_input('')

	
#keeps the bad pointer exception from being raised
del inp
pygame.midi.quit()
