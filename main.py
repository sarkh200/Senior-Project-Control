import ArmAngles
import paho.mqtt.publish as mqttPub




def publish(payload):
    mqttPub.single(topic="ESP32/Arm", payload=payload, hostname="192.168.1.17")
    
while True:
    x = float(input())
    y = float(input())
    z = float(input())
    arm1Len = 6
    arm2Len = 6

    a = (x,y)
    angles = ArmAngles.getAngles(armLenA=arm1Len, armLenB=arm2Len, targetPos=[x,y])
    print(f"{angles[1]} {180-angles[0]} {z}")
    publish(f"{angles[1]} {180-angles[0]} {z}")