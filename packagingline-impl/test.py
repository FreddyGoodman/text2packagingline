from PackagingLib import PackagingLine

pl = PackagingLine(4)

pl.add_conveyor_belt(0, 3, "tray")

for sub_machine in pl.submachines:
    sub_machine.attach_funnel()