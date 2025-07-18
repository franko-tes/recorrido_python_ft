#las listas almacenan la informacion entre corchetes.
#por ejemplo, si armamos una lista de viaje llamada to_do, se veria asi:

print("--LISTAS--")

to_do = ["llegar al hotel",
         "almorzar",
         "visitar un museo",
         "regresar al hotel"]
print("\nElementos en la lista to_do: ", to_do)

#creamos otra lista de numeros
numbers = [1,2,3,4,"cinco"]
print("\nElementos de la lista numbers: ", numbers)

#las listas son de tipo clase 'list' (es una palabra reservada).
print("\n1.Las listas son de tipo clase: 'list'")
print("to_do: ", type(to_do))
print("numbers: ", type(numbers))

#veamos una lista con distintos tipos de clase
print("\n2.Una lista con distintos tipos de clase:")
mix = ["uno", 2, 3.14, True, [1,2,3]]
print("Lista mix: ", mix)

#si queremos consultar la longitud o cantidad de elementos
print("Usamos 'len' para ver su longitud o cantidad de elementos: cantidad", len(mix))

#indexacion
#traernos el elemento que necesitemos
print("\n3.Indexacion")
print("Podemos traernos el elemento que necesitemos")
print("Por ejemplo, si usamos la lista anterior llamada 'mix'", "\nPrimer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Ultimo elemento:", mix[-1])

#lo mismo podemos hacer con una cadena de string
print("\nProbemos con un string:")
string = "hola mundo"
print("string =",string)
print("Primer elemento:", string[0])
print("Segundo elemento:", string[1])
print("Ultimo elemento:", string[-1])

#slicing
#nos permite traer una porcion de datos, indicando el 'inicio' y el 'final'
print("\n4.Slicing")
print("Tomemos de vuelta la lista 'mix'")
print("mix:", mix)
print("Nos traemos los datos desde la posicion 0 a la posicion 2:",mix[0:2])
#la posicion de final que indicamos no se incluye y no nos trae ese dato
#es buena practica si comenzamos desde la posicion '0' o si queremos ir hasta la posoicion final, dejar esos espacios vacios, o sea [:]
print("Nos traemos los datos desde la posicion 0 a la posicion 3:",mix[:3])
print("Nos traemos los datos desde la posicion 2 hasta el final:",mix[2:])

#veamos el uso de los metodos
print("\n5.Metodos")
print("A.El uso de 'append' para agregar un valor al final de la lista")
print("Seguimos usando nuestra lista 'mix'")
print("mix:", mix)
mix.append(False)
print("Con 'mix.append(dato_a_insertar)' agregamos un valor al final:", mix)

#Cuando agregamos una lista dentro de otra lista, la lista agregada es un valor INDEPENDIENTE

mix.append(["a", "b"])
print("\nAhora agreguemos una lista '[\"a\", \"b\"]' dentro de la lista mix")
print("mix:", mix)
print("Las listas son INDEPENDIENTES")

#'insert' parab indicar la posicion donde agregar un valor
print("\nB.Con 'insert' podemos indicar en que posicion queremos agregar el nuevo dato")
print("mix:", mix)
mix.insert(1,["a", "b"])
print("le agregamos de vuelta 'a' y 'b' en la posicion 1:", mix)

#'index' para consultar la posicion de un elemento
print("\nC.Con 'index' consultamos la posicion de un elemento")
print("El elemento '[\"a\", \"b\"]'  esta en la posicion:", mix.index(["a", "b"]))
#nos muestra solamente la primera coincidencia, si se repite no lo veremos

#conocer el valor 'max' y 'min'
print("\nD.Usamos 'max' para conocer el elemento mayor de la lista y 'min' para el menor")
numeros = [5,2,10,500.3,9.23,-1,1]
print("Usemos nuestra lista 'numeros':", numeros)
print("Mayor:",max(numeros))
print("Menor:",min(numeros))

#eliminar un elemento de la lista con 'del'
print("\nE.Eliminar un elemento con 'del'")
print("Usamos nuestra lista de numeros:", numeros)
del numeros[-1]
print("Y eliminamos el ultimo valor", numeros)

#tambien podemos indicar una porcion a eliminar o toda la lista
#si eliminamos toda la lista nos arrojara un error