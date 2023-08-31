#!/usr/bin/env python3
import os, sys

#help menu

options_description = {"-r" : "Runs the program recursively (in the subdirectories too)", "-v" : "Verbose execution: prints additional informations", "-h" : "Shows this help menu", "--help" : "Shows this help menu"}

help_text = "File Extension Replacer\nusage: " + sys.argv[0] + " [OPTIONS] root oExt nExt\n\
This utility replaces a chosen file extension with a new one.\n\
The utility does so on all files in the selected directory, subdirectories excluded by default.\n\
Arguments meaning:\n\
 root	The path to the folder where this program will be executed (insert \".\" to use the current working directory)\n\
 oExt	The file extension to delete (e.g., \".txt\"; use "" to select every file found)\n\
 nExt	The file extension to replace the old one with (use \"\" to simply remove the files extension)\n\
Options:"

def help():
	print(help_text)
	for opt in options_description:
		print(" "+opt+"\t"+options_description[opt])

#command line arguments

arguments = []
options = []
for el in sys.argv[1:]:
	if el.startswith("-"):
		options.append(el)
	else:
		arguments.append(el)
for opt in options:
	if not opt in options_description:
		sys.exit("Invalid options! Use -h for help.")
if "-h" in options or "--help" in options:
        help()
        sys.exit(0)
if len(arguments) != 3:
        sys.exit("Invalid arguments! Use -h for help.")

#begin execution

root, old_extension, new_extension = arguments

for dirpath, dirnames, filenames in os.walk(root, topdown=True):
	if "-v" in options:
		print("Entering directory '" + dirpath + "'")
	for filename in filenames:
		if filename.endswith(old_extension):
			if "-v" in options:
        			print("Replacing file '" + filename + "'")
			full_path = os.path.join(dirpath, filename)
			new_filename = filename.removesuffix(old_extension) + new_extension
			new_full_path = os.path.join(dirpath, new_filename)
			try:
				os.rename(full_path, new_full_path)
			except FileExistsError:
				print("Warning: skipping file '" + new_full_path + "' because a file or directory with the same name already exists")
	if not "-r" in options:
		#don't continue in the subdirectories if it's not requested
		break
