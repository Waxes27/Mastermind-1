import random
def master():
    numbers = []
    while len(numbers) < 4:
        x = random.randint(1,8)
        if x not in numbers:
            numbers.append(str(x))
    return "".join(numbers)
def guess_code(code):
    #print(code)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    number_guesses = 12
    while number_guesses > 0:
        #try:
        guess = input("Input 4 digit code: ")
        #except:
            #EOFError
        #print(list(int(guess)))
        while len((guess)) != 4 or guess.isdigit() is False:
            print("Please enter exactly 4 digits.")
            guess = input("Input 4 digit code: ")

        if code == guess:
            evaluate_code(code,guess)
            print("Congratulations! You are a codebreaker!")
            print("The code was: "+code)
            return 0
        else:    
            evaluate_code(code,guess)
            number_guesses -= 1
            print("Turns left: "+str(number_guesses))
    return guess
def evaluate_code(code,guess):
    wrong_place = 0
    correct_place = 0

    for i,j in zip(code,guess):
        if i == j:
            correct_place += 1
        elif j in code and j != i:
            wrong_place += 1
    
    print("Number of correct digits in correct place:     "+str(correct_place))
    print("Number of correct digits not in correct place: "+str(wrong_place))


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = master()
    guess = guess_code(code)
    #evaluate_code(code,guess)


if __name__ == "__main__":
    run_game()
