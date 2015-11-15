import pygame, sys
from pygame.locals import *

Contador,subcontador,S,submenu0,submenu1,submenu2 = 0,0,False,False,False,False
rojo,azul,negro,amarillo,verde = (170,58,46),(76,108,145),(0,0,0),(200,188,68),(100,168,74)
color = negro
FondoVentana = pygame.image.load("Fondos/imgFondo1peq.png")

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,375))
pygame.display.set_caption("Botones")
fuente = pygame.font.SysFont("Arial",20)
cuenta = fuente.render("0",0,verde)
subcuenta = fuente.render("o",0,rojo)
c0 = fuente.render("Opcion 0: ",0,negro)
c0_sma = fuente.render("Opcion 0.1 ",0,rojo)
c0_smb = fuente.render("Opcion 0.2 ",0,rojo)
c1 = fuente.render("Opcion 1: ",0,negro)
c1_sma = fuente.render("Opcion 1.1 ",0,rojo)
c1_smb = fuente.render("Opcion 1.2 ",0,rojo)
c2 = fuente.render("Opcion 2: ",0,negro)
c2_sma = fuente.render("Opcion 2.1 ",0,rojo)
c2_smb = fuente.render("Opcion 2.2 ",0,rojo)

def CargaInicial(): #Cargas en ventana
    ventana.blit(FondoVentana,(0,0))
    ventana.blit(cuenta,(35,20))
    ventana.blit(subcuenta,(55,20))
    ventana.blit(c0,(35,60))
    if submenu0 == True:
        ventana.blit(c0_sma,(140,60))
        ventana.blit(c0_smb,(260,60))
    ventana.blit(c1,(35,100))
    if submenu1 == True:
        ventana.blit(c1_sma,(140,100))
        ventana.blit(c1_smb,(260,100))
    ventana.blit(c2,(35,140))
    if submenu2 == True:
        ventana.blit(c2_sma,(140,140))
        ventana.blit(c2_smb,(260,140))

def submenus():
    if submenu0 == True:
        c0_sma = fuente.render("Opcion 0.1 ",0,azul)
    else:
        c0_sma = fuente.render("Opcion 0.1 ",0,rojo)

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
                        cuenta = fuente.render(str(Contador),0,verde)
                elif evento.key == K_UP:
                    if Contador > 0:
                        Contador -= 1

                elif evento.key == K_RIGHT:
                    if subcontador < 1:
                        subcontador += 1
                        subcuenta = fuente.render(str(subcontador),0,rojo)
                elif evento.key == K_LEFT:
                    if subcontador > 0:
                        subcontador -= 1
                        subcuenta = fuente.render(str(subcontador),0,rojo)

                elif evento.key == K_s:
                    S = True
                    print "-> S"
            #KEYDOWN
            #Menu:
            if Contador == 0:
                c0 = fuente.render("Opcion 0: ",0,amarillo)
                if S == True:
                    S = False
                    submenu0 = True
                if subcontador == 0:
                    c0_sma = fuente.render("Opcion 0.1 ",0,azul)
                    c0_smb = fuente.render("Opcion 0.1 ",0,rojo)
                else:
                    c0_sma = fuente.render("Opcion 0.1 ",0,rojo)
                    c0_smb = fuente.render("Opcion 0.1 ",0,azul)
            else:
                c0 = fuente.render("Opcion 0: ",0,negro)
                submenu0 = False
            #-------------------------------------------------
            if Contador == 1:
                c1 = fuente.render("Opcion 1: ",0,amarillo)
                if S == True:
                    S = False
                    submenu1 = True
            else:
                c1 = fuente.render("Opcion 1: ",0,negro)
                submenu1 = False
            #-------------------------------------------------
            if Contador == 2:
                c2 = fuente.render("Opcion 2: ",0,amarillo)
                if S == True:
                    S = False
                    submenu2 = True
            else:
                c2 = fuente.render("Opcion 2: ",0,negro)
                submenu2 = False
    #FOR: evento


#Ejecutar/Actualizar ventana:
    pygame.display.update()
