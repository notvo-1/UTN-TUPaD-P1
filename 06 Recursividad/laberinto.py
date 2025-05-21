def show_camino(laberinto, camino):
    for i in range(len(laberinto)):
        for k in range(len(laberinto[i])):
            if [i,k] == [0,0]:
                print("0",end="")
            elif [i,k] in camino:
                print(".", end="")
            else:
                print("#", end="")
        print("")
    
def resolver_laberinto(laberinto, x, y, camino,count):
         
    print(count)
    
    if x == len(laberinto)-1 and y == len(laberinto[-1])-1:
        print(f"LLegaste al final! el resultado es {camino}")
        return show_camino(laberinto, camino)
    elif y != (len(laberinto[x])-1) and laberinto[x][(y + 1)] == 0 and [x,y+1] not in camino:
        camino.append([x,y + 1])
        x, y = x, y + 1
    elif x != (len(laberinto)-1) and laberinto[x + 1][y] == 0 and [x +1 , y] not in camino:
        camino.append([x + 1, y])
        x, y = x +1, y
    elif  x != 0 and laberinto[x-1][y] == 0 and [x-1, y] not in camino:
        camino.append([x-1, y])
        x, y = x - 1, y
    elif  y != 0 and laberinto[x][y-1] == 0 and [x, y -1] not in camino:
        camino.append([x, y -1])
        x , y = x, y -1
    else:
        if len(camino)==0:
            print("no tiene solucion")
            return camino
        else:
            if count > 500:
                print("no solution")
                return show_camino(laberinto, camino)
            else:
                print("Ups!")
                x, y = camino[-2]
            
    count += 1
    
    resolver_laberinto(laberinto, x, y, camino, count)
    
            

laberinto = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
    
] #resuelve

laberinto1 = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
]
laberinto2 = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]

laberinto3 = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0]
] #no lo resuelve


laberinto4 = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
] #sin solucion desde 0,0


camino = []
resolver_laberinto(laberinto2, 0, 0, camino,0) #laberinto, x, y, camino, cuenta
