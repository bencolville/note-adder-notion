This simple python script is designed to be run from the CLI with user input and to add the markdown file to the bottom of the Meeting Notes database in the Resources section

To do:
- [X] make it work
- [X] make it into a global script to be called from any directory
- [] improve it so it can grab the v2 token on its own? 


## Making the script available everywhere
You can make this script available on the commandline globally by adding this 
```alias mdnotion="python3 /PATHTOSCRIPT/notion-note-uploader.py"``` 
to your `.bash_aliases` and then 
`source ~/.bashrc` 
