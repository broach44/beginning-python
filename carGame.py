command = input().lower()
in_progress = True
car_stopped = True

while in_progress:
    if command == 'help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to ext")
    elif command == 'start':
        if car_stopped:
            print("You started the car")
            car_stopped = False
        else:
            print("The car has already been started")
    elif command == 'stop':
        if not car_stopped:
            print("You stopped the car")
            car_stopped = True
        else:
            print("The car is already stopped")
    elif command == 'quit':
        print("Exiting the program now")
        in_progress = False
        break
    else:
        print("That was not a valid command, try again.  Enter 'help' for a list of valid commands")
    command = input().lower()
