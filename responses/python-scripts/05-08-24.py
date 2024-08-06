class PackagingLine:
    def __init__(self, n):
        self.SubMachines = [SubMachine() for _ in range(n)]
        self.ConveyorBelts = []

    def add_conveyor_belt(self, beginning, end):
        self.ConveyorBelts.append(ConveyorBelt(beginning, end))

class SubMachine:
    def __init__(self):
        self.PackagingRobots = []
        self.Funnel = False

    def add_packaging_robot(self, machine_type):
        self.PackagingRobots.append(PackagingRobot(machine_type))

    def attach_funnel(self):
        if self.Funnel:
            return False
        self.Funnel = True
        return True

class PackagingRobot:
    def __init__(self, machine_type):
        self.type = machine_type

class ConveyorBelt:
    def __init__(self, beginning, end):
        self.beginning = beginning
        self.end = end

# Step 1: Create a PackagingLine instance with 4 sub-machines
packaging_line = PackagingLine(4)

# Step 2: Attach funnels to each sub-machine
for sub_machine in packaging_line.SubMachines:
    sub_machine.attach_funnel()

# Step 3: Add a conveyor belt that connects all sub-machines
packaging_line.add_conveyor_belt(0, 3)

# Step 4: Add packaging robots to each sub-machine
for sub_machine in packaging_line.SubMachines:
    sub_machine.add_packaging_robot("scanner")
    sub_machine.add_packaging_robot("picker")

# The packaging line is now set up to handle 400 cookies