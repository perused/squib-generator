from PIL import Image
import os

orientation_dict = {"straight": "straight_squib", "left": "left_squib", "right": "right_squib"}
# common = ["eyes", "mouth", "left_arm", "right_arm", "left_leg", "right_leg", "shadow"]
# rare = []
# ultra_rare = []
# one_of_a_kind = []


class SquibGenerator:
    """A class for assembling squibs of different rarities."""
    def __init__(self, orientation, common_registry):
        self.orientation = orientation_dict[orientation]
        self.common_registry = common_registry
        self.output_path = os.path.join("generated", self.orientation)

    def construct_common_squib(self, part_idxs):
        """Given indexes referring to images in the squib directories, construct and save a generated squib."""
        squib = Image.open(os.path.join("squibs", "straight_squib", "body.png")).convert("RGBA")
        for i, part_idx in enumerate(part_idxs):
            part_name = list(self.common_registry)[i]
            img_name = self.common_registry[part_name].get(part_idx)
            img = Image.open(img_name).convert("RGBA")
            squib.paste(im=img, box=(0, 0, 420, 420), mask=img)
        output_file = f"{''.join([str(num) for num in part_idxs])}.png"
        squib.save(os.path.join(self.output_path, output_file), format="png")

    # TODO: create a strategy pattern to assemble different rarities rather than just common
    def assemble_common(self):
        """DFS of squib images to construct all possible combinations of common components."""
        seen = set()
        nodes = [(0, 0, 0, 0, 0, 0, 0)]
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
            # if count == 20:
            #     break
        print(f"{count} squibs generated.")
