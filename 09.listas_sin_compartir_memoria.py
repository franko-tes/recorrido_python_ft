#copiar una variable implica que apuntamos al mismo espacio en memoria donde esta la informacion
#eso quiere decir que si modificamos algo, se refleja en la copia
#pero si no queremos que se refleje, entonces utilizamos 'slicing'

#en este ejemplo tenemos la variable 'a', que es una lista
#y tenemos 'b' que es una copia de 'a'
a = [1,2,3,4,5]
b = a
print("\nCreamos dos variables, 'a' es igual a 'b'")
print("a:",a)
print("b:",b)

#cuando modificamos algo en 'a' se refleja en 'b' tambien
del a[0]
print("\nUna modificacion en 'a' se refleja en 'b'")
print("a:",a)
print("b:",b)

#esto sucede porque apuntan al mismo espacio en memoria
#podemos consultar el espacio en memoria con 'id'
print("\nRevisamos el espacio en memoria de ambos")
print("a:",id(a))
print("b:",id(b))
#nos devuelve el mismo valor

#utilizando 'slicing' evitamos esto
c = a[:]
print("\nAgregamos una tercer copia 'c' y revisamos el espacio en memoria")
print("a:",id(a))
print("b:",id(b))
print("c:",id(c))

#si hacemos una modificacion en 'a', esta no se reflejara en 'c'
a.append(6)
print("\nHacemos otra modificacion en 'a' y vemos que 'c' no cambia")
print("a:",a)
print("b:",b)
print("c:",c)