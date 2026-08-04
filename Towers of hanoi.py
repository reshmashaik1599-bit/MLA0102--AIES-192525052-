def tower(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower(n - 1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))
tower(n, 'A', 'B', 'C')