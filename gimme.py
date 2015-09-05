#!/usr/bin/env python3
import os
from os.path import join as joinpth
import shutil

import config as cfg

def backup(imp=False):
	if imp:
		print("Importing...")
		dst = cfg.sdir
	else:
		print("Backing up...")
		dst = cfg.bdir
	for item in cfg.items:
		print(" "+item)
		src = joinpth(cfg.dir, item)

		try:
			shutil.copy2(src, dst)
		except IsADirectoryError:
			print("Can't copy dirs yet!")
	print("Done!")

def import_():
	backup(imp=True)

if __name__ == '__main__':
	# main()
	backup()
