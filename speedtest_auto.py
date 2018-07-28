
# coding: utf-8

# In[34]:


import os
import re
import subprocess
import time
import csv

"""
I changed original script. These are the following changes:
set shell=False from shell=true
error when using re.findall 'can't use a string pattern on a bytes-like object'.Placed 'b' in front of strings to convert
used .decode('utf-8') instead of .replace because of error. Seems to produce same result.
I removed the newline parameter from open, and I started to get an extra blank row when run. I replaced
it, and now it works correctly. What does newline = '' do?

"""


filename = 'speedtest.csv'
dir_path = 'C:/Users/AJ/Documents/speedtest/speedtest_results/'
csv_path = dir_path + filename

def speed_test():

    response = subprocess.Popen('speedtest-cli --simple', shell=False, stdout=subprocess.PIPE).stdout.read()
    
    ping = re.findall(b'Ping:\s(.*?)\s', response, re.MULTILINE)
    download = re.findall(b'Download:\s(.*?)\s', response, re.MULTILINE)
    upload = re.findall(b'Upload:\s(.*?)\s', response, re.MULTILINE)
    
    ping[0] = ping[0].decode('utf-8')
    download[0] = download[0].decode('utf-8')
    upload[0] = upload[0].decode('utf-8')
    
    csv_entry(ping[0], download[0], upload[0], csv_path)
    

def csv_entry(lat_st, down_st, up_st, path):

    result = time.strftime('%m/%d/%y'), time.strftime('%H:%M'), lat_st, down_st, up_st
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    with open(path, "a", newline = '') as csv_file:        
        writer = csv.writer(csv_file)
        
        if os.stat(csv_path).st_size == 0:
            writer.writerow(['Date','Time','Latency(ms)','Down(Mbit/s)','Up(Mbit/s)'])        
        
        writer.writerow(result)

            

            
speed_test()

