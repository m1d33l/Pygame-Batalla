import pygame, sys
from pygame.locals import *

Contador,S = 0,False
rojo,azul,negro,amarillo,verde = (170,58,46),(76,108,145),(0,0,0),(200,188,68),(100,168,74)
color = negro

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Menu")
fuente = pygame.font.SysFont("Verdana",20)
cuenta = fuente.render("Cuenta: ",0,verde)
c0 = fuente.render("Numero 0: ",0,negro)
c1 = fuente.render("Numero 1: ",0,negro)
c2 = fuente.render("Numero 2: ",0,negro)

def CargaInicial(): #Cargas en ventana
    ventana.fill(azul)
    ventana.blit(cuenta,(200,20))
    ventana.blit(c0,(200,50))
    ventana.blit(c1,(200,80))
    ventana.blit(c2,(200,100))
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
            #KEYDOWN
            #Menu:
            if Contador == 0:
                c0 = fuente.render("Numero 0: ",0,amarillo)
                if S == True:
                    print "Accion 0"
                    S = False
            else:
                c0 = fuente.render("Numero 0: ",0,negro)
            #-------------------------------------------------
            if Contador == 1:
                c1 = fuente.render("Numero 1: ",0,amarillo)
                if S == True:
                    print "Accion 1"
                    S = False
            else:
                c1 = fuente.render("Numero 1: ",0,negro)
            #-------------------------------------------------
            if Contador == 2:
                c2 = fuente.render("Numero 2: ",0,amarillo)
                if S == True:
                    print "Accion 2"
                    S = False
            else:
                c2 = fuente.render("Numero 2: ",0,negro)
    #FOR: evento


#Ejecutar/Actualizar ventana:
    pygame.display.update()
