"""
#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('¡Hola, mundo!')

#2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

mensaje = '¡Hola, mundo!'
print(mensaje)

#3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input('Por favor ingrese su nombre:')
print(f'¡Hola, {nombre}!')

#4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 

print('El resultado de la operación es:', (((3 + 2) / (2 * 5))** 2))

#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = int(input('Por favor ingrese el número de horas trabajadas:'))
costo_hora = int(input('Ingrese el costo por horas:'))
print('El pago que le corresponde es:', (horas_trabajadas * costo_hora))

#6 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
invertir = int((input('Ingrese la cantidad que desea invertir:')))
interes = float(input('Ingrese la tasa de interes anual:'))
años = int(input('Ingrese la cantidad de años a la que desea invertir:'))
capital = invertir * (1 + (interes / 100) ** años)
print('El capital obtenido en la inversión es:', capital)

#7 Escribir un programa que muestre por pantalla el siguiente mensaje:

print('La felicidad se puede encontrar hasta en los más oscuros')
print('momentos, si somos capaces de usar bien la luz.')
print('— Albus Dumbledore')

#8 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
mensaje = '¡Hola Mundo!'
print(mensaje)

#9 Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, gusto en conocerte!
nombre = input('Introduce tu nombre:')
apellido = input('Introduce tu apellido:')
print(f'¡Hola {nombre} {apellido}, gusto en conocerte!')

#10 Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
n = int(input('Por favor, introduce un número positivo:'))
suma = n * (n + 1) / 2
print(f'La suma desde 1 hasta {n} es igual a {suma}')

#11 Programa que solicite al usuario los datos para calcular el área de un Cuadrado, finalmente mostrar el resultado en pantalla.
lado = int(input('Ingrese el lado de un cuadrado:'))
area = lado ** 2
print(f'El area de un cuadrado que su valor del lado es {lado} da como resultado {area} de area')

#12 Programa que solicite al usuario los datos para calcular el área de un Triángulo, finalmente mostrar el resultado en pantalla.
base = int(input('Ingrese la base de un triangulo:'))
altura = int(input('Ingrese la altura del triangulo:'))
area = (base* altura)/2
print(f'El area del triangulo que tiene como base {base} y  como altura {altura} es {area}')

#13 Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.
radio = int(input('Ingrese el area de un circulo:'))
PI = 3.1416
area = PI * (radio ** 2)
print(f'El area de un circulo que tiene como radio {radio} es igual a {area}')

#14 Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.
fahrenheit = int(input('Ingrese el valor de fahrenheit que desea pasar a grados celcius:'))
celcius = (fahrenheit - 32.0) * 5.0 / 9.0
print(f'El fahrenheit con valor {fahrenheit} convertido en grados celcius es igual a {celcius}°C.')

#15 Calculadora freelancer
dolares_hora = float(input('Ingrese la cantidad de dolares que gana por hora: '))
pago_semanal = dolares_hora * 40
pago_mensual = dolares_hora * 160
print('El valor que debe cobrar por semana trabajada es: ', pago_semanal)
print('El valor que debe cobrar al mes es: ', pago_mensual)

#16 Escribir un programa que solicite al usuario un número entero y muestre en pantalla si el número es Positivo (+) o Negativo (-). En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: El número no es Positivo ni Negativo.
numero = int(input('Ingrese un número entero:'))

if numero > 0:
    print(f'El número {numero} es un positivo')
elif numero < 0:
    print(f'El número {numero} es un número negativo')
elif numero == 0:
    print('El número no es Positivo ni Negativo.')

#17 Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor.
persona1 = input('Ingrese el nombre de la primera persona:')
persona2 = input('Ingrese el nombre de la segunda persona:')
edad1 = int(input(f'Ingrese la edad de {persona1}:'))
edad2 = int(input(f'Ingrese la edad de {persona2}:'))

if edad1 > edad2:
    print(f'{persona1} es mayor que {persona2}')
elif edad1 < edad2:
    print(f'{persona2} es mayor que {persona1}')
elif edad1 == edad2:
    print(f'{persona1} y {persona2} tienen la misma edad')

#18 Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.
numero = int(input('Ingrese un número:'))
if numero % 2 == 0:
    print(f'El número {numero} es par.')
else:
    print(f'El número {numero} es impar')

#19 Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.
numero = int(input('Ingrese un número:'))
if numero % 3 == 0:
    print(f'El número {numero} es multiplo de 3.')
else:
    print(f'El número {numero} no es multiplo de 3')

#20 Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.
letra = input('Ingrese una letra:')
if letra <= 'z' and letra >= 'a':
    print(f'La letra "{letra}" es minuscula')
elif letra <= 'Z' and letra >= 'A':
    print(f'La letra {letra} es MAYUSCULA')
else:
    print(f'Error: El caracter ingresado no es una letra')
 
#21 Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.
num1 = int(input('Ingrese el primer número:'))
num2 = int(input('Ingrese un segundo número:'))
num3 = int(input('Ingrese un tercer número:'))
numeros = [num1, num2, num3]

if num1 > num2:
    if num1 > num3:
        maximo = num1
    else:
        maximo = num3
else:
    if num2 > num3:
        maximo = num2
    else:
        maximo = num3

print('El número mayor de la lista es:', maximo)
  
#22 Escribir un programa que solicite al usuario 5 números, compararlos y decir cual es mayor.
num1 = int(input('Ingrese el primer número:'))
num2 = int(input('Ingrese el segundo número:'))
num3 = int(input('Ingrese el tercer número:'))
num4 = int(input('Ingrese el cuarto número:'))
num5 = int(input('Ingrese el quinto número:'))
numeros = [num1, num2, num3, num4, num5]

def listanumeros(lista):
    maximo = max(lista)
    return maximo

valor = listanumeros(numeros)
print('El valor maximo almacenado en la lista es:', valor)

#23 Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.
multiplicador = 1
resultado = 0
numero = 0
 
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero * multiplicador
    print("%d x %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1

numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))

#24 Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.
print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')
 
for pares in range(0, 201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#25 Escribir un programa que imprima los números pares entre el 0 y 200 de forma decreciente.
print('Números pares de manera descreciente:')

for pares in range(201, -1, -1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#26 Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.
numero = int(input('Ingrese el número limite del conteo:'))
for pares in range(0, numero):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#27 Escribir un programa que imprima todos los números primos hasta un número introducido por el usuario.
numero = int(input('Introduzca un número:'))
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(f'Los números primos hasta {numero} son: ')
for num in range(2, numero + 1):
    if es_primo(num):
        print(num)

#Sistema de reserva de Hoteles
print('Sistema de Reserva de Hoteles')

clientes = 'Laura'
dias = 5
tarifa_diaria = 1200.00
habitacion = True

print('Cliente:', clientes)
print('Días de estancia:', dias)
print('Tarifa diaria:', tarifa_diaria)
print('¿Habitación con vista al mar?:', habitacion)

#Generador de Email
print('***Generador de Emails***')
nombre = 'Jenny Pinto'
empresa = 'Grupo ASD'
dominio = ' com.mx'

nombre_normalizada = nombre.replace(' ', '.')
nombre_normalizado = nombre_normalizada.lower()
empresa_normalizada = "".join(empresa.split())
empresa_normalizado = empresa_normalizada.lower()
dominio_normalizado = dominio.replace(' ', '.')
email_normalizado = f'@{empresa_normalizado}{dominio_normalizado}'

cadenas = nombre_normalizado, empresa_normalizado, dominio_normalizado
print(f'\nNombre usuario: {nombre}')
print(f'Nombre usuario normalizado: {nombre_normalizado}')
print(f'\nNombre empresa: {empresa}')
print(f'Extensión del dominio: {dominio_normalizado}')
print(f'Dominio de email normalizado: {email_normalizado}')
print(f'\nEmail: {nombre_normalizado}.{empresa_normalizado}@{dominio_normalizado}')


#Sistema de empleados

nombre = input('Por favor introduzca su nombre: ')
edad = int(input('Ingrese su edad: '))
salario = float(input('Ingrese su salario: '))
jefe_departamento = input('¿Es jefe de departamento? (Si/No): ')

#convertir a un tipo bool la variable jefe_departamento
jefe_departamento = jefe_departamento.lower() == 'si'

print('\n Datos de Empleado ')
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Salario: {salario:.2f}')
print(f'¿Es jefe de departamento?: {jefe_departamento}')

#Receta de cocina
print('*** Recetas de cocina ***')
nombre_receta = input('Introduzca el nombre de la reseta: ')
ingredientes = input('Introduzca los ingredientes: ')
tiempo = int(input('Ingresa el tiempo de preparación (min): '))
dificultad = input('Ingresa la dificultad: ')
print('---------------------------------------------------------------')
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación (min): {tiempo}')
print(f'Dificultad: {dificultad}')

#Simular un dado de seis caras
from random import randint
dado = randint(1, 6)
print(f'Resultado de lanzar el dado: {dado}')

#Generador de id unico
print('*** Sistema Generador de ID Unico ***')
nombre = input('Ingrese su nombre: ' )
apellido = input('Ingrese su apellido: ')
fecha_nacimiento = int(input('Ingrese su año de nacimiento (YYYY): '))
nombre_normalizado = nombre.strip().upper()[:2]
apellido_normalizado = apellido.strip().upper()[:2]
fecha_normalizada = str(fecha_nacimiento)[-2:]

from random import randint
num_aleatorio = randint(1000, 9999)

print(f'Nombre: {nombre}')
print(f'Apellido {apellido}')
print(f'Año de nacimiento: {fecha_nacimiento}')
print('------------------------------------------------------------')
print(f'El número de Id del {nombre} {apellido} es: {nombre_normalizado}{apellido_normalizado}{fecha_normalizada}{num_aleatorio}')
 
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
texto = input('Intruduce tu nombre: ')
numero = int(input('Introduce la cantidad de veces que deseas imprimir: '))
print('\n'.join([texto] * numero))

#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre = input('¿Cual es tu nombre?: ') 
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
nombre = input('Introduzca su nombre: ')
n = len(nombre)
print(f'Nombre: {nombre}')
print(f'Cantidad de caracteres: {n}')

#Sistema descuentos VIP
print('*** Sistema de descuentos VIP ***')
no_productos_descuento = 10
articulos = int(input('Ingrese cuantos articulos ha comprado el día de hoy: '))
membresia = input('¿Cuenta con la membresia de la tienda? (Si/No): ')

es_elegible_descuento = articulos >= no_productos_descuento .and membresia.strip().lower() == 'si'

print(f'¿Tienes acceso al descuento VIP?: {es_elegible_descuento}')

#Sistema de préstamo de libros
print('*** Sistema Préstamo de Libros')
distancia_permitida_km = 3
credencial = input('¿Tiene credencial de estudiante?: ')
vivienda = int(input('¿A cuantos km vive de la biblioteca?: '))

es_elegible_prestamo = credencial.strip().lower() == 'si' or vivienda <= distancia_permitida_km

print(f'¿Eres elegible para prestamo de libros?: {es_elegible_prestamo}')

#Tiquet de venta
print('*** Generación ticket de venta ***')
precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))
descuento_porcentaje = int(input('¿Desea aplicar algún descuento (%)?: '))

#Precio del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos
#Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)
#Subtotal con descuento
subtotal_descuento = subtotal - descuento
#Calculo de impuestos (16%)
impuesto = subtotal_descuento * 0.16
#Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_descuento + impuesto

print(f'Subtotal: ${subtotal:.2f}\nDescuento: ${descuento}({descuento_porcentaje}%)\nSubtotal con descuento: ${subtotal_descuento}\nImpuesto (16%): ${impuesto:.2f}\nCosto total de la compra: ${costo_total_compra:.2f}')

#Sistema de Autenticación
print('*** Sistema Autenticación ***')
usuario = 'jpinto03'
password = '123456'

usuario_1 = input('Ingrese su usuario: ')
password_1 = input('Ingrese su contraseña: ')

#son_datos_correctos =(usuario_1.strip() == usuario and password_1.strip() == password) 
#Este es un ejemplo de como tambien podria funcionar.

usuarios = usuario == usuario_1
passwords = password == password_1

datos_correctos = usuarios and passwords
print(f'¿Datos correctos?: {datos_correctos}')

#Valor dentro de rango
print('*** Valor Dentro de Rango ***')
valor_minimo = 0
valor_maximo = 5

valor_usuario = int(input(f'Por favor, ingrese un número entre {valor_minimo} y {valor_maximo}: '))

dentro_rango = valor_usuario >= valor_minimo and valor_usuario <= valor_maximo
#dentro_rango = valor_minimo <= valor_usuario <= valor_maximo
print(f'¿El valor está dentro del rango?: {dentro_rango}')

#Cálculo Área y Perímetro de un Rectángulo
print('*** Cálculo Área y Perímetro de un Rectángulo ***)
base = float(input('Ingrese por favor la base del rectangulo: '))
altura = float(input('Ingrese por favor la altura del rectangulo: '))

area = base * altura
print(f'La altura de el rectangulo con base = {base} y altura = {altura} es: {area}')
perimetro = 2 * (base + altura)
print(f'El perimetro de el rectángulo con base = {base} y altura = {altura} es: {perimetro}')
"""











