import pygame, sys, math, datetime
from core.clock_controller import ClockController
from hal.sim_stepper import SimStepper

WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_clock_face(surface, center, radius):
    pygame.draw.circle(surface, BLACK, center, radius, width=2)

def draw_hand(surface, center, angle_deg, length, width):
    theta = math.radians(angle_deg - 90)
    endx = center[0] + length * math.cos(theta)
    endy = center[1] + length * math.sin(theta)
    pygame.draw.line(surface, BLACK, center, (endx, endy), width)

def run_sim():
    pygame.init()
    screen = pygame.display.set_mode((900, 400))
    # Erzeuge 24 Controller mit je 2 SimSteppern
    controllers = []
    for i in range(24):
        h = SimStepper(i, 'h', screen)
        m = SimStepper(i, 'm', screen)
        controllers.append(ClockController(h, m))

    clock = pygame.time.Clock()
    cols, rows = 8, 3

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        screen.fill(WHITE)
        w, h = screen.get_size()
        cell_w, cell_h = w/cols, h/rows
        radius = min(cell_w, cell_h) * 0.4

        now = datetime.datetime.now()
        for idx, ctl in enumerate(controllers):
            col = idx % cols
            row = idx // cols
            center = (int(col*cell_w + cell_w/2), int(row*cell_h + cell_h/2))

            draw_clock_face(screen, center, int(radius))

            hour_angle = ((now.hour % 12) + now.minute/60) * 30
            min_angle  = now.minute * 6

            ctl.move_to(hour_angle, min_angle, speed=100)

            draw_hand(screen, center, hour_angle, radius*0.5, width=4)
            draw_hand(screen, center, min_angle, radius*0.8, width=2)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    run_sim()
