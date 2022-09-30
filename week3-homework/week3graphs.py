#!/usr/bin/env python3

import matplotlib.pyplot as plt

f = open("annotateddecomposedsnps.vcf")

aflist = []
dplist=[]
annlist=[]
gqlist=[]
anndict={}
for l in f:
        if l.startswith("#"): #skip the headers
            continue
        fields = l.rstrip().split("\t") #make the fields into lists so you can pick out info from them 
        #print(fields[8])
        INFO=fields[7] #name column 7 as INFO (it is already called that)
        infolist = INFO.split(";")#split on the ;
        AF = infolist[3]#make the 3rd element from the list of elements in info into a list
        aflist.append(float(AF.split("=")[1].split(",")[0]))#make them floats and separate them into a list
        #the next values have to come from the FORMAT column
        FORMAT=fields[8]#check what's in this 
        #print(FORMAT) 
        ANN=infolist[41]#ANN is a variable containing the 41st element from infolist 
        annlist.append(ANN.split("|")[1])#grabbing the predicted effects of each variant
        #DP=infolist[7]#make the 7th element from the list of elements from the info column into a list
        #dplist.append(DP.split("=")[1].split(",")[0]) <--this is incorrect, the dp needed is in columns 9 and on
        
        for A0 in fields[9:]:#for each A0_1, grab the column's info, which is GT:GQ:DP:RO:QR:AO:QA:GL, want GQ and DP, which are the second and third values respectively
            #print(A0)
            a0list=A0.split(":") #pull out what's in each A0 and make it into a list for each A0
            GQ = a0list[1]#take the 2nd item from that list
            DP = a0list[2]#take the 3rd item from that list
            if GQ != '.':
                gqlist.append(float(GQ))
            if DP != '.':
                dplist.append(float(DP))
#print(annlist)
for ann in annlist:#makeing a dictionary of the items in annlist and how many times each item
   if ann in anndict.keys():
       anndict[ann]+=1
   else:
       anndict[ann]=1
               
            #print(A0)
        #print(aflist)


#for annotation, pull out ANN from infolist, make a list--same way you did the AF stuff

    
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.hist(aflist, label = "allele frequency")
ax1.set_ylabel("distribution")
ax1.set_xlabel("frequency")
ax1.legend()

ax2.hist(dplist, label = "read depth")
ax2.set_ylabel("distribution")
ax2.set_xlabel("depth")

ax3.hist(gqlist, label = "genotype quality")
ax3.set_ylabel("distribution")
ax3.set_xlabel("genotype quality")

ax4.bar(anndict.keys(), anndict.values(), label = "predicted effect of variant")
ax4.set_xlabel("predicted effect")
ax4.set_xticklabels(anndict.keys(), rotation=90)

plt.tight_layout()

plt.show()    
