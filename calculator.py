import tkinter as tk
import math

def calculate(value, number):
    global value_seperator
    global number_1
    global number_2
    global symbol
    global answer
    global symbol_check
    global equals_count
    #assigning numbers and symbol
    if number == '=':
        if number_1 == 0 or number_2 == 0 or symbol == "":
            answer_box.config(state=tk.NORMAL)
            answer_box.insert('1.0',"Wrong format! Press AC")
            answer_box.config(state=tk.DISABLED)
    if value == 0:
        if isinstance(number_1,float):
            number_1 = str(number_1)
            integer_part,decimal_part = number_1.split('.')
            if decimal_part == '0':
                decimal_part = str(number)
            else:
                decimal_part = decimal_part + str(number)
            number_1 = float(integer_part + '.' + decimal_part)
        else:
            if number != '.':
                number_1 = number_1*10+number
            else:
                number_1 = float(number_1)    
        print(number_1)
    elif value == 1 and equals_count == 0:
        value_seperator=2
        symbol_check = number
        if not symbol:
            if number != '=':
                symbol = number
            print(symbol)
    elif value == 2:
        if isinstance(number_2,float):
            number_2 = str(number_2)
            integer_part,decimal_part = number_2.split('.')
            if decimal_part == '0':
                decimal_part = str(number)
            else:
                decimal_part = decimal_part + str(number)
            number_2 = float(str(integer_part) + '.' + decimal_part)
        else:
            if number != '.':
                number_2 = number_2*10+number
            else:
                number_2 = float(number_2)
        print(number_2)
    else:
        pass
    #displaying numbers and symbols in screen
    if number != '=' and symbol == symbol_check and equals_count==0:
        entry_box.config(state=tk.NORMAL)
        entry_box.insert(tk.END,number)
        entry_box.config(state=tk.DISABLED)
    symbol_check = symbol
    #calculating
    if number == "=":
        equals_count += 1
        answer = int(0)
        if symbol == "+":
            answer = number_1 + number_2
        elif symbol == '-':
            answer = number_1 - number_2
        elif symbol == '*':
            answer = number_1 * number_2
        elif symbol == '/':
            answer = number_1 / number_2
        elif symbol == '**':
            answer = number_1 ** number_2
        elif symbol == "log":
            answer = math.log(number_1,number_2)
        print(answer)
    if not answer:
        pass
    else:
        answer_box.config(state=tk.NORMAL)
        answer_box.insert('1.0',answer)
        answer_box.config(state=tk.DISABLED)
        answer = ""
        symbol = ""
        symbol_check=""
        number_1=0
        number_2=0
        value_seperator=0
    



def ac_function():
    global equals_count
    global number_1
    global number_2
    global symbol
    global symbol_check
    global answer
    global value_seperator
    global button_click_times
    entry_box.config(state=tk.NORMAL)
    entry_box.delete('1.0',tk.END)
    entry_box.config(state=tk.DISABLED)
    answer_box.config(state=tk.NORMAL)
    answer_box.delete('1.0',tk.END)
    answer_box.config(state=tk.DISABLED)
    equals_count = 0
    number_1 = 0
    number_2 = 0
    symbol = ""
    symbol_check = ""
    answer = 0
    value_seperator = 0
    button_click_times = 0

def del_function():
    global value_seperator
    global number_1
    global number_2
    global symbol
    global symbol_check
    global button_click_times
    flag = int(0)
    num = int(0)
    float_to_int = int(0)

    text = entry_box.get('1.0',tk.END)
    last_character = text[-1]

    #deleting text from screen
    entry_box.config(state=tk.NORMAL)
    end_index = entry_box.index(tk.END)
    last_character_index = f"{end_index}-2c"
    entry_box.delete(last_character_index,tk.END)
    entry_box.config(state=tk.DISABLED)

    #deleting value in container
    if value_seperator == 0:
        button_click_times = 0
        if isinstance(number_1,float):
            number_1 = str(number_1)
            integer_part,decimal_part = number_1.split('.')
            if decimal_part != '0':
                decimal_part = int(int(decimal_part)/10)
                number_1 = float(integer_part + "." + str(decimal_part))
            else:
                if button_click_times == 0:
                    number_1 = float(integer_part)
                    button_click_times += 1
                else:
                    number_1 = int(number_1)
                    button_click_times = 0
        else:
            number_1 = int(number_1/10)
            print(number_1)
    elif value_seperator == 2:
        button_click_times = 0
        if isinstance(number_2,float):
            number_2 = str(number_2)
            integer_part,decimal_part = number_2.split('.')
            if decimal_part != '0':
                decimal_part = int(int(decimal_part)/10)
                number_2 = float(integer_part + "." + str(decimal_part))
            else:
                if button_click_times == 0:
                    number_2 = float(integer_part)
                    button_click_times += 1
                else:
                    number_2 = int(number_2)
                    button_click_times = 0
        elif isinstance(number_2,int):
            number_2 = int(number_2/10)
    elif value_seperator == 2 and not last_character.isdigit():
        symbol = ""
        symbol_check = ""

    text = entry_box.get('1.0',tk.END)
    if text == '0':
        ac_function


number_1 = int(0)
number_2 = int(0)
answer = ""
symbol = ""
symbol_check = ""
value_seperator = 0
button_click_times = 0
equals_count = 0


m = tk.Tk(className=" Calculator")
entry_box = tk.Text(m,width=14,height=2,font=("Arial",30),background="#181818",fg="white")
entry_box.config(state=tk.DISABLED)
entry_box.pack()
answer_box = tk.Text(m,width=14,height=2,font=("Arial",30),background="#181818",fg="white")
answer_box.config(state=tk.DISABLED)
answer_box.pack()
button_frame = tk.Frame(m)
button_frame.pack()
button_1 = tk.Button(button_frame,text=" ^ ",width=3,command= lambda : calculate(1,'**'),font=("Arial",20))
button_1.grid(row=0,column=0)
button_2 = tk.Button(button_frame,text="log",width=3,command= lambda : calculate(1,'log'),font=("Arial",20))
button_2.grid(row=0,column=1)
button_3 = tk.Button(button_frame,text=" . ",width=3,command= lambda : calculate(value_seperator,'.'),font=("Arial",20))
button_3.grid(row=0,column=2)
button_4 = tk.Button(button_frame,text="Del",width=3,command= del_function,font=("Arial",20))
button_4.grid(row=0,column=3)
button_5 = tk. Button(button_frame,text="AC",width=3,command= ac_function,font=("Arial",20))
button_5.grid(row=0,column=4)
button_6 = tk.Button(button_frame,text=" + ",width=3,command= lambda : calculate(1,'+'),font=("Arial",20))
button_6.grid(row=1,column=0)
button_7 = tk.Button(button_frame,text=" - ",width=3,command= lambda : calculate(1,'-'),font=("Arial",20))
button_7.grid(row=1,column=1)
button_8 = tk.Button(button_frame,text=" x ",width=3,command= lambda : calculate(1,'*'),font=("Arial",22))
button_8.grid(row=1,column=2)
button_9 = tk.Button(button_frame,text=" / ",width=3,command= lambda : calculate(1,'/'),font=("Arial",20))
button_9.grid(row=1,column=3)
button_10 = tk.Button(button_frame,text=" = ",width=3,command= lambda : calculate(1,'='),font=("Arial",20))
button_10.grid(row=1,column=4)
button_11 = tk.Button(button_frame,text=" 9 ",width=3,command= lambda : calculate(value_seperator,9),font=("Arial",20))
button_11.grid(row=2,column=0)
button_12 = tk.Button(button_frame,text=" 8 ",width=3,command= lambda : calculate(value_seperator,8),font=("Arial",20))
button_12.grid(row=2,column=1)
button_13 = tk.Button(button_frame,text=" 7 ",width=3,command= lambda : calculate(value_seperator,7),font=("Arial",20))
button_13.grid(row=2,column=2)
button_14 = tk.Button(button_frame,text=" 6 ",width=3,command= lambda : calculate(value_seperator,6),font=("Arial",20))
button_14.grid(row=2,column=3)
button_15 = tk.Button(button_frame,text=" 5 ",width=3,command= lambda : calculate(value_seperator,5),font=("Arial",20))
button_15.grid(row=2,column=4)
button_16 = tk.Button(button_frame,text=" 4 ",width=3,command= lambda : calculate(value_seperator,4),font=("Arial",20))
button_16.grid(row=3,column=0)
button_17 = tk.Button(button_frame,text=" 3 ",width=3,command= lambda : calculate(value_seperator,3),font=("Arial",20))
button_17.grid(row=3,column=1)
button_18 = tk.Button(button_frame,text=" 2 ",width=3,command= lambda : calculate(value_seperator,2),font=("Arial",20))
button_18.grid(row=3,column=2)
button_19 = tk.Button(button_frame,text=" 1 ",width=3,command= lambda : calculate(value_seperator,1),font=("Arial",20))
button_19.grid(row=3,column=3)
button_20 = tk.Button(button_frame,text=" 0 ",width=3,command= lambda : calculate(value_seperator,0),font=("Arial",20))
button_20.grid(row=3,column=4)
m.mainloop()