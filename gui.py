# import FreeSimpleGUI as sg

# label = sg.Text("Type in to do list")
# copy_button = sg.Button("Copy") 
# input_box = sg.Input()
# add_button = sg.Button("Add")

# window = sg.Window("To Do List", layout=[[label], [input_box, copy_button, add_button]])
# window.read()
# window.close()

import FreeSimpleGUI as sg

# 1. Define the layout (list of lists)
layout = [
    [sg.Text("Enter your name:")],
    [sg.InputText(key="-inputs-")],
    [sg.Button("Submit"), sg.Button("Exit")]
]

# 2. Create the window
window = sg.Window("My First GUI App", layout)

# 3. Event Loop
while True:
    event, values = window.read()
    
    # Check if user closed window or clicked Exit
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    if event == "Submit":
        # Access input value using its key
        user_name = values["-inputs-"]
        sg.popup(f"Hello, {user_name}!")

# 4. Close the window
window.close()
