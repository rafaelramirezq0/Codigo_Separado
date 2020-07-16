import pygame,sys,random
from UCSP_constantes import *
from UCSP_main import fondo_x
pygame.init()

class Player(pygame.sprite.Sprite):
    #velocidad inicial
    speed_x=0
    speed_y=0
    #animación base
    cambio=0
    imagen=0
    direc=0
    #constructor
    def __init__(self): 
        super().__init__() 
        # reemplazar con el sprite:
        self.image = runs[self.direc][self.imagen]
        # rectángulo que ocupa
        self.rect = self.image.get_rect()
        
    #esto efectúa el movimiento, va "actualizando" la velocidad e imagen
    def update(self,collision,vida,plataformas):
        self.plataformas=plataformas
        self.vida=vida
        self.ancho=self.image.get_size()[1]
        self.largo=self.image.get_size()[0]
        self.gravity()
        self.deten_ataque()
        #moverse
        self.rect.x += self.speed_x
        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self, self.plataformas, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.speed_x > 0:
                self.rect.right = bloque.rect.left
            elif self.speed_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right
        self.rect.y += self.speed_y
        bloque_col_list = pygame.sprite.spritecollide(self, self.plataformas, False)
        for bloque in bloque_col_list:
            
            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.speed_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.speed_y < 0:
                self.rect.top = bloque.rect.bottom

            self.speed_y = 0
        #animación
        self.imagen += self.cambio
        if self.imagen > len(run)-2 or (self.speed_x==0 and collision==False and self.vida>0):
            self.imagen = 0
        if self.speed_y!=0:
            self.imagen = 5
        if abs(self.speed_x)>5:
            self.imagen=len(run)-1
        self.image=runs[self.direc][self.imagen] 
 
    #gravedad
    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 5
        else:#aceleración de la gravedad
            self.speed_y += 0.35
        #tocar el suelo
        if self.rect.y >= 600 - self.ancho and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = 600 - self.ancho
        #paredes
        if self.rect.x >800-self.largo:
            self.rect.x = 800-self.largo
        if self.rect.x <0:
            self.rect.left =0    
        if fondo_x <= -1*bosque_fondo_lv1.get_rect().width + ancho or fondo_x == 0:
            mover_fondo = False
            #dfx = 0
        else:
          if self.direc == 0:
            if self.rect.right >=350:
                self.rect.x = 350 - self.rect.width
            elif self.rect.left <= 0:
                self.rect.x = 0
            elif self.rect.left >= 350 - (1.1*self.rect.width):
                self.rect.x = 350 - self.rect.width
                
          elif self.direc == 1:
            ### FALTA ARREGLAR
            pass





    #movimientos 
    def izquierda(self):
        if self.vida>0:
            self.speed_x = -5
            self.cambio = 1
            self.direc=1
    def derecha(self):
        if self.vida>0:
            self.speed_x = 5
            self.cambio = 1
            self.direc=0
    def saltar(self):
        if self.vida > 0:
            self.rect.y += 2
            plataforma_col_lista = pygame.sprite.spritecollide(self, self.plataformas, False)
            self.rect.y -= 2
            if len(plataforma_col_lista)>0 or self.rect.bottom >= 600: #si está en una plataforma o piso
                self.speed_y = -10
    def stop(self):
        self.speed_x = 0
        self.gravity()
    def ataque(self):
        if self.imagen!=len(run)-1:
            self.speed_x*=2
    #frenos (funciona de forma similar a la gravedad, solo que desacelera)
    def deten_ataque(self):
        if self.speed_x>5:
            self.speed_x-=0.15
        if self.speed_x<-5:
            self.speed_x+=0.15
    def get_hurt(self):
        self.cambio = 1
        if self.imagen>=len(hurt)-1:
            self.imagen=0
        self.image=hurts[self.direc][self.imagen]
    def die(self):
        self.cambio = 1
        if self.imagen>=len(dead)-1:
            self.imagen=len(dead)-1
        self.image=dies[self.direc][self.imagen]



    

class Enemy(pygame.sprite.Sprite):
    def __init__(self,movs,velocidad):
        super().__init__()
        self.imagen=0
        self.image = movs[self.imagen]
        self.speed = velocidad
        self.rect=self.image.get_rect()
        self.size=self.image.get_size()
        self.movs=movs   
    def muerte(self):
        self.imagen=movs[len(movs)-1]
class Spider(Enemy):
    def __init__(self,movs,velocidad):
        super().__init__(movs,velocidad)
    def mover(self):
        self.rect.y+=self.speed
        self.image = self.movs[self.imagen]
        #cuando choca arriba
        if self.rect.y <= 0:
            self.speed = 3
        #cuando choca abajo 
        elif self.rect.y >= random.randint(400, ancho):#alto- spider_size[0]:
            self.speed = -3
        self.imagen+=1
        if self.imagen>=len(self.movs)-2:
            self.imagen=0
class Rat(Enemy):
    def __init__(self,movs,velocidad):
        super().__init__(movs,velocidad)
    def mover(self):
        self.rect.x-=self.speed
        #izquierda
        if self.rect.x <= 0:
            self.speed = -3
            self.imagen = 1
        #derecha
        elif self.rect.x >= ancho- self.size[0]:
            self.speed = 3
            self.imagen = 0
        self.image = self.movs[self.imagen]
class Plataforma(pygame.sprite.Sprite):
 
    def __init__(self, largo, alto, x, y):
        super().__init__()
        self.image=pygame.image.load("Sprites/tronco.jpg")
        self.image=pygame.transform.scale(self.image,(100,20))
        self.rect = self.image.get_rect()                    
        self.rect.x = x
        self.rect.y = y

