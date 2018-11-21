# Secrets - Interactive lecture nov 21st 2018

import os

def rename_files(directory, removechars):
    # Get all names from folder.
    filetable = os.listdir(directory)

    # Change working directory
    savedir = os.getcwd()
    os.chdir(directory)

    translate = str.maketrans("", "", removechars)
    for file in filetable:
        print(file, "endres til", file.translate(translate))
        os.rename(file, file.translate(translate))

    os.chdir(savedir)

inputpath = input("Enter path: ")
charstoremove = input("What characters shall I remove: ")

rename_files(inputpath, charstoremove)

