textname = input("Enter a text Pls: ")
with open("new_text.txt","w")as file:
    container = file.write(textname)
    print(f"Total words in the file:{container}:")
