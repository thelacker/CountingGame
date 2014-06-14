import game_class
import sys

def main():
    try:
        game_file = open("counting_game.txt", 'x')
        header = ["Player", "Levels", "Time", "Score"]
        for info in header:
            game_file.write("{0:-^10}".format(info) + ' ')
        game_file.write("\n")
        game_file.close()
    except FileExistsError:
        pass
    game_file = open("counting_game.txt", 'a')
    try:
        game = game_class.Game(sys.argv[1], sys.argv[2])
    except IndexError:
        game = game_class.Game()
    game.start_game()
    for info in game.player_information:
        try:
            game_file.write("{0:^10}".format(int(info)) + ' ')
        except ValueError:
            game_file.write("{0:^10}".format(info) + ' ')
    game_file.write("\n")
    game_file.close()

if __name__ == "__main__":
    main()
