#!/usr/bin/env python3
import os
from os.path import join as joinpth
import shutil

import config as cfg

DEBUG=True

def backup(imp=False):
	if imp:
		print("Importing...")
		dst = cfg.sdir
	else:
		print("Backing up...")
		dst = cfg.bdir
		os.makedirs(dst)
	for item in cfg.items:
		print("  "+item)
		src = joinpth(cfg.dir, item)

		try:
			shutil.copy2(src, dst)
		except IsADirectoryError:
			dst = joinpth(dst, item)
			try:
				shutil.copytree(src, dst)
			except FileExistsError:
				shutil.rmtree(dst)
				shutil.copytree(src, dst)
		except shutil.SameFileError:
			pass
	print("Done!")

def import_():
	backup(imp=True)

def symlink():
	print("Linking...")
	for item in cfg.items:
		print("  "+item)
		src = joinpth(cfg.sdir, item)
		dst = joinpth(cfg.dir, item)
		try:
			os.symlink(src,dst)
		except FileExistsError:
			os.remove(dst)
			os.symlink(src,dst)
	print("Done!")

if __name__ == '__main__':
	# main()
	backup()
	# import_()
	# symlink()
