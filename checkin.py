#!/usr/bin/env python3


import glob
import sys
import os
import shutil
from os import path
def main():
    #  chack the user input is only 1 args 1 path is default and 1 file name
    if(len(sys.argv) != 2):
        print("please enter one file name")
        return 0
    print(sys.argv[1])
    print("Current working directory: {0}".format(os.getcwd()))
    print("The directory .MYCVS exits? : {}".format(path.isdir(".MYCVS")))
    # check if there is a file with in our args ,
    if not path.exists(sys.argv[1]):
        print("There is no file exitsts with name: {}".format(sys.argv[1]))
        return 0

    if not path.isdir(".MYCVS"):
        print("first checkin wow !!")
        # create .MYCVS Directory
        newpath = os.path.join(os.getcwd(),".MYCVS")
        print(newpath)
        os.mkdir(".MYCVS")
        # Create an copy of the original file
        shutil.copyfile(sys.argv[1],".MYCVS/{}.myv".format(sys.argv[1]))

        

    # for file in glob.glob("*"):
    #     file = "file: {}".format(file)
    #     print(file)

if __name__ == "__main__":
    main()