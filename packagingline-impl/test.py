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
    # Step 1: Create the packaging line with 2 submachines
    packaging_line = PackagingLine(2)

    # Step 2: Attach a funnel to the first submachine
    packaging_line.submachines[0].attach_funnel()

    # Step 3: Add an item conveyor belt spanning both submachines
    packaging_line.add_conveyor_belt(0, 1, 'item')

    # Step 4: Add a tray conveyor belt spanning both submachines
    packaging_line.add_conveyor_belt(0, 1, 'tray')

    # Step 5: Add 3 pickers to the first submachine (Submachine 0)
    for _ in range(3):
        packaging_line.submachines[0].add_packaging_robot('picker')

    # Step 6: Add 1 picker to the second submachine (Submachine 1)
    packaging_line.submachines[1].add_packaging_robot('picker')

    # Step 7: Add 1 scanner to the second submachine (Submachine 1)
    packaging_line.submachines[1].add_packaging_robot('scanner')

    return packaging_line



line = test_response()
print(line.throughput_string())
print(line.cost_string())
