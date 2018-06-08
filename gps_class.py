import serial
import binascii
import re

class gps_info_get:

    #初期処理
    #def __init__(self,root):
    #    self.root = root
        
    def get_gps_info(self):
        
        pattern = r"\$GPRMC"
        num=0
        no_output = True
        #while num < 20:
        while no_output: 
            ser = serial.Serial('/dev/ttyUSB0',4800,timeout=20)
            line = ser.readline().decode('utf-8','replace')

            match_res = re.match(pattern,line)
            if match_res:
                #print(re.sub(r'\r\n','',line))
                return re.sub(r'\r\n','',line)
                no_output = False
            #print(line)
            num += 1
        ser.close()
