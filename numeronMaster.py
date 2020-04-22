if __name__ == '__main__':

    from numeronPlayer import Player

    START = "GAME START"
    PICK_YOUR_NUMBER = "Pick your number!"
    YOUR_TURN = "It's your turn"
    ENTER_NAME = "{}!, enter your name"
    THREE = 3
    FOUR = 4
    VALID_NUMBER_VALIDATE = "Please enter valid numbers"
    DIGIT_VALIDATE = "please enter {} digits number"
    DIFFERENT_NUMBER_VALIDATE = "Please choose three different numbers"


    def print_console(contents):
        print("{}".format(contents))


    def num_validate(num):
        does_num_match_flg = True

        while not num.isdigit():
            print(VALID_NUMBER_VALIDATE)
            num = input()

        while len(list(num)) is not 3:
            print(DIGIT_VALIDATE.format(THREE))
            num = input()
            # TODO you would better come up with better algorithm for the following
        while does_num_match(num) == 0:
            print(DIFFERENT_NUMBER_VALIDATE)
            num = input()
        return num


    def does_num_match(num):
        number_list = []
        for i in range(len(list(num))):
            number_list.append(int(num[i]))
        for i in range(len(list(number_list))):
            for j in range(i + 1, len(list(number_list))):
                if list(number_list)[i] is list(number_list)[j]:
                    does_num_match_flg = True
                    return 0
        return num


    def game(player, opponent):
        print(player.name + " " + YOUR_TURN)
        num_list = num_validate(input())
        player.attack(num_list, opponent)
        if player.match_flg:
            return True
        else:
            False


    print(START)
    # each player picks their name, but for now, let it pass it as argument
    player1 = Player(name="player1")
    print(ENTER_NAME.format(player1.name))
    player1.choose_name(input())
    print(PICK_YOUR_NUMBER)
    num = num_validate(input())
    num_list = list(num)
    player1.set_number(list(num))

    # each player picks their name, but for now, let it pass it as argument
    player2 = Player(name="player2")
    print(ENTER_NAME.format(player2.name))
    player2.choose_name(input())
    print(PICK_YOUR_NUMBER)
    num = num_validate(input())
    num_list = list(num)
    player2.set_number(list(num))

    while player1.match_flg is False and player2.match_flg is False:

        if game(player1, player2):
            break
        if game(player2, player1):
            break
