#! /usr/bin/python3
import os
from notion.client import NotionClient
from notion.block import *
from md2notion.upload import upload

# open the file to retrieve token_v2

with open("v2.txt") as f:
    mylist = f.read().splitlines()

v2=mylist[0]

client = NotionClient(token_v2=v2)

# get user input for destination of upload

UploadDestination = input("Link to page you wish to upload to: \n")

NotePage = client.get_block(UploadDestination)

# get user input for name of file to be uploaded

file_to_upload = input("Name of file to upload (with extension): \n")
title_of_file = file_to_upload[:-3]
current_dir = os.getcwd()
path_to_file = current_dir + "/" + file_to_upload

print(path_to_file)

#upload the file 

with open(path_to_file,"r", encoding="utf-8") as mdFile:
        newPage = NotePage.children.add_new(PageBlock, title=title_of_file)
        upload(mdFile, newPage)
