#!/usr/bin/env python3

import sys

def parse_bed(fname): #defining the function
    try:#attempt to run the following script
        fs = open(fname, 'r')#open file as indicated by user in command line
    except:#if this script is attempted on a line and it fails, print the next line
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []#initialize a list
    field_types = [str, int, int, str, float, str, int, int, int, int, int, int]#define what you want the field types of your file to be, for every column)
    for i, line in enumerate(fs):#for loop applied to i, which is a line in the file
        if line.startswith("#"):#skip lines that start with #
            continue
        fields = line.rstrip().split()#remove white space after the line; white spaces will delineate separate units in a field
        fieldN = len(fields)#just saying fieldN refers to the length of fields (fields is a list of the items in a field)
        if fieldN not in [3,4,5,6,7,8,9,12]: #we only want lines that have 3,4,5,6,7,8,9,12 fields. therefore, this line means does not do the following line for 3-12
            print(f"Line {i} appears malformed", file=sys.stderr)#if fieldN is 1,2,10,11, or greater than 12, that's an error
            continue#keep going, don't stop the code if the line is an error
        if fieldN == 12:#if the line has a field length is 12, do the following. this part checks if the line is field length 12, does column 9 = column 10 or column 9 = 11, if either of these are not true, that's a fail
            blockCOUNT = int(fields[9])#first we have to define the integer in fields9 as blockcount
            blockSizes = fields[10].rstrip(',').split(',')#in fields10, make the info there into a list separated by commas
            blockStarts = fields[11].rstrip(',').split(',')#in fields11, make the info there into a list separated by commas
            if (len(blockSizes) != blockCOUNT) or (len(blockStarts) != blockCOUNT):#if the length of blocksizes isn't equal to blockcount, or if the length of blockstart isn't equal to blockcount, do the following
                print(f"Line {i} appears malformed", file=sys.stderr)
                continue
        if fieldN == 9 or fieldN == 12:#for lines that have fieldN of 9 or 12, do the following
            try:#attempt to do the following
                rgb = fields[8].split(',')#define rgb as a variable that is the info in fields8 as a list, define each unit in the list by commas
                for k in range(len(rgb)):#for loop applied to k, which is a number given back from the range function
                    rgb[k] = field_types[8](rgb[k])#making k in rgb into field_type[8], which is integer
                if len(rgb) != 3: #if the length of the list of integers in rgb is not 3, do the following (ie, give an error)
                    print(f"Line {i} appears malformed", file=sys.stderr)
                    continue #print line is malformed if rgb is not 3
            except:
                print(f"Line {i} appears malformed", file=sys.stderr)
                continue#got to next line
                  
        try:#attempt the following for loop
            for j in range(min(len(field_types), len(fields))):#match fields with field type, which we explained earlier
                if j == 8 or j == 10 or j == 11: # if that number is 8, 10, or 11...
                    currentField = fields[j].rstrip(',').split(',')#for fields with j length, grab those lines, strip the white space and convert it into a list separated by commas, call that list a variable named currentField so we can further use it
                    for k in range(len(currentField)):#looking in currentField
                        currentField[k] = field_types[j](currentField[k])#for those lines that we just grabbed, begin to apply field types to those lines
                    fields[j] = currentField
                else:
                    fields[j] = field_types[j](fields[j])
            bed.append(fields)#add this new info to the fields list we made earlier
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)#print "line is malformed" if not 8,  10, or 11.
    fs.close()#close the file
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
