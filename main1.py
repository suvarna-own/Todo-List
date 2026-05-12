todos=[]
while True: 
    input_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    match input_action:
        case "add":
            print("Adding a new todo item.")
            todo = input("Enter the todo item: ").strip()
            todos.append(todo + "\n") 
            file = open("todos.txt", "w")
            file.writelines(todos)
        case "show":
            print("Showing all todo items.")
            file = open("todos.txt", "r")
            todos = [line.strip() for line in file]
            file.close()    
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
        case "edit":
            print("Editing an existing todo item.")
        case "complete":
            print("Completing an existing todo item.")
        case "exit":
            print("Exiting the program.")
            break
            
                
