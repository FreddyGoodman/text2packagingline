from typing import List


class ConveyorBelt:
    beginning: int
    end: int
    type: str

    def __init__(self, beginning: int, end: int, type: str) -> None:
        self.beginning = beginning
        self.end = end
        self.type = type


class PackagingRobot:
    def __init__(self, machine_type: str) -> None:
        self.type = machine_type


class SubMachine:
    Funnel: bool
    PackagingRobots: List[PackagingRobot]
    RobotSlots: int
    BeltSlots: int

    def __init__(self) -> None:
        self.PackagingRobots = []
        self.Funnel = False
        self.RobotSlots = 4
        self.BeltSlots = 3

    def add_packaging_robot(self, machine_type: str) -> None:
        assert self.RobotSlots > 0
        self.PackagingRobots.append(PackagingRobot(machine_type))
        self.RobotSlots += -1

    def attach_funnel(self) -> None:
        assert self.Funnel == False
        self.Funnel = True
