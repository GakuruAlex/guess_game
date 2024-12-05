from random import randint
class Guess:
    def ask_for_guess(self):
        try:
            self.user_guess = int(input("Guess: "))
        except ValueError:
            self.ask_for_guess()
        else:
            self.check_user_guess()
    
    def ask_for_level(self):
        try:
            level: int = int(input("Level: "))
        except ValueError:
            self.ask_for_level()
        else:
            self.guess: int = randint(1, level)
        
    def check_user_guess(self):
        if self.user_guess == self.guess:
            print("Just right!")
        elif self.user_guess > self.guess:
            print("Too large!")
            self.ask_for_guess()
        else:
            print("Too small!")
            self.ask_for_guess()
    
    def main(self)-> None:
            self.ask_for_level()
            self.ask_for_guess()

    
if __name__ == "__main__":
    game = Guess()
    
    game.main()