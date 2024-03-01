import ArmAngles, time
import paho.mqtt.publish as mqttPub

offset = 1

prefab1 = [
    [0,0,0],
    [0,0,180],
    [6,-2,180],
    [0,0,180],
    [0,0,0],
]
prefab2 = [
    [0,0,0],
    [0,0,45],
    [6,-2,45],
    [0,0,45],
    [0,0,135],
    [6,-2,135],
    [0,0,135],
    [0,0,0],
]
prefab3 = [
    [0,0,0],
    [0,0,45],
    [6,-2,45],
    [0,0,45],
    [1,10,0],
    [1,10,0],
    [1,10,0],
    [0,0,0],
]
prefab4 = [
    [0,0,0],
    [1,0,0],
    [2,0,0],
    [3,0,0],
    [4,0,0],
    [5,0,0],
    [6,0,0],
    [7,0,0],
    [8,0,0],
    [9,0,0],
    [10,0,0],
    [11,0,0],
    [0,0,0],
]
prefab5 = [
    [0,0,0],
    [1,1,0],
    [2,2,0],
    [3,3,0],
    [4,4,0],
    [5,5,0],
    [6,6,0],
    [7,7,0],
    [8,8,0],
    [9,9,0],
    [10,10,0],
    [11,11,0],
    [0,0,0],
]

prefabs = [prefab1,prefab2,prefab3,prefab4,prefab5]

def publish(payload):
    mqttPub.single(topic="ESP32/Arm", payload=payload, hostname="192.168.137.221")

while True:
    prefabChosen = int(input())-1

    prefab = prefabs[prefabChosen]

    for item in prefab:
        x = item[0]
        y = item[1]
        z = item[2]

        arm1Len = 6
        arm2Len = 6

        angles = ArmAngles.getAngles(armLenA=arm1Len, armLenB=arm2Len, targetPos=[x,y+offset])
        print(f"{angles[1]} {180-angles[0]} {z}")
        publish(f"{angles[1]} {180-angles[0]} {z}")
        time.sleep(1)