import numpy,math

class distance2points:
    def exchange(self,lati1,lati2,long1,long2):
        print("lati1:["+str(lati1)+"]lati2:["+str(lati2)+"]long1:["+str(long1)+"]long2:["+str(long2)+"]")
        
        rad_lati1 = numpy.deg2rad(lati1)
        rad_lati2 = numpy.deg2rad(lati2)
        rad_long1 = numpy.deg2rad(long1)
        rad_long2 = numpy.deg2rad(long2)
        
        r = 6378137.0; #赤道半径
        averageLat = (rad_lati1 - rad_lati2) / 2;
        averageLon = (rad_long1 - rad_long2) / 2;
        return r * 2 * math.asin(math.sqrt(math.pow(math.sin(averageLat), 2) + math.cos(rad_lati1) * math.cos(rad_lati2) * math.pow(math.sin(averageLon), 2)));
        #return "lati1:["+lati1+"]lati2:["+lati2+"]long1:["+long1+"]long2:["+long2+"]"
        