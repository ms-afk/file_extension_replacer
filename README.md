# file_extension_replacer
A simple python command line tool to remove or replace a file extension with another one.  
The changes will be applied to every file in the selected directory and, if selected, in the subdirectories too.
## Usage
```
file_extension_replacer [OPTIONS] root oExt nExt
```
Arguments meaning:
+ **root** The path to the folder where this program will be executed (insert \".\" to use the current working directory)
+ **oExt** The file extension to delete (e.g., \".txt\"; use "" to select every file found)
+ **nExt** The file extension to replace the old one with (use \"\" to simply remove the files extension)"

Options meaning:
+ **-r** Runs the program recursively (in the subdirectories too)
+ **-h** Displays the help menu
+ **--help** Displays the help menu
