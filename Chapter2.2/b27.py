def main() -> None:
    # mapping from number of sides to shape name
    shapes: dict = {
        3: "Triangle",
        4: "Quadrilateral",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon",
    }

    try:
        sides: int = int(input("Enter the number of sides (3–10): "))
        if sides in shapes:
            print(f"A shape with {sides} sides is a {shapes[sides]}.")
        else:
            print("Error: This program only supports shapes with 3 to 10 sides.")
    except ValueError:
        print("Error: Please enter a valid integer.")