#OBS - BOTÃO DIREITO PARA COMPLETAR A FORMA E PREENCHER A COR
import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glOrtho(0, display[0], 0, display[1], -1, 1)

# Lista para armazenar pontos e formas
points = []
shapes = []

# Variáveis para cor e tamanho dos pontos
point_color = (1.0, 0.0, 0.0)
point_size = 5

def draw_points():
    """Função para desenhar todos os pontos armazenados na lista points."""
    glColor3f(point_color[0], point_color[1], point_color[2])  # Definição da cor dos pontos
    glPointSize(point_size)  # Difinição do tamanho dos pontos
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], display[1] - point[1])
    glEnd()

def draw_lines():
    """Função para desenhar linhas conectando os pontos na ordem em que foram clicados."""
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2f(point[0], display[1] - point[1])
    glEnd()

def draw_shapes():
    """Função para desenhar as formas geométricas preenchidas."""
    for shape in shapes:
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)  # Inicia o desenho da forma preenchida
        for point in shape:
            glVertex2f(point[0], display[1] - point[1])
        glEnd()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:  # Comando que verifica se o clique foi com o botão esquerdo do mouse
                points.append(pos)  # Comando que adiciona o ponto à lista de pontos
            elif event.button == 3:  # Comando que verifica se o clique foi com o botão direito do mouse
                shapes.append(points[:])  # Comando que adiciona uma cópia dos pontos à lista de formas
                points.clear()  # Comando que limpa todos os pontos após fechar uma forma

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_points()
    draw_lines()
    draw_shapes()

    pygame.display.flip() # Atualiza a tela
    pygame.time.wait(10)

pygame.quit()
