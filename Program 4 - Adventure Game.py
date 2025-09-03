print ("Welcome To Treasure Island")

print ("Your Mission Is To Find The Tresure")

Choice_1 = input ("you are at a crossroads, left are right ").lower()
if Choice_1 == "left":
    Choice_2 =input("You Come To A River. Swim Or Wait For A Boat? ")
    if Choice_2 == "wait":
        print("you get to the otherside and find the treasure, Hurray!")
    else:
        print("You Die")

else: print("You Get Eaten By Cannabals and Die")