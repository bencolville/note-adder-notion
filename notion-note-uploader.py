#! /usr/bin/python3
import os
from notion.client import NotionClient
from notion.block import *
from md2notion.upload import upload

client = NotionClient(token_v2="c623dcd5b65d87ab04eb416df760ce94408af158fec35d8afd29ef05f1e68cc03edf242dafd8a5ddda5de7d2db84e3f3c5554bd7725a92548ed24015ca25c2ec0090e3a53206e1e18ecb81eccba2")

NotePage = client.get_block("https://www.notion.so/3d3221983e854791bf6a8e6e01b2664c?v=007d4713000144d584531e4efa8b22fe")

file_to_upload = input("Name of file to upload (with extension): \n")
title_of_file = file_to_upload[:-3]
current_dir = os.getcwd()
path_to_file = current_dir + "/" + file_to_upload

print(path_to_file)

#upload the file 

with open(path_to_file,"r", encoding="utf-8") as mdFile:
        newPage = NotePage.children.add_new(PageBlock, title=title_of_file)
        upload(mdFile, newPage)
