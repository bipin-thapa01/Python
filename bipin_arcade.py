import os
import random



def tic_tac_toe():
    os.system('cls')
    l = [["   ","   ","   "],
         ["   ","   ","   "],
         ["   ","   ","   "]]
    while True:
        player_1 = input("Enter player 1 choice [O or X]: ")
        if player_1!='O' and player_1!='X':
            print("choice can only be O or X. Try again!")
        elif player_1=='O':
            player_2 = 'X'
            print("Player 2 will have X")
            break
        else:
            player_2 = 'O'
            print("Player 2 will have O")
            break
    turn = 1
    while True:
        os.system('cls')
        flag = 0
        print("\n\t\t\t\t\tTic Tac Toe")
        print(f"Player {turn} turn")
        print(f"\n\n\t\t\t\t\t{l[0][0]}|{l[0][1]}|{l[0][2]}")
        print("\t\t\t\t\t-----------",end="")
        print(f"\n\t\t\t\t\t{l[1][0]}|{l[1][1]}|{l[1][2]}")
        print("\t\t\t\t\t-----------",end="")
        print(f"\n\t\t\t\t\t{l[2][0]}|{l[2][1]}|{l[2][2]}")
        i,j = map(int, input("enter index: ").split())
        if l[i][j] != "   ":
            print("You have already entered in this index! Try again")
            continue
        if turn == 1:
            l[i][j] = " "+player_1+" "
        else:
            l[i][j] = " "+player_2+" "
        if turn == 1:
            turn = 2
        else:
            turn = 1
        length = len(l[0])
        for I in range(0,length):
            if l[I][0] == l[I][1] == l[I][2] == " X " or l[I][0] == l[I][1] == l[I][2] == " O ":
                flag = 1
                if l[I][0] == " "+player_1+" ":
                    print("Congratulations player 1! You have won the game")
                    break
                else:
                    print("Congratulations player 2! You have won the game")
                    break
            if l[0][I] == l[1][I] == l[2][I] == " X " or l[0][I] == l[1][I] == l[2][I] == " O ":
                flag = 1
                if l[0][I] == " "+player_1+" ":
                    print("Congratulations player 1! You have won the game")
                    break
                else:
                    print("Congratulations player 2! You have won the game")
                    break
            if l[0][0] == l[1][1] == l[2][2] == " X " or l[0][0] == l[1][1] == l[2][2] == " O ":
                flag = 1
                if l[0][0] == " "+player_1+" ":
                    print("Congratulations player 1! You have won the game")
                    break
                else:
                    print("Congratulations player 2! You have won the game")
                    break
            if l[0][2] == l[1][1] == l[2][0] == " X " or l[0][2] == l[1][1] == l[2][0] == " O ":
                flag = 1
                if l[0][2] == " "+player_1+" ":
                    print("Congratulations player 1! You have won the game")
                    break
                else:
                    print("Congratulations player 2! You have won the game")
                    break
        if flag == 1:
            print("\n\t\t\t\t\tTic Tac Toe")
            print(f"\n\n\t\t\t\t\t{l[0][0]}|{l[0][1]}|{l[0][2]}")
            print("\t\t\t\t\t-----------",end="")
            print(f"\n\t\t\t\t\t{l[1][0]}|{l[1][1]}|{l[1][2]}")
            print("\t\t\t\t\t-----------",end="")
            print(f"\n\t\t\t\t\t{l[2][0]}|{l[2][1]}|{l[2][2]}")
            while True:
                ans = input("Do you want to play again? [Y/N]: ")
                if ans != 'Y' and ans != 'N':
                    print("Please type Y or N")
                else:
                    return ans
        counter_to_end_game = 0
        for j in range(0,length):
            for k in range(0,length):
                if l[j][k] == "   ":
                    break
                else:
                    counter_to_end_game += 1
        if counter_to_end_game == 9:
            break
    
    print("It was a draw")
    ans = input("Do you want to play again? [Y/N]: ")
    if ans != 'Y' and ans != 'N':
      print("Please type Y or N")
    else:
        return ans


def r_p_s():
    l = ["rock","paper","scissors"]
    win_count = int(0)
    os.system('cls')
    print("\tWelcome to Rock Paper Scissors\n You have 3 try")
    for i in range(1,4):
        computer_choice = random.choice(l)
        print(f"Game number {i}")
        result = input("Enter you choice: ")
        if result == computer_choice:
            print("Draw")
        elif result == "rock":
            if computer_choice == "scissors":
                print(f"You won round {i}. Your opponent choosed {computer_choice}")
                win_count+=1
            else:
                 print(f"You lost round {i}. Your opponent choosed {computer_choice}")
        elif result == "paper":
            if computer_choice == "scissors":
                print(f"You lost round {i}. Your opponent choosed {computer_choice}")
            else:
                 print(f"You won round {i}. Your opponent choosed {computer_choice}")
                 win_count+=1
        elif result == "scissors":
            if computer_choice == "rock":
                print(f"You lost round {i}. Your opponent choosed {computer_choice}")
            else:
                 print(f"You won round {i}. Your opponent choosed {computer_choice}")
                 win_count+=1
    os.system('cls')
    print("You won "+str(win_count)+" times")
    print("Nice game!")
    ans = input("Do you want to play again?[Y/N]: ")
    return ans
       
                    




def main():
    while True:
        os.system('cls')
        print("\t\t\tWelcome to Bipin Arcade")
        print("\t\t\t\tGames list:")
        print("\n\t\t\ta. Tic Tac Toe")
        print("\n\t\t\tb. Rock Paper Scissors")
        ans = input("\n\t\t\tWhich game do you want to play: ")
        if ans == "a":
            want_to_play_again = tic_tac_toe()
            if want_to_play_again == 'Y':
                main()
            else:
                break
        if ans == "b":
            want_to_play_again = r_p_s()
            if want_to_play_again == 'Y':
                main()
            else:
                break
    print("\n\n\nThanks for playing my game!\nVisit again")


main()