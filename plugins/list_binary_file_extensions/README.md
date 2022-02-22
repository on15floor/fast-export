## List binary file extensions

This plugin generates a file consisting of a list of binary file extensions 
found in the mercurial repository at the time of conversion.

Note: You may need this list to further convert the git repository to git lfs.

To use this plugin, add the command line flag:  
`--plugin list_binary_file_extensions=<file_path_to_save>,bigger_then(bytes)`

Example:
`--plugin list_binary_file_extensions=/Users/username/rep-binary_ex.txt,1024`
