import pygame

pygame.init()
size = (640, 480)
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("Arcade Dragons")

game_state = False

reloj = pygame.time.Clock()

while not game_state:
    #eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_state = True


    pantalla.fill((255,255,255))
    panel_juego = pygame.draw.rect(pantalla, (248, 94, 89), [160,120,390,240],0)

    pygame.display.flip()
    reloj.tick(30)
pygame.quit()
