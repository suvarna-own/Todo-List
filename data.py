todos=[]
loves = []
while True: 
    input_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    match input_action:
        case "add":
            print("Adding a new todo item,please add.")
            todo = input("Enter the todo item: ").strip()
            todos.append(todo + "\n") 
            file = open("todos.txt", "w")
            file.writelines(todos)
        case "show":
            print("Showing all todo items.")
            file = open("love.txt", "r")
            loves.append("\n")
            loves=file.readlines()
            # loves = [line.strip() for line in file]
            file.close()    
            for index, love in enumerate(loves):
                print(f"{index + 1}. {love}")
        case "edit":
            print("Editing an existing todo item.")
        case "complete":
            print("Completing an existing todo item.")
        case "exit":
            print("Exiting the program.")
            break
            
                
