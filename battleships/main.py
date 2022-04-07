import random as random
from numpy.random.mtrand import randint
import numpy as np


x = 10
y = 10

tableroJugador1 = np.zeros((x, y), dtype=int)
tableroJugador2 = np.zeros((x, y), dtype=int)

global turno

nBarcos = 4


def validarPosicion(tablero, direccion, posicion, longitud):
  try:
      estaLibre = True
      if direccion == 0:
          for i in range(0, longitud):
            if tablero[int(posicion[0])][int(posicion[1])+i] == 1:
                estaLibre = False
      if direccion == 1:
          for i in range(0, longitud):
            if tablero[int(posicion[0])+i][int(posicion[1])] == 1:
                estaLibre = False
      return estaLibre
  except:
      print('Posición no disponible')
      return False


print('Usa estas coordenadas para ingresar las de tus barcos, donde la primer coordenada son las filas y la segunda la columna\n')
print('Por ejemplo, la coordenada 5,7=X ubicaría el barco en esta posición ')
print('Por ejemplo, la coordenada 0,1=Z ubicaría el barco en esta posición ')
print('''
[[X 0 1 2 3 4 5 6 7 8 9]
 [0 0 Z 0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 0 0 0]
 [2 0 0 0 0 0 0 0 0 0 0]
 [3 0 0 0 0 0 0 0 0 0 0]
 [4 0 0 0 0 0 0 0 0 0 0]
 [5 0 0 0 0 0 0 0 X 0 0]
 [6 0 0 0 0 0 0 0 0 0 0]
 [7 0 0 0 0 0 0 0 0 0 0]
 [8 0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0 0]]
 ''')


def ubicarBarcos():
  turno=0
  if turno == 0:
    print("Turno Jugador 1")
    for i in range(0, nBarcos):
      global posicion
      posicion = input(
          "¿En que posición quieres ubicar tus barcos?: ").split(sep=",")
      global direccion
      direccion = random.randint(0, 2)
      while validarPosicion(tableroJugador1, direccion, posicion, i+1) == False:
        posicion = input(
            "Posición no disponible, escoge otra posición por favor: ").split(sep=",")
        direccion = random.randint(0, 2)
      contador = i
      while contador >= 0:
        if direccion == 0:
          tableroJugador1[int(posicion[0])][int(posicion[1])+contador] = 1
        else:
          tableroJugador1[int(posicion[0])+contador][int(posicion[1])] = 1
        contador -= 1
        print(f"""
        Dibujando barco:
{tableroJugador1}
        -----------------------------------
        """)

    print("Asi ha quedado tu tablero: ")
    print(tableroJugador1)
    print("\n"*100)
    turno = 1
  if turno == 1:
    print("Turno Jugador 2")
    for i in range(0, nBarcos):
      posicion = input(
          "¿En que posición quieres ubicar tus barcos?: ").split(sep=",")
      direccion = random.randint(0, 2)
      while validarPosicion(tableroJugador2, direccion, posicion, i+1) == False:
        posicion = input("Posición no disponible, escoge otra posición por favor: ").split(sep=",")
        direccion = random.randint(0, 2)
      contador = i
      while contador >= 0:
        if direccion == 0:
          tableroJugador2[int(posicion[0])][int(posicion[1])+contador] = 1
        else:
          tableroJugador2[int(posicion[0])+contador][int(posicion[1])] = 1
        contador -= 1
        print(f"""
        Dibujando barco:
{tableroJugador2}
        -----------------------------------
        """)

    print("Asi ha quedado tu tablero: ")
    print(tableroJugador2)
    print("\n"*100)
    turno = 0


def jugar():
  turno=0
  longitudes = range(1, nBarcos+1)
  puntajeMaximo = sum(longitudes)
  puntajeJugador1 = 0
  puntajeJugador2 = 0
  racha1=False
  racha2=False
  global tableroDeAtaque1
  tableroDeAtaque1=np.zeros((x,y), dtype=str)
  global tableroDeAtaque2
  tableroDeAtaque2=np.zeros((x,y), dtype=str)
  while puntajeJugador1 != puntajeMaximo and puntajeJugador2 != puntajeMaximo:
       if turno == 0 or racha1:
          print(f"""
          Jugador 1
          Tu puntaje:{puntajeJugador1}
          Puntaje del Jugador 2:{puntajeJugador2}
          Tablero de ataque
          """)
          print(tableroDeAtaque1)
          posicion=input("Escribe las coordenadas de ataque: ").split(",")
          if(tableroDeAtaque1[int(posicion[0])][int(posicion[1])]=="" and tableroJugador2[int(posicion[0])][int(posicion[1])]==0):
              print("Has fallado manco")
              if racha1:
                racha1=False
          elif(tableroDeAtaque1[int(posicion[0])][int(posicion[1])]=="" and tableroJugador2[int(posicion[0])][int(posicion[1])]==1):
              print("Has Acertado")
              tableroDeAtaque1[int(posicion[0])][int(posicion[1])]="O"
              puntajeJugador1+=1
              racha1=True
          elif(tableroDeAtaque1[int(posicion[0])][int(posicion[1])]=="O" and tableroJugador2[int(posicion[0])][int(posicion[1])]==1): 
              print("Ya colocaste esa posicion estúpido")
              if racha1:
                racha1=False
          if racha1==False:
            turno=1
       if turno == 1 or racha2:
         print(f"""
         Jugador 2
         Tu puntaje:{puntajeJugador2}
         Puntaje del Jugador1:{puntajeJugador1}
         Tablero de ataque
         """)
         print(tableroDeAtaque2)
         posicion=input("Escribe las coordenadas de ataque: ").split(",")
         if(tableroDeAtaque2[int(posicion[0])][int(posicion[1])]=="" and tableroJugador1[int(posicion[0])][int(posicion[1])]==0):
             print("Has fallado manco")
             if racha2:
               racha2=False
         elif(tableroDeAtaque2[int(posicion[0])][int(posicion[1])]=="" and tableroJugador1[int(posicion[0])][int(posicion[1])]==1):
             print("Has Acertado")
             tableroDeAtaque2[int(posicion[0])][int(posicion[1])]="O"
             puntajeJugador2+=1
             racha2=True
         elif(tableroDeAtaque2[int(posicion[0])][int(posicion[1])]=="O" and tableroJugador1[int(posicion[0])][int(posicion[1])]==1): 
             print("Ya colocaste esa posicion estúpido")
             if racha2:
               racha2=False
         if racha2==False:
           turno=0

ubicarBarcos()
jugar()
