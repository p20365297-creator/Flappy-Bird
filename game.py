import pygame
import os
from settings import WIDTH, HEIGHT

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.high_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")
        self.highscore_file = "highscore.txt"
        self.highscore = self.load_highscore()

    def load_highscore(self):
        if os.path.exists(self.highscore_file):
            try:
                with open(self.highscore_file, "r") as file:
                    return int(file.read().strip())
            except (ValueError, OSError):
                return 0
        return 0

    def update_highscore(self, int_score):
        if int_score > self.highscore:
            self.highscore = int_score

            with open(self.highscore_file, "w") as file:
                file.write(str(self.highscore))

    def show_score(self, int_score):
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        score_rect = score.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(score, score_rect)

        self.update_highscore(int_score)
        high_text = self.high_font.render(f"Best : {self.highscore}", True, self.color)
        high_rect = high_text.get_rect(center=(WIDTH // 2, 100))
        self.screen.blit(high_text, high_rect)

    def instructions(self):
        inst_text1 = "Press SPACE button to Jump,"
        inst_text2 = "Press \"R\" Button to Restart Game."
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(ins1, (95, 400))
        self.screen.blit(ins2, (70, 450))