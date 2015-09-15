from commands import getoutput as go
import json
import time


class simplePhoton():
    def __init__(self,name):
        self.particle = name
        self.ac = open("/home/labroot/ac").read()

    def setOutput(self,bit,value):
        return go('curl -s https://api.particle.io/v1/devices/%s/setOutput \
         -d access_token=%s \
         -d "args=%i%i"' % (self.particle,self.ac,bit,value))


    def setOutputs(self,arr):
        if len(arr) != 4:
            return "need exactly four bits"
        else:
            value = ""
            for a in arr: value += str(a)
            return go('curl -s https://api.particle.io/v1/devices/%s/setOutputs \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,value))

    def getData(self):
        data = go("curl -s -G https://api.spark.io/v1/devices/%s/lab_data -d access_token=%s" % (self.particle,self.ac))
        data = json.loads(data)
        st = data['result']
        data['result'] =  json.loads(st)
        data['result']['time'] = time.time()
        return data['result']


if __name__ == "__main__":
    b = simplePhoton('surly_spike')
    #b.setOutput(0,0)
    #b.setOutput(2,0)
    print b.setOutputs([0,0,0,0])
    a = b.getData()
    print a
