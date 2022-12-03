USE_APPEND = False

member = input("Add a new member: ")
member

if USE_APPEND:
    file = open('members.txt', 'a')
    file.write(member)                                              # just append the new member
else:
    file = open('members.txt', 'r')
    members = [member.strip() for member in file.readlines()]       # get a list of members without \n
    file.close()

    print(members)
    members.append(member)                                          # append member
    print(members)

    file = open('members.txt', 'w')
    file.writelines(f'{member}\n' for member in members)            # rewrite the file appending \n to each member
    file.close()
