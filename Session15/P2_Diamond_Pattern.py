# Upper Part diamond code
for row in range(1, 6):
    # 1. spaces
    for col in range(5 - row):
        print(" ", end="")

    # 2. stars
    for col in range(2 * row - 1):
        print("*", end="")

    # 3. spaces
    for col in range(5 - row):
        print(" ", end="")

    print("\n")

# Below Part diamond code
for row in range(4, 0, -1):
    # 1. spaces
    for col in range(5 - row):
        print(" ", end="")

    # 2. stars
    for col in range(2 * row - 1):
        print("*", end="")

    # 3. spaces
    for col in range(5 - row):
        print(" ", end="")

    print("\n")
