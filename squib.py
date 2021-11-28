from PIL import Image
import random
import os

orientation_dict = {"straight": "straight_squib", "left": "left_squib", "right": "right_squib"}
dirs = ["eyes", "mouth", "left_arm", "right_arm", "left_leg", "right_leg", "shadow"]

class Squib:
    def __init__(self, orientation):
        self.orientation = orientation_dict[orientation]
        print(f"orientation: {self.orientation}")
        self.main = Image.new("RGB", (420, 420))

    def assemble(self):
        for root, dirs, files in os.walk(os.path.join("squibs", self.orientation)):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
        # path = ""
        # self.main.paste(im=Image.open(path))


        # self.body = Image.open(body)
        # self.mouth = Image.open(mouth)
        # self.leye = Image.open(leye)
        # self.reye = Image.open(reye)
        # self.larm = Image.open(larm)
        # self.rarm = Image.open(rarm)
        # self.lleg = Image.open(lleg)
        # self.rleg = Image.open(rleg)


    # def example_assemble(self):
    #     self.main.paste(im=self.body, box=(100, 100))
    #     self.main.paste(im=self.mouth, box=(180, 150))
    #     self.main.paste(im=self.leye, box=(130, 150))
    #     self.main.paste(im=self.reye, box=(230, 150))
    #     self.main.paste(im=self.larm, box=(70, 150))
    #     self.main.paste(im=self.rarm, box=(285, 150))
    #     self.main.paste(im=self.lleg, box=(130, 250))
    #     self.main.paste(im=self.rleg, box=(200, 250))

        
    # def attach(main, part, x, y):
    #     # squib = Image.new("RGB", (400, 400))
    #     # part = Image.open(f"example_photos/{file}")
    #     squib.paste(im=part, box=(x, y))
