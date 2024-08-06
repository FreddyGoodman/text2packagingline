from PackagingLib import PackagingLine

pl = PackagingLine(4)

pl.add_conveyor_belt(0, 3)

for sub_machine in pl.SubMachines:
    sub_machine.attach_funnel()