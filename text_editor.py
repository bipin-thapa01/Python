#Bipin Text Editor
import tkinter as tk
from tkinter import filedialog

def change_font(font_name):
    main_text.config(font=(font_name,font_size))

def change_font_size(font_size):
    main_text.config(font=(font_name,font_size))

def change_theme(theme):
    main_text.config(background=theme)
    m.config(background=theme)
    menu_bar.config(bg=theme)

def change_text_color(color):
    main_text.config(fg=color)

#input from text box
def take_text():
    input_string = main_text.get("1.0",tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(input_string)
        except Exception as e:
            print("File cretaion error!")

def open_new_file_without_doing_anything():
    new_window.destroy()
    main_text.delete('1.0',tk.END)


def take_text_for_new_file():
    input_string = main_text.get('1.0',tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files","*.txt"),("All Files","*,*")])
    if file_path:
        try:
            with open(file_path,"w") as file:
                file.write(input_string)
        except Exception as e:
            print("File creation error!")
    
    main_text.delete('1.0',tk.END)


#for new file
def new_file():
    global new_window
    new_window = tk.Toplevel(m)
    new_window.title("New File")
    label = tk.Label(new_window,text="Do you want to save the content of current file?")
    label.pack(padx=10,pady=10)
    frame = tk.Frame(new_window)
    frame.pack()
    button_1 = tk.Button(frame,text="Yes",command=take_text_for_new_file)
    button_1.grid(row=0,column=0)
    button_2 = tk. Button(frame,text="No",command=open_new_file_without_doing_anything)
    button_2.grid(row=0,column=1,padx=50)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files",".txt"),("All Files","*.*")])
    if file_path:
        try:
            with open(file_path,"r") as file:
                file_content = file.read()
        except Exception as e:
            print("File open error!")
    main_text.delete('1.0',tk.END)
    main_text.insert('1.0',file_content)
    

m = tk.Tk(className=" Bipin Text Editor")
m.geometry("1080x720")
font_size = 20
font_name = "Times"
theme = "white"
text_color = "black"
main_text = tk.Text(m,height=100,width=1000,font=(font_name,font_size),wrap='none',background="white",fg=text_color)
main_text.pack(padx=20,pady=20,expand=True)


#scroll bar
x_scroll = tk.Scrollbar(m,orient="horizontal")
x_scroll.pack(side="bottom",fill="x")
y_scroll = tk.Scrollbar(m,orient="vertical")
y_scroll.pack(side="left",fill="y")
main_text.config(xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)

#menu
menu_bar = tk.Menu(m)
m.config(menu=menu_bar)

#file
file = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File",command=new_file)
file.add_command(label="Open",command=open_file)
file.add_command(label="Save",command=take_text)
file.add_command(label="Exit",command=m.destroy)

#font style
font_style = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font Style",menu=font_style)
font_style_lists = ["Arial","Times","Courier","Helvetica","Verdana","Comic Sans MS","Fixedsys","MS Sans Serif","MS Serif","Symbol","System"] 
for i in font_style_lists:
    font_style.add_command(label=i,command= lambda s=i : change_font(s))
    #font_style.add_separator()

#font size
font_size_change = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font Size",menu=font_size_change)
for i in range(5,101,5):
    font_size_change.add_command(label=str(i),command = lambda s=i : change_font_size(s))

#background color
theme = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Theme",menu=theme)
theme_lists = {"Black":"#121212","Gray":"#444444","White":"white",}
for i,j in theme_lists.items():
    theme.add_command(label=i,command= lambda s=j: change_theme(s))

#text color
character_theme = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Text Color",menu=character_theme)
text_color_list = {"Black":"#121212","Gray":"#444444","White":"white","Red":"red","LightBlue":"lightblue","Blue":"blue","LightGreen":"lightgreen","Green":"green"}
for i,j in text_color_list.items():
    character_theme.add_cascade(label=i,command= lambda s=j: change_text_color(s))
m.mainloop()