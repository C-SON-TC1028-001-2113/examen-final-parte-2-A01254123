def matrizppal():
    lista=[]
    fila= int(input())
    columna=int(input())
    if fila>0 and columna>0: 
        for i in range(fila):
            lista.append([])
            for j in range(columna):
                valores=int(input())
                lista[i].append(valores)
    else: 
        print('Error')
    return lista

def main():
    matriz = matrizppal()
    listaColumna = []
    if len(matriz) > 0:
        for i in range(len(matriz[0])):
            count = 0
            for j in range(len(matriz)):
                count += matriz[j][i] 
            listaColumna.append(count)
        print(listaColumna)
if __name__=='__main__':
    main()