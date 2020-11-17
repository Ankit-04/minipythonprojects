import time
import os
import keyboard
def stopwatch():      
    second = 0    
    minute = 0    
    hour = 0   

    while(True):          
        print("{}:{}:{}".format(hour,minute,second))   
        time.sleep(1)    
        second+=1    
        if(second == 60):    
            second = 0    
            minute+=1    
        if(minute == 60):    
            minute = 0    
            hour+=1    
        if keyboard.is_pressed("e"):
            break
        os.system('cls')
    main()
def timmer(end_time):       
    end_time = end_time.split(":")   
    end_hour = int(end_time[0])
    end_minute = int(end_time[1])
    end_second = int(end_time[2])
    while True:          
        print("{}:{}:{}".format(end_hour,end_minute,end_second))  
            
        if end_second == 0:
            if end_minute == 0:
                if end_hour ==0:
                    break
                end_hour -= 1
                end_minute = 60
            end_second = 60  
            end_minute-=1   

        time.sleep(1) 
        end_second -=1
        
        if keyboard.is_pressed("e"):
            break
        os.system('cls')
    main()
def main():
    os.system('cls')
    choice = int(input("press 1 for a timmer, 2 for a stopwatch, 3 for the time, or anything else to exit:\n"))
    if choice == 1:
        timmer(input("how long do you want the stopwatch to be in 'hours:minutes:seconds':"))
    elif choice == 2:
        stopwatch()
    elif choice == 3:
        print("it is currently {}".format(time.strftime("%H:%M:%S", time.localtime())))
main()