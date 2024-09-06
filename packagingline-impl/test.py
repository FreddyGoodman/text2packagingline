from PackagingLib import PackagingLine

n = 7

# Initialize the packaging line with a sufficient number of submachines
packaging_line = PackagingLine(n=n)

# Add packaging robots to submachines
for i in range(n):
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("scanner")


# Add conveyor belts to connect the submachines
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, belt_type="item")
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, belt_type="item")
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, belt_type="tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()
packaging_line.submachines[2].attach_funnel()
packaging_line.submachines[3].attach_funnel()


print(packaging_line.throughput_string())
print(packaging_line.cost_string())

# Step 1: Initialize the packaging line with 4 sub-machines
packaging_line = PackagingLine(n=4)

# Step 2: Add conveyor belts
# Conveyor belt for items
packaging_line.add_conveyor_belt(beginning=0, end=3, belt_type='item')

# Conveyor belt for trays
packaging_line.add_conveyor_belt(beginning=0, end=3, belt_type='tray')

# Step 3: Configure sub-machines
# Add scanners and pickers to each sub-machine
for submachine in packaging_line.submachines:
    # Add one "scanner" robot
    submachine.add_packaging_robot(machine_type='scanner')
    
    # Add three "picker" robots (since each submachine can hold up to 4 robots and 1 is a scanner)
    for _ in range(3):
        submachine.add_packaging_robot(machine_type='picker')
    
    # Attach a funnel to the sub-machine
    submachine.attach_funnel()

# The PackagingLine is now set up with enough capacity to package 400 items.
print(packaging_line.throughput_string())
print(packaging_line.cost_string())