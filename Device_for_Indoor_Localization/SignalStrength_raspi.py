import subprocess
import serial
p = serial.Serial("/dev/serial0",9600,timeout=0.5)

while 1:
  with open("output.txt" , "w+") as output:
    subprocess.call(["python", "./xx.py"], stdout = output);

  with open('output.txt', 'r') as f:
    content = f.read()
    s = content.index('E2:DD:C0:F2:BE:E1')
    a  = content[s+67:s+69]
    print (a)
    if int(a) > 15 and int(a) < 35:
        print ("send a")
        p.write(str.encode('a'))
    elif int(a) > 35 and int(a) < 50:
        print ("send b")
        p.write(str.encode('b'))
    else:
        print ("send c")
        p.write(str.encode('c'))
