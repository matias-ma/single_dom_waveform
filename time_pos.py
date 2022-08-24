# python3

# This script gets the time and position of each of the two cascades in an HNL event

from icecube import icetray,dataio,dataclasses, simclasses, recclasses
import os

if os.path.exists('/home/mandia/waveform/wf/time') is True: 
    os.system('rm -r /home/mandia/waveform/wf/time')
    os.mkdir('/home/mandia/waveform/wf/time')

else:
    os.mkdir('/home/mandia/waveform/wf/time')

os.mkdir('/home/mandia/waveform/wf/time/not_important')

if os.path.exists('/home/mandia/waveform/wf/pos') is True: 
    os.system('rm -r /home/mandia/waveform/wf/pos')
    os.mkdir('/home/mandia/waveform/wf/pos')

else:
    os.mkdir('/home/mandia/waveform/wf/pos')

os.mkdir('/home/mandia/waveform/wf/pos/not_important')

for i in range(1,10):

    for x in range(1,25):
        f = dataio.I3File('/data/ana/BSM/HNL/MC/190607/Ares/IC86.AVG/Det/domeff_0.97/00001-01000/Det_00_11_0000'+str(i)+'.i3.zst')
        for q in range(x):
            frame = f.pop_daq()
        tree = frame['I3MCTree']

        # time

        bad_words = 'MajorID', 'MinorID', 'Azimuth', 'Zenith', 'Energy', 'Length', 'Type', 'PDG', 'Speed', 'Shape','Status','Location',']', 'X','Y','Z'

        with open('/home/mandia/waveform/wf/time/not_important/time'+str(i)+'_'+str(x)+'.txt', 'a+') as f:
                for line in tree:
                    f.write(str(line))
                    f.write('\n')
        
        with open('/home/mandia/waveform/wf/time/not_important/time'+str(i)+'_'+str(x)+'.txt', 'r+') as f:
                for line in tree:
                    f.write(str(line))
                    f.write('\n')

        in_t = open('/home/mandia/waveform/wf/time/not_important/time'+str(i)+'_'+str(x)+'.txt', 'r+')
        new_t = open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'a+')
        

        for line in in_t:
            if not any(bad_word in line for bad_word in bad_words):
                new_t.write(line)
        
        # position
        
        more_bad_words = 'MajorID', 'MinorID', 'Azimuth', 'Zenith', 'Energy', 'Length', 'Type', 'PDG', 'Speed', 'Shape','Status','Location',']', 'Time'

        with open('/home/mandia/waveform/wf/pos/not_important/pos'+str(i)+'_'+str(x)+'.txt', 'a+') as f:
                for line in tree:
                    f.write(str(line))
                    f.write('\n')
        
        with open('/home/mandia/waveform/wf/pos/not_important/pos'+str(i)+'_'+str(x)+'.txt', 'r+') as f:
                for line in tree:
                    f.write(str(line))
                    f.write('\n')

        in_p = open('/home/mandia/waveform/wf/pos/not_important/pos'+str(i)+'_'+str(x)+'.txt', 'r+')
        new_p = open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'a+')
        

        for line in in_p:
            if not any(more_bad_word in line for more_bad_word in more_bad_words):
                new_p.write(line)
       




        
