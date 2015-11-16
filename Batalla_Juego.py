import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint

#Variables. Inicializar:
posX,posY,posXenemigo,posYenemigo = 65,197,250,125
VidaPersonaje,VidaEnemigo = 120,980
Contador,e,S,aleatorio = 0,0,False,200
a = 0
rojo,azul,negro,amarillo,verde = (170,58,46),(76,108,145),(0,0,0),(200,188,68),(100,168,74)
color = rojo

#IMAGENES:
FondoVentana = pygame.image.load("Fondos/imgFondo1peq.png")
PQuieto = pygame.image.load("DerPersonaje/Quieto/Quieto0.png")#0~2
CARGAR = PQuieto
EQuieto = pygame.image.load("Enemigo/Enemigo0.png")#0~7
ENEMIGO = EQuieto
GOLPE = pygame.image.load("Enemigo/Llamas/vacio.png")
GOLPE2 = GOLPE

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Batalla")
fuente = pygame.font.SysFont("Verdana",20)
fuente2 = pygame.font.SysFont("Arial",35)
cuenta = fuente.render(str(Contador),0,verde)
c0 = fuente.render("Ataque 0",0,negro)
c1 = fuente.render("Ataque 1",0,negro)
c2 = fuente.render("Ataque 2",0,negro)
TextoVP = fuente.render("Personaje: "+str(VidaPersonaje),0,negro)
TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
TextoResultadoVP = fuente2.render("",0,rojo)
TextoResultadoVE = fuente2.render("",0,rojo)
Resultado = fuente2.render("",0,azul)

def CargaInicial(): #Cargas en ventana
    ventana.blit(FondoVentana,(0,0))
    ventana.blit(GOLPE,(posX,posY-95))
    ventana.blit(CARGAR,(posX,posY))
    ventana.blit(ENEMIGO,(posXenemigo,posYenemigo))
    ventana.blit(GOLPE2,(posXenemigo+100,posYenemigo-30))
    ventana.blit(cuenta,(35,15))
    ventana.blit(c0,(35,55))
    ventana.blit(c1,(35,95))
    ventana.blit(c2,(35,135))
    ventana.blit(TextoVP,(75,320))
    ventana.blit(TextoVE,(375,320))
    ventana.blit(TextoResultadoVP,(posX+25,posY-30))
    ventana.blit(TextoResultadoVE,(posXenemigo+140,posYenemigo-30))
    ventana.blit(Resultado,(200,50))

def Ambiente():
    for e in range(0,8): #0~7
        CARGAR = pygame.image.load("DerPersonaje/Quieto/Quieto"+str(e)+".png")
        ENEMIGO = pygame.image.load("Enemigo/Enemigo"+str(e)+".png")
        ventana.blit(FondoVentana,(0,0))
        ventana.blit(CARGAR,(posX,posY))
        ventana.blit(ENEMIGO,(posXenemigo,posYenemigo))
        ventana.blit(GOLPE,(posX,posY))
        ventana.blit(GOLPE2,(posXenemigo+100,posYenemigo-30))
        ventana.blit(cuenta,(35,15))
        ventana.blit(c0,(35,55))
        ventana.blit(c1,(35,95))
        ventana.blit(c2,(35,135))
        ventana.blit(TextoVP,(75,320))
        ventana.blit(TextoVE,(375,320))
        ventana.blit(TextoResultadoVP,(posX+25,posY))
        ventana.blit(TextoResultadoVE,(posXenemigo+140,posYenemigo))
        ventana.blit(Resultado,(200,50))
        pygame.time.wait(150)
        pygame.display.update()

#Ejecucion:
while True:
    CargaInicial()
    Ambiente()
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
                        cuenta = fuente.render(str(Contador),0,verde)
                elif evento.key == K_UP:
                    if Contador > 0:
                        Contador -= 1
                        cuenta = fuente.render(str(Contador),0,verde)
                elif evento.key == K_s:
                    print "S: Presionada"
                    S = True
                elif evento.key == K_d:
                    print "Ataque doble"
                    posX += 200
                    VidaEnemigo -= 100
                    TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
                    TextoResultadoVE = fuente2.render("-100",0,rojo)
                    for a in range(0,7): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque2/A2"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
                    for a in range(0,6): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque3/A3"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
                    posX -= 200
                    aleatorio = randint(0,100)
                    print "Aleatorio: "+str(aleatorio)
                    TextoResultadoVE = fuente2.render("",0,rojo)

#----------- Menu --------------------------------------------------------------
            if Contador == 0:
                c0 = fuente.render("Ataque 0: ",0,color)
                if S == True:
                    S = False
                    print "Ataque 1"
                    posX += 215
                    VidaEnemigo -= 80
                    TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
                    TextoResultadoVE = fuente2.render("-80",0,rojo)
                    for a in range(0,10): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque1/A1"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
                    posX -= 215
                    TextoResultadoVE = fuente2.render("",0,rojo)
            else:
                c0 = fuente.render("Ataque 0: ",0,negro)
            #-------------------------------------------------
            if Contador == 1:
                c1 = fuente.render("Ataque 1: ",0,color)
                if S == True:
                    S = False
                    print "Ataque 2"
                    posX += 215
                    VidaEnemigo -= 40
                    TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
                    TextoResultadoVE = fuente2.render("-40",0,rojo)
                    for a in range(0,7): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque2/A2"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
                    posX -= 215
                    TextoResultadoVE = fuente2.render("",0,rojo)
            else:
                c1 = fuente.render("Ataque 1: ",0,negro)
            #-------------------------------------------------
            if Contador == 2:
                c2 = fuente.render("Ataque 2: ",0,color)
                if S == True:
                    S = False
                    print "Ataque 2"
                    posX += 215
                    VidaEnemigo -= 45
                    TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
                    TextoResultadoVE = fuente2.render("-45",0,rojo)
                    for a in range(0,6): #0~5
                        A2 = pygame.image.load("DerPersonaje/Ataque3/A3"+str(a)+".png")
                        CARGAR = A2
                        CargaInicial()
                        pygame.time.wait(130)
                        pygame.display.update()
                    posX -= 215
                    TextoResultadoVE = fuente2.render("",0,rojo)
            else:
                c2 = fuente.render("Ataque 2: ",0,negro)

            if aleatorio < 40:
                posYenemigo -= 30
                VidaPersonaje -= 30
                TextoVP = fuente.render("Personaje: "+str(VidaPersonaje),0,negro)
                TextoResultadoVP = fuente2.render("-30",0,rojo)
                for a in range(0,5):
                    GOLPE = pygame.image.load("Enemigo/Llamas/llamasA-"+str(a)+".png")
                    CargaInicial()
                    pygame.time.wait(120)
                    pygame.display.update()
                GOLPE = pygame.image.load("Enemigo/Llamas/vacio.png")
                aleatorio = 200
                posYenemigo += 30
                TextoResultadoVP = fuente2.render("",0,rojo)

            elif aleatorio > 40 and aleatorio < 80:
                posYenemigo += 30
                VidaEnemigo += 15
                TextoVE = fuente.render("Enemigo: "+str(VidaEnemigo),0,negro)
                TextoResultadoVE = fuente2.render("+15",0,verde)
                for a in range(0,6):
                    GOLPE2 = pygame.image.load("Enemigo/Llamas/llamasflotantes-"+str(a)+".png")
                    CargaInicial()
                    pygame.time.wait(120)
                    pygame.display.update()
                GOLPE2 = pygame.image.load("Enemigo/Llamas/vacio.png")
                aleatorio = 200
                posYenemigo -= 30
                TextoResultadoVE = fuente2.render("",0,verde)

            if VidaPersonaje <= 0:
                Resultado = fuente2.render("Game Over",0,rojo)
            elif VidaEnemigo <= 0:
                Resultado = fuente2.render("Has ganado",0,azul)

#----------- End ---------------------------------------------------------------

#Ejecutar/Actualizar ventana:
    pygame.display.update()
