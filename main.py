todos = []
while True:
    item=input("Enter a todo item (add,edit,update,delete,exit): ").strip()
    match item:
        case "add":
            print("Adding a new todo item.")
            new_item = input("Enter the todo item: ").strip()
            todos.append(new_item)
        case "show":
            print("Showing all todo items.")
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
        case "update":
            print("Updating an existing todo item.")
        case "delete":
            print("Deleting an existing todo item.")
        case _:
            print("Exiting the program.")
            break        