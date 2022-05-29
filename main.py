import tkinter as tk
import random
from tkinter import messagebox

count = 0
answer_list = []
answer_dic = {}
flag = 0

def onClick(b,num, lst,root):
    global count,answer_list,answer_dic,flag
    if b["image"] == '' and count < 2:
        b.config(image=lst[num], width=110, height=100)

        #add image to answerList
        answer_list.append(lst[num])

        #add button and image to answer dictionary
        answer_dic[b] = lst[num]

        #increment counter
        count += 1

        #increment flag
        flag += 1

    if len(answer_list) == 2:
        #check if the user picks r the same
        if answer_list[0] == answer_list[1] and count == 2:
            for b in answer_dic.keys():
                b["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dic = {}
        else:
            flag -= 2
            count = 0
            answer_list = []
            messagebox.showerror("MESSAGE", "incorrect")
            for b in answer_dic.keys():
                b.config(image='', width=15, height=7)
            answer_dic = {}
    #restart the game or quit the game
    if flag == 12:
        flag = 0
        choice = messagebox.askyesno("Message", "wanna play again?")
        if choice == True:
            setTheGame(lst,root)
        else:root.quit()









def setTheGame(lst, root):

 b0 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b0, 0, lst, root))
 b1 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b1, 1, lst, root))
 b2 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b2, 2, lst, root))
 b3 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b3, 3, lst, root))
 b4 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b4, 4, lst, root))
 b5 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b5, 5, lst, root))
 b6 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b6, 6, lst, root))
 b7 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b7, 7, lst, root))
 b8 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b8, 8, lst, root))
 b9 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b9, 9, lst, root))
 b10 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b10, 10, lst, root))
 b11 = tk.Button(root, image='', width=15, height=7,  command=lambda:onClick(b11, 11, lst, root))

 b0.grid(row=0, column=0)
 b1.grid(row=0, column=1)
 b2.grid(row=0, column=2)
 b3.grid(row=0, column=3)

 b4.grid(row=1, column=0)
 b5.grid(row=1, column=1)
 b6.grid(row=1, column=2)
 b7.grid(row=1, column=3)

 b8.grid(row=2, column=0)
 b9.grid(row=2, column=1)
 b10.grid(row=2, column=2)
 b11.grid(row=2, column=3)




def main():
    root = tk.Tk()

    cards = {}

    root.title("Card-Game")
    root.geometry("1000x700")
    root.configure(background='lightblue')
    root.resizable(False, False)

    apple_img = tk.PhotoImage(file='res/apple.png')
    banana_img = tk.PhotoImage(file='res/bananas.png')
    melon_img = tk.PhotoImage(file='res/melon.png')
    kiwi_img = tk.PhotoImage(file='res/kiwi.png')
    orange_img = tk.PhotoImage(file='res/orange.png')
    watermelon = tk.PhotoImage(file='res/watermelon.png')

    cards[1] = apple_img
    cards[2] = banana_img
    cards[3] = melon_img
    cards[4] = kiwi_img
    cards[5] = orange_img
    cards[6] = watermelon
    lst = []

    my_frame = tk.Frame(root)
    my_frame.pack(pady=100)

    for x in cards.values():
        for y in range(2):
            lst.append(x)
    random.shuffle(lst)
    setTheGame(lst, my_frame)

    root.mainloop()






if __name__ == "__main__":
    main()







