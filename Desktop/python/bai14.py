numInput = input()
listNum = [i for i in numInput.split(',')]
for item in listNum:
    intp = int(item,2)
    if not intp%5:
        print(item)

