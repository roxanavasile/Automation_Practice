import shutil


class FileMover:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        source_path = self.source_path
        self.destination_path = destination_path

    def move_file(self):
        shutil.move(self.source_path, self.destination_path)

mover = FileMover('C:\\Users\\roxan\\OneDrive\\Documents\\learn_Py\\FileMover\\file_to_move.txt',
                  'C:\\Users\\roxan\\OneDrive\\Documents\\learn_Py\\FileMover\\Moved_files\\file_to_move.txt')

mover.move_file()