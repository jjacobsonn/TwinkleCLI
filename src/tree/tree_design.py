import random
import os
import time
from rich.console import Console

console = Console()

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

ORNAMENT_COLORS = ["red", "yellow", "blue", "magenta", "cyan", "white"]
TREE_COLOR = "green"
STAR_COLOR = "bold yellow"
TRUNK_COLOR = "rgb(139,69,19)"

class ChristmasTree:
    def __init__(self):
        self.tree = TREE

    def generate_colored_tree(self):
        decorated_tree = []
        for row in self.tree:
            decorated_row = ""
            for char in row:
                if char == "●":
                    decorated_row += f"[{random.choice(ORNAMENT_COLORS)}]{char}[/]"
                elif char == "*":
                    decorated_row += f"[{TREE_COLOR}]{char}[/]"
                elif char == "★":
                    decorated_row += f"[{STAR_COLOR}]{char}[/]"
                elif char == "|":
                    decorated_row += f"[{TRUNK_COLOR}]{char}[/]"
                else:
                    decorated_row += f"[{TREE_COLOR}]{char}[/]"
            decorated_tree.append(decorated_row)
        return decorated_tree

    def animate_tree(self, iterations=50, delay=0.5):
        for _ in range(iterations):
            os.system("clear" if os.name == "posix" else "cls")
            for row in self.generate_colored_tree():
                console.print(row)
            time.sleep(delay)
