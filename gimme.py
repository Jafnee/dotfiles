#!/usr/bin/env python3
import sys
import os
from os.path import join as joinpth
import shutil

import config as cfg

def _mkdirs(path):
	"""Silent makedirs
	"""
	try:
		os.makedirs(path)
	except FileExistsError:
		pass

def backup():	
	for df in cfg.dotfiles:
		# backup files
		for f, fp in zip(df.files, df.file_paths):
			_mkdirs(joinpth(cfg.BACKUP_DIR, df.name, os.path.dirname(f)))
			shutil.copy2(fp, joinpth(cfg.BACKUP_DIR, df.name, f))

		# backup dirs
		for d in df.dirs:
			print(d)


def print_help():
	print("Help msg\nand stuff")
	sys.exit()

if __name__ == '__main__':
	try:
		arg = 	sys.argv[1]
	except IndexError:
		print_help()
	if arg in ('backup', 'b'):
		backup()
	else:
		print_help()
	# main()
	# backup()
	# import_()
	# symlink()
