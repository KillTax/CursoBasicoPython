#Primero pediremos al usuario un tipo de dato con la sentencia input, este dato se guardara en la variable numero1
numero1 = input("Escribe un numero: ")
print(numero1)

numero2 = input("Escribe un numero: ")
print(numero2)

print(numero1 + numero2)

#El problema es que al guardar estas variables van a guardarse como cadenas de texto para convertir utilizaremos una funcion
#ahora numero1 hara que su dato sea de tipo entero

numero1 = int(numero1)

numero2 = int(numero2)

print(numero1 + numero2)

#Ahora si nos dara una suma de enteros

#Si convertimos nuestros numeros decimales a enteros estos haran que se quite el punto decimal y solo nos quedmos con la parte
#entera

numero_decimal = 4.5
numero_decimal = int(numero_decimal)
print(numero_decimal)

#Tambien podemos transformar los numero ya sean enteros o decimales a cadenas de texto con la siguiente funcion

numero_decimal = str(numero_decimal)
print(numero_decimal)


