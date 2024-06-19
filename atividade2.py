import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# Comando que define a projeção ortográfica, que projeta os pontos na tela
glOrtho(0, display[0], 0, display[1], -1, 1)

# Lista de armazenamento de pontos
points = []

def draw_points():
    """Função para desenhar todos os pontos armazenados na lista points."""
    # Inicia o desenho de pontos
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], display[1] - point[1])  # Define a posição do ponto, ajustando a coordenada Y
    glEnd()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        # Condição que verifica se o evento de saída foi acionado
        if event.type == pygame.QUIT:
            running = False
        # Verifica se o evento de clique do mouse foi acionado
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Comando que consegue a posição do clique do mouse
            pos = pygame.mouse.get_pos()
            # Comando que adiciona a posição do clique à lista de pontos
            points.append(pos)

    # Comando para limpar a tela
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa os buffers de cor e profundidade

    # Comando que Desenha os pontos
    draw_points()  # Chama a função para desenhar todos os pontos

    # Comandos para atualizar a tela
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()  # Encerra o Pygame
