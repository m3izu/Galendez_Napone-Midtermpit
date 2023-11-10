import sys
import subprocess
import tkinter as tk
import threading
import time
import webbrowser

# Printing a title using ASCII art
print("▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .\n██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·\n██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄\n▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌\n ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀")

# Function to prompt the user to press 1 to proceed
def input1():
    print("Press 1 to Proceed:")

# Calling the function to prompt user input
input1()

# Function to check if user input is '1', otherwise exit
def proceed():
    useri = input()
    if useri == '1':
        pass
    else:
        print("You Failed")
        sys.exit(0)

# Definitions of image filenames
E1 = "E1.jpg"
E2 = "E2.jpg"
E3 = "E3.jpg"
E4 = "E4.jpg"
E5 = "E5.jpg"

# Prompting the user to press 1
proceed()

# Storytelling and displaying images
print("You are but a lonely adventurer stuck in a cave full of professors who would grade you a failing mark")
proceed()
print("In order to escape the cave, you must solve their problems to get a passing grade and destroy the final boss")
proceed()
print("SIR RALPH!!!")
proceed()
subprocess.run(['start', E1], shell=True)
print("Albert: \'You are facing me!\'")
proceed()

# Quiz on famous equations
Ques1 = (input("What is the famous equation that expresses the fact that mass and energy are the same physical entity and can be changed into each other?\n Type:   A. e=mc^2 B. a^2+b^2=c^2 C. F=ma D. v-e+f=2 "))

# Checking the user's answer and providing feedback
if Ques1 == "A":
    print("Correct! E=mc^2 is one of the most famous equations in physics...")
elif Ques1 == "B":
    print("Wrong! The Pythagorean theorem is a fundamental principle in geometry...")
    sys.exit(0)
elif Ques1 == "C":
    print("Wrong! The equation F=ma represents Newton's second law of motion...")
    sys.exit(0)
elif Ques1 == "D":
    print("Wrong! The equation \"V - E + F = 2\" is known as Euler's formula...")
    sys.exit(0)
else:
    print("You chose none of the given letters. YOU DIE")
    sys.exit(0)

# Continuing the story
proceed()
print("*Albert succumbed and died because he wasn't able to fail the user*")
proceed()
subprocess.run(['start', E2], shell=True)
print("Nikola: I'll be giving you a hint, P = V x I cos(0)")
proceed()

# Quiz on electrical power
print(" In a circuit with a voltage of 120 volts and a current of 5 amperes, if the phase angle (θ) between the voltage and current waveforms is 45 degrees, what is the power (P) dissipated in the circuit?")
Ques2 = input("Answer Directly, given answer doesn't need its decimal numbers")

# Checking the user's answer and providing feedback
if Ques2 == "424":
    print("Correct! \nV (voltage) = 120 volts ...")
else:
    print("You Failed!")
    sys.exit(0)

# Continuing the story
proceed()
print("You defeated Nikola. On to the Next Opponent!!!")
proceed()
subprocess.run(['start', E3], shell=True)
print("Robert: Good Evening ")
proceed()
print("It would seem you have defeated two opponents already")
proceed()
print("Nonetheless, I am no one but an ally.")
proceed()
print("Take this, it will be useful for your future endeavors. A tool that would be of much use when facing your last two opponents")
proceed()
print("\033 You Have Obtained a Calculator \033")
proceed()
print("\' HINT: Do not close your calculator")

# Function to run a simple calculator using Tkinter
def run_calculator():
    # Nested functions for calculator functionality
    def evaluate_expression(expression):
        try:
            result = str(eval(expression))
            entry_var.set(result)
            return result
        except Exception as e:
            entry_var.set("Error")
            return str(e)

    def on_button_click(value):
        current_text = entry_var.get()
        if value == "=":
            evaluate_expression(current_text)
        elif value == "C":
            entry_var.set("")
        else:
            entry_var.set(current_text + str(value))

    # Creating the calculator window
    root = tk.Tk()
    root.title("Simple Calculator")

    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    row_val = 1
    col_val = 0

    # Creating calculator buttons
    for button in buttons:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                  command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Running the calculator window
    root.mainloop()

# Creating a thread to run the calculator concurrently
calculator_thread = threading.Thread(target=run_calculator)
calculator_thread.start()

# Continuing the story
proceed()
subprocess.run(['start', E4], shell=True)
print("I'm ADA!!!")
proceed()
print("I'll be destroying you with some time trial questions!!")
proceed()

# Function to print questions and get user answers
def print_question(question, options):
    print(question)
    for option in options:
        print(option)

def get_user_answer():
    return input("Your answer (enter the number): ").strip()

# Time trial quiz
def quiz():
    questions = [
        {"question": "What happens if a number is divided by 0?", "options": ["1. Complex Infinity", "2. One", "3. Undefined", "4. IDK"], "answer": "1"},
        {"question": "What is Base10?", "options": ["1. Hexadecimal", "2. Decimal", "3. Octal", "4. Binary"], "answer": "2"},
        {"question": "What number system starts a '0b'", "options": ["1. Decimal", "2. Binary", "3. Hexadecimal", "4. Octal"], "answer": "2"},
    ]

    time_limit = 15

    print("Welcome young one! You have {} seconds to complete it.".format(time_limit))
    time.sleep(1)

    start_time = time.time()

    for i, q in enumerate(questions, 1):
        print("\nQuestion {}: ".format(i))
        print_question(q["question"], q["options"])

        user_answer = get_user_answer()

        if user_answer == q["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is: {}".format(q["answer"]))
            print("You chose the wrong answer. Quiz over!")
            proceed()
            sys.exit(0)

        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit:
            print("Time's up! You ran out of time.")
            proceed()
            sys.exit(0)

    print("\nQuiz completed!")

# Running the time trial quiz
if __name__ == "__main__":
    quiz()

# Continuing the story
proceed()

print("On to the last boss...")
print(" ______     __     ______        ______     ______     __         ______   __  __    \n/\  ___\   /\ \   /\  == \      /\  == \   /\  __ \   /\ \       /\  == \ /\ \_\ \  \n\ \___  \  \ \ \  \ \  __<      \ \  __<   \ \  __ \  \ \ \____  \ \  _-/ \ \  __ \ \n \/\_____\  \ \_\  \ \_\ \_\     \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\    \ \_\ \_\ \n  \/_____/   \/_/   \/_/ /_/      \/_/ /_/   \/_/\/_/   \/_____/   \/_/     \/_/\/_/")
proceed()

# Final boss battle
print("ho..")
proceed()
print("ho...")
proceed()
print("You have made it this far little one")
proceed()
print("PREPARE TO MEET YOUR MAKER!")
proceed()
subprocess.run(['start', E5], shell=True)
webbrowser.open("Boss.wav")
proceed()
print("You will die here!!!")
proceed()
print("\'Hint: Now's the time to use the calculator, Sir Ralph will attack you with some basic arithmetic questions")

# Function to print questions and get user answers for the final boss battle
def print_question2(question, options):
    print(question)
    for option in options:
        print(option)

def get_user_answer2():
    return input("Your answer (enter the number): ").strip()

# Final boss battle quiz
def quiz2():
    questions = [
        {"question": "7656 multiply by 76173 =", "options": ["1. 583,180,487", "2. 643,656,853", "3. 734,854,422", "4. 583,180,488"], "answer": "4"},
        {"question": "52167 divided by 725 ", "options": ["1. 71", "2. 65", "3. 53", "4. 70"], "answer": "1"},
        {"question": "7632 plus 6325426 divided by 23", "options": ["1. 643,864", "2. 642,854", "3. 282,650", "4. 654,864"], "answer": "3"},
    ]

    time_limit2 = 30

    print("You have {} seconds to complete it.".format(time_limit2))
    time.sleep(1)

    start_time = time.time()

    for i, q in enumerate(questions, 1):
        print("\nQuestion {}: ".format(i))
        print_question(q["question"], q["options"])

        user_answer = get_user_answer()

        if user_answer == q["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is: {}".format(q["answer"]))
            print("You chose the wrong answer. Quiz over!")
            proceed()
            sys.exit(0)

        elapsed_time2 = time.time() - start_time

        if elapsed_time2 > time_limit2:
            print("Time's up! You ran out of time.")
            proceed()
            sys.exit(0)

    print("\nQuiz completed!")

# Running the final boss battle quiz
if __name__ == "__main__":
    quiz2()

# Continuing the story
proceed()
print("YOU WON!!!")
proceed()
print("Due to us meeting our deadline in a few minutes. We won't be able to make a proper salutations. BUT nonetheless, YOU WON!! Congrats!!")
proceed()
print("made by")
print("Jobert and Franco")
sys.exit(0)
