# import FreeSimpleGUI as sg

# label = sg.Text("Type in to do list")
# copy_button = sg.Button("Copy") 
# input_box = sg.Input()
# add_button = sg.Button("Add")

# window = sg.Window("To Do List", layout=[[label], [input_box, copy_button, add_button]])
# window.read()
# window.close()

# import FreeSimpleGUI as sg

# # 1. Define the layout (list of lists)
# layout = [
#     [sg.Text("Enter your name:")],
#     [sg.InputText(key="-inputs-")],
#     [sg.Button("Submit"), sg.Button("Exit")]
# ]

# # 2. Create the window
# window = sg.Window("My First GUI App", layout)

# # 3. Event Loop
# while True:
#     event, values = window.read()
    
#     # Check if user closed window or clicked Exit
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
    
#     if event == "Submit":
#         # Access input value using its key
#         user_name = values["-inputs-"]
#         sg.popup(f"Hello, {user_name}!")

# # 4. Close the window
# window.close()

# File-Zip GUI
# import FreeSimpleGUI as sg

# # 1. Define the layout (list of lists)
# layout = [
#     [sg.Text("Select a file to compress:"),sg.InputText(key="-inputs-"),sg.FilesBrowse("Choose")],
#     [sg.Text("Select destination folder:"),sg.InputText(key="-inputs-"),sg.FolderBrowse("Choose")],
#     [sg.Button("Compress")]
# ]

# # 2. Create the window
# window = sg.Window("File zipper", layout)

# # 3. Event Loop
# while True:
#     event, values = window.read()
    
#     # Check if user closed window or clicked Exit
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
    
#     if event == "Compress":
#         # Access input value using its key
#         user_name = values["-inputs-"]
#         sg.popup(f"Hello, {user_name}!")

# # 4. Close the window
# window.close()


#Improved File-Zip GUI
import FreeSimpleGUI as sg
import zipfile
from pathlib import Path

# 1. Define the layout (list of lists)
layout = [
    [sg.Text("Select a file to compress:"),sg.InputText(key="-files-inputs-"),sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder:"),sg.InputText(key="-folder-inputs-"),sg.FolderBrowse("Choose")],
    [sg.Button("Compress")]
]

# 2. Create the window
window = sg.Window("File zipper", layout)

# file_paths = [
#     "/home/user/documents/report.pdf",
#     "C:\\Users\\Admin\\Desktop\\notes.txt",
#     "data/images/photo.png"
# ]


# 3. Event Loop
files_to_zip = []
while True:
    event, values = window.read()
    
    # Check if user closed window or clicked Exit
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    if event == "Compress":
        file_paths = values["-files-inputs-"].split(";")
    # print(file_paths)  # This will print the list of file paths to the console")    

    for path_str in file_paths:
      path_obj = Path(path_str)
      files_to_zip.append(path_obj.name)
      
    # print(files_to_zip)

    # Access input value using its key
    # files_to_zip = values["-files-inputs-"].split(";")  # Split the string of file paths into a list
    destination_folder = values["-folder-inputs-"]
    zip_name = f"{destination_folder}.zip"  # Get the last part of the folder path as zip name
    print(f"files to zip, {files_to_zip}!")
    print(f"destination folder, {destination_folder}!")

  
# Use 'w' mode to create a new file; ZIP_DEFLATED enables compression
with zipfile.ZipFile(f'{zip_name}', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        zipf.write(file)
print("Files have been zipped successfully!")


