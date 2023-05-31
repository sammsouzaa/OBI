teste = 0

while True:
    retangulos = int(input())

    if retangulos == 0:
        break

    listx1 = [retangulos]
    listy1 = [retangulos]
    listx2 = [retangulos]
    listy2 = [retangulos]

    for i in range(retangulos):

        x1, y1, x2, y2 = list(map(int, input().split()))

        listx1[i] = x1
        listy1[i] = y1
        listx2[i] = x2
        listy2[i] = y2
    
    x1Principal = max(listx1)
    y1Principal = min(listy1)
    x2Principal = min(listx2)
    y2Principal = max(listy2)

    teste = teste + 1

    print("Teste", teste)
    print(x1Principal, y1Principal, x2Principal, y2Principal)
    print("")