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

from PackagingLib import PackagingLine

# Constants
PICKER_CAPACITY = 25
ITEMS_PER_TRAY = 50
TRAYS_PER_BELT = 20
ITEMS_PER_FUNNEL = 100
ROBOT_PER_SUBMACHINE = 4
BELTS_PER_SUBMACHINE = 3

# Given that each picker has a capacity of 25, we need 4 pickers to handle 100 items.
# We also need at least one scanner to scan the conveyor belt before the items can be picked.

# Number of submachines needed:
# 1 submachine with a funnel for loading items
# 1 submachine with a funnel for loading trays
# 1 submachine with a scanner and 4 pickers (to reach 100 items capacity)

n = 3  # Number of submachines

# Initialize the packaging line with 3 submachines
packaging_line = PackagingLine(n)

# Adding conveyor belts for items and trays
packaging_line.add_conveyor_belt(0, 2, "item")  # Belt for items from submachine 0 to 2
packaging_line.add_conveyor_belt(1, 2, "tray")  # Belt for trays from submachine 1 to 2

# Attach funnels to submachines 0 and 1 for loading items and trays
packaging_line.submachines[0].attach_funnel()  # Funnel for items in submachine 0
packaging_line.submachines[1].attach_funnel()  # Funnel for trays in submachine 1

# Add robots to submachine 2
# Submachine 2 needs one scanner and four pickers to handle 100 items
packaging_line.submachines[2].add_packaging_robot("scanner")  # Scanner in submachine 2
packaging_line.submachines[2].add_packaging_robot("picker")   # Picker 1 in submachine 2
packaging_line.submachines[2].add_packaging_robot("picker")   # Picker 2 in submachine 2
packaging_line.submachines[2].add_packaging_robot("picker")   # Picker 3 in submachine 2
packaging_line.submachines[2].add_packaging_robot("picker")   # Picker 4 in submachine 2

# The packaging line is now set up with enough capacity to package 100 items
