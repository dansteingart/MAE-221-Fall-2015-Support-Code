from commands import getoutput as go
import json
import time


class motorPhoton():
    def __init__(self,name=None):
        self.particle = name
        self.ac = open("/home/labroot/ac").read().strip()

    
    def getNames(self):
        return go('curl -s https://api.particle.io/v1/devices?access_token=%s' % self.ac)


    def setMotor(self,motor,mode,pwm):
        out = str(motor)+str(mode)+str(pwm).rjust(3,"0")
        return go('curl -s https://api.particle.io/v1/devices/%s/setMotor \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,out))

    def getData(self):
        data = go("curl -s -G https://api.spark.io/v1/devices/%s/lab2_data -d access_token=%s" % (self.particle,self.ac))
        data = json.loads(data)
        st = data['result']
        data['result'] =  json.loads(st)
        data['result']['time'] = time.time()
        return data['result']


if __name__ == "__main__":
    b = motorPhoton("FearlessFearow")
    print b.setMotor(0,0,55)
    time.sleep(1)
    a = b.getData()
    keys = a.keys()
    keys.sort()
    for k in keys: print k,":",a[k]
