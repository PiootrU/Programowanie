


number = input("Podaj ile liczb kolejnych ciągu fibonacciego chcesz wyświetlić:")

number = int(number)
list = [0, 1]
def series(list):
    add = list[-1] + list[-2]
    list.append(add)
    print(list[1:number+1])
    return series(list)
series(list)
