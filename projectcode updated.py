import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "9i3akk",
        "typeId": "ESP32",
        "deviceId":"27045"
    },
    "auth": {
        "token": "Royal@2704"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data)
    m=cmd.data
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(200,300)
    liters=random.randint(0,5000)
    myData={'lubrication level is':level, 'lubrication in liters':liters}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully to ibm iot : %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
    if(level<210):
       mydata={'lubrication level is low':level}
       client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
       print("Published data Successfully to ibm iot : %s", mydata)
       time.sleep(2)
       client.commandCallback = myCommandCallback
client.disconnect()
