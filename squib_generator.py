from PIL import Image
import random
import os
from squib_part import SquibPart
import logging

orientation_dict = {"straight": "straight_squib", "left": "left_squib", "right": "right_squib"}
common = ["eyes", "mouth", "left_arm", "right_arm", "left_leg", "right_leg", "shadow"]
rare = []
ultra_rare = []
one_of_a_kind = []

class SquibGenerator:
    def __init__(self, orientation, common_registry):
        self.orientation = orientation_dict[orientation]
        self.common_registry = common_registry
        self.output_path = os.path.join("generated", self.orientation)
        # self.main = Image.new("RGB", (420, 420))

    def is_exhausted(self):
        for part in self.common_registry:
            if not part.is_exhausted():
                return True
        return False

    def construct_common_squib(self, part_idxs):
        # squib = Image.new("RGBA", (420, 420))
        squib = Image.open(os.path.join("squibs", "straight_squib", "body.png")).convert("RGBA")
        for i, part_idx in enumerate(part_idxs):
            part_name = list(self.common_registry)[i]
            img_name = self.common_registry[part_name].get(part_idx)
            if img_name == None:
                continue
            img = Image.open(img_name).convert("RGBA")
            squib.paste(im=img, box=(0, 0, 420, 420), mask=img)
        output_file = f"{''.join([str(num) for num in part_idxs])}.png"
        squib.save(os.path.join(self.output_path, output_file), format="png")

    def assemble_common(self):
        seen = set()
        nodes = [(0, 0, 0, 0, 0, 0, 0)]
        count = 0
        while nodes: 
            cur = nodes.pop()
            # print(f"{cur=}")
            self.construct_common_squib(cur)
            # we add a new one to nodes if 1. the index can support it and 2. it is not in seen
            for i, num in enumerate(cur):
                if self.common_registry[list(self.common_registry)[i]].can_increment(num):
                    next_node = list(cur)
                    next_node[i] += 1
                    next_node = tuple(next_node)
                    if next_node not in seen:
                        nodes.append(next_node)
                        seen.add(next_node)
            count += 1
            if count == 20:
                break
        print(f"{count} squibs generated.")

        # for root, dirs, files in os.walk(os.path.join("squibs", self.orientation)):
        #     for name in files:
        #         print(os.path.join(root, name))
        #     for name in dirs:
        #         print(os.path.join(root, name))
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
