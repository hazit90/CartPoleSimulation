import pygame
import numpy as np
from utilities import BLUE, GREEN, HEIGHT, CART_WIDTH, CART_HEIGHT, POLE_LENGTH, POLE_WIDTH

def draw_cartpole(screen, cartpole):
    # Draw cart with BLUE color
    pygame.draw.rect(screen, BLUE, (cartpole.cart_pos, HEIGHT - CART_HEIGHT, CART_WIDTH, CART_HEIGHT))
    
    # Calculate pole endpoints
    pole_x1 = cartpole.cart_pos + CART_WIDTH // 2
    pole_y1 = HEIGHT - CART_HEIGHT
    pole_x2 = pole_x1 + POLE_LENGTH * np.sin(cartpole.pole_angle)
    pole_y2 = pole_y1 - POLE_LENGTH * np.cos(cartpole.pole_angle)
    
    # Draw pole with GREEN color
    pygame.draw.line(screen, GREEN, (pole_x1, pole_y1), (pole_x2, pole_y2), POLE_WIDTH)
