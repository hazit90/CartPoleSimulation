from utilities import WIDTH, CART_WIDTH

class CartPole:
    def __init__(self):
        self.cart_pos = WIDTH // 2
        self.cart_vel = 0
        self.pole_angle = 0  # in radians
        self.pole_angular_vel = 0

    def update(self, action, angular_velocity_value):
        # Update cart properties
        self.cart_pos = min(max(self.cart_pos + self.cart_vel, 0), WIDTH - CART_WIDTH)
        self.cart_vel += action

        # Update pole properties
        self.pole_angle += self.pole_angular_vel
        self.pole_angular_vel = angular_velocity_value / 100.0