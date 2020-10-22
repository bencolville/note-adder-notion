# Notion Note Uploader

This simple python script is designed to be run from the command line (CLI) with user input. It adds a markdown file to the bottom of a specified page. It uses the unofficial [Notion API](https://github.com/jamalex/notion-py) and [md2notion](https://github.com/Cobertos/md2notion). The current implementation of the latter is not very user friendly and that is what is solved here.

## Set up

1. Clone the repo
2. Obtain your Notion v2 token:
  - Go to Notion.so and Inspect the page.
  - Locate 'Application' and select 'Cookies'
  - Double-click on the token_v2 Value cell and copy it
2. Then simply create a text file called v2.txt containing your Notion v2 token that you have obtained

## Usage

To use this simply run the script from any directory where you have a markdown file you wish to upload. Provide first the URL of the page you wish to upload to and then the name of the file to be uploaded including the extension.

## Making the script available everywhere
You can make this script available on the commandline globally by adding this 
```alias mdnotion="python3 /PATHTOSCRIPT/notion-note-uploader.py"``` 
to your `.bash_aliases` and then 
`source ~/.bashrc` 
