import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([800, 800])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Cor de fundo preta, caso não seja padrão

    # Orelhas
    pygame.draw.polygon(screen, WHITE, ((350, 150), (300, 250), (400, 250)), 6)  # Orelha esquerda
    pygame.draw.polygon(screen, WHITE, ((450, 150), (400, 250), (500, 250)), 6)  # Orelha direita

    # Cabeça
    pygame.draw.polygon(screen, WHITE, ((300, 250), (500, 250), (550, 350), (400, 400), (250, 350)), 6)

    # Olhos
    pygame.draw.line(screen, WHITE, (340, 290), (360, 290), 6)  # Olho esquerdo
    pygame.draw.line(screen, WHITE, (440, 290), (460, 290), 6)  # Olho direito

    # Nariz
    pygame.draw.polygon(screen, WHITE, ((395, 320), (405, 320), (400, 330)), 6)

    # Boca
    pygame.draw.line(screen, WHITE, (400, 330), (400, 340), 6)  # Linha vertical da boca
    pygame.draw.line(screen, WHITE, (400, 340), (390, 350), 6)  # Lado esquerdo da boca
    pygame.draw.line(screen, WHITE, (400, 340), (410, 350), 6)  # Lado direito da boca

    # Bigodes
    pygame.draw.line(screen, WHITE, (380, 350), (350, 360), 3)  # Bigodes esquerdo
    pygame.draw.line(screen, WHITE, (380, 350), (350, 370), 3)
    pygame.draw.line(screen, WHITE, (380, 350), (350, 380), 3)
    pygame.draw.line(screen, WHITE, (420, 350), (450, 360), 3)  # Bigodes direito
    pygame.draw.line(screen, WHITE, (420, 350), (450, 370), 3)
    pygame.draw.line(screen, WHITE, (420, 350), (450, 380), 3)

    pygame.display.flip()  # Atualiza a tela

pygame.quit()
