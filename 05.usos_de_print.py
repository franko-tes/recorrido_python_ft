print("\n--01.Uso basico--")
print("Pondremos entre comillas simples, dobles o triples lo que queremos que se imprima en pantalla.")
print('''Ejemplo: print("prueba")''')
print("Salida: prueba")

print("\n--02.Uso de la coma--")
print("Usamos la coma para separar argumentos y Python añade un espacio.")
print('''Ejemplo: print("Hoy", "es", "domingo")''')
print("Salida:", "Hoy", "es", "domingo")

print("\n--03.Uso del + --")
print("Usamos el signo + para concatenar pero no se agrega el espacio.")
print('''Ejemplo: print("Hoy" + "es" + "domingo")''')
print("Salida:", "Hoy" + "es" + "domingo")
print("Debemos agregar nosotros el espacio")
print('''Ejemplo: print("Hoy" + " " + "es" + " " + "domingo")''')
print("Salida:", "Hoy" + " " + "es" + " " + "domingo")

print("\n--04.Uso de sep--")
print("El parametro sep permite especificar como separar los elementos.")
print('''Ejemplo: print("Hoy", "es", "domingo", sep="; ")''')
print("Salida: Hoy", "es", "domingo", sep="; ")

print("\n--05.Uso de end--")
print("Print por defecto agrega un salto de linea. Con el uso de END podemos evitarlo o definir lo que se imprimira al final de la linea.")
print('''Ejemplo: print("Mañana", end=" ")

print("lunes")''')
print("Salida: Mañana",  end=" ")
print("lunes")

print("\n--06.Impresion de variables--")
print("Mostraremos el valor de una variables.")
print('''Ejemplo: 
año = 2025
mes = enero
print(año, mes)''')
año = 2025
mes = "enero"
print("Salida:", año, mes)

print("\n--07.Uso de formato con f-strings--")
print("Podemos insertar expresiones dentro de cadenas de texto.")
print('''Ejemplo:
mes = enero
año = 2025
print(f"Mes: {mes}, Año: {año}")''')
mes = "enero"
año = 2025
print(f"Salida: Mes: {mes}, Año: {año}")

print("\n--08.Uso de formato con format--")
print("Usando {} como marcadores de posición, puedes pasar los valores que quieres insertar como argumentos de format.")
print('''Ejemplo:
mes = enero
año = 2025
print("Mes: {}, Año: {}".format(mes, año))''')
mes = "enero"
año = 2025
print("Salida: Mes: {}, Año: {}".format(mes, año))

print("\n--09.Impresion con formato especifico--")
print("Podemos indicar la cantidad de decimales a imprimir.")
print('''Ejemplo:
valor = 3.14159
print("Valor: {:.2f}".format(valor))''')
valor = 3.14159
print("Salida: Valor: {:.2f}".format(valor))

print("\n--10.Salida de linea y caracteres especiales--")
print("A.Hacer saltos de linea con \\n")
print('''Ejemplo: print("Hola\\nmundo")''')
print("Salida: Hola\nmundo")
print("B.Imprimir una cadena que contenga comillas simples o dobles dentro de ellas, debes usar secuencias de escape para evitar confusiones con la sintaxis de Python.")
print('''Ejemplo: print("Hola soy \\'TARS\\'")''')
print("Salida: Hola soy \'TARS\'")
print("C.Imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que Python interprete las barras invertidas como parte de secuencias de escape")
print('''Ejemplo: print("La ruta de archivo es: C:\\\\Users\\\\Usuario\\\\Desktop\\\\ejemplo.txt")''')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
