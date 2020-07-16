import pygame, sys
import time
import random
from UCSP_intros import *
from JUGADOR import *
pygame.init()
pygame.mixer.init()
pygame.init()

#Constante
ancho= 800
largo = 600
vidas=10

pygame.display.set_caption("Doggo Adventure")
pygame.display.set_icon(pygame.image.load("Sprites/icon.png"))
screen = pygame.display.set_mode((ancho,largo))
reloj = pygame.time.Clock()
listade_todoslos_sprites = pygame.sprite.Group()

# Estado del Juego
Intro1 = False
Intro2 = False
Intro3 = False
Nivel1 = True

# Fondos Niveles
bosque_fondo_lv1 = pygame.image.load("Backgrounds/nivel1_x3.png").convert()
bosque_fondo_lv2 = pygame.image.load("Backgrounds/nivel2_x3.png").convert()
bosque_fondo_lv3 = pygame.image.load("Backgrounds/nivel3_x4.png").convert()
fondo_x = -100

listade_todoslos_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
enemigo_rat= pygame.image.load("Sprites/rat/rat_idle.png")
enemigo_rat_inv= pygame.transform.flip(enemigo_rat,True,False)
rats=[enemigo_rat,enemigo_rat_inv]

enemigo_spider=pygame.image.load("Sprites/spider/idle1.png")
enemigo_spider2=pygame.image.load("Sprites/spider/idle2.png")
enemigo_spider3=pygame.image.load("Sprites/spider/idle3.png")
enemigo_spider4=pygame.image.load("Sprites/spider/idle4.png")
spiders=[enemigo_spider,enemigo_spider2,enemigo_spider3,enemigo_spider4]

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
tipo_letra1 = pygame.font.Font('freesansbold.ttf', 28)
tipo_letra2 = pygame.font.Font('freesansbold.ttf', 100)
vidas=1000
jugador=Player()
rat=Rat(rats,4)
rat2=Rat(rats,4)
rat3=Rat(rats,4)
rat4=Rat(rats,4)
rat5=Rat(rats,4)
spider=Spider(spiders,3)

enemigos.add(rat,rat2,rat3,rat4,rat5,spider)
plataformas.add(plat1,plat2,plat3)
listade_todoslos_sprites.add(jugador,enemigos,plataformas)
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
rat.rect.x=800//2-(rat.size[0]//2)
rat.rect.y=600-(rat.size[1])
rat2.rect.x=500
rat2.rect.y=600-(rat2.size[1])
rat3.rect.x=450
rat3.rect.y=500
rat4.rect.x=200
rat4.rect.y=600-(rat4.size[1])
rat5.rect.x=100
rat5.rect.y=600-(rat5.size[1])

spider.rect.x= random.randint(0,largo-spider.rect.width)
spider.rect.y= random.randint(0,ancho-spider.rect.height)
gets_hit = False

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


# Función Intro
animation_list1 = [intro1,intro2,intro3,intro4,intro5,intro6,intro7,intro8,intro9,intro10,intro11,intro12,intro13,intro14,intro15,intro16,intro17,intro18,intro19,intro20,intro21,intro22,intro23,intro24,intro25,intro26,intro27,intro28,intro29,intro30,intro31,intro32,intro33,intro34,intro35,intro36,intro37,intro38,intro39,intro40,intro41,intro42,intro43,intro44,intro45,intro46,intro47,intro48,intro49,intro50,intro51,intro52,intro53,intro54,intro55,intro56,intro57,intro58,intro59,intro60,intro61,intro62,intro63,intro64,intro65,intro66,intro67,intro68,intro69,intro70,intro71,intro72,intro73,intro74,intro75,intro76,intro77,intro78,intro79,intro80,intro81,intro82,intro83,intro84,intro85,intro86,intro87,intro88,intro89,intro90,intro91,intro92,intro93,intro94,intro95,intro96,intro97,intro98,intro99,intro100,intro101,intro102,intro103,intro104,intro105,intro106,intro107,intro108,intro109,intro110,intro111,intro112,intro113,intro114,intro115,intro116,intro117,intro118,intro119,intro120,intro121,intro122,intro123,intro124,intro125,intro126,intro127,intro128,intro129,intro130,intro131,intro132,intro133,intro134,intro135,intro136,intro137,intro138,intro139,intro140,intro141,intro142,intro143,intro144,intro145,intro146,intro147,intro148,intro149,intro150,intro151,intro152,intro153,intro154,intro155,intro156,intro157,intro158,intro159,intro160,intro161,intro162,intro163,intro164,intro165,intro166,intro167,intro168,intro169,intro170,intro171,intro172,intro173,intro174,intro175,intro176,intro177,intro178,intro179,intro180,intro181,intro182,intro183,intro184,intro185,intro186,intro187,intro188,intro189,intro190,intro191,intro192,intro193,intro194,intro195,intro196,intro197,intro198,intro199,intro200,intro201,intro202,intro203,intro204,intro205,intro206,intro207,intro208,intro209,intro210,intro211,intro212,intro213,intro214,intro215,intro216,intro217,intro218,intro219,intro220,intro221,intro222,intro223,intro224,intro225,intro226,intro227,intro228,intro229,intro230,intro231,intro232,intro233,intro234,intro235,intro236,intro237,intro238,intro239,intro240,intro241,intro242,intro243,intro244,intro245,intro246,intro247,intro248,intro249,intro250,intro251,intro252,intro253,intro254,intro255,intro256,intro257,intro258,intro259,intro260,intro261,intro262,intro263,intro264,intro265,intro266,intro267,intro268,intro269,intro270,intro271,intro272,intro273,intro274,intro275,intro276,intro277,intro278,intro279,intro280,intro281,intro282,intro283,intro284,intro285,intro286,intro287,intro288,intro289,intro290,intro291,intro292,intro293,intro294,intro295,intro296,intro297,intro298,intro299,intro300,intro301,intro302,intro303,intro304,intro305,intro306,intro307,intro308,intro309,intro310,intro311,intro312,intro313,intro314,intro315,intro316,intro317,intro318,intro319,intro320,intro321,intro322,intro323,intro324,intro325,intro326,intro327,intro328,intro329,intro330,intro331,intro332,intro333,intro334,intro335,intro336,intro337,intro338,intro339,intro340,intro341,intro342,intro343,intro344,intro345,intro346,intro347,intro348,intro349,intro350,intro351,intro352,intro353,intro354,intro355,intro356,intro357,intro358,intro359,intro360,intro361,intro362,intro363,intro364,intro365,intro366,intro367,intro368,intro369,intro370,intro371,intro372,intro373,intro374]
animation_list2 = [intro_img1,intro_img2,intro_img3,intro_img4]
animation_list3 = [cutscene1,cutscene2,cutscene3,cutscene4,cutscene5,cutscene6,cutscene7,cutscene8,cutscene9,cutscene10,cutscene11,cutscene12,cutscene13,cutscene14,cutscene15,cutscene16,cutscene17,cutscene18,cutscene19,cutscene20,cutscene21,cutscene22,cutscene23,cutscene24,cutscene25,cutscene26,cutscene27,cutscene28,cutscene29,cutscene30,cutscene31,cutscene32,cutscene33,cutscene34,cutscene35,cutscene36,cutscene37,cutscene38,cutscene39,cutscene40,cutscene41,cutscene42,cutscene43,cutscene44,cutscene45,cutscene46,cutscene47,cutscene48,cutscene49,cutscene50,cutscene51,cutscene52,cutscene53,cutscene54,cutscene55,cutscene56,cutscene57,cutscene58,cutscene59,cutscene60,cutscene61,cutscene62,cutscene63,cutscene64,cutscene65,cutscene66,cutscene67,cutscene68,cutscene69,cutscene70,cutscene71,cutscene72,cutscene73,cutscene74,cutscene75,cutscene76,cutscene77,cutscene78,cutscene79,cutscene80,cutscene81,cutscene82,cutscene83,cutscene84,cutscene85,cutscene86,cutscene87,cutscene88,cutscene89,cutscene90,cutscene91,cutscene92,cutscene93,cutscene94,cutscene95,cutscene96,cutscene97,cutscene98,cutscene99,cutscene100,cutscene101,cutscene102,cutscene103,cutscene104,cutscene105,cutscene106,cutscene107,cutscene108,cutscene109,cutscene110,cutscene111,cutscene112,cutscene113,cutscene114,cutscene115,cutscene116,cutscene117,cutscene118,cutscene119,cutscene120,cutscene121,cutscene122,cutscene123,cutscene124,cutscene125,cutscene126,cutscene127,cutscene128,cutscene129,cutscene130,cutscene131,cutscene132,cutscene133,cutscene134,cutscene135,cutscene136,cutscene137,cutscene138,cutscene139,cutscene140,cutscene141,cutscene142,cutscene143,cutscene144,cutscene145,cutscene146,cutscene147,cutscene148,cutscene149,cutscene150,cutscene151,cutscene152,cutscene153,cutscene154,cutscene155,cutscene156,cutscene157,cutscene158,cutscene159,cutscene160,cutscene161,cutscene162,cutscene163,cutscene164,cutscene165,cutscene166,cutscene167,cutscene168,cutscene169,cutscene170,cutscene171,cutscene172,cutscene173,cutscene174,cutscene175,cutscene176,cutscene177,cutscene178,cutscene179,cutscene180,cutscene181,cutscene182,cutscene183,cutscene184,cutscene185,cutscene186,cutscene187,cutscene188,cutscene189,cutscene190,cutscene191,cutscene192,cutscene193,cutscene194,cutscene195,cutscene196,cutscene197,cutscene198,cutscene199,cutscene200,cutscene201,cutscene202,cutscene203,cutscene204,cutscene205,cutscene206,cutscene207,cutscene208,cutscene209,cutscene210,cutscene211,cutscene212,cutscene213,cutscene214,cutscene215,cutscene216,cutscene217,cutscene218,cutscene219,cutscene220,cutscene221,cutscene222,cutscene223,cutscene224,cutscene225,cutscene226,cutscene227,cutscene228,cutscene229,cutscene230,cutscene231,cutscene232,cutscene233,cutscene234,cutscene235,cutscene236,cutscene237,cutscene238,cutscene239,cutscene240,cutscene241,cutscene242,cutscene243,cutscene244,cutscene245,cutscene246,cutscene247,cutscene248,cutscene249,cutscene250,cutscene251,cutscene252,cutscene253,cutscene254,cutscene255,cutscene256,cutscene257,cutscene258,cutscene259,cutscene260,cutscene261,cutscene262,cutscene263,cutscene264,cutscene265,cutscene266,cutscene267,cutscene268,cutscene269,cutscene270,cutscene271,cutscene272,cutscene273,cutscene274,cutscene275,cutscene276,cutscene277,cutscene278,cutscene279,cutscene280,cutscene281,cutscene282,cutscene283,cutscene284,cutscene285,cutscene286,cutscene287,cutscene288,cutscene289,cutscene290,cutscene291,cutscene292,cutscene293,cutscene294,cutscene295,cutscene296,cutscene297,cutscene298,cutscene299,cutscene300,cutscene301,cutscene302,cutscene303,cutscene304,cutscene305,cutscene306,cutscene307,cutscene308,cutscene309,cutscene310,cutscene311,cutscene312,cutscene313,cutscene314,cutscene315,cutscene316,cutscene317,cutscene318,cutscene319,cutscene320,cutscene321,cutscene322,cutscene323,cutscene324,cutscene325,cutscene326,cutscene327,cutscene328,cutscene329,cutscene330,cutscene331,cutscene332,cutscene333,cutscene334,cutscene335,cutscene336,cutscene337,cutscene338,cutscene339,cutscene340,cutscene341,cutscene342,cutscene343,cutscene344,cutscene345,cutscene346,cutscene347,cutscene348,cutscene349,cutscene350,cutscene351,cutscene352,cutscene353,cutscene354,cutscene355,cutscene356,cutscene357,cutscene358,cutscene359,cutscene360,cutscene361,cutscene362,cutscene363,cutscene364,cutscene365,cutscene366,cutscene367,cutscene368,cutscene369,cutscene370,cutscene371,cutscene372,cutscene373,cutscene374,cutscene375,cutscene376,cutscene377,cutscene378,cutscene379,cutscene380,cutscene381,cutscene382,cutscene383,cutscene384,cutscene385,cutscene386,cutscene387,cutscene388,cutscene389,cutscene390,cutscene391,cutscene392,cutscene393,cutscene394,cutscene395,cutscene396,cutscene397,cutscene398,cutscene399,cutscene400,cutscene401,cutscene402,cutscene403,cutscene404,cutscene405,cutscene406,cutscene407,cutscene408,cutscene409,cutscene410,cutscene411,cutscene412,cutscene413,cutscene414,cutscene415,cutscene416,cutscene417,cutscene418,cutscene419,cutscene420,cutscene421]
def animation_intro1():
    for i in animation_list1:
        screen.blit(i, [0,0])
        time.sleep(0.015)
        pygame.display.update()        
def animation_intro2():
    for i in animation_list2:
        screen.blit(i, [0,0])
        time.sleep(0.3289)
        pygame.display.update()
def animation_intro3():
    for i in animation_list3:
        screen.blit(i, [0,0])
        time.sleep(0.025)
        pygame.display.update()

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
def evento():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
def KeyDown():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            jugador.izquierda()
            mover_fondo = True
            dfx = 5

        if event.key == pygame.K_RIGHT:
            jugador.derecha()
            mover_fondo = True
            dfx = -5
                
        if event.key == pygame.K_UP:
            jugador.saltar()
def KeyUp():
    if event.type == pygame.KEYUP:
        mover_fondo = False 
        if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
            jugador.stop()
                                
        if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
            jugador.stop()




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
                Nivel1 = True

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
                rat.rect.x += dfx + 5
                if fondo_x >= -(4020 - ancho):
                    pass
                else:
                    mover_fondo = True
                    dfx = 5

            if event.key == pygame.K_RIGHT:
                jugador.derecha()
                mover_fondo = True
                dfx = -5
                rat.rect.x -= dfx*2     
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