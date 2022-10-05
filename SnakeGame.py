import random
import pygame


class cuerpo():
    def __init__(self, pantalla):
        self.x = 0
        self.y = 0
        self.direccion = 0
        self.pantalla = pantalla
    
    def dibujar(self):
        pygame.draw.rect(self.pantalla, (255,255,255), (self.x, self.y, 10, 10))
    
    def movimiento(self):
        if self.direccion == 0:
            self.x += 10
        elif self.direccion == 1:
            self.x -= 10
        elif self.direccion == 2:
            self.y += 10
        elif self.direccion == 3:
            self.y -= 10
        
class manzanas():
    def __init__(self, pantalla):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.pantalla = pantalla
    
    def dibujar(self):
        pygame.draw.rect(self.pantalla, (255, 0, 0), (self.x, self.y, 10, 10))
    
    def nuevaManzana(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10       

def refrescar(pantalla):
    pantalla.fill((0,0,0))      
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()

def seguirCabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente)-i-1].x = serpiente[len(serpiente)-i-2].x
        serpiente[len(serpiente)-i-1].y = serpiente[len(serpiente)-i-2].y

def colision():
    choque = False
    if (len(serpiente)) > 1:
        for i in range(len(serpiente) - 1):
            if serpiente[0].x == serpiente[i + 1].x and serpiente[0].y == serpiente[i + 1].y:
                choque = True
    return choque

def main():
    global serpiente, comida
    pantalla = pygame.display.set_mode((400,400))
    pantalla.fill((0, 0, 0))
    pygame.display.set_caption("Serpiente")
    serpiente = [cuerpo(pantalla)]
    serpiente[0].dibujar()
    comida = manzanas(pantalla)
    refrescar(pantalla)
    run = True
    velocidad = 100
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    serpiente[0].direccion = 0
                if event.key == pygame.K_LEFT:
                    serpiente[0].direccion = 1
                if event.key == pygame.K_DOWN:
                    serpiente[0].direccion = 2
                if event.key == pygame.K_UP:
                    serpiente[0].direccion = 3
        seguirCabeza()
        serpiente[0].movimiento()
        refrescar(pantalla)            
        pygame.display.update()
        pygame.time.delay(velocidad)
        
        
        #Si la serpiente se sale de pantalla doy opcion de que apararezca por el otro extremo. 
        
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        elif serpiente[0].x <= 0:
            serpiente[0].x = 390
            
        if serpiente[0].y >= 400:
            serpiente[0].y = 0
        elif serpiente[0].y <= 0:
            serpiente[0].y = 390
        
        
        #Si no doy otra opcion de que salga automaticamente del juego
        
        # if serpiente[0].x >= 400:
        #     run = False
        # elif serpiente[0].x < 0:
        #     run = False
        # if serpiente[0].y >= 400:
        #     run = False
        # elif serpiente[0].y < 0:
        #     run = False
            
        if colision():
            serpiente = [cuerpo(pantalla)]
            comida.nuevaManzana()
            velocidad = 100
        
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            if velocidad > 35:
                velocidad -= 5
            comida.nuevaManzana()
            serpiente.append(cuerpo(pantalla))
            seguirCabeza()
if __name__ == "__main__":
    main()
    pygame.quit()
    