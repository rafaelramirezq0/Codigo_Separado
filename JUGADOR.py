import pygame, sys

screen=pygame.display.set_mode([800,600])
reloj=pygame.time.Clock()
background=pygame.image.load("Backgrounds/forest_loop.png")
#colores
blanco=(255,255,255)
negro=(0,0,0)
#===========
pygame.init()

listade_todoslos_sprites = pygame.sprite.Group()
#Jugador (o sea el perrito)
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