from random import randint

rnd=randint(1,101)
num=-1
guess_count=0
while(num!=rnd):
    num=int(input("Enter the number to guess:"))
    guess_count+=1
    if(rnd<num):
        print(f"Your guess {num} is more than the number..Guess Again!!!!")
    elif(rnd>num):
        print(f"Your guess {num} is less than the number..Guess Again!!!!")
    else:
        print(f"your guess {num} is perfect")
        
print(f"You have taken {guess_count} attempts to guess the correct answer {rnd}")