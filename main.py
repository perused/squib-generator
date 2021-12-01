from squib_generator import SquibGenerator
from squib_part import SquibPart
import os


def main():
    """Oversee the generation of different rarity squibs from supplied squib images."""
    common_registry = {
        ""
        "face": SquibPart(os.path.join("squibs", "straight_squib", "face")),
        "arms": SquibPart(os.path.join("squibs", "straight_squib", "arms")),
        "legs": SquibPart(os.path.join("squibs", "straight_squib", "legs"))
        # "right_arm": SquibPart(os.path.join("squibs", "straight_squib", "right_arm")),
        # "left_leg": SquibPart(os.path.join("squibs", "straight_squib", "left_leg")),
        # "right_leg": SquibPart(os.path.join("squibs", "straight_squib", "right_leg")),
        # "shadow": SquibPart(os.path.join("squibs", "straight_squib", "shadow"))
    }
    straight_squibs = SquibGenerator("straight", common_registry)
    straight_squibs.assemble_common()


if __name__ == "__main__":
    main()
