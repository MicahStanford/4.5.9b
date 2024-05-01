
#The code tells the user that the car breaks down and they have to choose options to survive!
print("You have been driving alone in a forest for a while now and you car has broken down.")
car1 = input("Now you have to choose, (Get out of the car/Stay in the car): ")
if car1 == "Get out of the car":
    test1 = input("You have exited the car, will you (Walk up the road/Go the other direction): ")
    if test1 == "Walk up the road":
        print("You walked for many miles and many hours, but you finnaly make it to town!!!")
    else:
        test2 = input("Now you are lost in the woods and you can't find the road, you can (Try to find car/Stay in same direction): ")
        if test2 == "Try to find car":
            print("You never find you car and you never make it out of the woods.")
        else:
            print("You find the road and someone driving pulls over right next to you and helps you out. ")
elif car1 == "Stay in the car":
    food1 = input("You are now getting hungry, should you (Look inside car/Hunt in the woods): ")
    if food1 == "Look inside car":
        food2 = input("You find a granola bar but there is no other food, should you (Stay in car/Leave car to find water): ")
        if food2 == "Stay in car":
            print("Some cars do pass by but none check in on your car. ")
        else:
            water1 = input("You are out of the car and you must choose which way to go, (Right/Left)")
            if water == "Right":
                print("You do find a creek to get water from and you decide that you can build a house so you do and you learn how to live in the woods. ")
            else:
                print("You don't find any water and you don't make it out of the forest. ")
    else:
        hunt1 = input("You don't find any food hunting and now you need to (Find car/Stay in woods): ")
        if hunt1 == "Find car":
            print("You do find your car but there is no food or water in the car. Many years later, people do find your car but you are nowhere to be found. ")
        else:
            ("You find a deer and kill it for food, then you decide to live in the woods, so you make a home and you learn how to live in the forest. ")
elif car1 == "Get out of the car" and car1 == "Stay in the car":
    print("You have hit the self-destruct button.")
else:
    print("Wrong choice")
