import requests
import json
import os
os.system('cls')
import time
import tkinter as tk
import random
import customtkinter
import sqlite3
import os


def filmek():
    global filmek_label
    for label in filmek_label:
        label.destroy()
    filmek_label=list()
    res = cur.execute("SELECT * FROM movie;")
    for movie in res.fetchall():
        film = customtkinter.CTkLabel(window, text=f"\nCím: {movie[1]}\nGyártási év: {movie[2]}\nPont: {movie[3]}\n", font=("Helvetica", 18))
        film.pack()
        filmek_label.append(film)
        #filmek.place(relx=0)

def submit_input():
    title = cim.get()
    year = gyart.get()
    score = pont.get()
    print(title, year, score)
    ins = cur.execute(f"insert into movie (title, year, score) values ('{title}','{year}', '{score}')")
    con.commit()

def refresh():
    filmek()
    
    
os.system("cls")

global filmek_label
filmek_label = list()

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE movie(id INT PRIMARY KEY ,title, year, score)")
except:
    pass
window = customtkinter.CTk()
window.geometry("1000x700")
window.title("Időjárás")
window.resizable(0, 0.00000001)
label = customtkinter.CTkLabel(window, text="filmek", font=("Helvetica", 24))
label.place(relx=0.1, rely=0)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
def lightd():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("light-blue")
    text_entry = customtkinter.CTkEntry(master=window,
                                   placeholder_text="Település / Ország",
                                   width=200,
                                   height=20,
                                   font=("Helvetica", 18),
                                   corner_radius=50,
                                   text_color="green",
                                   placeholder_text_color="lightblue",
                                   fg_color=("blue", "darkblue"),
                                   state="normal")

def dark():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")


"""light = customtkinter.CTkButton(master=window,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=10,
                                  text="Világos",
                                  hover_color="lightblue",
                                  command=lightd)

light.place(relx=0.01, rely=0)

dark = customtkinter.CTkButton(master=window,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=10,
                                  text="Sötét",
                                  hover_color="lightblue",
                                  command=dark)

dark.place(relx=0.14, rely=0)"""

cim = customtkinter.CTkEntry(master=window,
                                   placeholder_text="Film cím",
                                   width=200,
                                   height=20,
                                   font=("Helvetica", 18),
                                   corner_radius=50,
                                   text_color="green",
                                   placeholder_text_color="darkblue",
                                   fg_color=("blue", "lightblue"),
                                   state="normal")
gyart = customtkinter.CTkEntry(master=window,
                                   placeholder_text="Film gyártása",
                                   width=200,
                                   height=20,
                                   font=("Helvetica", 18),
                                   corner_radius=50,
                                   text_color="green",
                                   placeholder_text_color="darkblue",
                                   fg_color=("blue", "lightblue"),
                                   state="normal")
pont = customtkinter.CTkEntry(master=window,
                                   placeholder_text="Film értékelése(1-10)",
                                   width=200,
                                   height=20,
                                   font=("Helvetica", 18),
                                   corner_radius=50,
                                   text_color="green",
                                   placeholder_text_color="darkblue",
                                   fg_color=("blue", "lightblue"),
                                   state="normal")
label.pack()
cim.place(relx=0.1, rely=0.1)
label.pack()
gyart.place(relx=0.1, rely=0.2)
label.pack()
pont.place(relx=0.1, rely=0.3)

filmek()

    
button = customtkinter.CTkButton(master=window,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=10,
                                  text="Beküldés",
                                  hover_color="lightblue",
                                  command=submit_input)
button.place(relx=0.1, rely=0.4)
button = customtkinter.CTkButton(master=window,
                                  width=120,
                                  height=32,
                                  border_width=0,
                                  corner_radius=10,
                                  text="Frissít",
                                  hover_color="lightblue",
                                  command=refresh)
button.place(relx=0.1, rely=0.5)
window.mainloop()