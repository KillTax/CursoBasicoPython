#Haremos un conversor de dolares a pesos mexicanos

#Pedimos al usuario la cantidad a transformar
dolares = input("Ingresa cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso = 0.049

#Dividimos la cantidad de dolares que tenemos entre el valor actual del peso
peso = dolares / valor_peso

#Con round reduciomos el numero de decimales que tiene nuestra variable dolares que es tipo float
peso = round(peso, 2)

#Cambiamos el tipo de dato de dolares a tipo texto
peso = str(peso)

#Imprimimos la cantidad de dolares
print("Tienes $" + peso + " pesos mexicanos.")