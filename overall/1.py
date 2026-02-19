with open('newFile1.txt', 'w') as file:
    try:
        l = list(map(int, input().split()))
        file.write(str(l))
    except ValueError:
        print("Invalid value!")

with open('newFile1.txt', 'r') as file:
    with open('newFile2.txt', 'w') as file2:
        total = 0
        count = 0

        data = file.read()
        data = data.strip('[]')
        data = data.replace(',', '')
        for i in data.split():
            total += int(i)
            count += 1

        file2.write(f'Total sum : {total} \nAverage : {str(total/count)}')

    with open('newFile2.txt', 'r') as file2:
        print(file2.read())
