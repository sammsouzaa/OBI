cartas, vezes= list(map(int, input().split()))
listacartas1 = input().split()
listacartas2 = input().split()
for i in range(vezes):
    x, y = list(map(int, input().split()))
    z = x
    while z <= y:
        listacartas1[x-1], listacartas2[x-1] = listacartas2[x-1], listacartas1[x-1]
        z += 1
print(" ".join(listacartas1))