#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int]
    
    malformed = 0
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
            #check that we have 3-9 or 12 columns but not 10 or 11 columns
            #for files with 9 columns, verify that there are 3 integers for itemRGB
            #strip the comma from blocksizes(11) and blockstarts(12)
            #check that blocksizes and blockstarts length matches blockcount
            #report malformed lines#return a bed file list with the edits we made
            #convert items into an integer--convert 9th column to a list
            #if any of that fails, we wwant to record that a malformed line was found
            #add to the malformed counter
            try:
                if fieldsN >= 9:#make sure the file we're working with has 9 columns
                    rgb = fields[8] #pull out the 9th column, call it rgb
                    rgb_list = rgb.split(',')#convert that to a list
                    #it would look like ["254", "0", "0"]
                    #first run would be i = 0, item = 254, so it is rgb_list[0]=int("254") --> rgb[0] = 254
                    for i, item in enumerate(rgb_list):
                        rgb_list[i] = int(item)
                        #replace the 9th column with the list
                    fields[8] = rgb_list
                #only do this for files that have 12 columns    
                if fieldsN == 12:
                    blockSizes = fields[10].rstrip(",").split(",")
                    blockStarts = fields[11].rstrip(",").split(",")
                    for i, item in enumerate(blockSizes):
                        blockSizes[i] = int(item)
                        fields[10] = blockSizes
                    for i, item in enumerate(blockStart):
                        blockStarts[i] = int(item)
                        fields[11] = blockStarts
                    blockCount = int(fields[9])
                    if len(blockStarts) != blockCount:
                        malformed += 1
                    if len(blockSizes) != blockCount:
                        malformed += 1
                    fields[9] = blockCount #replace 10th column with its integer                
                    #blockSizes looks like ["76", "140", "86", "211"]
                    #blockStarts looks like ["0", "749", "2587"]
                    #now you want to pull out the value of blockcount
            except:
                raise FileNotFoundError("That file doesn’t appear to exist")
            #strip commas, convert column 11 and 12 into lists (11 into a list and 12 into a list)
            #check that blocksizes and block start length matches blockcount (column 10)               
        try:
            #convert all columns to the correct data type
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])#if it works, append the correct lines to the fields list
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed #return the bed list we made, with all the edits we're making in the for loop area
    #a bedfile needs at least the first 3 columns
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)