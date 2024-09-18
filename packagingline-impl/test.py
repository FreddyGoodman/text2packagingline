# A PackagingLine needs tray and item belts.
# To input items in the line attach a funnel to the submachine.
# Tray dont have to be added or removed from the line.
# Items can only be picked if a scanner scanned them.
# Item added by a funnel can not be scanned in the same machine.


from PackagingLib import PackagingLine


def test_small() -> PackagingLine:
    line_length = 3
    line = PackagingLine(line_length)

    line.submachines[0].attach_funnel()

    line.submachines[1].add_packaging_robot("scanner")
    line.submachines[1].add_packaging_robot("picker")
    line.submachines[1].add_packaging_robot("picker")
    line.submachines[1].add_packaging_robot("picker")

    line.submachines[2].add_packaging_robot("picker")

    line.add_conveyor_belt(0, 2, "item")
    line.add_conveyor_belt(1, 2, "tray")

    return line


def test_medium() -> PackagingLine:
    line_length = 4
    line = PackagingLine(line_length)

    line.submachines[0].attach_funnel()

    line.submachines[1].attach_funnel()
    # line.submachines[1].add_packaging_robot("scanner")
    # line.submachines[1].add_packaging_robot("picker")
    # line.submachines[1].add_packaging_robot("picker")
    # line.submachines[1].add_packaging_robot("picker")

    line.submachines[2].add_packaging_robot("scanner")
    line.submachines[2].add_packaging_robot("picker")
    line.submachines[2].add_packaging_robot("picker")
    line.submachines[2].add_packaging_robot("picker")

    line.submachines[3].add_packaging_robot("picker")
    line.submachines[3].add_packaging_robot("picker")
    line.submachines[3].add_packaging_robot("picker")
    line.submachines[3].add_packaging_robot("picker")

    line.add_conveyor_belt(0, 3, "item")
    line.add_conveyor_belt(1, 2, "tray")
    line.add_conveyor_belt(2, 3, "tray")

    return line


def test_large() -> PackagingLine:
    n = 30
    line = PackagingLine(n)
    for i in range(20):
        line.submachines[i].attach_funnel()

    line.submachines[12].add_packaging_robot("scanner")
    line.submachines[12].add_packaging_robot("picker")
    line.submachines[12].add_packaging_robot("picker")
    line.submachines[12].add_packaging_robot("picker")

    for i in range(13, 20):
        line.submachines[i].add_packaging_robot("picker")
        line.submachines[i].add_packaging_robot("picker")
        if i < 19:
            line.submachines[i].add_packaging_robot("picker")
            line.submachines[i].add_packaging_robot("picker")

    line.submachines[20].add_packaging_robot("scanner")
    line.submachines[20].add_packaging_robot("picker")
    line.submachines[20].add_packaging_robot("picker")
    line.submachines[20].add_packaging_robot("picker")

    for i in range(21, n):
        line.submachines[i].add_packaging_robot("picker")
        line.submachines[i].add_packaging_robot("picker")
        line.submachines[i].add_packaging_robot("picker")
        if not i == n - 1:
            line.submachines[i].add_packaging_robot("picker")

    line.add_conveyor_belt(12, 13, "tray")
    line.add_conveyor_belt(13, 14, "tray")
    line.add_conveyor_belt(14, 16, "tray")
    line.add_conveyor_belt(16, 17, "tray")
    line.add_conveyor_belt(17, 18, "tray")
    line.add_conveyor_belt(18, 20, "tray")
    line.add_conveyor_belt(20, 21, "tray")
    line.add_conveyor_belt(21, 23, "tray")
    line.add_conveyor_belt(23, 24, "tray")
    line.add_conveyor_belt(24, 25, "tray")
    line.add_conveyor_belt(25, 27, "tray")
    line.add_conveyor_belt(27, 28, "tray")
    line.add_conveyor_belt(28, 29, "tray")

    line.add_conveyor_belt(0, n - 1, "item")

    return line


def test_response() -> PackagingLine:
    # Create a packaging line with 3 submachines
    packaging_line = PackagingLine(3)
    
    # Attach the necessary funnels to input 100 items
    total_items = 100
    funnel_capacity = 100  # Each funnel can supply 100 items
    submachine_index = 0  # Attach funnel to the first submachine
    attached_funnels = 0

    # Attach funnel to the first submachine (since 1 funnel can handle 100 items)
    if total_items > 0:
        if packaging_line.submachines[submachine_index].attach_funnel():
            attached_funnels += 1

    # Attach an item belt from the first to the last machine (index 0 to 2)
    packaging_line.add_conveyor_belt(0, 2, "item")

    # Attach scanners to the second submachine (index 1) to scan all items
    submachine_index = 1  # Attach scanners to the second submachine
    packaging_line.submachines[submachine_index].add_packaging_robot("scanner")

    # Attach pickers to the third submachine (index 2) to pick up all scanned items
    submachine_index = 2  # Attach pickers to the third submachine
    picker_capacity = 30  # Each picker can pick up to 30 items
    pickers_needed = (total_items + picker_capacity - 1) // picker_capacity  # Round up

    for _ in range(pickers_needed):
        packaging_line.submachines[submachine_index].add_packaging_robot("picker")

    # Compute how many trays are necessary to output all items
    tray_capacity = 40  # Each tray can hold up to 40 items
    trays_needed = (total_items + tray_capacity - 1) // tray_capacity  # Round up
    conveyor_belt_capacity = 4  # Each conveyor belt can carry 4 trays
    tray_belts_needed = (trays_needed + conveyor_belt_capacity - 1) // conveyor_belt_capacity  # Round up

    # Attach the necessary tray conveyor belts from the second to the third submachine
    packaging_line.add_conveyor_belt(1, 2, "tray")

    return packaging_line


line = test_small()
print(line.throughput_string())
print(line.cost_string())
