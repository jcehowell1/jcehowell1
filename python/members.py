new_member = input("Add a new member: ") ## Get input from user

file = open('python/members.txt', 'r') ## Variable to open the file so previous contents are not overwritten
members = file.readlines()
file.close()

members.append(new_member + "\n")

file = open('python/members.txt', 'w')
members = file.writelines(members)
file.close()

# member = input("Add a new member: ")

# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()

# existing_members.append(member + "\n")

# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()