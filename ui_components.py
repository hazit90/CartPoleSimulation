import pygame
from utilities import BLACK, GREEN

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont(None, 25)
        label = font.render(self.text, True, BLACK)
        screen.blit(label, (self.x + (self.width - label.get_width()) // 2, self.y + (self.height - label.get_height()) // 2))

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

class Slider:
    def __init__(self, x, y, width, min_val, max_val):
        self.x = x
        self.y = y
        self.width = width
        self.min_val = min_val
        self.max_val = max_val
        self.value = (min_val + max_val) / 2
        self.slider_pos = x + width // 2  # Start in the middle

    def draw(self, screen):
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.width, self.y), 3)
        pygame.draw.circle(screen, GREEN, (self.slider_pos, self.y), 10)

    def update(self, pos):
        if self.x <= pos[0] <= self.x + self.width:
            self.slider_pos = pos[0]
            self.value = self.min_val + (self.slider_pos - self.x) * (self.max_val - self.min_val) / self.width
