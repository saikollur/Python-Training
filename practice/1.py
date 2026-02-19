with open('newtxt.txt', 'w') as file:
    file.write("Creating a file in write mode.")
with open('newtxt.txt', 'r') as file:
    print(file.read())
