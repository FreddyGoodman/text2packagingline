from typing import List
from Machines import SubMachine, ConveyorBelt, PackagingRobot

PICKER_CAPACITY = 25
ITEMS_PER_TRAY = 50
TRAYS_PER_BELT = 20
ITEMS_PER_FUNNEL = 100


class PackagingLine:
    conveyor_belts: List[ConveyorBelt]
    submachines: List[SubMachine]

    def __init__(self, n: int) -> None:
        self.submachines = [SubMachine() for _ in range(n)]
        self.conveyor_belts = []

    def add_conveyor_belt(self, beginning: int, end: int, belt_type: str) -> int:
        assert 0 <= beginning <= len(self.submachines) - 1
        assert beginning <= end < len(self.submachines)
        for SubMachine in self.submachines[beginning : end + 1]:
            assert SubMachine.belt_slots > 0
            SubMachine.belt_slots += -1
        self.conveyor_belts.append(ConveyorBelt(beginning, end, belt_type))
        return beginning - end + 1

    def compute_throughput(self) -> int:
        #       - Maybe only allow no more than 100 items per submachine on a belt
        picker_capacity = []
        for submachine in self.submachines:
            capacity = 0
            for robot in submachine.packaging_robots:
                if robot.type == "picker":
                    capacity += PICKER_CAPACITY
            picker_capacity.append(capacity)

        item_belts = 0
        item_belts_at_submachnine = [0 for _ in range(len(self.submachines))]
        tray_belts = 0
        tray_belts_at_submachnine = [0 for _ in range(len(self.submachines))]

        for conveyor_belt in self.conveyor_belts:
            if conveyor_belt.belt_type == "item":
                for i in range(conveyor_belt.beginning, conveyor_belt.end + 1):
                    item_belts_at_submachnine[i] += 1
                item_belts += 1
            elif conveyor_belt.belt_type == "tray":
                for i in range(conveyor_belt.beginning, conveyor_belt.end + 1):
                    tray_belts_at_submachnine[i] += 1
                tray_belts += 1

        # calculates the load at all machines despite not every machine having a funnel attached
        # doesnt really matter because load is only used when a funnel is attached at the machine
        funnel_input_at_submachine = []
        funnels = 0
        for i in range(len(self.submachines)):
            if self.submachines[i].funnel:
                funnels += 1
            loads = []
            total = ITEMS_PER_FUNNEL
            fraction = ITEMS_PER_FUNNEL // item_belts_at_submachnine[i]
            for j in range(item_belts_at_submachnine[i]):
                if total <= fraction:
                    loads.append(total)
                    break
                else:
                    loads.append(fraction)
                    total += -fraction
            funnel_input_at_submachine.append(loads)

        item_belt_loads = []
        for conveyor_belt in self.conveyor_belts:
            if not conveyor_belt.belt_type == "item":
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
                if submachine.funnel: # every machine has load even if it doesnt have a funnel
                    load[1] += funnel_input_at_submachine[i].pop()
                belt_load[i] = load.copy()
            item_belt_loads.append(belt_load)

        remaining_trays = 0
        total_items_picked = 0
        for conveyor_belt in self.conveyor_belts:
            if not conveyor_belt.belt_type == "tray":
                continue

            remaining_slots = TRAYS_PER_BELT * ITEMS_PER_TRAY

            for i in range(conveyor_belt.beginning, conveyor_belt.end + 1):
                for j in range(len(item_belt_loads)):
                    picked_items = min(
                        picker_capacity[i], item_belt_loads[j][i][0], remaining_slots
                    )

                    for k in range(i, conveyor_belt.end + 1):
                        item_belt_loads[j][k][0] -= picked_items

                    total_items_picked += picked_items
                    remaining_slots -= picked_items
                    picker_capacity[i] -= picked_items

            remaining_trays += float(remaining_slots) / ITEMS_PER_TRAY

        return (
            tray_belts * TRAYS_PER_BELT - remaining_trays,
            funnels * ITEMS_PER_FUNNEL,
            funnels * ITEMS_PER_FUNNEL - total_items_picked,
        )

    def throughput_string(self) -> str:
        data = self.compute_throughput()
        return f"Throughput: {data[0]} trays filled and {data[2]} out of {data[1]} items remained unpicked"

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
