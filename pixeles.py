
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = int(640)
HEIGHT = int(480)
 
# Clases
# ---------------------------------------------------------------------
 
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.centery = int(HEIGHT / 2)
        self.speed = [0.5, -0.5]
 
    def actualizar(self, time, pala_jug, pala_cpu, puntos):
        self.rect.centerx += int(self.speed[0] * time)
        self.rect.centery += int(self.speed[1] * time)
 
        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= WIDTH:
            puntos[0] += 1
 
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += int(self.speed[0] * time)
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += int(self.speed[1] * time)
 
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += int(self.speed[0] * time)
 
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += int(self.speed[0] * time)
 
        return puntos
 
class Pala(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = int(HEIGHT / 2)
        self.speed = 0.5
 
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= int(self.speed * time)
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += int(self.speed * time)
 
    def ia(self, time, ball):
        if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += int(self.speed * time)
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= int(self.speed * time)
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error as message:
        raise SystemExit(message)
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

#----------------------------------------------------------------------
# Tipos de fuente
#----------------------------------------------------------------------


def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/coure.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect



"""
### El estilo de fuente pixelado (.fon) no permite cambiar el tamaño.
"""
def coure(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/coure.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect
    
def serife(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/serife.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect

def sserife(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/sserife.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect
    
def vgafix(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/vgafix.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect
    
def vgasys(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("font/pixel/vgasys.fon", 12)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = int(posx)
    salida_rect.centery = int(posy)
    return salida, salida_rect
    
"""
### -------------------------------------------------------------------
"""

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
 
    background_image = load_image('images/fondo_pong.png')
    bola = Bola()
    pala_jug = Pala(30)
    pala_cpu = Pala(WIDTH - 30)
    
    clock = pygame.time.Clock()
 
    puntos = [0, 0]
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos)
        pala_jug.mover(time, keys)
        pala_cpu.ia(time, bola)
        
        titulo, titulo_rect = texto(str("EMSITEL S.A.S."), WIDTH/4, 10)
        titulo2, titulo2_rect = coure(str("EMSITEL S.A.S."), WIDTH/4, 30)
        titulo3, titulo3_rect = serife(str("EMSITEL S.A.S."), WIDTH/4, 50)
        titulo4, titulo4_rect = sserife(str("EMSITEL S.A.S."), WIDTH/4, 70)
        titulo5, titulo5_rect = vgafix(str("EMSITEL S.A.S."), WIDTH/4, 90)
        titulo6, titulo6_rect = vgasys(str("EMSITEL S.A.S."), WIDTH/4, 110)

        p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 60)
        p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)
        
        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)

        screen.blit(titulo2, titulo2_rect)
        screen.blit(titulo3, titulo3_rect)
        screen.blit(titulo4, titulo4_rect)
        screen.blit(titulo5, titulo5_rect)
        screen.blit(titulo6, titulo6_rect)
        
        screen.blit(p_jug, p_jug_rect)
        screen.blit(p_cpu, p_cpu_rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()