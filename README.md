ls-json
=======

ls-json generates a JSON file, listing files in a directory.

##what?
ls-json lists the contents of a directory, crams it in a JSON string, throws some metadata in it and writes to stdout.

##why?
* I needed it for some personal projects
* I needed some typing exercise
* I missed Python

##how?
just execute ls-json in a directory of your choosing. or, alternatively you can give the path to the directory whose items you want listed. e.g. ```ls-json /home/yasa/superInterestingStuff/```

also, you can use ```-e``` flag to exclude dotfiles, and ```-p``` flag to pretty-print the resulting JSON.