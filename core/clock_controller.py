# pure logic, keine Hardware-Abhängigkeiten
def angle_to_steps(angle_deg: float, steps_per_rev=200) -> int:
    return int((angle_deg / 360) * steps_per_rev)

class ClockController:
    def __init__(self, stepper_hour, stepper_min):
        self.h = stepper_hour
        self.m = stepper_min

    def move_to(self, hour_angle: float, min_angle: float, speed: float):
        steps_h = angle_to_steps(hour_angle)
        steps_m = angle_to_steps(min_angle)
        self.h.step(steps_h, speed)
        self.m.step(steps_m, speed)
