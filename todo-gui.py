# import FreeSimpleGUI as sg

# todo_list = []

# # 1. Define the layout (list of lists)
# layout = [
#     [sg.Text("Type in a Todo:")],
#     [sg.InputText(key="-inputs-"),sg.Button("Add"),sg.Button("Clear")],
#     [sg.Text("Todo List:")],
#     [sg.Listbox(values=todo_list, key="-todo-list-", size=(40, 10))]
# ]

# # 2. Create the window
# window = sg.Window("My Todo App", layout)

# # 3. Event Loop
# while True:
#     event, values = window.read()
    
#     # Check if user closed window or clicked Exit
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
    
#     if event == "Add":
#         # Access input value using its key
#         todo_item = values["-inputs-"]
#         todo_list.append(todo_item)
#         window["-todo-list-"].update(values=todo_list)
#         print(f"Todo added: {todo_list}")
#         window["-inputs-"].update(value="")

#     if event == "Clear":
#         todo_list.clear()
#         window["-todo-list-"].update(values=todo_list)
#         print("Todo list cleared!")

# # 4. Close the window
# window.close()


from unittest import case

import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# list_box = sg.Listbox(values=functions.get_todos(), key="todos",
#                       enable_events=True, size=(45, 10))
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=(40, 5))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button]
                   ]
                  )

while True:
    event, values = window.read()
    print(f"event, {event}")
    print(f"values, {values}")
    
    if event == "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
    
    if event == "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

            window["todos"].update(values=todos)
      
    if event == "sg.WIN_CLOSED":
                break

window.close()
