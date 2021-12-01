from PIL import Image, ImageDraw, ImageFont
import os

orientation_dict = {"straight": "straight_squib", "left": "left_squib", "right": "right_squib"}

class SquibGenerator:
    """A class for assembling squibs of different rarities."""
    def __init__(self, orientation, common_registry):
        self.orientation = orientation_dict[orientation]
        self.common_registry = common_registry
        self.output_path = os.path.join("generated", self.orientation)

    def attach(self, img, file_name):
        attacher = Image.open(file_name).convert("RGBA")
        img.paste(im=attacher, box=(0, 0, 420, 420), mask=attacher)

    def construct_common_squib(self, part_idxs):
        """Given indexes referring to images in the squib directories, construct and save a generated squib."""
        squib = Image.open(os.path.join("squibs", "white.png")).convert("RGBA")
        self.attach(squib, os.path.join("squibs", "straight_squib", "body.png"))
        self.attach(squib, os.path.join("squibs", "straight_squib", "bubble", "bubble.png"))
        for i, part_idx in enumerate(part_idxs):
            part_name = list(self.common_registry)[i]
            img_name = self.common_registry[part_name].get(part_idx)
            self.attach(squib, img_name)
        output_file = f"{''.join([str(num) for num in part_idxs])}.png"
        squib.save(os.path.join(self.output_path, output_file), format="png")

    # TODO: create a strategy pattern to assemble different rarities rather than just common
    def assemble_common(self):
        """DFS of squib images to construct all possible combinations of common components."""
        seen = set()
        nodes = [tuple([0]*len(self.common_registry))]
        count = 0
        while nodes: 
            cur = nodes.pop()
            print(cur)
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
            # if count == 20:
            #     break
        print(f"{count} squibs generated.")
