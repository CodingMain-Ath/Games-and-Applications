print ("The rules of the game are as follows:")
print ("1) choose any whole number between 1 to 100, both inclusive\n2) At every try you will get hint if u are getting close to the number or not\n3) Only ten chances will be provided")

from random import randint
x = randint(1,100)

for i in range (1,11):
    y = int((input("Enter an integer from 1 to 100: ")))
    if y>100 or y<0 or y==None:
        print ("Kevda hushar jhalas re tu?")
        break

    else:

        if i == 5:
            
            if x==y:
                print (f"You have guessed it ryt, the number was {x}")
                print (f"Trial number: {i}")
                break

            elif x>y:
                print (f"{y} is less than the hidden number")

            elif x<y:
                print (f"{y} is greater than the hidden number")

            print ("5 more guesses left!")

        if i == 9:
            
            if x==y:
                print (f"You have guessed it ryt, the number was {x}")
                print (f"Trial number: {i}")
                break

            elif x>y:
                print (f"{y} is less than the hidden number")

            elif x<y:
                print (f"{y} is greater than the hidden number")

            print ("last guess!")

        elif i!=5 and i!=9 and i!=10:
            if x==y:
                print (f"You have guessed it ryt, the number was {x}")
                print (f"Trial number: {i}")
                break

            elif x>y:
                print (f"{y} is less than the hidden number")

            elif x<y:
                print (f"{y} is greater than the hidden number")

            
        elif i==10:
            if x==y:
                print (f"You have guessed it ryt, the number was {x}")
                print (f"Trial number: {i}")
                break

            else:
                print ("Computer wins over humans!!!")
                print ("Met by destiny again na? HAHAHAHA!")
                print (f"The correct guess was: {x}")

