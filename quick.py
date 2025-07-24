
import random
import math




def main():

    snumber = round(random.random() * 10)
    
    attempts = 0
    max_attempts = 3

    print("I am thinking of a number between 0-10\n")
    print("You have to guess the number within 3 attempts. Good luck!")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            
        except ValueError:
            print("One through ten.")
            continue
                
        
        
        if guess != snumber:
            if guess < snumber:
                print("Too low.")
            else: 
                print("Too high!")
        else:
            print("You got it! Great job.")
            return

        if attempts == 3:
            print(f"Unlucky. The number was {snumber}")
            break

        
    

    


main()



    

