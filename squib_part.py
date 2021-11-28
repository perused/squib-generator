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
            raise IndexError(f"Index {idx} requested in squib directory {self.path_to_dir} which only has size {self.dir_size}.")
        file_name = os.listdir(self.path_to_dir)[idx]
        if file_name[0] == ".":
            raise Exception(f"Invalid file '{file_name}' exists in squib directory {self.path_to_dir}.")
        return os.path.join(self.path_to_dir, file_name)