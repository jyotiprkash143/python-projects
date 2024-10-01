import  random as r
from time import *
#creating a function to calculate errors
def error(test,usertest):
    error=0
    for i in range(len(test)):
        try:
            if test[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
#creating fumction for time speed....
def speed_time(time1,time2,userinput):
    time=time1-time2
    time_delay=round(time,2)
    #heere i am dividing to get speed by sec
    speed=len(userinput)/time_delay
    return round(speed)

list=["yes i am here to see you, and i am happy","can you please tell me your name",
      "do one thing go and take the big fish","yes tell me your best friend name"]
print("***********************typing_calculator*********************")
#here randomly i am giving some line to my user,....
test=r.choice(list)
print(test)
#here i am giving two balnk line for comfortabe space........ 
print()
print()
strat_time=time()
usertest=input("enter:")
end_time=time()
print('****************************Result*****************************')
print()
print("speed: ",speed_time(strat_time,end_time,usertest))
print()
print('Error: ',error(test,usertest))