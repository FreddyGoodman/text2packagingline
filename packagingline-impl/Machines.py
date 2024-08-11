from typing import List

ROBOT_SLOTS = 4
BELT_SLOTS = 3


class ConveyorBelt:
    beginning: int
    end: int
    type: str

    def __init__(self, beginning: int, end: int, type: str) -> None:
        self.beginning = beginning
        self.end = end
        self.type = type


class PackagingRobot:
    machine_type: str

    def __init__(self, machine_type: str) -> None:
        self.type = machine_type


class SubMachine:
    funnel: bool
    packaging_robots: List[PackagingRobot]
    robot_slots: int
    belt_slots: int

    def __init__(self) -> None:
        self.packaging_robots = []
        self.funnel = False
        self.robot_slots = ROBOT_SLOTS
        self.belt_slots = BELT_SLOTS

    def add_packaging_robot(self, machine_type: str) -> None:
        assert self.robot_slots > 0
        self.packaging_robots.append(PackagingRobot(machine_type))
        self.robot_slots += -1

    def attach_funnel(self) -> None:
        assert self.funnel == False
        self.funnel = True
