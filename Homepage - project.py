import tkinter as tk

root = tk.Tk()
root.geometry("1280x720")
root.title("Stone Paper Scissors GAME")

# Background image
bg_image = tk.PhotoImage(file="C://Users//Rahul//Downloads//bgimage (1).png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title label
title_label = tk.Label(root, text="STONE PAPER & SCISSORS !", font=("Kyomadoka", 36),fg='white',bg='violet')
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Name label
name_label = tk.Label(root, text="Enter your name:", font=("Consolas", 18))
name_label.place(relx=0.5, rely=0.4, anchor="center")

# Name input field
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var, font=("Helvetica", 18))
name_entry.place(relx=0.5, rely=0.5, anchor="center")

# Play button
play_button = tk.Button(root, text="Play", font=("Helvetica", 18), bg="#00b300", fg="white", width=10, height=2)
play_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()



