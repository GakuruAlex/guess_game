from random import randint
        
    
def main()-> None:
            while True:
                try:
                    level: int = int(input("Level: "))
                except ValueError:
                    continue
                else:
                    if level < 1:
                        continue
                    else:
                        guess: int = randint(1, level)
                        while True:
                            try:
                                user_guess: int = int(input("Guess: "))
                            except ValueError:
                                continue
                            else:
                                if guess < user_guess:
                                    print("Too large!")
                                    continue
                                elif guess > user_guess:
                                    print("Too small!")
                                    continue
                                else:
                                    print("Just right!")
                                    break
                break
    
if __name__ == "__main__":
    main()