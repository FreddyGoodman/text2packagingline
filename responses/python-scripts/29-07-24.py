# Definition der Klassen gemäß den gegebenen Typen
class PackagingRobot:
    def __init__(self, robot_type):
        self.type = robot_type

class SubMachine:
    def __init__(self):
        self.PackagingRobots = []

    def add_packaging_robot(self, machine_type):
        robot = PackagingRobot(machine_type)
        self.PackagingRobots.append(robot)

class ConveyerBelt:
    def __init__(self, beginning, end):
        self.beginning = beginning
        self.end = end

class PackagingLine:
    def __init__(self, n):
        self.SubMachines = [SubMachine() for _ in range(n)]
        self.ConveyerBelts = []

    def add_conveyer_belt(self, beginning, end):
        conveyer_belt = ConveyerBelt(beginning, end)
        self.ConveyerBelts.append(conveyer_belt)
        return end - beginning

# Programm zur Erstellung der Verpackungsstraße
def create_packaging_line(n):
    return PackagingLine(n)

# Hauptprogramm
def main():
    # Erstelle eine Verpackungsstraße mit vier Teilmaschinen
    packaging_line = create_packaging_line(4)
    
    # Füge ein Förderband von Maschine zwei bis sieben hinzu
    packaging_line.add_conveyer_belt(2, 7)
    
    # Füge der ersten Teilmaschine einen Scanner hinzu
    packaging_line.SubMachines[0].add_packaging_robot("Scanner")
    
    # Debug-Ausgabe um die Struktur zu prüfen
    print(f"Anzahl der Teilmaschinen: {len(packaging_line.SubMachines)}")
    print(f"Anzahl der Förderbänder: {len(packaging_line.ConveyerBelts)}")
    print(f"Erste Teilmaschine hat {len(packaging_line.SubMachines[0].PackagingRobots)} Roboter.")
    print(f"Der Roboter der ersten Teilmaschine ist vom Typ: {packaging_line.SubMachines[0].PackagingRobots[0].type}")

# Ausführen des Hauptprogramms
if __name__ == "__main__":
    main()
