#las condicionales nos permitiran ir por varios caminos al avanzar por nuestro codigo


# Ejemplo1

"""
#Podemos acortar el hacer entero una variable solicitada al usuario de la siguiente manera
edad = int(input("Escribe tu edad: "))

#La condicional if nos permite decidir si se cumple cierta condicion ejecute cierto codigo, de no ser asi
#no lo ejecuta
if edad > 17:
    #Podemos rellenar con pass si de momento no tenemos algo que poner en lineas de codigo
    print("Eres mayor de edad")
#La condicional else solo se puede ejecutar despues de una condicional if y esta nos sirve para condicionar que si
#no se cumple la condicion de if se ejecute el codigo que esta en else
else:
    print("Eres menor de edad")

#Siempre despues de cualquier funcion o condicional dodnde se pongan ":" la linea de codigo siguiente se tiene
#que dejar con un tabulador o 4 espacios ya que si no marcara error y el codigo no funcionara, a esto se le llama
#identacion y es para llevar un orden correcto en el codigo
"""

#Ejemplo2

numero = int(input("Escribe un numero: "))
if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")

#elif nos permite hacer una excepcion al condicionar entre if y else donde si no se cumple if cheque primero la condicion
#de elif para saber si cumple o no para ejecutar el codigo y despues pasar a else donde se ejecutaria si o si si ninguna
#de las otras condiciones se cumplio