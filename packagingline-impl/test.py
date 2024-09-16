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
    
    packagingLine = PackagingLine(3)

    
    packagingLine.submachines[0].attach_funnel()

    
    packagingLine.add_conveyor_belt(0, 1, 'item')

    
    packagingLine.submachines[0].add_packaging_robot('picker')

    
    packagingLine.submachines[1].add_packaging_robot('scanner')

    
    packagingLine.submachines[1].add_packaging_robot('picker')

    
    packagingLine.add_conveyor_belt(2, 2, 'tray')

    



line = test_smallest()
print(line.throughput_string())  
print(line.cost_string())