from typing import List
from Machines import SubMachine, ConveyorBelt, PackagingRobot

PICKER_CAPACITY = 25
TRAY_CAPACITY = 50
TRAYS_PER_BELT = 4
ITEMS_PER_FUNNEL = 100


class PackagingLine:
    conveyor_belts: List[ConveyorBelt]
    submachines: List[SubMachine]

    def __init__(self, n: int) -> None:
        self.submachines = [SubMachine() for _ in range(n)]
        self.conveyor_belts = []

    def add_conveyor_belt(self, beginning: int, end: int, type: str) -> None:
        assert 0 <= beginning < len(self.submachines) - 1
        assert beginning <= end < len(self.submachines)
        for SubMachine in self.submachines[beginning : end + 1]:
            assert SubMachine.belt_slots > 0
            SubMachine.belt_slots += -1
        self.conveyor_belts.append(ConveyorBelt(beginning, end, type))

    def compute_throughput(self) -> int:
        picker_capacity = []
        for submachine in self.submachines:
            capacity = 0
            for robot in submachine.packaging_robots:
                if robot.type == "picker":
                    capacity += PICKER_CAPACITY
            picker_capacity.append(capacity)

        funnels = 0
        item_belt_loads = []
        for conveyor_belt in self.conveyor_belts:
            if not conveyor_belt.type == "item":
                continue

            belt_load = [[0, 0] for _ in range(len(self.submachines))]
            load = [0, 0]  # scanned_load, unscanned_load

            for i, submachine in enumerate(
                self.submachines[conveyor_belt.beginning : conveyor_belt.end + 1],
                conveyor_belt.beginning,  # offset to first submachine
            ):
                for robot in submachine.packaging_robots:
                    if robot.type == "scanner" and i > 0:
                        load[0] += belt_load[i - 1][1]  # add unscanned
                        load[1] = 0
                        break  # submachine can only scan once
                if submachine.funnel:
                    load[1] += ITEMS_PER_FUNNEL
                    funnels += 1
                belt_load[i] = load.copy()
            item_belt_loads.append(belt_load)

        tray_belts = 0
        remaining_trays = 0
        total_items_picked = 0
        for conveyor_belt in self.conveyor_belts:
            if not conveyor_belt.type == "tray":
                continue

            remaining_slots = TRAYS_PER_BELT * TRAY_CAPACITY

            for i in range(conveyor_belt.beginning, conveyor_belt.end + 1):
                for j in range(len(item_belt_loads)):
                    picked_items = min(
                        picker_capacity[i], item_belt_loads[j][i][0], remaining_slots
                    )
                    total_items_picked += picked_items
                    remaining_slots -= picked_items
                    picker_capacity[i] -= picked_items

            remaining_trays += float(remaining_slots) / TRAY_CAPACITY
            tray_belts += 1

        return (
            tray_belts * TRAYS_PER_BELT - remaining_trays,
            funnels * ITEMS_PER_FUNNEL - total_items_picked,
        )

    def throughput_string(self) -> str:
        data = self.compute_throughput()
        return f"Throughput: {data[0]} trays filled and {data[1]} items remained unpicked"

    def compute_line_cost(self) -> int:
        cost = 1000
        for submachine in self.submachines:
            for robot in submachine.packaging_robots:
                if robot.type == "picker":
                    cost += 100
                if robot.type == "scanner":
                    cost += 300
            if submachine.funnel:
                cost += 25
            cost += 500
        for conveyor_belt in self.conveyor_belts:
            cost += 5 * (conveyor_belt.end - conveyor_belt.beginning + 1)
            cost += 50

        return cost
    
    def cost_string(self) -> str:
        return f"Cost: {self.compute_line_cost()}"