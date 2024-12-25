import time
import random
import os
from rich.console import Console

# Initialize Rich Console for colorful rendering
console = Console()

# Define the Christmas tree design
TREE = [
    "         ★         ",
    "        * *        ",
    "       *   *       ",
    "      * ● * ●      ",
    "     *   *   *     ",
    "    * ● * ● * ●    ",
    "   *   *   *   *   ",
    "  * ● * ● * ● * ●  ",
    "        |||        ",
]

# Define colors for ornaments, tree, and trunk
TREE_COLOR = "green"
TRUNK_COLOR = "rgb(139,69,19)"  # Explicit RGB code for brown
ORNAMENT_COLORS = ["red", "yellow", "blue", "magenta", "cyan", "white"]
STAR_COLOR = "bold yellow"  # Star stays constant in yellow


def generate_colored_tree(tree):
    """Generate a single tree frame with dynamic ornament colors and a green tree."""
    decorated_tree = []
    for row in tree:
        decorated_row = ""
        for char in row:
            if char == "●":  # Ornaments
                decorated_row += f"[{random.choice(ORNAMENT_COLORS)}]{char}[/]"
            elif char == "*":  # Tree lights (green)
                decorated_row += f"[{TREE_COLOR}]{char}[/]"
            elif char == "★":  # Star
                decorated_row += f"[{STAR_COLOR}]{char}[/]"
            elif char == "|":  # Trunk
                decorated_row += f"[{TRUNK_COLOR}]{char}[/]"
            else:
                decorated_row += f"[{TREE_COLOR}]{char}[/]"  # Tree body (green spaces)
        decorated_tree.append(decorated_row)
    return decorated_tree


def display_tree(tree):
    """Display the tree with current colors."""
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen for animation
    for row in tree:
        console.print(row)


def animate_tree(iterations=50, delay=0.5):
    """Animate the tree by changing ornament colors."""
    for _ in range(iterations):
        decorated_tree = generate_colored_tree(TREE)
        display_tree(decorated_tree)
        time.sleep(delay)


if __name__ == "__main__":
    # Start the tree animation with predefined settings
    print("TwinkleCLI: Dynamic Ornaments Tree 🎄")
    print("Press Ctrl+C to stop the animation.")
    animate_tree(iterations=100, delay=0.5)
