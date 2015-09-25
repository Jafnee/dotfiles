import os

#Script Dir
THIS_DIR = os.path.dirname(os.path.realpath(__file__))

HOME_DIR = os.path.expanduser('~/')

# Dot files backup dir
BACKUP_DIR = os.path.join(sdir,'dotfiles_backup')

"""Used to configure where dotfiles are located.
Can choose whether to backup individual files or a whole directory.
Examples:
    DotFile('Shells', files=['.bashrc', '.zshrc'])
    DotFile('i3', dirs=['.i3'])
    DotFile('i3', files=['.i3/config'])
    DotFile('i3', path='.i3', files=['config'])
"""
class DotFile(object):
    def __init__(self, name, path='~/', dirs=[], files=[]):
        """How to use.
        Args:
            name (str):                 Name or description.
            path (Optional str):        Path of dotfile's directory. Defaults to $HOME.
            dirs (Optional [str]):      List of directory paths relative to path.
            files (Optional [str]):     List of file paths relative to path.
        """
        self.name = name
        self.path = path
        self.dirs = dirs
        self.files = files

# Add dotfiles here
dotfiles = [
    DotFile('i3', files='.i3'),
    DotFile('subl3', path='.config/sublime-text-3', dirs='Packages/User'),
]