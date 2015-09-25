import os

#Script Dir
THIS_DIR = os.path.dirname(os.path.realpath(__file__))

HOME_DIR = os.path.expanduser('~/')

# Dot files backup dir
BACKUP_DIR = os.path.join(THIS_DIR,'dotfiles_backup')

"""Used to configure where dotfiles are located.
Can choose whether to backup individual files or a whole directory.
Examples:
    DotFile('Shells', files=['.bashrc', '.zshrc'])
    DotFile('i3', dirs=['.i3'])
    DotFile('i3', files=['.i3/config'])
    DotFile('i3', path='.i3', files=['config'])
"""
class DotFile(object):
    def __init__(self, name, path=HOME_DIR, dirs=[], files=[]):
        """How to use.
        Args:
            name (str):                 Name or description.
            path (Optional str):        Path of dotfile's directory. Defaults to $HOME.
            dirs (Optional [str]):      List of directory paths relative to path.
            files (Optional [str]):     List of file paths relative to path.
        """
        self.name = name
        self.path = path
        if type(dirs) == str:
            self.dirs = [dirs]
        elif type(dirs) == list:
            self.dirs = dirs
        if type(files) == str:
            self.files = [files]
        elif type(files) == list:
            self.files = files

        self.clean()

    def __str__(self):
        return self.name

    def clean(self):
        """What ever prep needs to be done.
        """
        self.path = os.path.expanduser(self.path)

    @property
    def all(self):
        return self.dirs + self.files
    @property
    def dir_paths(self):
        return [os.path.join(self.path, d) for d in self.dirs]

    @property
    def file_paths(self):
        return [os.path.join(self.path, f) for f in self.files]

    @property
    def all_paths(self):
        return self.dir_paths + self.file_paths


# Add dotfiles here
dotfiles = [
    DotFile('i3', dirs='.i3'),
    DotFile('subl3', path='~/.config/sublime-text-3', dirs='Packages/User'),
]
