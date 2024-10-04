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

    line.submachines[2].add_packaging_robot("picker")
    line.submachines[2].add_packaging_robot("picker")
    line.submachines[2].add_packaging_robot("picker")
    line.submachines[2].add_packaging_robot("picker")

    line.add_conveyor_belt(0, 2, "item")
    line.add_conveyor_belt(2, 2, "tray")

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
    # Step 1: Create the packaging line with 3 submachines.
    packaging_line = PackagingLine(3)

    # Step 2: Attach a funnel to the first submachine.
    # Submachine 1 handles the input of items through the funnel.
    packaging_line.submachines[0].attach_funnel()

    # Step 3: Add the conveyor belts.
    # Belt 1: Item conveyor belt spanning from submachine 1 to submachine 2
    packaging_line.add_conveyor_belt(0, 1, "item")

    # Belt 2: Tray conveyor belt spanning from submachine 2 to submachine 3
    packaging_line.add_conveyor_belt(1, 2, "tray")

    # Step 4: Add the scanner in submachine 2.
    packaging_line.submachines[1].add_packaging_robot("scanner")

    # Step 5: Add the picker robots.
    # We need 3 pickers in submachine 2 (which can hold up to 4 robots in total, including the scanner).
    for _ in range(3):
        packaging_line.submachines[1].add_packaging_robot("picker")

    # Add 1 picker in submachine 3.
    packaging_line.submachines[2].add_packaging_robot("picker")

    return packaging_line


line = test_small()
print(line.throughput_string())
print(line.cost_string())
