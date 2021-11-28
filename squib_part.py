import os
import logging

class SquibPart:
    def __init__(self, path_to_dir):
        self.path_to_dir = path_to_dir
        self.dir_size = len(os.listdir(self.path_to_dir))

    def get_dir_size(self):
        return self.dir_size

    def can_increment(self, num):
        return num < self.dir_size - 1

    def get(self, idx):
        if idx >= self.dir_size:
            logging.warning(f"'get' called in SquibPart with idx {idx} when dir size is {self.dir_size}.")
            return None
        file_name = os.listdir(self.path_to_dir)[idx]
        if file_name[0] == ".":
            return None
        return os.path.join(self.path_to_dir, file_name)