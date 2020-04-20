class Player(object):
    def __init__(self, name, first_digit=None, second_digit=None, third_digit=None):
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit
        self.name = name
        self.match_flg = False

    def pick_number(self, first_digit, second_digit, third_digit):
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit

    def attack(self, first_digit, second_digit, third_digit, opponent):
        attack_nums = [first_digit, second_digit, third_digit]
        opponent_nums = [opponent.first_digit, opponent.second_digit, opponent.third_digit]

        bite = 0
        eat = 0
        for attack_num in attack_nums:
            for opponent_num in opponent_nums:
                if attack_num == opponent_num:
                    bite += 1

        for i in range(len(attack_nums)):
            if attack_nums[i] == opponent_nums[i]:
                bite -= 1
                eat += 1

        if eat == 3:
            self.match_flg = True
            print("{} EAT! {} win!".format(eat, self.name))
        else:
            print( "{} EAT, {} BITE".format(eat, bite))
