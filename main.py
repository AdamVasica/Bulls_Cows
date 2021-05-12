import random

#Greetings
separator = 40 * '-'
print('Hi there!')
print(separator)
print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print(separator)

#User is guessing a number
guess_number = 0


#Generating a random number
n = random.randrange(1000,9999)
count = 0



while guess_number != n:
    bulls = 0
    cows = 0

    guess_number = input('Enter a number: ')

    # For loop for duplicates
    t = ""
    for i in guess_number:
        if i in t:
            pass
        else:
            t = t + i

    #Checking if the number is in a correct format
    if len(guess_number) != 4:
        print('The number must contain 4 digits')
        continue
    elif guess_number[0] == '0':
        print('The number can not start with 0')
        continue
    elif guess_number.islower() or guess_number.isupper():
        print('Please type only numbers')
        continue
    elif len(guess_number) != len(t):
        print('Number can not contain duplicates')
        continue

    str_n = str(n)
    for i in range(0,4):
        if str_n[i] == guess_number[i]:
            bulls += 1

        else:
            guess_num = guess_number[:i] + guess_number[i + 1:]
            if str_n[i] in guess_num:
                cows += 1
    if n != guess_number:
        count += 1



    print(bulls,'bulls', ',' ,cows, "cows")
    if int(guess_number) == n:
        break

print(separator)
print("Correct, you've guessed the right number in", count, "guesses!")

if 5 >= count:
    print('You are amazing!')

elif count >= 6 and count <= 10:
    print('You did well!')

else:
    print('Come on, you can do better')





















