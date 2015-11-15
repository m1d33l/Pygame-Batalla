import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint

#Variables. Inicializar:
posX,posY,posXenemigo,posYenemigo = 65,197,250,125
#VidaDePersonaje,VidaEnemigo = 120,350
Contador,S = 0,False
colorRojo,colorAzul,colorNegro = (122,58,46),(76,108,145),(0,0,0)
color = colorNegro

#IMAGENES:
FondoVentana = pygame.image.load("Fondos/imgFondo1peq.png")
PQuieto = pygame.image.load("DerPersonaje/Quieto/Quieto0.png")
CARGAR = PQuieto
EQuieto = pygame.image.load("Enemigo/Enemigo0.png")
ENEMIGO = EQuieto

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Batalla")
fuente = pygame.font.SysFont("Arial",20)
#VidaPersonaje = fuente.render("Vida del personaje: "+str(VidaDePersonaje),0,(50,10,255))

def CargaInicial(): #Cargas en ventana
    ventana.blit(FondoVentana,(0,0))
    ventana.blit(CARGAR,(posX,posY))
    ventana.blit(ENEMIGO,(posXenemigo,posYenemigo))

#Ejecucion:
while True:
    CargaInicial()
    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Presionar tecla: Movimiento Lateral
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_a:
                    if Contador < 2:
                        Contador += 1
                        print "Contador: "+str(Contador)
                elif evento.key == K_s:
                    if Contador > 0:
                        Contador -= 1
                        print "Contador: "+str(Contador)
                elif evento.key == K_d:
                    print "s"
                    S = True
            #KEYDOWN

    #FOR: evento


#Ejecutar/Actualizar ventana:
    pygame.display.update()
