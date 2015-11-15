import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint

#Variables. Inicializar:
posX,posY,posXenemigo,posYenemigo = 65,197,250,125
rojo,azul,negro,amarillo,verde = (170,58,46),(76,108,145),(0,0,0),(200,188,68),(100,168,74)
color = rojo
e = 0

#IMAGENES:
FondoVentana = pygame.image.load("Fondos/imgFondo1peq.png")
PQuieto = pygame.image.load("DerPersonaje/Quieto/Quieto0.png")#0~2
CARGAR = PQuieto
EQuieto = pygame.image.load("Enemigo/Enemigo0.png")#0~7
ENEMIGO = EQuieto

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Batalla en pruebas")

def CargaInicial(): #Cargas en ventana
    ventana.blit(FondoVentana,(0,0))
    ventana.blit(CARGAR,(posX,posY))
    ventana.blit(ENEMIGO,(posXenemigo,posYenemigo))

#Ejecucion:
while True:
    CargaInicial()
    #Ambiente()
    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Movimiento en menu:
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_d:
                    print "Tecla D presionada"
                    for e in range(0,10): #0~5
                        CARGAR = pygame.image.load("DerPersonaje/Ataque1/A1"+str(e)+".png")
                        CargaInicial()
                        pygame.time.wait(200)
                        print e
                        pygame.display.update()

#----------- Menu --------------------------------------------------------------


#----------- End ---------------------------------------------------------------

#Ejecutar/Actualizar ventana:
    pygame.display.update()
