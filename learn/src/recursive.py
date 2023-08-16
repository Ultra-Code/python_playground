def hanoi(disks: int, source: str, helper: str, destination: str) -> None:
    if disks == 1:
        print(f"Disk {disks} moves from tower {source} to tower {destination}.")
        return

    hanoi(disks - 1, source, destination, helper)
    print(f"Disk {disks} moves from tower {source} to tower {destination}.")
    hanoi(disks - 1, helper, source, destination)


# Driver code
disks_no = int(input("Number of disks to be displaced: "))
"""
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
"""
# Actual function call
hanoi(disks_no, "A", "B", "C")


