from typing import List
from Machines import SubMachine, ConveyorBelt, PackagingRobot

PICKER_CAPACITY = 25
TRAY_CAPACITY = 50
TRAY_PER_BELT = 4


class PackagingLine:
    conveyor_belts: List[ConveyorBelt]
    submachines: List[SubMachine]

    def __init__(self, n: int) -> None:
        self.submachines = [SubMachine() for _ in range(n)]
        self.conveyor_belts = []

    def add_conveyor_belt(self, beginning: int, end: int, type: str) -> None:
        assert 0 <= beginning < len(self.submachines)
        assert beginning <= end < len(self.submachines)
        assert not beginning == end
        for SubMachine in self.submachines[beginning:end]:
            assert SubMachine.belt_slots > 0
            SubMachine.belt_slots += -1
        self.conveyor_belts.append(ConveyorBelt(beginning, end, type))

    def compute_throughput(self, desired_throughput: int) -> float:
        picker_capacity = []
        for submachine in self.submachines:
            capacity = 0
            for robot in submachine.packaging_robots:
                if robot.type == "picker":
                    capacity += PICKER_CAPACITY
            picker_capacity.append(capacity)

        for conveyor_belt in self.conveyor_belts:
            pass

        # compute cookies per submachine
        # count cookies on conveyor belts
        # and accessible cookies
        
