import random
def master():
    a = str(random.randint(1,8))
    b = str(random.randint(1,8))
    c = str(random.randint(1,8))
    d = str(random.randint(1,8))


    code = set([a,b,c,d])
    while len(code) != 4:
        code.add(str(random.randint(1,8)))
    
    return list(code)

def guess_code(code):
    number_guesses = 12
    print(code)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    while number_guesses != 0:
       
        guess = str(input("Input 4 digit code: "))

        if len(guess) != 4 or guess.isdigit() is False:
            print("Please enter exactly 4 digits")
            return guess_code(code)
        
        if list(guess) == code:
            print("Congratulations! You are a codebreaker!")
            print("the code was: "+str("".join(code)))
            break
        
        else:
            evaluate_code(code,guess)
            number_guesses -= 1
            print("turns left: "+str(number_guesses))
    return list(guess)
        
def evaluate_code(code,guess):
    correct_place = 0
    wrong_place_correct_digit= 0

    print(code)
    print(list(guess))
    if code == list(guess):
        return 0
    j = 0
    for i in code:#zip(code,guess):
        if guess[j] in code:
            print(list(zip(code,guess)))
            print(j)
        j += 1
            
    #if code in range(0,4) == guess in range(0,4):
            



def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = master()
    guess = guess_code(code)
    evaluate_code(code,guess)


if __name__ == "__main__":
    run_game()
