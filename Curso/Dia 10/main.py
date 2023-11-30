import io
import pygame
import random
import math
from pygame import mixer

def fuente_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)
#  Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Musica
mixer.music.load('song_fondo.mp3')
mixer.music.set_volume(0.15)
mixer.music.play(-1)

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

# Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font(fuente_como_bytes, 20)
texto_x = 10
texto_y = 10
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))


# Tecto final
fuente_final = pygame.font.Font(fuente_como_bytes, 40)
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (210,200))
    mostrar_puntaje(350,400)


# Jugador
img_jugador = pygame.image.load("nave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 7
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x,y))

for e in range(cantidad_enemigos +1 ):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(0,250))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(25)


# Bala 
balas = []  # ! Queda pendiente xd
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 584
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False
def bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+ 16, y + 10))


# Detectar Colisiones
def colision(x_1,y_1, x_2,y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1,2) + math.pow(y_2 - y_1,2))
    if distancia <= 27:
        return True
    return False


# ! Loop del juego
se_ejecuta = True
while se_ejecuta:
    #Pantalla
    pantalla.blit(fondo, (0,0))

    #Salir
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # Movimiento
        if evento.type == pygame.KEYDOWN:
            # Movimiento a la izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1.7
            # Movimiento a la derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1.7
            # Movimiento a arriba
            if evento.key == pygame.K_UP:
                jugador_y_cambio = -1.7
            # Movimiento a abajo
            if evento.key == pygame.K_DOWN:
                jugador_y_cambio = 1.7
            # Disparar bala 
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.set_volume(0.5)
                    sonido_bala.play()
                    bala_x = jugador_x
                    bala_y = jugador_y
                    bala(bala_x, bala_y)

        # Dejar de moverse
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                jugador_x_cambio = 0
                jugador_y_cambio = 0

    # Cambio de posicion jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio
    # Mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    elif jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536
    jugador(jugador_x,jugador_y)

    
    # Cambio de posicion enemigo
    for e in range(cantidad_enemigos + 1):

        #Fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos +1):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
    # Mantener dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = round(random.uniform(1,2),1)
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1*round(random.uniform(1,2),1)
            enemigo_y[e] += enemigo_y_cambio[e]
        enemigo(enemigo_x[e],enemigo_y[e], e)

        # Colision
        col = colision(enemigo_x[e],enemigo_y[e], bala_x,bala_y)
        if col:
            sonido_colision = mixer.Sound("golpe.mp3")
            sonido_colision.set_volume(0.5)
            sonido_colision.play()
            bala_y = 584
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(0,250)
    


    # Movimiento bala
    if bala_y <= -32:
        bala_y = jugador_y
        bala_visible = False
    if bala_visible:
        bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # Puntaje
    mostrar_puntaje(texto_x, texto_y)


    #Actualizar
    pygame.display.update()
