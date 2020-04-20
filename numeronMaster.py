if __name__ == '__main__':

    from numeronPlayer import Player

    START = "GAME START"
    CHOOSE_NAME = "Player 1, choose your name"
    PICK_YOUR_NUMBER = "Pick your number!"
    YOUR_TURN = "It's your turn"


    def print_console(contents):
        print("{}".format(contents))


    print_console(START)
    print_console(CHOOSE_NAME)
    # each player picks their name, but for now, let it pass it as argument
    player1 = Player(name='Koizumi')
    player1.pick_number(1, 2, 3)

    print_console(CHOOSE_NAME)
    player2 = Player(name='Ajioka')
    print_console(PICK_YOUR_NUMBER)
    player2.pick_number(1, 2, 3)

    while player1.match_flg == False and player2.match_flg == False:
        print_console(player1.name + YOUR_TURN)
        player1.attack(1, 3, 5, player2)

        print_console(player2.name + YOUR_TURN)
        player2.attack(1, 2, 3, player1)
