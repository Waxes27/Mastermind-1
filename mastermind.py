import random
def master():
    a = random.randint(1,8)
    b = random.randint(1,8)
    c = random.randint(1,8)
    d = random.randint(1,8)


    code = set([a,b,c,d])
    while len(code) != 4:
        code.add(random.randint(1,8))
    return list(code)

def guess_code(code):
    code = code[0:]
    print(code)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    guess = "1234"#input("Input 4 digit code: ")
    print(list(guess))
    if len(guess) != 4 or guess.isdigit() is False:
        print("Please enter exactly 4 digits")
        return guess_code(code)
    if list(guess) == code:
        print("Congratulations! You are a codebreaker!")
        #code = "".join(code)
        # print(code)
        #print("The code was: "+code)
    #for i in enumerate(code):
    #    print(i)


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = master()
    guess_code(code)



if __name__ == "__main__":
    run_game()
