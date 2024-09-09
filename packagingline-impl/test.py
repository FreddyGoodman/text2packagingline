# A PackagingLine needs tray and item belts. 
# To input items in the line attach a funnel to the submachine. 
# Tray dont have to be added or removed from the line. 
# Items can only be picked if a scanner scanned them.
# Item added by a funnel can not be scanned in the same machine.


from PackagingLib import PackagingLine

n = 3

packaging_line = PackagingLine(n)

packaging_line.add_conveyor_belt(0, 2, "item")
packaging_line.add_conveyor_belt(1, 2, "tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()

packaging_line.submachines[1].add_packaging_robot("scanner")
packaging_line.submachines[1].add_packaging_robot("picker")
packaging_line.submachines[1].add_packaging_robot("picker")
packaging_line.submachines[1].add_packaging_robot("picker")

packaging_line.submachines[2].add_packaging_robot("picker")

print(packaging_line.throughput_string())
print(packaging_line.cost_string())

n = 4

packaging_line = PackagingLine(n)

packaging_line.add_conveyor_belt(0, 3, "item")
packaging_line.add_conveyor_belt(1, 3, "tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()

packaging_line.submachines[1].add_packaging_robot("scanner")
packaging_line.submachines[1].add_packaging_robot("picker")
packaging_line.submachines[1].add_packaging_robot("picker")
packaging_line.submachines[1].add_packaging_robot("picker")

packaging_line.submachines[2].add_packaging_robot("scanner")
packaging_line.submachines[2].add_packaging_robot("picker")
packaging_line.submachines[2].add_packaging_robot("picker")
packaging_line.submachines[2].add_packaging_robot("picker")

packaging_line.submachines[3].add_packaging_robot("picker")
packaging_line.submachines[3].add_packaging_robot("picker")

print(packaging_line.throughput_string())
print(packaging_line.cost_string())

n = 8

packaging_line = PackagingLine(n)
packaging_line.add_conveyor_belt(0, 7, "item")
packaging_line.add_conveyor_belt(1, 7, "tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()
packaging_line.submachines[2].attach_funnel()
packaging_line.submachines[3].attach_funnel()
packaging_line.submachines[4].attach_funnel()

for i in range(1, 6):
    packaging_line.submachines[i].add_packaging_robot("scanner")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")

packaging_line.submachines[6].add_packaging_robot("picker")
packaging_line.submachines[6].add_packaging_robot("picker")
packaging_line.submachines[6].add_packaging_robot("picker")
packaging_line.submachines[6].add_packaging_robot("picker")

packaging_line.submachines[7].add_packaging_robot("picker")

print(packaging_line.throughput_string())
print(packaging_line.cost_string())
