from PIL import Image
from squib import Squib

def add_to_squib(squib, file, x, y):
    part = Image.open(f"example_photos/{file}")
    squib.paste(im=part, box=(x, y))

def main():
    squib = Squib("straight")
    squib.assemble()
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