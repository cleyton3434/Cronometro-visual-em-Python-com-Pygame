import pygame
import sys
import os
from pygame._sdl2 import Window

# ================= SOM (ROBUSTO PARA WINDOWS) =================
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOM_PATH = os.path.join(BASE_DIR, "beep.wav")

try:
    pygame.mixer.set_num_channels(8)
    som_fim = pygame.mixer.Sound(SOM_PATH)
    som_fim.set_volume(1.0)
    canal_som = pygame.mixer.Channel(0)
except:
    som_fim = None
    canal_som = None
# =============================================================

# ---------------- CONFIG ----------------
ALTURA = 140#150
LARGURA_MIN = 200#220
FPS = 60#60

PRETO = (15, 15, 15)
CINZA = (40, 40, 40)
BRANCO = (230, 230, 230)
VERDE = (0, 200, 120)
VERMELHO = (220, 60, 60)

# ---------------- FONTES ----------------
fonte = pygame.font.SysFont("arial", 22, bold=True)
fonte_peq = pygame.font.SysFont("arial", 16)
fonte_alerta = pygame.font.SysFont("arial", 18, bold=True)

clock = pygame.time.Clock()

# ---------------- JANELA ----------------
cronometros = []

def largura_auto():
    return max(LARGURA_MIN, 40 + len(cronometros) * 180)

tela = pygame.display.set_mode((largura_auto(), ALTURA), pygame.NOFRAME)
pygame.display.set_caption("Cronômetros Aula")
window = Window.from_display_module()

# ---------------- ARRASTO ----------------
arrastando = False
offset = (0, 0)

# ---------------- CLASSE ----------------
class Cronometro:
    def __init__(self, m=1, s=0):
        self.tempo = m * 60 + s
        self.inicial = self.tempo
        self.rodando = False
        self.finalizado = False
        self.alerta_timer = 0  # controla o piscar

    def atualizar(self, dt):
        if self.rodando and self.tempo > 0:
            self.tempo -= dt
            if self.tempo <= 0:
                self.tempo = 0
                self.rodando = False
                self.finalizado = True
                self.alerta_timer = 3  # segundos de alerta

                if som_fim and canal_som:
                    canal_som.play(som_fim)

        if self.alerta_timer > 0:
            self.alerta_timer -= dt
            if self.alerta_timer < 0:
                self.alerta_timer = 0

    def texto(self):
        t = int(self.tempo)
        return f"{t // 60:02}:{t % 60:02}"

    def reset(self):
        self.tempo = self.inicial
        self.rodando = False
        self.finalizado = False
        self.alerta_timer = 0

# ---------------- FUNÇÕES ----------------
def adicionar():
    cronometros.append(Cronometro())
    ajustar_janela()

def remover(i):
    cronometros.pop(i)
    ajustar_janela()

def ajustar_janela():
    global tela, window
    tela = pygame.display.set_mode((largura_auto(), ALTURA), pygame.NOFRAME)
    window = Window.from_display_module()

def sequencia_auto():
    for i, c in enumerate(cronometros):
        if c.finalizado:
            c.finalizado = False
            if i + 1 < len(cronometros):
                cronometros[i + 1].rodando = True

# ---------------- LOOP ----------------
while True:
    dt = clock.tick(FPS) / 1000

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.pos[0] < 40:
                arrastando = True
                offset = e.pos

            if 10 < e.pos[0] < 35 and 10 < e.pos[1] < 35:
                adicionar()

            for i, c in enumerate(cronometros):
                x = 50 + i * 180

                if x + 10 < e.pos[0] < x + 35 and 90 < e.pos[1] < 115:
                    c.rodando = not c.rodando

                if x + 140 < e.pos[0] < x + 165 and 10 < e.pos[1] < 35:
                    remover(i)
                    break

                if x + 40 < e.pos[0] < x + 80 and 50 < e.pos[1] < 70:
                    c.tempo += 60
                    c.inicial = c.tempo

                if x + 90 < e.pos[0] < x + 130 and 50 < e.pos[1] < 70:
                    c.tempo = max(0, c.tempo - 10)
                    c.inicial = c.tempo

        if e.type == pygame.MOUSEMOTION and arrastando:
            mx, my = pygame.mouse.get_pos()
            wx, wy = window.position
            window.position = (wx + mx - offset[0], wy + my - offset[1])

        if e.type == pygame.MOUSEBUTTONUP:
            arrastando = False

    for c in cronometros:
        c.atualizar(dt)

    sequencia_auto()

    # ---------------- DESENHO ----------------
    tela.fill(PRETO)
    pygame.draw.rect(tela, CINZA, (0, 0, 40, ALTURA))
    tela.blit(fonte.render("+", True, BRANCO), (14, 8))

    for i, c in enumerate(cronometros):
        x = 50 + i * 180

        # Piscar vermelho se alerta ativo
        cor_fundo = VERMELHO if c.alerta_timer > 0 and int(c.alerta_timer * 5) % 2 == 0 else CINZA

        pygame.draw.rect(tela, cor_fundo, (x, 40, 160, 90), border_radius=8)

        tela.blit(fonte.render(c.texto(), True, BRANCO), (x + 35, 10))

        if c.alerta_timer > 0:
            tela.blit(fonte_alerta.render("TEMPO ESGOTADO", True, BRANCO), (x + 15, 70))

        tela.blit(fonte_peq.render("▲ min", True, VERDE), (x + 40, 50))
        tela.blit(fonte_peq.render("▼ seg", True, VERDE), (x + 90, 50))

        pygame.draw.rect(tela, VERDE, (x + 10, 90, 25, 25), border_radius=5)
        tela.blit(fonte_peq.render("▶", True, PRETO), (x + 15, 93))

        pygame.draw.rect(tela, (180, 60, 60), (x + 140, 10, 25, 25), border_radius=5)
        tela.blit(fonte_peq.render("X", True, BRANCO), (x + 147, 12))

    pygame.display.flip()
