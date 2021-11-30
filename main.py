from squib_generator import SquibGenerator
from squib_part import SquibPart
import os


def main():
    """
    Generate the squibs from supplied squib images.
    :return: None
    :rtype: None
    """
    common_registry = {
        "eyes": SquibPart(os.path.join("squibs", "straight_squib", "eyes")),
        "mouth": SquibPart(os.path.join("squibs", "straight_squib", "mouth")),
        "left_arm": SquibPart(os.path.join("squibs", "straight_squib", "left_arm")),
        "right_arm": SquibPart(os.path.join("squibs", "straight_squib", "right_arm")),
        "left_leg": SquibPart(os.path.join("squibs", "straight_squib", "left_leg")),
        "right_leg": SquibPart(os.path.join("squibs", "straight_squib", "right_leg")),
        "shadow": SquibPart(os.path.join("squibs", "straight_squib", "shadow"))
    }
    straight_squibs = SquibGenerator("straight", common_registry)
    straight_squibs.assemble_common()


if __name__ == "__main__":
    main()
