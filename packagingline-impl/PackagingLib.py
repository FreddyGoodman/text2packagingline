from typing import List
from Machines import SubMachine, ConveyorBelt, PackagingRobot


class PackagingLine:
    ConveyorBelts: List[ConveyorBelt]
    SubMachines: List[SubMachine]

    def __init__(self, n: int) -> None:
        self.SubMachines = [SubMachine() for _ in range(n)]
        self.ConveyorBelts = []

    def add_conveyor_belt(self, beginning: int, end: int) -> None:
        assert 0 <= beginning < len(self.SubMachines)
        assert beginning <= end < len(self.SubMachines)
        self.ConveyorBelts.append(ConveyorBelt(beginning, end))
