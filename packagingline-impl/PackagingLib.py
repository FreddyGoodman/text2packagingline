from typing import List
from Machines import SubMachine, ConveyorBelt, PackagingRobot


class PackagingLine:
    ConveyorBelts: List[ConveyorBelt]
    SubMachines: List[SubMachine]

    def __init__(self, n: int) -> None:
        self.SubMachines = [SubMachine() for _ in range(n)]
        self.ConveyorBelts = []

    def add_conveyor_belt(self, beginning: int, end: int, type: str) -> None:
        assert 0 <= beginning < len(self.submachines)
        assert beginning <= end < len(self.submachines)
        assert not beginning == end
        for SubMachine in self.submachines[beginning:end]:
            assert SubMachine.belt_slots > 0
            SubMachine.belt_slots += -1
        self.conveyor_belts.append(ConveyorBelt(beginning, end, type))
