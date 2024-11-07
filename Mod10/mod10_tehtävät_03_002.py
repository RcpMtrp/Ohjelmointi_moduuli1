class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.floor = lowest_floor

    def move_to_floor(self, target_floor):
        if target_floor > self.floor:
            while target_floor > self.floor:
                self.floor_up()
        elif target_floor < self.floor:
            while target_floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1

class House:
    def __init__(self, num_elevators, lowest_floor, highest_floor):
        self.elevators = [Elevator(lowest_floor, highest_floor) for _ in range(num_elevators)]
        self.fire_alarm_on = False
    def operate_elevator(self, elevator_number, target_floor):
        if self.fire_alarm_on:
            print("Elevators are not working")
            return
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.move_to_floor(target_floor)
            print(f"Elevator {elevator_number} is on floor {target_floor}.")
        else:
            print("Invalid elevator number")

    def fire_alarm(self, fire: bool):
        self.fire_alarm_on = fire
        if fire != False:
            print("Fire alarm has been activated, all elevators will go to the lowest floor.")
            for i, elevator in enumerate(self.elevators):
                elevator.move_to_floor(0)
                print(f"Elevator{i} will go to {elevator.floor}.")
        else:
            print("Fire alarm has been deactivated, you're free to operate the elevators.")

house = House(num_elevators=3, lowest_floor=0, highest_floor=10)

house.operate_elevator(0, 3)
house.operate_elevator(1, 3)
house.operate_elevator(2, 3)
house.fire_alarm(True)
house.operate_elevator(2, 3)