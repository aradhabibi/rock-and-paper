import random

def arad():

    #by arad habibi


    rond = int(input("chand bar?"))

    def check_win(user, computer):
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return True

    def rock_paper_scissors():
        player = input("salam r = rock  va  s = scissors  va p = paper: ")
        choices = ['r','s','p']
        opponent = random.choice(choices)


        if player == opponent:
            return print(f"mosavi! Choice is {opponent}")

        if check_win(player, opponent):
            return print(f"yes! to bord i! Choice is {opponent}")

        if check_win(player, opponent) != True:
            return print(f"bakhti ! Choice is {opponent}")
    for  x  in range(rond):
        rock_paper_scissors()


arad()
