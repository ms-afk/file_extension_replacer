#!/usr/bin/env python3
import os, sys

help_text = "File Extension Replacer\nusage: " + sys.argv[0] + " [OPTIONS] root oExt nExt\n\
This utility replaces a chosen file extension with a new one.\n\
The utility does so on all files in the selected directory, SUBDIRECTORIES INCLUDED.\n\
Arguments meaning:\n\
root	The path to the folder where this program will be executed (insert \".\" to use the current working directory)\n\
oExt	The file extension to delete (e.g., \".txt\")\n\
nExt	The file extension to replace the old one with (use \"\" to simply remove the files extension)\n\
Options:\n\
-h	Shows this help menu\n\
--help	Shows this help menu"

if "-h" in sys.argv or "--help" in sys.argv:
	print(help_text)
	sys.exit(0)
if len(sys.argv) != 4:
	sys.exit("Invalid arguments!")

root, old_extension, new_extension = sys.argv[1:]

for dirpath, dirnames, filenames in os.walk(root, topdown=True):
	for filename in filenames:
		if filename.endswith(old_extension):
			full_path = os.path.join(dirpath, filename)
			new_filename = filename.removesuffix(old_extension) + new_extension
			new_full_path = os.path.join(dirpath, new_filename)
			os.rename(full_path, new_full_path)
