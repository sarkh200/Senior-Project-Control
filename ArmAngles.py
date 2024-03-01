import math as __math

def getAngles(armLenA, armLenB, targetPos):
    ogTargetX = targetPos[0]
    targetPos[0] = abs(targetPos[0])
    armLenC = __math.sqrt(targetPos[0]**2 + targetPos[1]**2)
    try:
        angleC = round(__math.degrees(__math.acos((armLenA**2+armLenB**2-armLenC**2)/(2*armLenA*armLenB))),2)
        #angleB = round(degrees(acos((armLenA**2+armLenC**2-armLenB**2)/(2*armLenA*armLenC))),2) #not used, but could be useful
        angleA = round(__math.degrees(__math.acos((armLenC**2+armLenB**2-armLenA**2)/(2*armLenC*armLenB))),2)

        angleD = round(__math.degrees(__math.acos((armLenC**2+targetPos[0]**2-targetPos[1]**2)/(2*targetPos[0]*armLenC))),2)
        
        if(targetPos[1] < 0):
            angleAD = angleA - angleD
        else:
            angleAD = angleA + angleD
        
    except ValueError as error:
        print(f"Value Error: {error}. Target position likely out of reach for the arm.")
        print("Will attempt to get arm as close as possible")
        targetPos[0] = ogTargetX
        if(targetPos[0] < 0):
            return [180+round(__math.degrees(__math.atan(targetPos[1]/targetPos[0])),2), 180]
        else:
            return [round(__math.degrees(__math.atan(targetPos[1]/targetPos[0])),2), 180]
    except ZeroDivisionError as error:
        return [180, 0]
    if(ogTargetX < 0):
        return[180-angleAD, 360-angleC]
    else:
        return [angleAD, angleC]