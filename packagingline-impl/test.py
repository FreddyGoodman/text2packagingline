from PackagingLib import PackagingLine

pl = PackagingLine(4)

pl.add_conveyor_belt(0, 3, "item")
pl.add_conveyor_belt(1, 3, "tray")


pl.submachines[0].attach_funnel()

pl.submachines[1].attach_funnel()

pl.submachines[1].add_packaging_robot("scanner")
pl.submachines[1].add_packaging_robot("picker")
pl.submachines[1].add_packaging_robot("picker")
pl.submachines[1].add_packaging_robot("picker")

pl.submachines[2].add_packaging_robot("scanner")
pl.submachines[2].add_packaging_robot("picker")
pl.submachines[2].add_packaging_robot("picker")
pl.submachines[2].add_packaging_robot("picker")

pl.submachines[3].add_packaging_robot("picker")
pl.submachines[3].add_packaging_robot("picker")


print(pl.throughput_string())
print(pl.cost_string())