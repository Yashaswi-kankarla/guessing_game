from tkinter import *
import time
import random
import tkinter as tk
    
def game_piece():
    backg=tk.Tk()
    backg.title("GUESS IT!")
    backg.geometry("900x500+250+120")
    backg.configure(background="mediumpurple1")
    used=IntVar()
    tk.Label(backg,text="Hey! Let's start the game",font='Comic_Sans_MS 30 italic',bg="mediumpurple1",padx=215,pady=25,justify="center").grid(row=0,columnspan=2,column=0)
    tk.Label(backg,text="Enter the number that you want to guess\n remember from 1 to 100",bg="mediumpurple1",font="Times 20").grid(row=1,column=0,columnspan=2)
    tk.Entry(backg,textvariable=used,font="Times 27").grid(row=2,column=0)
    comp=int(random.uniform(1,101))
    def pri():
        try:
            user=used.get()
        except (tk.TclError):
            tk.Label(backg,text="It is not a number.",fg="blue",bg="white",font="Comic_Sans_MS 15 bold ",height=9,width=30,relief="ridge").grid(row=3)        
        if type(user)==int:
            if comp>user :
                tk.Label(backg,text="The number you guessed is\n LESSER than the actual number.",fg="orange",bg="white",font="Comic_Sans_MS 15 bold ",height=9,width=30,relief="ridge").grid(row=3)
            elif comp<user:
                tk.Label(backg,text="The number you guessed is\n GREATER than the actual number.",fg="orange",bg="white",font="Comic_Sans_MS 15 bold ",height=9,width=30,relief="ridge").grid(row=3)
            else :
                tk.Label(backg,text=f"Yehee! You guessed it RIGHT.\n The number is {user}",fg="blue",bg="white",font="Comic_Sans_MS 15 bold ",height=9,width=30,relief="ridge").grid(row=3)
                def New_Game():
                    backg.destroy()
                    Welcome_note()
                tk.Button(backg,text="New Game",fg="red",font="Times 25",padx=40,command=New_Game).grid(row=3,column=1)
    tk.Button(backg,text="Try!",fg="green",font="Times 25",command=pri,padx=40).grid(row=2,column=1)
    outputs=tk.Label(backg,bg="White",font="Comic_Sans_MS 15 bold ",height=9,width=30,relief="ridge").grid(row=3)
    backg.mainloop()
def Welcome_note():
    backg=tk.Tk()
    backg.title("GUESS IT!")
    backg.geometry("900x500+250+120")
    backg.configure(background="mediumpurple1")
    def Next_frame():
        backg.destroy()
        game_piece()
    tk.Label(backg,text='Welcome to the game!',font=("Comic_Sans_MS  30  underline  bold"),background="mediumpurple1",justify="center",padx=250,pady=40).grid(columnspan=2,sticky="s")
    tk.Label(backg,text="Do you want to start?",font=("Times 25"),background="mediumpurple1",justify="center",pady=30).grid(columnspan=2)
    tk.Button(backg,text="PLAY",font=("Times 25"),justify="left",foreground="green",command=Next_frame,relief="groove",padx=70,pady=30).grid(row=2,column=0)
    tk.Button(backg,text="QUIT",font=("Times 25"),justify="right",foreground="red",command=quit,relief="groove",padx=62,pady=30).grid(row=2,column=1)
    backg.mainloop()
Welcome_note()


