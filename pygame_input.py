import pygame
import pygame.midi
from pygame.locals import *
import time
#from giantwin32 import *

pygame.init()

size = (1500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

gitImg = pygame.image.load('guitar.png')

def guitar(x,y):
    screen.blit(gitImg, (x,y))

# string positions for each string
stringPos = {1: 35, 2: 80 , 3 : 125, 4 : 170, 5: 215, 6 : 260}
# positions for each fret
fretPos = {0 : 20, 1:100, 2: 205, 3 : 305, 4 : 400, 5 : 485, 6 : 570, 7 : 650, 8 : 723, 9 : 790, 10 : 855, \
           11: 920, 12: 978, 13: 1033, 14: 1081 , 15: 1132, 16: 1180, 17: 1225, 18: 1266, 19: 1305,\
           20 : 1343, 21 : 1378, 22 : 1413}



pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()


print (pygame.midi.get_default_output_id())
print (pygame.midi.get_device_info(0))
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input(input_id)



print("starting")

going = True
rate = 0.001

while going:

    #screen.fill(BLACK)
    guitar(0, 0)

    events = event_get()
    for e in events:
        if e.type in [QUIT]:
            going = False
        if e.type in [KEYDOWN]:
            going = False

    if i.poll():
        midi_events = i.read(10)
        print(str(midi_events[0][0]))
        if (midi_events[0][0][0] == 144):
            print("midi channel 1")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note-64], stringPos[1]), 12, 0)
            rate = 0.05
        if (midi_events[0][0][0] == 145):
            print("midi channel 2")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note-59], stringPos[2]), 12, 0)
            rate = 0.05
        if (midi_events[0][0][0] == 146):
            print("midi channel 3")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note -55], stringPos[3]), 12, 0)
            rate = 0.05
        if (midi_events[0][0][0] == 147):
            print("midi channel 4")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note - 50], stringPos[4]), 12, 0)
            rate = 0.05
        if (midi_events[0][0][0] == 148):
            print("midi channel 5")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note - 45], stringPos[5]), 12, 0)
            rate = 0.05
        if (midi_events[0][0][0] == 149):
            print("midi channel 6")
            print(str(midi_events[0][0][1]))
            note = midi_events[0][0][1]
            pygame.draw.circle(screen, (255, 255, 0), (fretPos[note - 40], stringPos[6]), 12, 0)
            rate = 0.05


        #if int(midi_events[0][0][0]) in [224, 225, 226]:  # Pitch Bender
            #print(str(midi_events[0][0][2]) ) # right(0)  center(64)  left(124)

        # print "full midi_events " + str(midi_events)
        # print "my midi note is " + str(midi_events[0][0][1])
        # convert them into pygame events.
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
        pygame.display.flip()
        time.sleep(rate)






        for m_e in midi_evs:
            event_post(m_e)

print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()
"""
reads num_events midi events from the buffer.
Input.read(num_events): return midi_event_list
Reads from the Input buffer and gives back midi events. [[[status,data1,data2,data3],timestamp],
 [[status,data1,data2,data3],timestamp],...]
"""