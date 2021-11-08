import os
import random

extensions = [".rst",".txt",".md",".docx",".odt",".html",".ppt",".doc"]

os.chdir("./RandomFiles")

for item in extensions:
    DirName = item.split(".")[1].upper()
    os.mkdir(DirName)

    for i in range(20):
        file_name = random.randint(1,50)
        file_to_create = str(file_name) + item
        open(DirName+"/"+file_to_create,"w").close()
