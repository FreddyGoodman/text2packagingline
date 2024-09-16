# A PackagingLine needs tray and item belts. 
# To input items in the line attach a funnel to the submachine. 
# Tray dont have to be added or removed from the line. 
# Items can only be picked if a scanner scanned them.
# Item added by a funnel can not be scanned in the same machine.


from PackagingLib import PackagingLine

def test_smallest() -> PackagingLine:
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

def test_small() -> PackagingLine:
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
    pass
    
def test_response() -> PackagingLine:
    # Assuming the provided functions and types are accessible

    # Create a packaging line with 3 submachines
    packaging_line = PackagingLine(3)

    # First submachine (index 0) - Attach a funnel
    packaging_line.submachines[0].attach_funnel()

    # Second submachine (index 1) - Add one scanner and three pickers
    packaging_line.submachines[1].add_packaging_robot('scanner')  # Add scanner
    packaging_line.submachines[1].add_packaging_robot('picker')   # Add first picker
    packaging_line.submachines[1].add_packaging_robot('picker')   # Add second picker
    packaging_line.submachines[1].add_packaging_robot('picker')   # Add third picker

    # Third submachine (index 2) - Add one picker
    packaging_line.submachines[2].add_packaging_robot('picker')   # Add picker

    # Add a conveyor belt for items, spanning all three machines (from 0 to 2)
    packaging_line.add_conveyor_belt(0, 2, 'item')

    # Add a conveyor belt for trays, connecting the second and third machines (from 1 to 2)
    packaging_line.add_conveyor_belt(1, 2, 'tray')

    return packaging_line
line = test_smallest()
print(line.throughput_string())  
print(line.cost_string())