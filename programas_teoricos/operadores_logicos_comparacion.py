#Estos operadores nos permiten hacer mas cosas ademas de lo operadores como la suma, resta, etc.

es_estudiante = True
trabaja = False

#Son los operadores logicos and, or y not, que tienen diferentes usos
#Esto nos permite plantear casos donde necesitemos que algunas variables cumplan ciertas condiciones
#Por ejemplo :

es_estudiante and trabaja

#Aqui estariamos viendo si es estudiante y trabaja, ambas deben de ser True ya que asi nos lo pide el operador
#Ya que es False que trabaja al checar las variables con estas condiciones nos dara false

#Otro plantemiento es donde sea estudiante o trabaja podriamos usar el siguiente operador

es_estudiante or trabaja

#Con or si alguna de nuestras variables es verdadera siempre nos dara True ya que solo necesita
#cumplir una condicion para que sea True

#Otro operador es not, este nos sirve para cambiar el valor booleano de nuestra variable al contrario, si es
#True a False y si es False a True

not es_estudiante
not trabaja

#Ahora es_estudiante que en un inicio era True ahora sera False, trabaja que era False ahora es True gracias al operador

#Aparte de estos operadores logicos hay operadores de comparacion
#Serian == , != , > , < , >= , <=
numero1 = 5
numero2 = 5

numero1 == numero2
#Esto nos daria True gracias a nuestro operador de comparacion ==

numero3 = 7
numero1 == numero3
#En caso contrario de que no sean iguales como ahora nos daria False ya que 5 no es igual a 7

#Un operador contrario a == seria != que nos indica si son diferentes

numero1 != numero3
#Ahora nos daria True que con == era False ya que son diferentes

#El operador > nos indica que si la primer variable es mayor a la segunda

numero1 > numero3
#Aqui nos da False ya que numero1 es menor a numero3

#El operador < nos indica que si la primer variable es menor a la segunda

numero1 < numero3
#Aqui python nos dira que es True ya que ahora si es cierto que numero1 es menor a numero3

#Tambien podemos necesitar que no se solo mayor o menor que, si no mayor o igual o menor o igual para lo cual usaremos el signo =
#Despues de cada operador ya sea < o >, quedando de la siguiente manera <= menor o igual, >= mayor o igual

numero1 >= numero3

#Nos dara False ya que numero1 (5) no es mayor o igual a numero3 (7)

numero1 >= numero2

#En cambio ahora nos dara True ya que numero1 (5) si es mayor o igual a numero2 (5)

numero1 <= numero2
#True

numero1 <= numero3
#True
