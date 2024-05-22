from tkinter import *
import random

def next_turn(i,j):
    global player
    if button[i][j]['text'] == "" and check_winner() is False:
        if player == players[0]:
            button[i][j]['text']=player
            if check_winner() is False:
                player = players[1]
                label.config(text="Player = "+player)
            elif check_winner() is True:
                label.config(text=player[0]+" is winner")
            elif check_winner() == "draw":
                label.config(text="Tie!")
        else:
            button[i][j]['text']=player
            if check_winner() is False:
                player = players[0]
                label.config(text="Player=  "+player)
            elif check_winner() is True:
                label.config(text=player+" is winner")
            elif check_winner() == "draw":
                label.config(text="Tie!")

def empty_space():
    flag = int(0)
    for i in range(3):
        for j in range(3):
            if button[i][j]['text'] != "":
                flag+=1
    if flag == 9:
        return True
    else:
        return False

def check_winner():
    for i in range(3):
        if button[i][0]['text'] == button[i][1]['text'] == button[i][2]['text'] != '':
            return True
        if button[0][i]['text'] == button[1][i]['text'] == button[2][i]['text'] != '':
            return True
    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != '':
        return True
    elif button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != '':
        return True
    elif empty_space() is True:
        return "draw"
    else:
        return False
    
def reset_game():
    global player
    player = random.choice(players)
    label.config(text="Player = "+player)
    for i in range(3):
        for j in range(3):
            button[i][j].config(text="")


m = Tk()
m.config(background="gray")
players = ['O','X']
player = random.choice(players)
label = Label(m,text="Player = "+player,font=("Arial",40),fg="lightblue",background="gray")
label.pack(side="top")
reset = Button(m,text="Restart",command=reset_game,font={"Arial",30})
reset.pack()
frame = Frame(m)
frame.pack()
button = [[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(3):
    for j in range(3):
        button[i][j] = Button(frame,text="",width=3,fg="black",font=("Arial",40),command= lambda r=i,c=j: next_turn(r,c))
        button[i][j].grid(row=i,column=j)
m.mainloop()