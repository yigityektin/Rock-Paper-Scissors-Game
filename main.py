from tkinter import *
import random
import time

root = Tk()
root.title("Rock-Paper-Scissors!")
root.geometry("375x350")
root.configure(bg="#696969")
root.iconbitmap("icon.ico")

choose_of_user = ""
choose_of_computer = ""
Rock = "Rock"
Scissor = "Scissor"
Paper = "Paper"
user_win_count = 0
user_lose_count = 0
draw_count = 0


def control():
    global choose_of_computer
    global choose_of_user
    global user_win_count
    global user_lose_count
    global draw_count
    global result
    if choose_of_user == "Rock" and choose_of_computer == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_user == "Rock" and choose_of_computer == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_user == "Rock" and choose_of_computer == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_user == "Paper" and choose_of_computer == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    elif choose_of_user == "Paper" and choose_of_computer == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_user == "Paper" and choose_of_computer == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    elif choose_of_user == "Scissor" and choose_of_computer == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    elif choose_of_user == "Scissor" and choose_of_computer == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_user == "Scissor" and choose_of_computer == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_computer == "Rock" and choose_of_user == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    elif choose_of_computer == "Rock" and choose_of_user == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_computer == "Rock" and choose_of_user == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    elif choose_of_computer == "Paper" and choose_of_user == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_computer == "Paper" and choose_of_user == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_computer == "Paper" and choose_of_user == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_computer == "Scissor" and choose_of_user == "Rock":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "User Wins!")
        result = "win"
    elif choose_of_computer == "Scissor" and choose_of_user == "Scissor":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Draw!")
        result = "draw"
    elif choose_of_computer == "Scissor" and choose_of_user == "Paper":
        text1.delete("1.0", "end")
        text1.insert(END, f"User chosen {choose_of_user}!\n")
        text1.insert(END, f"Computer chosen {choose_of_computer}!\n")
        text1.insert(END, "Computer Wins!")
        result = "lose"
    if result == "win":
        user_win_count += 1
    elif result == "lose":
        user_lose_count += 1
    else:
        draw_count += 1
    return result


def rock():
    global choose_of_user
    choose_of_user = Rock
    computer_choose()
    control()


def scissor():
    global choose_of_user
    choose_of_user = Scissor
    computer_choose()
    control()


def paper():
    global choose_of_user
    choose_of_user = Paper
    computer_choose()
    control()


def result():
    global user_win_count
    global user_lose_count
    global draw_count
    global result
    global choose_of_user
    global choose_of_computer
    text1.delete("1.0", "end")
    text1.insert(END, f"User wins: {user_win_count}\n"
                      f"User loses: {user_lose_count}\n"
                      f"Draws: {draw_count}\n")


btn_rock = Button(root, command=rock, padx=15, pady=10, text="Rock", bg="#ED945E")
btn_scissor = Button(root, command=scissor, padx=15, pady=10, text="Scissors", bg="#ED945E")
btn_paper = Button(root, command=paper, padx=15, pady=10, text="Paper", bg="#ED945E")
btn_result = Button(root, command=result, padx=15, pady=10, text="Results", bg="#ED945E")
btn_exit = Button(root, command=exit, padx=15, pady=10, text="Exit", bg="#FF0000")
btn_rock.place(x=75, y=150)
btn_scissor.place(x=135, y=150)
btn_paper.place(x=210, y=150)
btn_result.place(x=135, y=200)
btn_exit.place(x=143, y=250)


def computer_choose():
    global choose_of_computer
    list1 = ["Rock", "Scissor", "Paper"]
    choose_of_computer = random.choice(list1)


text1 = Text(root, height=3, width=30, padx=20, pady=20, borderwidth=2)
text1.place(x=45, y=50)
text1.insert(END, "Be Ready!\n")
time.sleep(2)
text1.insert(END, "Choose one!\n")

root.mainloop()
