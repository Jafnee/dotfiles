import os

#Script Dir
sdir = os.path.dirname(os.path.realpath(__file__))


# Where to put the dot files
dir = os.path.expanduser('~/')
# Dot files backup dir
bdir = os.path.join(sdir,'dotfiles_backup')

# Dotfile names or dir
items = ['.bashrc']