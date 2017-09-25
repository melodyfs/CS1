import random
random.seed(1)


# bank_account = 1000
# bet_amount = 0
# bet_color = None
# bet_number = None
# ranNum = 0
#
# green = [0, 37]
# red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
# black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
#
# def take_bet(color, number, amount):
#     bet_color = color
#     bet_number = number
#     bet_amount = amount
#
# def roll_ball():
#     '''returns a random number between 0 and 37'''
#     ranNum = random.randint(0,37)
#     return ranNum
#     pass
#
# def check_results(bet_color, bet_number):
#     '''Compares bet_color to color rolled.  Compares
#     bet_number to number_rolled.'''
#
#     color_rolled  = None
#
#     if ranNum in green:
#         color_rolled = "green"
#     elif ranNum in red:
#         color_rolled = "red"
#     elif ranNum in black:
#         color_rolled = "black"
#     print("Color is %s, Number is %s" % (color_rolled, ranNum))
#
#     pass
#
# def payout():
#     '''returns total amount won or lost by user based on results of roll. '''
#
#
#     pass
#
# def play_game():
#     """This is the main function for the game.
#     When this function is called, one full iteration of roulette,
#     including:
#     Take the user's bet.
#     Roll the ball.
#     Determine if the user won or lost.
#     Pay or deduct money from the user accordingly.
#     """
#     pass


class Roulette2:
    bank_account = 1000
    bet_amount = 0
    bet_color = None
    bet_number = None

    green = [0, 37]
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    def take_bet(color, number, amount):
        bet_color = color
        bet_number = number
        bet_amount = amount
        return [bet_color, bet_number, bet_amount]

    def roll_ball():

        return random.randint(0, 37)

    def check_results(bet, number_result):
        # Compares bet_color to color rolled. Compares bet_number to number_rolled.
        color_result = None
        if number_result in Roulette2.red:
            color_result = "red"
        elif number_result in Roulette2.black:
            color_result = "black"
        else:
            color_result = "green"
        print("Boll number is %s, and Color is %s" % (number_result, color_result))
        
        if bet[0] == color_result:
            if bet[1] == number_result:
                return [True, True]
            else:
                return [True, False]
        else:
            if bet[1] == number_result:
                return [False, True]
            else:
                return [False, False]

    def payout(check, bet):
        # returns total amount won or lost by user based on results of roll.
        if check[0] is True:
            if check[1] is True:
                return bet[2] * 2 * 38
            else:
                return bet[2] * 2
        else:
            if check[1] is True:
                return bet[2] * 2
            else:
                return -(bet[2])

    def confirm_amount():
        amount = int(input("Amount: "))
        if amount < 1:
            print("Minimum bet is $1.")
            amount = Roulette2.confirm_amount()
        elif amount > Roulette2.bank_account:
            print("You do not have that much money.")
            amount = Roulette2.confirm_amount()
        else:
            amount = amount
            print("%s" % amount)

        return amount

    def continue_bet():
        yes_or_no = input("Continue? Yes or No: ")
        if yes_or_no == "Yes" or yes_or_no == "yes":
            Roulette2.play_game()
        elif yes_or_no == "No" or yes_or_no == "no":
            pass


    def play_game():

        color = input("Color: ")
        if color != "red" and color != "black" and color != "green":
            print("Please choose from red, black or green")
            Roulette2.play_game()
        else:
            number = int(input("Number: "))
            if number in range(0, 38):
                number = number
                amount = Roulette2.confirm_amount()
            else:
                number = None
                amount = Roulette2.confirm_amount()

        bet = Roulette2.take_bet(color, number, amount)
        number_result = Roulette2.roll_ball()
        check = Roulette2.check_results(bet, number_result)
        print("%s" % bet)

        money = Roulette2.payout(check, bet)
        win = Roulette2.bank_account - bet[2] + money
        lost = Roulette2.bank_account + money

        if money > 0:
            print("YOU WON $%s!" % (money))
            Roulette2.bank_account = win
        else:
            print("YOU LOST $%s!" % (-money))
            Roulette2.bank_account = lost

        Roulette2.continue_bet()


roulette = Roulette2
roulette.play_game()