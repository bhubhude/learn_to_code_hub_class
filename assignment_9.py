# from tkinter import *
# from  tkinter import messagebox
# from PIL import  ImageTk, Image
#
# # 1. Simple Login Form
# # Create a simple login form using Tkinter with two labels (Username and Password), two
# # entry widgets, and a button (Login).
# # When the Login button is clicked, display a message box saying “Login Successful” if
# # the username is “user” and the password is “pass”. Otherwise, display “Invalid
# # Credentials”.
#
# try:
#     root = Tk()
#     # Center title
#     blank_space = "  "
#     root.title(blank_space * 110 + "Admire Ncube")
#     root.resizable(False,False)
#     root.geometry("1300x700+0+0")
#     try:
#         root.iconbitmap("C:\\Users\\sbhub\\PycharmProjects\\learn_to_code_hub_class\\me.ico")
#     except Exception as e:
#         messagebox.showerror("Error", f"icon file not found: {e}")
#
#     try:
#         bg_img = Image.open("C:\\Users\\sbhub\\PycharmProjects\\learn_to_code_hub_class\\IMG_20241225_094917.jpg")
#         background_image = ImageTk.PhotoImage(bg_img)
#         Label(root,image=background_image).place(x=0, y=0, width=1300,height=700)
#     except Exception as e:
#         messagebox.showerror("Error", f"Image file not found: {e}")
#
#
#
#     def clear(event,entry, placeholder):
#         if entry.get() == placeholder:
#             entry.delete(0, "end")
#             entry.config(fg="cadet blue")
#
#     user = Entry(root,width=35,fg='cadet blue',font=("arial",18,"bold"))
#     user.insert(0, "Enter username")
#     user.bind("<FocusIn>", lambda event: clear(event, user,"Enter username"))
#     user.pack(pady=20,ipady=10,ipadx=10)
#
#
#     pass_word = Entry(root,show="*",width=35,fg='cadet blue',font=("arial",18,"bold"))
#     pass_word.insert(0,"Enter password")
#     pass_word.bind("<FocusIn>", lambda event: clear(event, pass_word, "Enter password"))
#     pass_word.pack(pady=20,ipady=10,ipadx=10)
#     def login():
#         try:
#             username = user.get()
#             password = pass_word.get()
#             if username and password:
#                 messagebox.showinfo("Login", "Login successful!")
#                 user.delete(0, "end")
#                 pass_word.delete(0, "end")
#             else:
#                 messagebox.showwarning("Login", "Please enter both username and password.")
#         except Exception as e:
#             messagebox.showerror("Error", f"An unexpected error occurred during login: {e}")
#
#
#
#
#
#     login_button = Button(root,width=15, text="Login", font=("Arial", 15), bg='grey',command=login)
#     login_button.pack(pady=10,ipady=10,ipadx=10)
#
#
#     root.mainloop()
# except Exception as ee:
#     messagebox.showerror("Error", f"An unexpected error occurred: {e}")
#-------------------------------------------------------------------------------------------------------------------#

# 2. Temperature Converter
# Build a temperature converter that converts Celsius to Fahrenheit and Fahrenheit to
# Celsius.
# o Use Entry widgets to accept user input.
# o Provide Buttons for conversion and Labels to display the results.
# o Use the formula:
# ▪ Fahrenheit = (Celsius × 9/5) + 32
# ▪ Celsius = (Fahrenheit - 32) × 5/9
# import tkinter as tk
# from tkinter import messagebox
#
# class TemperatureConverter:
#
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Temperature Converter")
#         try:
#             self.window.iconbitmap("C:\\Users\\sbhub\\PycharmProjects\\learn_to_code_hub_class\\me.ico")
#         except Exception as e:
#                 messagebox.showerror("Error", f"icon file not found: {e}")
#
#
#         title = tk.Label(self.window,text="Temperature Converter",font=("arial",17,"bold"),fg="red",relief="raised")
#         title.pack()
#
#
#         # Creating  frames
#         self.celsius_frame = tk.Frame(self.window)
#         self.fahrenheit_frame = tk.Frame(self.window)
#         self.results_frame = tk.Frame(self.window)
#         self.history_frame = tk.Frame(self.window)
#         self.menu_frame = tk.Frame(self.window)
#
#         self.clear_entries_button = tk.Button(self.menu_frame,text="Clear Entries",pady=10,borderwidth=10,font=("arial", 17, "bold"),fg="cadet blue",command=self.clear_all_entries)
#         self.clear_entries_button.pack(side=tk.RIGHT)
#
#         #Celsius to Fahrenheit
#         self.celsius_label = tk.Label(self.celsius_frame, text="Celsius",font=("arial",17))
#         self.celsius_label.pack(side=tk.LEFT)
#         self.celsius_entry = tk.Entry(self.celsius_frame,width=30,borderwidth=10)
#         self.celsius_entry.pack(side=tk.LEFT)
#         self.celsius_button = tk.Button(self.celsius_frame,text="Convert to Fahrenheit",bg="yellow",font=("arial",17),command=self.celsius_to_fahrenheit)
#         self.celsius_button.pack(side=tk.LEFT)
#
#
#         #Fahrenheit to Celsius
#         self.fahrenheit_label = tk.Label(self.fahrenheit_frame,text="Fahrenheit",font=("arial",17))
#         self.fahrenheit_label.pack(side=tk.LEFT)
#         self.fahrenheit_entry = tk.Entry(self.fahrenheit_frame,width=30,borderwidth=10)
#         self.fahrenheit_entry.pack(side=tk.LEFT)
#         self.fahrenheit_button = tk.Button(self.fahrenheit_frame,text="Convert to Celsius",bg="yellow",font=("arial", 17),command=self.fahrenheit_to_celsius)
#         self.fahrenheit_button.pack(side=tk.LEFT)
#
#
#         # Result
#         self.results_label = tk.Label(self.results_frame, text="Results: ",font=("arial",17,"bold"),bg="green",fg="cadet blue")
#
#         self.results_label.pack(side=tk.LEFT)
#         self.results_value = tk.Label(self.results_frame,text="",font=("arial",17,"bold"))
#         self.results_value.pack(side=tk.LEFT)
#
#         #History
#         self.history_label = tk.Label(self.history_frame, text="Conversion History", font=("arial",17),fg="cadet blue")
#         self.history_label.pack()
#         self.history_text = tk.Text(self.history_frame, height=10,width=50,fg="grey",font=("arial",15))
#         self.history_text.pack()
#
#         # Menu
#         self.menu_label = tk.Label(self.menu_frame,pady=10,text="Menu", font=("arial",17),fg="cadet blue")
#         self.menu_label.pack(side=tk.LEFT)
#         self.clear_button = tk.Button(self.menu_frame,text="Clear History",borderwidth=10, font=("arial",17,"bold"),fg="cadet blue",command=self.clear_history)
#         self.clear_button.pack(side=tk.LEFT)
#
#         #Exit Button
#         self.exit_button = tk.Button(self.menu_frame,text="Exit",pady=10,padx=10, font=("arial",17),fg="cadet blue",command=self.window.destroy)
#         self.exit_button.pack(side=tk.LEFT)
#
#         # Packs Frames-----------------------------------------------------
#         self.celsius_frame.pack(pady=10)
#         self.fahrenheit_frame.pack(pady=10)
#         self.results_frame.pack(pady=10)
#         self.history_frame.pack(pady=10)
#         self.menu_frame.pack(pady=10)
#
#     # -----------------------------------------------------------------------------------
#         #Initialize History
#         self.history = []
#
#     def celsius_to_fahrenheit(self):
#         try:
#             celsius = float(self.celsius_entry.get())
#             fahrenheit = (celsius * 9/5) + 32
#             self.results_value.config(text= f"{fahrenheit:.2f} ⁰F")
#             self.history.append(f"{celsius} ⁰C = {fahrenheit:.2f} ⁰F")
#             self.update_history()
#         except ValueError:
#             messagebox.showerror("Error","Invalid input")
#
#     def fahrenheit_to_celsius(self):
#         try:
#             fahrenheit = float(self.fahrenheit_entry.get())
#             celsius = (fahrenheit - 32) * 5/9
#             self.results_value.config(text=f"{celsius:.2f} ⁰C")
#             self.history.append(f"{fahrenheit} ⁰F = {celsius:.2f} ⁰C")
#             self.update_history()
#         except ValueError:
#             messagebox.showerror("Error","Invalid input")
#
#
#     def update_history(self):
#         self.history_text.delete(1.0, tk.END)
#         for entry in self.history:
#             self.history_text.insert(tk.END,entry + "\n")
#
#     def clear_history(self):
#         self.history = []
#         self.update_history()
#
#
#     # Method for clearing all entries
#     def clear_all_entries(self):
#         self.celsius_entry.delete(0, tk.END)
#         self.fahrenheit_entry.delete(0, tk.END)
#
#     # Inside __init__:
#     def run(self):
#         self.window.mainloop()
#
# if __name__ == "__main__":
#     converter = TemperatureConverter()
#     converter.run()

# --------------------------------------------------------------------------------------------------#

# 3. Simple Calculator
# Create a basic calculator that can perform addition, subtraction, multiplication, and
# division.
# o Use Entry widgets for displaying the input/output.
# o Use Buttons for digits (0-9) and operators (+, -, *, /).
# o Include a Clear button to reset the calculator.

# import  tkinter as tk
# from tkinter import messagebox
#
#
# class CalculatorApp:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Simple Calculator")
#         title = tk.Label(self.window, text="Simple Calculator", relief="raised",font=("arial",24,"bold"),fg="magenta")
#         title.grid(row=0,column=0,columnspan=4)
#         self.window.geometry("400x500")
#         self.window.configure(bg="gainsboro",borderwidth=10)
#
#          # Initialise calculator app
#         self.expression = ""
#
#         # Entry widgets to display output/input
#
#
#         self.entry = tk.Entry(self.window,width=33,font=("arial",17,"bold"),bg="cadet blue",borderwidth=10,relief="ridge",justify="right")
#         self.entry.insert(0,"0")
#         self.entry.grid(row=1,column=0,columnspan=4,padx=10, pady=10)
#
#     #     Create Buttons
#         self.create_buttons()
#
#     def create_buttons(self):
#         buttons = [
#             ("7",2,0), ("8",2,1), ("9",2,2), ("/",2,3),
#             ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
#             ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
#             ("0", 5, 0), ("=", 5, 1), ("-", 5, 2), ("←", 5, 3)
#         ]
#     #      Add buttons to the grid
#         for(text, row,col) in buttons:
#             buttons_grid = tk.Button(self.window,width=5,height=2,text=text,bg="lightblue",font=("arial",18),command=lambda t=text: self.on_button_click(t))
#             buttons_grid.grid(row=row,column=col,sticky="nsew",padx=5,pady=5)
#
#         for i in range(6):
#             self.window.rowconfigure(i, weight=1)
#         for i in range(4):
#             self.window.columnconfigure(i,weight=1)
#
#     def on_button_click(self, button_text):
#         if button_text == "←":
#             self.expression = ""
#             self.update_entry()
#         elif button_text == "=":
#             try:
#                 result = eval(self.expression)
#                 self.expression = str(result)
#                 self.update_entry()
#             except Exception as e:
#                 self.expression = "Error"
#                 self.update_entry()
#         else:
#             self.expression += button_text
#             self.update_entry()
#
#
#     def update_entry(self):
#         self.entry.delete(0,tk.END)
#         self.entry.insert(0,self.expression)
#
#
#
#
#     def run(self):
#         self.window.mainloop()
#
# if __name__ == "__main__":
#     calculator = CalculatorApp()
#     calculator.run()

# 4. To-Do List App
# Build a simple To-Do List application with the following functionalities:
# o Entry widget to add new tasks.
# o Button to add tasks to the list.
# o Listbox to display tasks.
# o Button to delete selected tasks from the list.
# import tkinter as tk
# from tkinter import font
#
# class ToDoList:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("To DO List")
#         self.window.geometry("500x600")
#         self.window.iconbitmap("C:\\Users\\sbhub\\PycharmProjects\\learn_to_code_hub_class\\me.ico")
#
#     #     creating frames
#         frame = tk.Frame(self.window,width=500,height=600)
#         frame.grid(columnspan=3)
#         custom_font = font.Font(family="Lucida Calligraphy",size=24,underline=True)
#         heading = tk.Label(frame,font=custom_font,text="To Do List",fg="blue")
#         heading.grid(row=0,column=0,pady=15)
#
#     #     create list box
#         self.my_list = tk.Listbox(frame,font=("Brush  Script MT",14),border=0,
#                              highlightthickness=0,
#                              fg="grey",
#                              bg="SystemButtonFace",
#                              selectbackground="light grey",
#                              activestyle="none",
#                              width=25,
#                              height=5)
#         self.my_list.grid(row=1,column=0,sticky="nsew")
#         programming_languages =["Python","Sql","R","Javascript","Java","Kotlin"]
#         for language in programming_languages:
#             self.my_list.insert(tk.END,language)
#
#         my_scrollbar = tk.Scrollbar(frame,bg="grey")
#         my_scrollbar.grid(row=1,column=1,sticky="ns")
#         self.my_list.config(yscrollcommand=my_scrollbar.set)
#         my_scrollbar.config(command=self.my_list.yview)
#
#     #     entry widget to add items
#         self.entry_items = tk.Entry(frame,font=("Cascadia Code",12),width=40)
#         self.entry_items.grid(row=2,column=0,pady=20,padx=10)
#
#     # Creating buttons
#         btn_add = tk.Button(frame, text="Add Item",font=("Lucida Fax",12),fg="blue",command=self.add_items)
#         btn_add.grid(row=3, column=0, padx=5, sticky="w")
#
#         btn_save = tk.Button(frame, text="Save", font=("Lucida Fax", 12), fg="blue", command=self.save_items)
#         btn_save.grid(row=3, column=1, padx=5,  sticky="w")
#
#         btn_delete = tk.Button(frame, text="Delete Item",font=("Lucida Fax",12),fg="blue",command=self.delete_item)
#         btn_delete.grid(row=3, column=2, padx=5, sticky="w")
#
#         btn_exit = tk.Button(frame, text="Exit",command=self.exit_button,font=("Lucida Fax",12),fg="blue")
#         btn_exit.grid(row=3, column=3, padx=5, sticky="w")
#
#     def add_items(self):
#         new_item = self.entry_items.get()
#         if new_item:
#             self.my_list.insert(tk.END,new_item)
#             self.entry_items.delete(0,tk.END)
#
#     def delete_item(self):
#         selected_item = self.my_list.curselection()
#         if selected_item:
#             for index in selected_item:
#                 self.my_list.delete(index)
#
#     def save_items(self):
#         try:
#             with open("to_do_list", "w") as file:
#                 items = self.my_list.get(0,tk.END)
#                 for item in items:
#                     file.write(f"{item}\n")
#             print("Items saved successfully")
#         except Exception as e:
#             print(f"An error occurred while saving file {e}")
#
#
#     def exit_button(self):
#         self.window.destroy()
#
#     def root(self):
#         self.window.mainloop()
#
# if __name__ == "__main__":
#     to_do_list = ToDoList()
#     to_do_list.root()
#

# 5. Quiz Application
# Design a basic quiz application that asks 5 multiple-choice questions.
# o Use Labels for questions and Radiobuttons for options.
# o Provide a Submit button that shows the score after completing all questions.
# o Display the score using a message box.

import tkinter as tk
from tkinter import messagebox
from tkinter import font
questions = [

{"Question":"1. In which year Matebeleland defeated by  the British South Africa Company?",
"Option":[1987,1893,1921,1981],
"Correct":1893
},

{"Question":"2. In which year did Zimbabwe and North Korea committed genocide killing people of Matebeleland ?",
"Option":[1955,1896,1979,1980],
"Correct":1980
},
{"Question":"3. Which liberation army fought along with Zipra force in 1970s ?",
"Option":["Umkhonto Wesizwe","M23", "Frelimo","PAC"],
"Correct":"Umkhonto Wesizwe"
},
{"Question":"4. Which border separate Matebeleland and Zimbabwe ?",
"Option":["Ramagwebana","David Livingston","Jameson Line","Beitbridge"],
"Correct":"Jameson Line"
},
{"Question":"5. Which river separate Matebeleland and South Africa ?",
"Option":["Limpopo","Zambezi","Manzamnyama","Mzingwane"],
"Correct":"Limpopo"
}
]
class QuizApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("\t Quiz Application")
        self.root.geometry("800x500+0+0")
        try:
            self.root.iconbitmap("C:\\Users\\sbhub\\PycharmProjects\\learn_to_code_hub_class\\me.ico")
        except Exception as e:
            messagebox.showerror("Error",f"Icon image not found {e}")


        # creating fonts
        my_font = font.Font(family="Book Antiqua",size=14,underline=True)
        self.frame = tk.Frame(self.root,width=800,height=500,border=10)
        self.frame.pack()

        heading_text = tk.Label(self.frame,text="Quiz Application",font=my_font,fg="blue")
        heading_text.pack(side=tk.TOP)

        self.current_question = 0
        self.score = 0

        # Variable to store a selected answer
        self.selected_answer = tk.StringVar()

        # question label
        self.question_label = tk.Label(self.frame,text="",font=("Book Antiqua",12), anchor="w")
        self.question_label.config(wraplength=700)
        self.question_label.pack(pady=20)

    #     Radio buttons for options
        self.option_btn = []
        for i in range(4):
            button = tk.Radiobutton(self.frame,text="", variable=self.selected_answer, font=("Book Antiqua", 12, "bold"),
                                         fg="black", anchor="w",width=50)
            button.pack(pady=5)
            self.option_btn.append(button)

        # back button
        self.back_btn = tk.Button(self.frame, text="<<", font=("Book Antiqua", 12, "bold"), bg="cadet blue",
                                     fg="black", command=self.back_button)
        self.back_btn.pack(padx=10,pady=10,side=tk.LEFT)

    #        Next label
        self.next_button = tk.Button(self.frame, text=">>", font=("Book Antiqua", 12,"bold"),bg="cadet blue",fg="black",command=self.next_question)
        self.next_button.pack(padx=10,pady=10,side=tk.LEFT)


        self.submit_btn = tk.Button(self.frame, text="Submit_quiz", font=("Book Antiqua", 12, "bold"), bg="cadet blue",
                                     fg="black", command=self.submit_button)
        self.submit_btn.pack(padx=10,pady=10,side=tk.LEFT)

        self.exit_btn = tk.Button(self.frame, text="Exit", font=("Book Antiqua", 12, "bold"), bg="cadet blue",
                                     fg="black", command= self.exit)
        self.exit_btn.pack(padx=10,pady=10,side=tk.LEFT)

    #     display the current question
        self.display_question()


    # Back button function
    def back_button(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.selected_answer.set("")
            self.display_question()

        if self.current_question == 0:
            self.back_btn.config(state="disabled")
        else:
            self.back_btn.config(state="normal")

        if self.current_question == len(questions)-1:
            self.back_btn.config(state="disabled")
        else:
            self.back_btn.config(state="normal")

    # Check if answer is correct and update the question
    def next_question(self):
        if self.selected_answer.get() != "":
            if self.selected_answer.get() == str(questions[self.current_question]["Correct"]):
                self.score += 1

        #move to the next question
        # self.score =+ 1
        self.current_question += 1

        if self.current_question < len(questions):
            self.selected_answer.set("")
            self.display_question()

        else:
            self.next_button.config(state="normal" if self.current_question > 0 else "disabled")
            self.submit_btn.config(state="normal")

    # display current question
    def display_question(self):
        try:
            current_q = questions[self.current_question]
            self.question_label.config(text=current_q["Question"])

            #update the options for current question
            for i, option in enumerate(current_q["Option"]):
                self.option_btn[i].config(text=option, value=str(option))
        except IndexError:
            messagebox.showerror("Error","Index is out of range")
        except Exception as e:
            messagebox.showerror("Error","An unexpected error occurred :{e")

    def submit_button(self):
        messagebox.showinfo("Quiz answers successfully submitted",f"Your score is : {self.score} out of {len(questions)} ")
        if not questions and self.current_question == len(questions):
            messagebox.showerror("Error","No question available or index is out of range")

    def exit(self):
        self.root.quit()
        self.root.destroy()


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    application = QuizApplication()
    application.run()
