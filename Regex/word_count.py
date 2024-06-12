textname = input("Enter a text Pls: ")
with open("text.txt","w")as file:
    container = file.write(textname)
    print(f"Total words in the file:{container}:")
