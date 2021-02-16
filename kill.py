import os
procname = "strandtest.py" # Ur procces name
os.system('pgrep -f '+procname+' > ./txt/kled.txt') # Need a dir «txt» next to your script
f = open('./txt/kled.txt', 'r') # Open temp file
text = str(f.readline()) # read first line of txt
os.system('sudo kill '+text) # Kill process.
print('LED Controller - отключён') # Debug message
