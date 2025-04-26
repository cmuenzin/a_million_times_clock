import pygame, sys
from core.clock_controller import ClockController
from hal.sim_stepper import SimStepper

def run_sim():
    pygame.init()
    screen = pygame.display.set_mode((900, 400))
    clocks = []
    for i in range(24):
        h = SimStepper(i, 'h', screen)
        m = SimStepper(i, 'm', screen)
        clocks.append(ClockController(h, m))

    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        screen.fill((255,255,255))
        # Beispiel: alle Uhren auf aktuelle Systemzeit setzen
        import datetime
        now = datetime.datetime.now()
        for idx, ctl in enumerate(clocks):
            hour_angle = ((now.hour % 12) + now.minute/60)*30
            min_angle  = now.minute * 6
            ctl.move_to(hour_angle, min_angle, speed=100)
            # hier Render-Code ergänzen: draw_hand(screen, idx,…)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    run_sim()
