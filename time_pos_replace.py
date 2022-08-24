# python3

import os 
from ast import literal_eval
import pandas as pd
import numpy as np

for i in range(1,10):
    for x in range(1,25):
        # time

        with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'r') as file:
            t_data = file.read()
            t_data = t_data.replace('                Time : ', '')
            # t_data = t_data.replace('\n', ',')
        with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'w') as file:
            file.write(t_data)
        with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()
        
        time = open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'r+')
        t = np.array([])
        for line in time:
            line = line.strip()

            t = np.append(t,float(line))

        t = np.unique(t)
        try:
            t = np.reshape(t, (1,2))
            with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'w') as file:
                file.write(str(t))
            
            with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'r') as file:
                t_data = file.read()
                t_data = t_data.replace('[ ', '')
                t_data = t_data.replace('[', '')
                t_data = t_data.replace(']', '')
                t_data = t_data.replace('  ', ' ')
                # t_data = t_data.replace('[ ', '')
                # t_data = t_data.replace(' ]', '')
                # t_data = t_data.replace(' ', ',')
                # t_data = t_data.replace(',,', ',')

            with open('/home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt', 'w') as file:
                file.write(t_data)
            
        except:
            with open('/home/mandia/waveform/wf/time/many_body'+str(i)+'_'+str(x)+'.txt','a+') as file:
                file.write(str(t))

            with open('/home/mandia/waveform/wf/time/many_body'+str(i)+'_'+str(x)+'.txt','r') as file:
                t_data = file.read()
                t_data = t_data.replace('[ ', '')
                t_data = t_data.replace('[', '')
                t_data = t_data.replace(']', '')
                t_data = t_data.replace('  ', ' ')
                # t_data = t_data.replace('[ ', '')
                # t_data = t_data.replace(' ]', '')
                # t_data = t_data.replace(' ', ',')
                # t_data = t_data.replace(',,', ',')  
            with open('/home/mandia/waveform/wf/time/many_body'+str(i)+'_'+str(x)+'.txt','w') as file:
                file.write(t_data)
            os.system('rm /home/mandia/waveform/wf/time/time'+str(i)+'_'+str(x)+'.txt')
            
            
        # position
        with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'r') as file:
            p_data = file.read()
            p_data = p_data.replace('                   X : ', '')   
            p_data = p_data.replace('                   Y : ', '')
            p_data = p_data.replace('                   Z : ', '')
            # p_data = p_data.replace('\n', ',')
        with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'w') as file:
            file.write(p_data)
        with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()
        
        pos = open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'r+')
        p = np.array([])
        for line in pos:
            line = line.strip()
            p = np.append(p,float(line))
        # p = np.reshape(p, (int(len(pos.readlines())/3),3))
        
        
        _, idx = np.unique(p, return_index=True)
        p = p[np.sort(idx)]
        try:
            p = np.reshape(p, (2,3))
            with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'w') as file:
                file.write(str(p))
            with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'r') as file:
                p_data = file.read()
                p_data = p_data.replace('[ ', '')
                p_data = p_data.replace('[', '')
                p_data = p_data.replace(']', '')
                p_data = p_data.replace('  ', ' ')
                # p_data = p_data.replace('  ', ',')
                # p_data = p_data.replace(' ', ',')
            with open('/home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt', 'w') as file:
                file.write(p_data)

        except:
            try:
                p = np.reshape(p, (-1,3))
                with open('/home/mandia/waveform/wf/pos/many_body'+str(i)+'_'+str(x)+'.txt','a+') as file:
                    file.write(str(p))
                with open('/home/mandia/waveform/wf/pos/many_body'+str(i)+'_'+str(x)+'.txt', 'r') as file:
                    p_data = file.read()
                    p_data = p_data.replace('[', '')
                    p_data = p_data.replace(']', '')
                    # p_data = p_data.replace(' ', ',')
                with open('/home/mandia/waveform/wf/pos/many_body'+str(i)+'_'+str(x)+'.txt', 'w') as file:
                    file.write(p_data)
                os.system('rm /home/mandia/waveform/wf/pos/pos'+str(i)+'_'+str(x)+'.txt')
                
            except:
                pass
        
            
        
        



        

                


        