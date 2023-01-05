#!/usr/bin/env python
# coding: utf-8

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
mi_varentero = 10
print(mi_varentero)

#2) Imprimir el tipo de dato de la constante 8.5
type(8.5)

#3) Imprimir el tipo de dato de la variable creada en el punto 1
type(mi_varentero)

#4) Crear una variable que contenga tu nombre
mi_nombre = "Felipe "

#5) Crear una variable que contenga un número complejo
mi_varcomp = 1+1j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
type(mi_varcomp)

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
variable_pi = 3.1416

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var_True_string = "True"
var_True_bool = True

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
type(var_True_string)
type(var_True_bool)

#10) Asignar a una variable, la suma de un número entero y otro decimal
var_sumaint_dec = 10 + 11.5
print(var_sumaint_dec)

#11) Realizar una operación de suma de números complejos
a = 10 + 10j
b = 5 + 7j
print(a+b)

#12) Realizar una operación de suma de un número real y otro complejo
c = 20
print(c+a)

#13) Realizar una operación de multiplicación
print(4*2)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
var_cociente = 27/4
print(var_cociente)

#16) De la división anterior solamente mostrar la parte entera
print(27//4)

#17) De la división de 27 entre 4 mostrar solamente el resto
print(27%4)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6 * 4 + 3)

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
mi_apellido = "Acevedo"
print(mi_nombre+mi_apellido)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso? Porque el primero es un string y el segundo un número entero.
"2" == 2

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2")==2)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8') Porque la "," no se utiliza para números decimales (floats) se utiliza "."
a = float('3,8')

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var_1 = -3
var_1 -= 1
print(var_1)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1 << 2

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado? Si fueran dos numeros enteros se sumarían dando como resultado "4" pero si fueran dos string es posible concatenarlos.
2 + "2"

#26) Realizar una operación válida entre valores de tipo entero y string
var_2 = "tuve que leer esto " 
var_3 = 15
print(var_2 + str(var_3) + " veces para entenderlo")

# %%
