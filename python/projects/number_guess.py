import random 

sec_number=random.randint(1,1000)


attempt=0
max_attempt=5

print("welcome to the number guessing game")
print("pls guess a number between 1 to 100 ")

while attempt < max_attempt:
    try:
        guess=int(input(f"guess a number attempt {attempt+1} : enter your guess"))
    except ValueError:
        print("enter the valid number")
        continue
    
    attempt+=1

    if guess < sec_number:
        print("you have enter low number")
    elif guess > sec_number:
        print("you have enter high number ")
    else:
        print(f"congrats you have guess the right number {sec_number} \n in {attempt} attempts")
        break
else :
    print(f"you ran out of max attemps the secret number is {sec_number}")     