#!/usr/bin/env python3

f = open("annotateddecomposedsnps.vcf")
for l in f:
        if l.startswith("#"): #skip the headers
            continue
        fields = l.rstrip().split("\t") #make the fields into lists so you can pick out info from them 
        INFO=fields[7] #name column 7 as INFO (it is already called that)
        infolist = INFO.split(";")#split on the ;
        AF = infolist[3]#make the 3rd element from the list of elements in info into a list
        aflist = float(AF.split("=")[1].split(",")[0])#make them floats and separate them into a list
        #ANN=infolist[41]#
        #annlist = ANN.split("|")[1]#grabbing the predicted effects of each variant
        #DP=infolist[7]#make the 7th element from the list of elements from the info column into a list
        #dplist=DP.split("=")[1].split(",")[0]
        
        #print(aflist)
print(aflist)
#for annotation, pull out ANN from infolist, make a list--same way you did the AF stuff

    
        
        
