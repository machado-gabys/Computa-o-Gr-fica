import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Inicializar Pygame e criar a janela
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glOrtho(0, display[0], 0, display[1], -1, 1)

# Lista para armazenar pontos
points = []

# Variáveis para cor e tamanho dos pontos
point_color = (1.0, 0.0, 0.0)  # Cor inicial vermelha
point_size = 5

def draw_points():
    #Função para desenhar todos os pontos armazenados na lista points.
    glColor3f(point_color[0], point_color[1], point_color[2])  # Define a cor dos pontos
    glPointSize(point_size)  # Define o tamanho dos pontos
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], display[1] - point[1])
    glEnd()

def reset_points():
    #Função para limpar todos os pontos da lista points.
    global points
    points = []

def random_color():
    """Função para gerar uma cor aleatória."""
    return (random.random(), random.random(), random.random())

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 10 < pos[0] < 110 and 10 < display[1] - pos[1] < 40:  # Verifica se o clique do mouse foi dentro das coordenadas do botão de reset
                reset_points()  # Limpa todos os pontos se o botão de reset foi clicado
            else:
                points.append(pos)  # Adiciona o ponto à lista de pontos se o clique do mouse não foi no botão de reset
                point_color = random_color()  # Atualiza a cor dos pontos para uma cor aleatória

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_points()

    # Desenhar o botão de reset
    glColor3f(0.0, 0.0, 1.0)  # Cor azul para o botão
    glBegin(GL_QUADS)
    glVertex2f(10, 10)  # Canto superior esquerdo
    glVertex2f(110, 10)  # Canto superior direito
    glVertex2f(110, 40)  # Canto inferior direito
    glVertex2f(10, 40)  # Canto inferior esquerdo
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
