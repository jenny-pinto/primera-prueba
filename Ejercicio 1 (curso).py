#print('Hola mundo')
# Comentarios y declaración (los comentarios se hacen con el '#' o con '"""' tres comillas al inicio y final del comentario cuando sean más de una linea)
"""
print('Mientras más practico, más suerte tengo')
print('Si lo imaginas lo puedes crear')

nombre = 'Jenny'
print(nombre)
print('Hola, mi nombre es:', nombre)

#Variables.

variable = 'Pinto'
print(variable)

#Las constantes se definen en MAYUSCULA.
PI = 3.1416
print(PI)

#Llamar otro modulo.

import Modulo

print(Modulo.PI)

#Define diferentes variables con el mismo dato.

variable1 =  variable2 = variable3 = 'Hello'
print(variable1)
print(variable2)
print(variable3)

#Define varias variables en una sola linea.

variable4, variable5, variable6 = 'Emily', 'Sofia', 'Andres'
print(variable4)
print(variable5)
print(variable6)

#Tipos de datos:

#Solicitar al usuario los datos.

cadena = input("Introduzca su nombre:")
print(cadena)
print(type(cadena))

 #Especificar que tipo de dato es.

numero = int(input('Introduce un numero:'))
print(numero)
print(type(numero))

#Definir decimales

decimal = float(input('Introduzca un numero con decimales:'))
print(decimal)
print(type(decimal))

#Operadores aritmeticos

x = 15
y = 3

#sumar '+'
print('Este es el resultado de la suma de x + y =', x + y)

#resta '-'
print('Este es el resultado de la resta de x - y =', x - y)

#multiplicación '*'
print('Este es el resultado de la ultiplicación de x * y =', x * y)

#división '/'
print('Este es el resultado de la división de x / y=', x / y)

#producto entero de una división '//'
print('Este es el producto entero de la división de x // y =', x // y)

#exponente '**'
print('Este es el exponente de x ** y =', x ** y)

#Operadores comparativos

#mayor que '>'
print('x es mayor que y =', x > y)

#menor que '<'
print('x es menor que y =', x < y)

#igual a '=='
print('x y y son iguales =', x == y)

#no igual a '!='
print('x no es igual a y =', x != y)

#mayor o igual '>='
print('X es mayor o igual a y =', x >= y)

#menor o igual '<='
print('x es menor o igual a y =', x <= y)

#la sentencia if solo se ejecuta cuando la sentencia es verdadera 
#la sentencia elif se utiliza para cuando la sentencia if no es verdadera y se da una respuesta alternativa
#la sentencia else es para finalizar el if
x = 10
if x < 5:
    print('x es menor que 5')
elif x < 20:
    print('x es menor que 20')    
else:
    print('x es mayor o igual que 20')

#estructura completa de un if

edad = int(input('Por favor, ingresa tu edad:'))

if edad < 0:
    print('Edad invalida, por favor ingrese una edad valida.')
elif edad < 12:
    print('Eres un niño.')
elif edad < 18:
    print('Eres un adolescente.')    
elif edad < 65:
    print('Eres un adulto.')
else:
    print('Eres un adulto mayor.')    

calificación = float(input('Por favor ingrese su calificación como un número decimal'))

if calificación < 0:
    print ('Ingrese un valor valido')
elif calificación < 60:
    print('Lo siento, has suspendido. Debes esforzarte más en la proxima evaluación.')    
elif calificación < 70:
    print('Has aprobado, pero necesitas mejorar un poco.')
elif calificación < 90:
    print('Has aprobado satisfactoriamente.')
else:
    print('¡Felicidades! Has aprobado con unha calificación sobresaliente.')

#la sentencia match es una sentencia logica, sirve para evaluar condiciones.

numero = 3

match numero:
    case 1:
        print('Uno')
    case 2:
        print('Dos')    
    case 3:
        print('Tres')
    case _:
        print('Número no reconocido')

numero = int(input('Por favor, introduce un número entero:'))

match numero:
    case 0:
        print('El número es un cero')
    case numero if numero % 2 == 0:
        print('El número es par.')
    case numero if numero % 2 != 0:
        print('El número no es par.')
    case _:
        print('Número no reconocido')

#Solicitar un número a un usuario

numero = int(input('Por favor, ingrese un número entero:'))

#Verificar y mostrar el resultado al numero que se ingresó

match numero:
    case numero if numero < 0:
        print(f'El número {numero} se encuentra en el Rango 1:Números negativos (menores que 0)'),
    case numero if numero < 9:
        print(f'El número {numero} se encuentra en el Rango 2:Números entre 0 (incluido) y 10 (excluido)')
    case numero if numero >= 10:
        print(f'El número {numero} se encuentra en el Rango 3:Números mayores o iguales a 10')

#Sentencia for, es para trabajar con grandes cantidades de información.

frutas = ['mango', 'fresa', 'pera', 'sandia']
contador = 0

#Bucle for que itera sobre la lista de frutas.

for fruta in frutas:
    contador += 1
    print(f'fruta #{contador}: {fruta}')
    if contador == 2:
        break

numero = [1, 2, 3, 4, 5, 20]

for numeros in numero:
    cuadrado = numeros ** 2
    print(f'El cuadrado de {numeros} es {cuadrado}')

numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero
    promedio = suma / len(numeros)
    print('El promedio de numeros es:', promedio)

#La sentencia while se utiliza para estructuras repetitivas de codigo o cualquier tarea repetitiva

contador = 1
while contador <= 100:
    print(contador)
    contador += 1
    if contador == 60:
        break

contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

print('FELIZ AÑO NUEVO')

suma = 0
numero = int(input('Ingrese un número positivo (o un número negativo para salir):'))

while numero >= 0:
    suma += numero
    numero = int(input('Ingrese un número positivo (o un número negativo para salir):'))
print('La suma de los números ingresados es:', suma)

contador = 1
numero = int(input('Ingrese un número limite para detener el conteo:'))

while contador <= numero:
    print (contador)
    contador += 1

print('Conteo completado')    

#Cadenas
nombre = 'JENNY'
apellido = 'pinto'
frase = 'Esto es una frase'

longitud = len(frase)
print(longitud)
    
print(apellido[3])

palabras = frase.split()
print(palabras)

mayusculas = apellido.upper()
print(mayusculas)

minusculas = nombre.lower()
print(minusculas)

#Reemplazar texto 

mensaje = 'Hola, mundo '
print(mensaje)
cambio = mensaje.replace('Hola', 'Buenos días')
print(cambio)

#separar una cadena por caracteres

for x in apellido:
    print(x)


#Las tuplas no se pueden eliminar
#tupla con números
mi_tupla1 = (1, 2, 3)

#tupla con cadenas de texto
mi_tupla2 = ('mango', 'fresa', 'papaya')

#tupla mixta con diferentes tipos de datos
mi_tupla3 = ('Hola', 1, 7.37)

#tupla vacia
tupla_vacia = ()

print(mi_tupla1[0])
print(mi_tupla2[1])
print(mi_tupla3[2])

#ejm mostrando datos
personas = (('jenny', 20), ('tatiana', 15), ('andres', 26))

for nombre, edad in personas:
    if edad > 18:
        print(nombre, edad)

#ejm sumando números
numeros = (10, 20, 30, 40, 50, 100, 1000)

suma = sum(numeros)
print('La suma de los números es:', suma)

#ejm
palabras = ('manzana', 'banana', 'cereza')
palabra_buscar = input('Por favor ingrese una palabra:')

if palabra_buscar in palabras:
    print(f'La palabra {palabra_buscar} está en la tupla')
else:
    print(f'La palabra {palabra_buscar} no está en la tupla')

#las listas se hacen con [], las tuplas se hacen con ()
#La listas si se pueden modificar
#Lista de números enteros
numeros = [1, 2, 3, 4, 5]

#Lista de cadenas de texto
frutas = ['mango', 'fresa', 'cereza']

#Lista mixta con diferentes tipos de datos
mixta = [1, 'jenny', 3.34, True]

print(numeros[2])
print(frutas[0])
print(mixta[1])

numeros[2] = 9
print(numeros[2])

#Para agregar datos a una lista se utiliza .append
numeros.append(8) 
print(numeros)
 
frutas.append('coco')
print(frutas)

#Para eliminar datos de una lista
del numeros[2]
print(numeros)

del frutas[1]
print(frutas)

for fruta in frutas:
    print(fruta)

suma = sum(numeros)
print(suma)

colores = ['rojo', 'verde', 'azul', 'morado', 'violeta']

for color in colores:
    print(color)

#Diccionarios se comonen de una clave principal y de un dato, se utilizan con {},

persona ={
    'nombre': 'jenny',
    'edad': 20,
    'ciudad': 'bogota'
}

perfil = persona
print(perfil['edad'])

#Diccionario anidado, se divide por sesiones

personas = {
    'persona1':{
        'nombre': 'jenny',
        'edad': 20,
        'ciudad': 'bogota'
    },
    'persona2':{
        'nombre': 'emily',
        'edad': 25,
        'ciudad': 'tunja'
    },
    'persona3':{
        'nombre': 'carolina',
        'edad': 30,
        'ciudad': 'manizales'
    }
}

datos = personas['persona1']
datos2 = personas['persona2']
datos3 = personas['persona3']
print(datos['nombre'])
print(datos2['edad'])
print(datos3['ciudad'])

#Diccionario para que el usuario ingrese los datos
persona1 = {
    'nombre': None,
    'edad': None,
    'direccion': None,
    'telefono': None
}

persona1['nombre']= input('Introduce tu nombre:')
persona1['edad']= input('Introduce tu edad:')
persona1['direccion']= input('Introduce tu dirección:')
persona1['telefono']= input('Introduce tu telefono:')

print(persona1['nombre'], 'tiene', persona1['edad'], 'años, vive en',persona1['direccion'], 'y su número de telefono es', persona1['telefono'])

datos_personales = { 
    'nombre': None,
    'edad': None,
    'direccion': None,
    'telefono': None
}

datos_personales['nombre']=input('Ingrese su nombre:')
datos_personales['edad']=input('Ingrese su edad:')
datos_personales['direccion']=input('Ingrese su dirección:')
datos_personales['telefono']=input('Ingrese su número de telefono:')

print(datos_personales['nombre'], 'tiene', datos_personales['edad'], 'años, su dirección es', datos_personales['direccion'], 'y su número de telefono es', datos_personales['telefono'])

#Funciones, son estructuras de codigo reutilizables 

def saludar(nombre):
    print(f'¡Hola, {nombre}!')

saludar('jenny')

saludar(input('Introduce tu nombre:'))

def suma(a, b):
    resultado = a + b
    return resultado

numero1 = int(input('Introduce un número:'))
numero2 = int(input('Introduce un segundo número:'))

resultado = suma(numero1, numero2)

print(resultado)

def espar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Ingrese un número:'))
if espar(numero)==True:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} no es par')        

#max es el maximo factor almacenado en una lista
def listanumeros(lista):
    maximo = max(lista)
    return maximo

numeros = [10, 40, 50, 5, 6]
valor = listanumeros(numeros)

print('El valor maximo almacenado en la lista es:', valor)

#Calculadora
def calculadora(num1, num2, operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        return num1 / num2
    else:
        return 'Operación no valida'

num1 = int(input('Ingrese un número:'))
operacion = input('Ingrese un signo de operación(+,-,*,/):')
num2 = int(input('Ingrese un segundo número:'))

resultado = calculadora(num1, num2, operacion)        
print(f'El resultado de la operación {num1} {operacion} {num2} es igual a {resultado}')

#Modulo

import Modulo

numero1 = int(input('Hola, por favor introduce un número:'))
numero2 = int(input('Por favor introduce un segundo número:'))

suma = Modulo.suma(numero1, numero2)
resta = Modulo.resta(numero1, numero2)
multiplicacion = Modulo.multiplicacion(numero1, numero2)
print(suma)
print(resta)
print(multiplicacion)

#ejm
import Modulo

numero = int(input('Hola, por favor ingresa un número:'))

es_par = Modulo.es_par(numero)
print(es_par)

#Programación orientada a oljetos
#Clases (se crea con class y luego va el nombre que va  atener la clase)
#_init_ es el metodo inicial con el que siempre tiene que arrancar
#self es el atributo con el que se inician los metodos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años de edad.')

#Crear una instancia de la clase Persona
persona1 = Persona('jenny', 20)

#Llamar al metodo saludar
persona1.saludar()

#ejm
class calculadora1:
    def __init__(self, numero):
        self.resultado = numero

    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero

    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print('Error:No se puede dividir por cero')
    
    def resultado(self):
        return self.resultado
    
calculo = calculadora1(0)

calculo.sumar(5)
calculo.multiplicar(4)
calculo.restar(5)
calculo.dividir(2)
        
resultado = calculo.resultado
print('Resultado:', resultado)

#ejm sin el metodo _init_ y los datos ingresados por el usuario
class calculadora2:
    def suma(self, num1, num2):
        return num1 + num2
    def resta(self, num1, num2):
        return num1 - num2
    def multiplicar(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        if num2 == 0:
            return 'Error: No se puede sividir por cero.'
        
num1 = float(input('Por favor ingresa el primer número:'))
num2 = float(input('Ingresa el segundo número:'))

calc = calculadora2()

resulsuma = calc.suma(num1, num2)
resulresta = calc.resta(num1, num2)
resultmultiplicacion = calc.multiplicar(num1, num2)
resuldivision = calc.division(num1, num2)

print('Suma:', resulsuma)
print('Resta:', resulresta)
print('Multiplicación:', resultmultiplicacion)
print('División:', resuldivision)

#Contador de palabras
class ContadorPalabras:
    def __init__(self):
        self.contador = 0
    def contar(self, cadena_texto):
        palabra = cadena_texto.split()
        self.contador += len(palabra)
    def obtener_contador(self):
        return self.contador

Contador_palabras = ContadorPalabras()

cadena_texto = 'Esta es la frase de prueba que se va a utilizar en el ejercicio'
Contador_palabras.contar(cadena_texto)

resultado = Contador_palabras.obtener_contador()
print('El número de palabras que tiene mi texto es:', resultado)

#Herencia y poliformismoy
#La herencia es la posibilidad de que una clase padre herede la información a una clase hijo para que realicen diferentes funciones

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f'{self.marca} {self.modelo} está arrancando'
    
#clase hijo que ereda la información
class coche(vehiculo):
    def acelerar(self):
        return f'{self.marca} {self.modelo} está acelerando'
    
class motocicleta(vehiculo):
    def caballito(self):
        return f'{self.marca} {self.modelo} está haciendo un caballito'
    
cochee = coche('Toyota', 'Carmy')
motocicletaa = motocicleta('Harley-Davidson', 'sportster')

print(f'Coche, marca y modelo: {cochee.marca}, {cochee.modelo}')
print(f'Motocicleta, marca y modelo: {motocicletaa.marca}, {motocicletaa.modelo}')

print(cochee.acelerar())
print(motocicletaa.arrancar())

#Polimorfismo es la utilización de objetos que están declarados en diferentes metodos y clases

print(cochee.arrancar())
print(motocicletaa.arrancar())

#ejm
class animales:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass

class perro(animales):
    def hablar(self):
        return 'Guau'

class gato(animales):
    def hablar(self):
        return 'Miau'
    
perroo = perro('Schnauzer')
gatoo = gato('Angora')

print(f'El perro {perroo.nombre} hace {perroo.hablar()}')
print(f'El gato {gatoo.nombre} hace {gatoo.hablar()}')

#Encapsulamiento es definir cuando un atributo de algun metodo sea privado o publico (son atributos que pueden ser modificados)
#Para que no se puedan modificar se declaran con doble raya al piso '__' en todas la variables al principio
class encap:
    def __init__(self):
        self.__numero = 0

    def operacion(self):
        print(self.__numero + 20)

    def resultado(self):
        return self.__numero
    
ejemplo = encap()
ejemplo.operacion()
ejemplo.numero = 100
print(ejemplo.resultado())

multiplicando = 11
multiplicador = 1
producto = 0

while multiplicador <= 10:
      producto = multiplicando * multiplicador
      print (f'{multiplicando} x {multiplicador} = {producto}')
      multiplicador = multiplicador + 1 


nombres = ['juan', 'antonio', 'pedro', 'herminio']

for nombre in nombres:
    print(nombre)

base = int(input('> Intriduce el número a elevar:'))

for exponente in range (0,10):
    potencia = base ** exponente
    print(f'{base} elevado a {exponente} es {potencia}')

#Caractertes Especiales
#Es un salto de linea
print('Hola \nMundo') 

#Es un tabulador
print('\t Python \t es genial')

#Comillas simples
print('Jenny\' "pinto')

#Comillas dobles
print("'Tatiana' \"Pinto")

#Diagonal invertida
print('Hola \\ jenny')

#Concatenación de cadenas
#Utilizando +
cadena1 = 'Hola'
cadena2 = 'Mundo'
concatenacion = cadena1 + ' ' + cadena2

print(concatenacion)

#Utilizando .join
concatenacion = ''.join([cadena1, ' ', cadena2])
print(concatenacion)

#Formateo de cadenas
nombre = 'Jenny'
edad = 21

#f-string
mensaje =f'Hola, me llamo {nombre} y tengo {edad} años.'
print(mensaje)

#metodo format
mensaje ='Hola, me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje)

#Metodos de cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')

#Poner la cadena en MAYUSCULAS
MAYUSCULAS = cadena1.upper()
print(f'Cadena en mayúsculas: {MAYUSCULAS}')

#Poner la cadena en minusculas
minusculas =cadena1.lower()
print(f'Cadena en minusculas: {minusculas}')

#Para imprimir directamente la cadena sin asignar una variable
print(f'Cadena en nimúsculas: {cadena1.lower()}')

cadena2 = ' Jenny Pinto '
print(f'Cadena con espacios: {cadena2}')
#Eliminar espacios
print(f'Cadena sin espacios: {cadena2.strip()}')

#Largo de la cadena
cadena ='Hola, Mundo!'
largo_cadena = len(cadena)
print(f'Cadena original: {cadena}')
print(f'Largo de la cadena: {largo_cadena}')

#Manejo de Subcadenas
cadena = 'Hola, Mundo!'
#Obtenemos la subcadena de Hola [inicio:fin (sin incluirlo)]
subcadena_hola = cadena[0:4]
print(f'Subcadena de Hola: {subcadena_hola}')
subcadena_mundo = cadena[6:11]
print(f'Subcadena de Mundo: {subcadena_mundo}')

#Buscar subcadenas
cadena = 'Hola, mundo!'
indice = cadena.find('mundo')
print(f'Indice de la subcadena mundo: {indice}')

#Obtener el indice de la subcadena de Hola
indice = cadena.find('Hola')
print(f'Indice de la subcadena de Hola {indice}')

#Reemplazar subcadenas
cadena = 'Hola, mundo!'
print(f'Cadena Original: {cadena}')
nueva_cadena = cadena.replace('mundo', 'a todos')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

#Substituir Hola por adios
nueva_cadena = cadena.replace('Hola', 'Adios')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

#Separar subcadenas
#Para separar cada elemento por espacios en blanco
datos = 'Hola mundo'
lista = datos.split() 
print(lista)

#Para separar cadenas por cada ,
datos = 'Jenny,21,Colombia'
lista = datos.split(',')
print(lista)

#Multiplicación de cadenas
texto = 'Hola'
veces = 5
resultado = texto * veces
print(resultado)

#Conversion de tipos de datos
#Convertir de cadena a número
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

#Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

#Convertir de número a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Número a cadena: {numero_cadena}')

#Convertir a booleano
#Tipo bool es False en los siguientes casos:
#Si el valor es 0, cadena vacia, o None, entonces regresa False
#Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia y tambien si es distinto de None
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}') #False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}') #True, incluye 0, 0.0

cadena = '' #El largo de la cadena es 0
booleano = bool(cadena)
print(f'Valor booleano de cadena vacia: {booleano}') #False, incluye condiciones vacias

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de cadena NO vacia: {booleano}') #True

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}') #False

#Ejm Tipos de datos
#Ejm de concatenación o suma de valores
numero1_cadena = '10'
print(f'Número 1 en cadena: {numero1_cadena}')
numero2_cadena = '20'
print(f'Número 2 en cadena: {numero2_cadena}')
resultado = numero1_cadena + numero2_cadena
print(f'Concatenacion: {resultado}')

#Convertimos a tipos enteros
numero1_entero = int(numero1_cadena)
numero2_entero = int(numero2_cadena)
resultado = numero1_entero + numero2_entero
print(resultado)

#Entrada de datos:
nombre = input('Ingrese un nombre: ')
print(f'Recibiendo el valor de nombre: {nombre}')

#Convertir la cadena a tipo entero.
edad = int(input('Introsuce tu edad: '))
print(f'Tu edad es: {edad} y en un año tendras {edad + 1}')
"""
#Valores aleatorios con la función randint
""" 
Forma 1:
import random
numero = random.randint(a,b)

#Forma 2:
from random import randint

#Generar un número aleatorio entre 1 y 10
numero = randint(1, 10)
print(f'Número aleatorio entre 1 y 10: {numero}')

#Operadores Aritmeticos
a = 10
b = 3

suma = a + b
print(f'Suma: {suma}')

resta = a - b 
print(f'Resta: {resta}')

multiplicacion = a * b
print(f'Multiplicación: {multiplicacion}')

division = a / b 
print(f'División: {division:.2f}')

division_entera = a // b
print(f'División Entera: {division_entera}')

modulo = a % b
print(f'Residuo de la división: {modulo}')

exponente = a ** b 
print(f'Exponente: {exponente}')

#Operadores de asignación

numero = 5
print(f'Valor de número: {numero}')
cadena = 'Saludos desde python'
print(f'Valor de la cadena: {cadena}')

#Asignación multiple
a, b, c = 10, 'Saludos', 14.5
print(f'Valor de a = {a}, b = {b}, c = {c}')
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

#Asignación Encadenada
contador1 = contador2 = 0
print(f'Valor de contador1 = {contador1}, contador2 = {contador2}')
a = b = c = 10
print(f'Valor de a = {a}, b = {b}, c = {c}')

#Intercambio de valores de una variable, sin utilizar temporales
x, y = 5, 10
print(f'Valores iniciales de x = {x}, y = {y}')
#Aplicando el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Valores iniciales de x = {x}, y = {y}')
#Resibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'nombre: {nombre.strip()}, apellido: {apellido.strip()}')

#Operadores compuestos
a, b = 10, 15
print(f'Valor inicial a : {a}, b : {b}')

a += b # a = a + b
print(f'Operador a += b es: {a}')

a = 10 #Reiniciamos la variable a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

a = 10
a *= b # a = a * b
print(f'Operador a *= b es: {a}')

a = 10
a /= b # a = a / b
print(f'Operador a /= b es: {a:.2f}')

#Operadores de comparación o relacionales
a, b = 7, 5 
print(f'Valor inicial a: {a}, b: {b}')

resultado = a == b
print(f'Resultado a == b es: {resultado}')

resultado = a != b
print(f'Resultado a != b es: {resultado}')

resultado = a > b
print(f'Resultado a > b es: {resultado}')

resultado = a >= b
print(f'Resultado a >= b es: {resultado}')

resultado = a < b 
print(f'Resultado a < b es: {resultado}')

resultado = a <= b 
print(f'Resultado a <= b es: {resultado}')

#Operador and (reguesa verdadero si ambos valores son verdaderos)
condicion1 = False
condicion2 = False
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

condicion1 = True
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

#Operador lógico or (regresa True si cualquiera de los operandos es verdadero)
condicion1 = False
condicion2 = False
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2} es: {resultado}')

condicion1 = False
condicion2 = True
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2} es: {resultado}')

condicion1 = True
condicion2 = True
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2} es: {resultado}')

#Operador not 
condicion1 = False
resultado = not condicion1
print(f'Operador not sobre {condicion1}: {resultado}')

#Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'\n¿La variable no tiene ningún valor?: {es_cadena_vacia}')

#Revisar si unna variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\n¿La variable no tiene nungún valor asignado?: {es_variable_sin_valor}')

#Ejm:
#Revisar si una variable se encuentra dentro de rango entre 1 y 10
dato = int(input('Proporciona un dato entero: '))

#Revisamos si está dentro de rango 
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable está dentro de rango (entre 1 y 10)? : {esta_dentro_rango}')

#Revisamos la lógica inversa, si el dato está fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'¿Variable está fuera de rango (entre 1 y 10)?: {esta_fuera_rango}')

#Presedencia de operadores
# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

# Ejemplo de precedencia de operadores
# 1. Division 12 / 3 = 4
# 2. Multiplicacion 2 * 3 = 6
# 3. Suma 4 + 6 = 10
# 4. Resta 10 - 1 = 9

resultado = 12 // 3 + 2 * 3 - 1
print(f'Resultado: {resultado}')
"""
#Sentencias de Desición
#Sentencia if
print('*** Sentencia if ***')
edad = 30
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')

#Sentencia if else
print('*** Sentencia if else ***')
edad = 10
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
else:
    print(f'Eres menor de edad. Tienes {edad} años')

#Sentencia if elif else
print('*** Sentencia elif ***')
edad = 16
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años.')
elif 13 <= edad < 18:
    print(f'Eres un adolescente. Tienes {edad} años.')
else:
    print(f'Eres un menor de edad. Tienes {edad} años.')









