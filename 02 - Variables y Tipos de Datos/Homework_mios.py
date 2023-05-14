## Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable1 = 1
print (variable1)

#2) Imprimir el tipo de dato de la constante 8.5
print (type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print (type(variable1))

#4) Crear una variable que contenga tu nombre
variable2 = 'Alejandro'
#5) Crear una variable que contenga un número complejo
variable3 = 15 + 5j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(variable3))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416
print(round(pi,4))
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable4 = 'True'
variable5 = True
# no, no es lo mismo. 'True' es str y True es booleano
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print (type(variable4))
print (type(variable5))
#10) Asignar a una variable, la suma de un número entero y otro decimal
variable6 = 4 + 1.5
#11) Realizar una operación de suma de números complejos

#12) Realizar una operación de suma de un número real y otro complejo
variable6 + variable3
#13) Realizar una operación de multiplicación
print(2 * 2) 
#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
variable7 = 27/4
print(variable7)
#16) De la división anterior solamente mostrar la parte entera
variable8 = 27//4
print (variable8)
#17) De la división de 27 entre 4 mostrar solamente el resto
variable9 = 27%4
print(variable9)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
variable10 = variable8 * 4 + variable9
print (variable10)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print (variable2 + variable4)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
var11 = "2"
var12 = 2
print(var11==var12)
# eso ocurre porque "2" es un string y 2 un numero entero
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
var12 = "2"
print(var11==var12)
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#porque se utilizó mal el separador decimal. Tiene que ir punto y no coma
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var13 = 3
var13 -= 1
print(var13)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#no está permitido hacer operaciones con variables de distinto tipo. Si fueran las dos numericas, se sumarian. Si fueran las dos string las concatenaria

#26) Realizar una operación válida entre valores de tipo entero y string
print(2+2)
print('hola' + 'mundo')