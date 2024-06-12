file = input("Enter name of the source file: ")
with open("new_text.txt","r")as file:
    contain = file.read()
    copy = input("Enter the name of the destination file: ")
    with open(copy,"w")as file:
        copied = file.write(contain)
        print("copied Successful ")
