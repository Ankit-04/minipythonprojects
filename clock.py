import time
def stopwatch():
    start_time = time.time()
    print("your timmer has started press s to stop it, p to pause it, r to resume")
    
def timmer(end_time):
    pass
def main():
    while True:
        choice = int(input("press 1 for a timmer, 2 for a stopwatch, 3 for the time, or anything else to exit:\n"))
        if choice == 1:
            timmer(input("how long do you want the stopwatch to be in seconds:"))
        elif choice == 2:
            stopwatch()
        elif choice == 3:
            print("it is currently {}".format(time.strftime("%H:%M:%S", time.localtime())))
        else:
            break
main()