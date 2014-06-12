import random
import time
import collections

PLUS = 1
MINUS = 2
MULTIPLY = 3
EQUATION_STR = 0
EQUATION_INT = 1

class Game:


    def __init__(self, levels=3, player_name="Player"):
        self.score = 0
        self.total_time = 0
        self.Player = collections.namedtuple("Player", "player_name levels total_time score")
        try:
            self.levels = int(levels) - 1
            self.player_name = str(player_name)
            self.player_name = self.player_name.capitalize()
        except IndexError:
            print("You have no arguments, so this game will have 3 levels\n")
            self.levels = 3
            self.player_name = "Player"
        except ValueError as error:
            print("Your arguments are not in right condition. "
                  "Try to use 'help' to find out your mistake\n"
                  "Further information:\n", error)
        pass

    def score_count(self, timer, level, score):
        score += (1/timer)*level*100
        return score

    def get_number(self, last=1, sign=PLUS):
        if sign == MINUS:
            return random.randint(1, last) if last != 0 else random.randint(1, 10)
        else:
            return random.randint(1,15)

    def get_equation(self, level):
        i = 0
        while i < level:
            if i == 0:
                equation_int = self.get_number()
                new_number = equation_int
                equation_str = str(new_number)
                sign = random.randint(1,3)
            else:
                if sign == MULTIPLY:
                    sign = random.randint(1,3)
                sign = random.randint(1,2)
            new_number = self.get_number(new_number, sign)
            if sign == PLUS:
                equation_str += " + "
                equation_int += new_number
            elif sign == MINUS:
                equation_str += " - "
                equation_int -= new_number
            elif sign == MULTIPLY:
                equation_str += " * "
                equation_int *= new_number
            equation_str += str(new_number)
            i += 1
        equation = [equation_str, equation_int]
        return equation

    def start_game(self):

        level = 1
        print("\tLet's Start!\n")
        while level <= self.levels:
            equation = self.get_equation(level)
            print(equation[EQUATION_STR], "= ?")
            timer = time.time()
            while True:
                try:
                    answer = input("Answer: ")
                    break
                except SyntaxError as error:
                    print("Your answer is not INT argument.\nFurther information:\n", error)
                    continue
            answer = answer.lower()
            if answer == "exit" or answer == "quit":
                break
            elif answer == "cheat":
                print(equation[EQUATION_INT], "\n\n")
                level += 1
                timer = 0.1
            elif answer == str(equation[EQUATION_INT]):
                print("YES\n\n")
                level += 1
                timer = time.time() - timer
            else:
                print("NO, it was", equation[EQUATION_INT], "\n\n")
                self.score -= 100/level
                continue
            self.total_time += timer
            self.score = self.score_count(timer, level, self.score)
        if self.score < 0:
            self.score = 0
        player_information = self.Player(self.player_name, self.levels, self.total_time, self.score)
        print(player_information.player_name, ", your score is:", int(player_information.score))
        pass