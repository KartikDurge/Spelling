import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct Text is :",font=("poppins",20),bg="#dae6f6",fg="Black")
    cs.place(x=100,y=250)
    spell.config(text=right)


heading= Label(root,text="Spelling Checker",font=("Trebuchet Ms",30,"bold"),bg="#dae6f6",fg="Black")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="pink",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check",font=("arial",20,"bold"),fg="pink",bg="black",command=check_spelling)
button.pack()
spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="Black")
spell.place(x=350,y=250)

root.mainloop()
