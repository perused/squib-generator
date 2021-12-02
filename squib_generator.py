from PIL import Image, ImageDraw, ImageFont
from names_generator import generate_name
from text_generator import TextGenerator
import os

orientation_dict = {"straight": "straight_squib", "left": "left_squib", "right": "right_squib"}

class SquibGenerator:
    """A class for assembling squibs of different rarities."""
    def __init__(self, orientation, common_registry):
        self.orientation = orientation_dict[orientation]
        self.common_registry = common_registry
        self.output_path = os.path.join("resources", "generated", self.orientation)
        self.tg = TextGenerator(os.path.join("resources", "text", "africa.txt"))


    def attach_image(self, squib, file_name):
        attacher = Image.open(file_name).convert("RGBA")
        squib.paste(im=attacher, box=(0, 0, 420, 420), mask=attacher)


    def attach_id(self, squib):
        pass


    def attach_name(self, squib):
        # name = generate_name(style="captial")
        # squib = ImageDraw.Draw(squib)
        pass


    def attach_speech(self, squib):
        pass


    def construct_common_squib(self, part_idxs):
        """Given indexes referring to images in the squib directories, construct and save a generated squib."""
        # construct the squib
        squib = Image.open(os.path.join("resources", "squibs", "white.png")).convert("RGBA")
        self.attach_image(squib, os.path.join("resources", "squibs", "straight_squib", "body.png"))
        self.attach_image(squib, os.path.join("resources", "squibs", "straight_squib", "bubble", "bubble.png"))
        for i, part_idx in enumerate(part_idxs):
            part_name = list(self.common_registry)[i]
            img_name = self.common_registry[part_name].get(part_idx)
            self.attach_image(squib, img_name)
        
        # to add the squib name, id, quote
        editable_squib = ImageDraw.Draw(squib)
        # name
        name = generate_name().split("_")
        font = ImageFont.truetype("Arial Bold.ttf", size=20)
        editable_squib.text((80, 360), " ".join(name), fill =(0, 0, 0), font=font)
        # id
        id = ''.join([str(num) for num in part_idxs])
        squib_id = f"SQUIB#{id}"
        editable_squib.text((150, 10), squib_id, fill =(0, 0, 0), font=font)
        # text
        speech = self.tg.get_next_sentence()
        font = ImageFont.truetype("Arial Bold.ttf", size=14)
        editable_squib.text((190, 130), speech, fill =(0, 0, 0), font=font)
        
        output_file = f"{id}.png"
        squib.save(os.path.join(self.output_path, output_file), format="png")


    def assemble_common(self):
        """DFS of squib images to construct all possible combinations of common components."""
        seen = set()
        nodes = [tuple([0]*len(self.common_registry))]
        count = 0
        while nodes: 
            cur = nodes.pop()
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
        print(f"{count} squibs generated.")
