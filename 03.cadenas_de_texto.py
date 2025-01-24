print("----Cadenas de texto----")

print("--Ver el tipo de dato--")
# str = string
name = "Juan"
caracter = "c"
print(type(name))
print(type(caracter))

print("--Uso de comillas--")
#en el ejemplo usamos las comillas dobles.
#pero se pueden usar comillas simples y triples.
comillas_simples = 'uso de comillas simples'
print(comillas_simples)
comillas_triples = '''comillas triples'''
print(comillas_triples)
#las comillas triples son sensibles al espaciado.
espaciado = '''las comillas triples

son sensibles al espaciado'''
print(espaciado)
#con comillas simples y dobles se produce un error de sintaxis.

print("--Indexacion--")
name = 'Juan Rodrigo'
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

print("--Concatenacion--")
name = 'Nombre'
last_name = 'Apellido'
print(name)
print(name + last_name)
print(name + ' ' + last_name) #aplicacion de espacio

print("--Replicacion--")
name = 'Nombre'
print(name * 5)

print("--Consultar la longitud--")
name = 'Nombre'
last_name = 'Apellido'
print(len(name))
print(len(last_name))

print("--Metodos--")
name = 'JUAN carlos'
last_name = '  Rodriguez Gonzalez  '
print(name.lower()) #en este caso lower es un metodo
print(name.upper()) #upper es un metodo
print(last_name.strip()) #strip es metodo. strip elimina los espacios al prinicipio y al final