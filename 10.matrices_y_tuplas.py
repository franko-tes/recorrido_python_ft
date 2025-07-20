#las listas de listas se conocen como MATRICES
#separamos en FILAS y COLUMNAS para acceder a cada posicion

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print("\nTenemos nuestra 'MATRIZ' que contiene 3 listas que cada una contiene a su vez 3 elementos")
print("Matriz:",matriz)
print("Nos traemos el elemento '0' y nos devuelve la primera lista:",matriz[0])

#los corchetes que encierran a las listas, nos determinan las dimensiones que tenemos en nuestra matriz
#esto nos determinara la posicion de cada elemento
#debemos prestar atencion para saber como ubicar su posicion y traer el valor

#agregamos otra dimension en un ejemplo
caja = [[[1,2],[3,4]],[[5,6],[7,8]]]
print("\nEn este ejemplo tenemos 1 lista que dentro tiene 2 listas que tienen 2 elementos ")
print("caja: es nuestra lista completa",caja)
print("\nDentro de caja tenemos 2 listas:")
print("La posicion '0':",caja[0])
print("La posicion '1':",caja[1])
print("\nEstas a su vez tienen 2 listas:")
print("La posicion '0' de la posicion '0' anterior es:",caja[0][0])
print("La posicion '1' de la posicion '0' anterior es:",caja[0][1])
print("\nY nos traemos los elementos que estan dentro:")
print("La posicion '0' de la posicion '0' de la posicion '0' es:",caja[0][0][0])
print("La posicion '0' de la posicion '1' de la posicion '0' es:",caja[0][1][0])

#tuplas
#las tuplas se escriben con parenteses '()'
#su tipo de clase es 'tuple'
numeros = (1,2,3,4,5)
print("\nLas 'TUPLAS' las definimos entre parentesis")
print("numeros:",numeros)
print("Clase:",type(numeros))
print("Si no usamos los parentesis, Python lo interpreta como 'TUPLA'")

#probamos traernos un valor de la tupla
print("\nDe la misma forma podemos traernos 'indexar' valores de esta tupla")
print("Nos traemos la posicion '0':",numeros[0])

#las tuplas son inmutables, no podemos modificarlas
print("Las 'TUPLAS' son inmutables, no podemos modificarlas")