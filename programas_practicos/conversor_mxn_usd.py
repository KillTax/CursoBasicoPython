#Haremos un conversor de pesos mexicanos a dolares

#Pedimos al usuario la cantidad a transformar
pesos = input("Ingresa cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20.59

#Dividimos la cantidad de pesos que tenemos entre el valor actual del dolar
dolares = pesos / valor_dolar

#Con round reduciomos el numero de decimales que tiene nuestra variable dolares que es tipo float
dolares = round(dolares, 2)

#Cambiamos el tipo de dato de dolares a tipo texto
dolares = str(dolares)

#Imprimimos la cantidad de dolares
print("Tienes $" + dolares + " dolares.")