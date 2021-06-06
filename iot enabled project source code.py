import wiotp.sdk.device
import time
import random


myConfig = { 
    "identity": {
        "orgId": "gbyafd",
        "typeId": "esp32",
        "deviceId":"1208"
    },
    "auth": {
        "token": "akashsg2001"
    }
}



def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data)
    m=cmd.data
   

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

   

while True:
    level=random.randint(200,800)
    lubrication=random.randint(0,5000)
    myData={'level':level, 'lubrication':lubrication}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)

client.disconnect()
