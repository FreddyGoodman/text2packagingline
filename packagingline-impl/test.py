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

# Step 1: Create a PackagingLine instance with 3 sub-machines
packaging_line = PackagingLine(3)

# Step 2: Add conveyor belts
# A belt of the type "item" runs from machine 1 to machine 3
packaging_line.add_conveyor_belt(beginning=0, end=2, belt_type="item")

# A belt of the type "tray" runs from machine 2 to machine 3
packaging_line.add_conveyor_belt(beginning=1, end=2, belt_type="tray")

# Step 3: Attach a funnel to Machine 1 (index 0)
machine_1 = packaging_line.submachines[0]
machine_1.attach_funnel()

# Step 4: Add robots to sub-machines
# Machine 2 (index 1) contains a scanner robot and three picker robots
machine_2 = packaging_line.submachines[1]
machine_2.add_packaging_robot(machine_type="scanner")
for _ in range(3):
    machine_2.add_packaging_robot(machine_type="picker")

# Machine 3 (index 2) contains a picker robot
machine_3 = packaging_line.submachines[2]
machine_3.add_packaging_robot(machine_type="picker")

print(packaging_line.throughput_string())
print(packaging_line.cost_string())

