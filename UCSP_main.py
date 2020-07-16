import pygame, sys
import time
import random
from UCSP_clases import *
from UCSP_constantes import *
from UCSP_intros import *

pygame.init()
pygame.mixer.init()


vidas=10
listade_todoslos_sprites = pygame.sprite.Group()

# Estado del Juego
Intro1 = True
Intro2 = False
Intro3 = False
Nivel1 = False

#Música
# Sonidos
def load_intro():
    pygame.mixer.music.load("Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
def unload_music():
    pygame.mixer.music.stop()  
def load_level1():
    pygame.mixer.music.load("Sounds/nivel_01.mp3")
    pygame.mixer.music.play(-1)
if Intro1 == True:
    pygame.mixer.music.load("Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
elif Nivel1 == True:
    pygame.mixer.music.load("Sounds/nivel_01.mp3")
    pygame.mixer.music.play(-1)



fondo_x = -100

listade_todoslos_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()


plat1=Plataforma(150,40,200,220)
plat2=Plataforma(150,40,600,450)
plat3=Plataforma(100,30,400,350)
plataformas=pygame.sprite.Group()

def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra1.render("Vidas : "+ str
    (vidas), True, blanco)
    screen.blit(vidas_render,(x,y))

def game_over(x,y):
    imprimir= tipo_letra2.render("GAME OVER ", True, blanco)
    screen.blit(imprimir,(x,y))

def win(x,y):
    imprimir= tipo_letra2.render("YOU WIN ", True, blanco)
    screen.blit(imprimir,(x,y))

#JUEGO

vidas=1000
jugador = Player()
rat=Rat(rats,4)
spider=Spider(spiders,3)

enemigos.add(rat,spider)
plataformas.add(plat1,plat2,plat3)
listade_todoslos_sprites.add(jugador,enemigos,plataformas)
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
rat.rect.x=800//2-(rat.size[0]//2)
rat.rect.y=600-(rat.size[1])


spider.rect.x= random.randint(0,largo-spider.rect.width)
spider.rect.y= random.randint(0,ancho-spider.rect.height)

gets_hit = False




###        While Loop Juego         ###
# Intro1
while Intro1 == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2500)
                time.sleep(2.5)
                unload_music()
                load_level1()
                Intro1 = False
                Nivel1 = True
    
    animation_intro1()
    Intro1 = False
    Intro2 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)

# Intro2
while Intro2 == True:
    animation_intro2()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2000)
                fadeout_screen(800,600)
                time.sleep(2.0)
                unload_music()
                load_level1()
                Intro2 = False
                Intro3 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)
    
# Intro3
while Intro3 == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            pass


    animation_intro3()
    Intro3 = False
    time.sleep(2)
    Nivel1 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)




# Nivel1
mover_fondo = False

while Nivel1 == True:

    screen.blit(bosque_fondo_lv1, [fondo_x,0])
    jugador.update(gets_hit,vidas,plataformas)
    rat.mover()
    spider.mover()
    if vidas >0:
        if mover_fondo == True or jugador.speed_x > 0 or jugador.speed_x < 0:
            fondo_x += dfx
        if fondo_x <= 0 or fondo_x >= ancho:
            mover_fondo = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #mover_fondo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador.izquierda()
                mover_fondo = True
                dfx = 5
                Rat.rect.x += dfx
                if fondo_x >= -(4020 - ancho):
                    pass
                else:
                    mover_fondo = True
                    dfx = 5

            if event.key == pygame.K_RIGHT:
                jugador.derecha()
                mover_fondo = True
                dfx = -5
                Rat.rect.x -= dfx     
                if  fondo_x <= 0:
                    pass
                else:
                    mover_fondo = True
                    dfx = -5                   
            if event.key == pygame.K_UP:
                jugador.saltar() 
            if event.key == pygame.K_SPACE:
                jugador.ataque()        
        #detenerse            
        if event.type == pygame.KEYUP:
            mover_fondo = False 
            if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                jugador.stop()
                                
            if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                jugador.stop()


    if fondo_x >= 0:
      fondo_x = 0
    
    if fondo_x <= -1*bosque_fondo_lv1.get_rect().width + ancho:
      fondo_x = -1*bosque_fondo_lv1.get_rect().width + ancho
      
    if vidas > 0:
        mostrar_vidas(10,10)
    elif vidas <=0:
        game_over(100,250)
        jugador.die()
    if checkCollision(spider,jugador)==True:
        if jugador.imagen!=7:#imagen cuando está atacando
            gets_hit=True
            vidas-=1
            if vidas>0:
                jugador.get_hurt()
    else:
        gets_hit=False
    if checkCollision(rat,jugador)==True and rat in listade_todoslos_sprites:
        
        if jugador.imagen!=7:
            gets_hit=True
            vidas-=3
            if vidas>0:
                jugador.get_hurt()
        else:
            listade_todoslos_sprites.remove(rat)

    else:
        gets_hit=False
    listade_todoslos_sprites.draw(screen)
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()