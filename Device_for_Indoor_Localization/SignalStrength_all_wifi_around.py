import os
os.system('sudo iwlist wlan0 scan | egrep "Cell|ESSID|Signal|Rates"')
'''import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = orig_stdout
f.close'''