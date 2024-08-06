class SubMachine:
    def __init__(self) -> None:
        self.PackagingRobots = []
        self.Funnel = False

    def add_packaging_robot(self, machine_type: str) -> None:
        self.PackagingRobots.append(PackagingRobot(machine_type))

    def attach_funnel(self) -> bool:
        if self.Funnel:
            return False
        self.Funnel = True
        return True


class ConveyorBelt:
    def __init__(self, beginning: int, end: int) -> None:
        self.beginning = beginning
        self.end = end


class PackagingRobot:
    def __init__(self, machine_type: str) -> None:
        self.type = machine_type
