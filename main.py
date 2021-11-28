from PIL import Image
from squib_generator import SquibGenerator
from squib_part import SquibPart
import os
import logging

def add_to_squib(squib, file, x, y):
    part = Image.open(f"example_photos/{file}")
    squib.paste(im=part, box=(x, y))

def main():
    # not sure if we should have squib parts for each individual directory or just abstract all the eyes ones...
    # this is the temp solution
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
    # squib = Image.new("RGB", (400, 400))
    # add_to_squib(squib, "body.png", 100, 100)
    # add_to_squib(squib, "mouth.png", 180, 150)
    # add_to_squib(squib, "leye.png", 130, 150)
    # add_to_squib(squib, "reye.png", 230, 150)
    # add_to_squib(squib, "larm.png", 70, 150)
    # add_to_squib(squib, "rarm.png", 285, 150)
    # add_to_squib(squib, "lleg.png", 130, 250)
    # add_to_squib(squib, "rleg.png", 200, 250)
    # squib.show()
    # squib.save("generated_squibs/first_squib.png")

if __name__=="__main__":
    main()