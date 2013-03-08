#!/usr/bin/python
import os, argparse, json, time

# hidden == dotfile as far as we're concerned
def is_hidden(filename):
	if filename.startswith('.'):
		return True

parser = argparse.ArgumentParser(description="Output directory contents as JSON")
parser.add_argument('path', nargs='?', default=".", help="The path to the directory whose contents will be listed")
parser.add_argument('-o', default="./ls.json", help="The path to the output file. Defaults to ./ls.json")
parser.add_argument('-e', dest="exclude_hidden", action="store_true", help="Exclude hidden files (dotfiles)")
parser.add_argument('-p', dest="pretty_print_indent", action="store_const", help="Pretty print the output JSON", const=2)
args = parser.parse_args()

filelist = os.listdir(args.path)
timestamp = int(round(time.time() * 1000))

if args.exclude_hidden:
	filelist = [item for item in filelist if not is_hidden(item)]

result = {"timestamp":timestamp, "hiddenFiles": not args.exclude_hidden, "files":filelist}
print(json.dumps(result,indent=args.pretty_print_indent))