def p_number(i):
    i = 0
    numbers = []
    while i < i_number:
        print("At the top i is %d"%i)
        numbers.append(i)
        i = i + 1
        print("Numbers now: ",numbers)
        print("At the bottom i is %d"%i)    
    print("The numbers: ")
    for num in numbers:
        print(num)

i_number = int(input("Please input the number: "))
p_number(i_number)

