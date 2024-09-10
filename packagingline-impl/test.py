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
    # Define constants
    PICKER_CAPACITY = 30
    ITEMS_PER_TRAY = 40
    TRAYS_PER_BELT = 4
    ITEMS_PER_FUNNEL = 100
    ROBOT_PER_SUBMACHINE = 4
    BELTS_PER_SUBMACHINE = 3

    PACKAGING_LINE_COST = 1000
    SUBMACHINE_COST = 500
    BELT_FIXED_COST = 50
    BELT_LENGTH_COST = 5
    PICKER_COST = 100
    SCANNER_COST = 3000
    FUNNEL_COST = 25

    # Assuming function calls are defined as methods on objects, we follow the provided descriptions.

    # Step 1: Create a packaging line with 3 submachines
    packaging_line = PackagingLine(3)  # Creates a new packaging line with 3 submachines

    # Step 2: Add a conveyor belt of type 'item' from machine 1 to machine 3
    beginning_machine_1 = 0  # Index for Machine 1
    end_machine_3 = 2  # Index for Machine 3
    packaging_line.add_conveyor_belt(beginning_machine_1, end_machine_3, 'item')

    # Step 3: Add a conveyor belt of type 'tray' from machine 2 to machine 3
    beginning_machine_2 = 1  # Index for Machine 2
    packaging_line.add_conveyor_belt(beginning_machine_2, end_machine_3, 'tray')

    # Step 4: Attach a funnel to Machine 1
    machine_1 = packaging_line.submachines[beginning_machine_1]  # Access Machine 1
    machine_1.attach_funnel()  # Attach a funnel to Machine 1

    # Step 5: Add robots to Machine 2
    machine_2 = packaging_line.submachines[beginning_machine_2]  # Access Machine 2
    machine_2.add_packaging_robot('scanner')  # Add a scanner robot to Machine 2

    # Add three picker robots to Machine 2
    for _ in range(3):
        machine_2.add_packaging_robot('picker')

    # Step 6: Add a picker robot to Machine 3
    machine_3 = packaging_line.submachines[end_machine_3]  # Access Machine 3
    machine_3.add_packaging_robot('picker')  # Add a picker robot to Machine 3

    return packaging_line


line = test_smallest()
print(line.throughput_string())  
print(line.cost_string())