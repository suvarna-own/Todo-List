new_member = input("Add a new member: ")

file = open("member.txt", "a")
file.write(f"{new_member}" + "\n")
file.close()