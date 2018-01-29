import time
import datetime

timer = int(input("please input the amount of minutes you'd like to set the timer to: "))
var = 0
seconds = 0
print(" _____________")
print("| Timer start |")
print(" _____________")
while var < timer:
    StartNew = str(datetime.datetime.now().time())
    HourNew = str(StartNew[0:2])
    MinuteNew = str(StartNew[3:5])
    print("|  ",HourNew,":",MinuteNew,"  |")
    time.sleep(60)
    seconds = seconds + 60
    var = var + 1
print(" _____________")
print ("|  Time's UP! |")
print(" _____________")
print ("| Total time  |")
print ("| in seconds: |")
print ("|    ",seconds,"    |")
print(" _____________")