from .base_stepper import StepperInterface

class SimStepper(StepperInterface):
    def __init__(self, clock_id, hand, surface):
        self.id = clock_id
        self.hand = hand      # 'h' oder 'm'
        self.surface = surface
        self.pos = 0          # in Steps

    def init(self):
        pass  # hier ggf. Pygame-Primitiven anlegen

    def step(self, steps, speed):
        self.pos = (self.pos + steps) % 200
        # optional: Animation in Pygame-Loop einplanen

    def reset(self):
        self.pos = 0
