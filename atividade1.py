import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 200, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_shapes():
    # Comando para desenhar uma linha
    pygame.draw.line(screen, WHITE, (10, 20), (100, 50))

    # Comando para desenhar um retângulo
    pygame.draw.rect(screen, WHITE, pygame.Rect(10, 10, 8, 5), 1)

    # Comando para desenhar um retângulo preenchido
    pygame.draw.rect(screen, WHITE, pygame.Rect(10, 10, 8, 5))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_shapes()  # Chama a função para desenhar as formas na tela
        pygame.display.flip()  # Atualiza a tela

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
