import pygame
from cart_pole import CartPole
from ui_components import Button, Slider
from utilities import WHITE, WIDTH, HEIGHT, SLIDER_RANGE, GREEN
from render import draw_cartpole

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cart-Pole Simulation")

cartpole = CartPole()
angular_velocity_slider = Slider(50, HEIGHT - 50, 300, -SLIDER_RANGE, SLIDER_RANGE)
reset_button = Button(WIDTH - 100, HEIGHT - 50, 80, 30, "Reset", GREEN)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if reset_button.is_clicked(event.pos):
                    cartpole = CartPole()  # Reset the cart-pole simulation
                    angular_velocity_slider = Slider(50, HEIGHT - 50, 300, -100, 100)
                else:
                    angular_velocity_slider.update(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:  # Check for mouse button release
            if event.button == 1:  # Left mouse button
                # Reset the slider position to the middle (which represents a value of zero)
                angular_velocity_slider.slider_pos = angular_velocity_slider.x + angular_velocity_slider.width // 2
                angular_velocity_slider.value = (angular_velocity_slider.min_val + angular_velocity_slider.max_val) / 2

    # Update and draw cart-pole
    cartpole.update(angular_velocity_slider.value, angular_velocity_slider.value)
    draw_cartpole(screen, cartpole)
    angular_velocity_slider.draw(screen)
    reset_button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
