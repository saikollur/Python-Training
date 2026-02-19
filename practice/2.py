with open('new.txt', 'w') as file1:
    file1.write("Hello, all.")
with open('new.txt', 'r') as file1:
    with open('copy.txt', 'w') as file2:
        file2.write(file1.read())
    with open('copy.txt', 'r') as file2:
        print(file2.read())
