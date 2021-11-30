import os


class SquibPart:
    """A class for storing information on a squib image directory and facilitating indexing of that directory."""
    def __init__(self, path_to_dir):
        self.path_to_dir = path_to_dir
        self.dir_size = len(os.listdir(self.path_to_dir))

    def get_dir_size(self):
        """Return the size of the directory."""
        return self.dir_size

    def can_increment(self, num):
        """Return if it is possible to retrieve index num + 1 from the directory."""
        return num < self.dir_size - 1

    def get(self, idx):
        """Return the name of a non-hidden file at a certain index of the directory."""
        if idx >= self.dir_size:
            raise IndexError(f"Index {idx} requested in squib directory {self.path_to_dir} which only has size {self.dir_size}.")
        file_name = os.listdir(self.path_to_dir)[idx]
        if file_name[0] == ".":
            raise Exception(f"Invalid file '{file_name}' exists in squib directory {self.path_to_dir}.")
        return os.path.join(self.path_to_dir, file_name)
