#Math Library is used for the calculation to improve productivity 
import math

#Pass temperature in celcius and this function will return the value in Farenhit 
def toFarenhit(a):
    return (1.8*a)+32

#pass total fule consumptions in gallon as first parameter
#pass total miles driven as second parameter
def calculateMpg(gallons, miles):
    return miles/gallons

#pass radius as parameter while calling the function
def calculateAreaOfCircle(r):
    pie=3.14
    area=pie*r*r
    return area

def calculateDistanceBetweenPoints(x,y,x1,y1):
      totalDistance=math.sqrt((x1-x)**2+(y1-y)**2)
      return totalDistance


