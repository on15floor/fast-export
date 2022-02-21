## Gitignore Extension

This plugin generates a **.gitignore** file from a **.hgignore** at the time 
of conversion.

Note: You can specify additional exceptions that will not go into the 
**.gitignore** file in the plugin class (self.remove_from_hgignore).

To use this plugin, add the command line flag:  
`--plugin gitignore_extension`
