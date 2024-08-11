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
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, type="item")
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, type="item")
packaging_line.add_conveyor_belt(beginning=0, end=n - 1, type="tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()
packaging_line.submachines[2].attach_funnel()
packaging_line.submachines[3].attach_funnel()


print(packaging_line.throughput_string())
print(packaging_line.cost_string())
