#!/usr/bin/python3

import re, csv, subprocess
from shutil import which
# TODO: Finish up the fallback using re, write main


def reader(my_sites, the_list):
    # Import the user's list of passwords.  
    # We want a csv with one entry per line

    with open(my_sites, 'r') as f:
          reader = csv.reader(f)
            site_list = list(reader)
    # tweaks for formatting go here when we have an exemplar file

    # file stuff
    new_path = 'change_these_passwords.txt')

    # if we have access to grep we get to do this the elegant way
    if(which(grep)):
        for site in site_list:
            tmp = subprocess.getoutput("grep -w "site" the_list")
            if len(tmp) > 0:
                # make no assumptions about user dir structure
                # just drop the file in the same dir we're in
                output_file = open(new_path,'w')
                output_file.write(site)
    # We don't have grep.  Sadface
    else:
        with open(the_list, 'r') as cloudflare:

