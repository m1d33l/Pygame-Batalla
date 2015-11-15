import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint

#Variables. Inicializar:
posX,posY,posXenemigo,posYenemigo = 65,197,250,125
#VidaDePersonaje,VidaEnemigo = 120,350
Contador,e,S = 0,0,False
a = 0
rojo,azul,negro,amarillo,verde = (170,58,46),(76,108,145),(0,0,0),(200,188,68),(100,168,74)
color = rojo

#IMAGENES:
FondoVentana = pygame.image.load("Fondos/imgFondo1peq.png")
PQuieto = pygame.image.load("DerPersonaje/Quieto/Quieto0.png")#0~2
CARGAR = PQuieto
EQuieto = pygame.image.load("Enemigo/Enemigo0.png")#0~7
ENEMIGO = EQuieto

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Batalla")
fuente = pygame.font.SysFont("Verdana",20)
cuenta = fuente.render("Cuenta: "+str(Contador),0,verde)
c0 = fuente.render("Ataque 1",0,negro)
c1 = fuente.render("Ataque 2",0,negro)
c2 = fuente.render("Ataque 3",0,negro)

def CargaInicial(): #Cargas en ventana
    ventana.blit(FondoVentana,(0,0))
    ventana.blit(CARGAR,(posX,posY))
    ventana.blit(ENEMIGO,(posXenemigo,posYenemigo))
    ventana.blit(cuenta,(35,15))
    ventana.blit(c0,(35,55))
    ventana.blit(c1,(35,95))
    ventana.blit(c2,(35,135))

#Ejecucion:
while True:
    CargaInicial()
    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Movimiento en menu:
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_DOWN:
                    if Contador < 2:
                        Contador += 1
                        cuenta = fuente.render("Cuenta: "+str(Contador),0,verde)
                elif evento.key == K_UP:
                    if Contador > 0:
                        Contador -= 1
                        cuenta = fuente.render("Cuenta: "+str(Contador),0,verde)
                elif evento.key == K_s:
                    print "S: Presionada"
                    S = True
                elif evento.key == K_d:
                    print "Tecla D presionada"
                    for a in range(0,10): #0~5
                        CARAR = pygame.image.load("DerPersonaje/Ataque1/A1"+str(a)+".png")
                        CargaInicial()
                        pygame.time.wait(150)
                        pygame.display.update()

#----------- Menu --------------------------------------------------------------
            if Contador == 0:
                c0 = fuente.render("Ataque 0: ",0,color)
                if S == True:
                    S = False

            else:
                c0 = fuente.render("Ataque 0: ",0,negro)
            #-------------------------------------------------
            if Contador == 1:
                c1 = fuente.render("Ataque 1: ",0,color)
                if S == True:
                    S = False

            else:
                c1 = fuente.render("Ataque 1: ",0,negro)
            #-------------------------------------------------
            if Contador == 2:
                c2 = fuente.render("Ataque 2: ",0,color)
                if S == True:
                    S = False
                    print "Ataque 2"
                    for a in range(0,7): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque2/A2"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
            else:
                c2 = fuente.render("Ataque 2: ",0,negro)

#----------- End ---------------------------------------------------------------

#Ejecutar/Actualizar ventana:
    pygame.display.update()
