import pygame,sys
pygame.init()

#Constante
ancho= 800
largo = 600
pygame.display.set_caption("Doggo Adventure")
pygame.display.set_icon(pygame.image.load("Sprites/icon.png"))
screen = pygame.display.set_mode((ancho,largo))
reloj = pygame.time.Clock()
blanco = (255,255,255)
negro=(0,0,0)
tipo_letra1 = pygame.font.Font('freesansbold.ttf', 28)
tipo_letra2 = pygame.font.Font('freesansbold.ttf', 100)


#Fondos
bosque_fondo_lv1 = pygame.image.load("Backgrounds/nivel1_x3.png").convert()
bosque_fondo_lv2 = pygame.image.load("Backgrounds/nivel2_x3.png").convert()
bosque_fondo_lv3 = pygame.image.load("Backgrounds/nivel3_x4.png").convert()



# Otras Funciones
def fadeout_screen(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        #redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)



enemigo_rat= pygame.image.load("Sprites/rat/rat_idle.png")
enemigo_rat_inv= pygame.transform.flip(enemigo_rat,True,False)
rats=[enemigo_rat,enemigo_rat_inv]

enemigo_spider=pygame.image.load("Sprites/spider/idle1.png")
enemigo_spider2=pygame.image.load("Sprites/spider/idle2.png")
enemigo_spider3=pygame.image.load("Sprites/spider/idle3.png")
enemigo_spider4=pygame.image.load("Sprites/spider/idle4.png")
spiders=[enemigo_spider,enemigo_spider2,enemigo_spider3,enemigo_spider4]


run1=pygame.image.load("Sprites/dog/run1.png")
run2=pygame.image.load("Sprites/dog/run2.png")
run3=pygame.image.load("Sprites/dog/run3.png")
run4=pygame.image.load("Sprites/dog/run4.png")
run5=pygame.image.load("Sprites/dog/run5.png")
run6=pygame.image.load("Sprites/dog/run6.png")
run7=pygame.image.load("Sprites/dog/run7.png")
attack=pygame.image.load("Sprites/dog/atack.png")
run1i=pygame.transform.flip(run1,True,False)
run2i=pygame.transform.flip(run2,True,False)
run3i=pygame.transform.flip(run3,True,False)
run4i=pygame.transform.flip(run4,True,False)
run5i=pygame.transform.flip(run5,True,False)
run6i=pygame.transform.flip(run6,True,False)
run7i=pygame.transform.flip(run7,True,False)
attack_inv=pygame.transform.flip(attack,True,False)
run=[run1,run2,run3,run4,run5,run6,run7,attack]
run_inv=[run1i,run2i,run3i,run4i,run5i,run6i,run7i,attack_inv]
runs=[run,run_inv]
#Atacado
hurt1=pygame.image.load("Sprites/dog/hurt1.png")
hurt2=pygame.image.load("Sprites/dog/hurt2.png")
hurt3=pygame.image.load("Sprites/dog/hurt3.png")

hurt1i=pygame.transform.flip(hurt1,True,False)
hurt2i=pygame.transform.flip(hurt2,True,False)
hurt3i=pygame.transform.flip(hurt3,True,False)

hurt=[hurt1,hurt2,hurt3]
hurt_inv=[hurt1i,hurt2i,hurt3i]
hurts=[hurt,hurt_inv]
#Muere
dead1=pygame.image.load("Sprites/dog/dead1.png")
dead2=pygame.image.load("Sprites/dog/dead2.png")
dead3=pygame.image.load("Sprites/dog/dead3.png")
dead4=pygame.image.load("Sprites/dog/dead4.png")
dead1i=pygame.transform.flip(dead1,True,False)
dead2i=pygame.transform.flip(dead2,True,False)
dead3i=pygame.transform.flip(dead3,True,False)
dead4i=pygame.transform.flip(dead4,True,False)
dead=[dead1,dead2,dead3,dead4]
dead_inv=[dead1i,dead2i,dead3i,dead4i]
dies=[dead,dead_inv]