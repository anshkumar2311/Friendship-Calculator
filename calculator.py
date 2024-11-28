from tkinter import *
import random

#size and header
root = Tk()
root.geometry('430x300')
root.title('Friendship Percentage Calculator?????')


def calculate_friendship():
    # name entry
    name1_val = name1.get().strip()
    name2_val = name2.get().strip()

    if name1_val == "" or name2_val == "":
        result.config(text="Please enter both names!", fg="red")
    else:
        #random percentage
        percentage = random.randint(10, 100)

        #friendship strength
        if percentage > 80:
            strength = "Strong 🌟"
            color = "green"
        elif 50 <= percentage <= 80:
            strength = "Moderate 😊"
            color = "blue"
        elif 30 <= percentage < 50:
            strength = "Weak 😐"
            color = "dark orange"
        else:
            strength = "Poor 😞"
            color = "red"

        # Display the result
        result.config(
            text=f"The friendship between {name1_val} and {name2_val} is {percentage}% is {strength}!\nStrength: {strength}",
            fg=color)


# Heading
heading = Label(root, text='Friendship Calculator - Discover Your Friendship Strength!',font=('Helvetica',11,"bold"),fg='teal')
heading.pack(pady=10)

# Name 1
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=3, width=30)
name1.pack()

# Name 2
slot2 = Label(root, text="Enter Your Friend's Name:")
slot2.pack()
name2 = Entry(root, border=3, width=30)
name2.pack()

# Calculate Button
bt = Button(root, text="Calculate", height=2, width=12, bg="lightblue", command=calculate_friendship)
bt.pack(pady=10)

# Result Label
result = Label(root, text='Friend Percentage between both of you:')
result.pack()

root.mainloop()
