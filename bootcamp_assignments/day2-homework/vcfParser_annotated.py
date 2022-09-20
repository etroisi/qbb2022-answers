#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = [] 
    info_description = {}
    info_type = {}
    format_description = {}#create a dictionary
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }# allows us to use information from the headerr to tell python what data types to expect
    malformed = 0 #initialize variable to count the number of malformed VCF lines
#trying to open the VCF file, if file cannot open, give error message
    try:
        fs = open(fname) #create a variable called fs, which is storing the opened vcf file
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)#error message it will tell you if the file does not open

    for h, line in enumerate(fs):#tells it to keep track of item in the list's position
        if line.startswith("#"):#for header lines, this is the header parsing section
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: #if not on a header line, do the next thing
            try:#try doing the following, if anything here fails, increment "malformed" variable by 1
            #fields is a list that stores the info in one line of the VCF
                fields = line.rstrip().split("\t")#for the line, get rid of the white space after the line, then separate each line on a tab character so that every column in  the line is an item in the list ("fields") (note line is a string before we split it into separate strings)
                fields[1] = int(fields[1])#turns the second column (SNP position) into an integer (was a string before this step) if it cannot become an integer, go to except
                if fields[5] != ".":#if the 5th column (ie, QUAL) is not . , then do the next thing...
                    fields[5] = float(fields[5])#turn it into a float (if the QUAL column is not a . , turn it into a float)
                info = {}#initializing a dictionary to store the info in the INFO column, next part is for parsing the INFO column
                #we want the info dictionary to look like this: {"AC" : 91,
                                                                # "AN" : 5-96
                                                            # etc
                                                                # "NS" : 2548}
                for entry in fields[7].split(";"):#for loop for the 8th column (INFO column). all that info is a string. separate it into separate items in a list, separate when there is a ; #this will look like this ["AC=91", "AN=5096", ... "NS=2548"]
                #the first entry we're working with is "AC=91"
                    temp = entry.split("=") #this will look like ["AC", "91"]
                    if len(temp) == 1: #if there's only one item in the temp list ( like "AC="), update the dictionary so that we know AC has no value for this SNP
                        info[temp[0]] = None #temp[0] is "AC"
                        #dictionaries have keys and values, you can add info to a dictionary by doing dict_name[new_key]  = new_value. EX: info["AC"] = "91". this is updating the dictionary we made called "info" so that the key AC has the value none. so it will look like {"AC" : None}
                    else: #otherwise, the value is the item in position 1
                        name, value = temp #temp = ["AC", "91"]. name = "AC", value = "91"
                            #another way: name = temp[0]. value = temp[1] #this says item in position 0 is "name" and item in position 1 is the matching value
                            #in these next two lines, we're converting the data in each entry to its correct data type. that info is in the header lines that we parsed before
                        Type = info_type[name]#we're getting the python function for data type conversion that corresponds to what the entry should be.
                        # Ex: type = info_type["AC"]. info_type is a dictionary we made in the header parsing section that tells us what data type that entry should be
                        info[name] = type_map[Type](value)#we're getting the python function for converting the entry to the correct data type. 
                        #ex: for AC: info["AC"] = type_map["Integer"]["91"]
                fields[7] = info #replace the 8th item of the "fields"
                if len(fields) > 8: #if we still have more columns after the INFO column, then do the next things:
                    fields[8] = fields[8].split(":") #example of fields[8] (FORMAT) gt:dp:af:bg:ru
                    #splitting FORMAT columns by :
                    #example: gt:dp:af:bg:ru would become ["GT", "DP", "AF", etc]
                
                    if len(fields[8]) > 1: #how many items are in this new list? if there are more than 1, do the following for each item
                    #example: if it said GT:DP then HG00097 would be 0|0:0.3
                        for i in range(9, len(fields)): #this goes through all the columns after the FORMAT column -> this would be range(9, 2513)
                            fields[i] = fields[i].split(':')#splits each genotype column along :
                                                            #like if it was 0|0:0.3-> ["0|0", "0.03"]
                                                            
                    else: #if the genotypes (from fields8) don't have more than one value in them, do the next thing
                        fields[8] = fields[8][0] #fields[8] is ["GT"], this makes fields[8] equal the first position element, which is GT. so now fields[8] is GT
                vcf.append(fields)#we analyzed and changed a lot of data, and so we're going to put those changes into the list we created at the beginning, VCF. fields was changed, so this reads listyouwanttochange.makechange(addthefileswechanged)
                #fields is a list that contains info for the current line we're working on
            except:#if anything in the try block fails, do the following 
                malformed += 1 #counts how many malformed lines there are, ie, lines that did not pass the preceeding try block
    vcf[0][7] = info_description #these next three lines modifying the first line of the vcf list to match the information of the header
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0:#if there were malformed lines, we're going to print the number of lines so the user knows how many are wrong
        print(f"There were {malformed} malformed entries", file=sys.stderr)
        #at the very end of running the function, return the vcf.
    return vcf

if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
