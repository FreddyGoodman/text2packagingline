from PackagingLib import PackagingLine

# Initialize the packaging line with a sufficient number of submachines
packaging_line = PackagingLine(n=100)

# Add packaging robots to submachines
for i in range(100):
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("picker")
    packaging_line.submachines[i].add_packaging_robot("scanner")


# Add conveyor belts to connect the submachines
packaging_line.add_conveyor_belt(beginning=0, end=99, type="item")
packaging_line.add_conveyor_belt(beginning=0, end=99, type="item")
packaging_line.add_conveyor_belt(beginning=0, end=99, type="tray")

packaging_line.submachines[0].attach_funnel()
packaging_line.submachines[1].attach_funnel()
packaging_line.submachines[2].attach_funnel()
packaging_line.submachines[3].attach_funnel()


# Check the throughput to ensure it can process at least 350 items
throughput = packaging_line.compute_throughput()
print(packaging_line.throughput_string())
print(packaging_line.cost_string())
