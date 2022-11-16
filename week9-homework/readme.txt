readme for assignment 8 week 9 Bulk RNA-seq

If there is no relationship between fpkm and developmental stage, you would expect each p value to have the same chance of occurring as any other p value. therefore, under the null hypothesis, the distribution would be uniform.

Multiple testing corrections: Each gene is tested 1 time, say you have 1000 genes. Say you know that there are 10 that do have a relationship to y. if your p value is 0.05, that means you’ll get 50 false positives. So, false discovery rate is 5/6 (50 false, 10 true, 60 total, 50/60 are false). This is high. If you want to lower it, meaning you would identify fewer false positives, you would need to lower the p-value that is considered significant. One way to do this is to divide the original pvalue by the number of tests--> 0.05/1000 = 0.00005. This would mean that you would get 0.05 false positives (so 0 false positives), which would make the FDR 0.05/10, which would be 0.005, essentially 0. 


without correction:
FBtr0078736' 'FBtr0081712' 'FBtr0082279' 'FBtr0082570' 'FBtr0082648'
 'FBtr0082668' 'FBtr0082980' 'FBtr0337054' 'FBtr0083541' 'FBtr0083616'
 'FBtr0083847' 'FBtr0085754' 'FBtr0072872' 'FBtr0300240' 'FBtr0073347'
 'FBtr0077157' 'FBtr0077112' 'FBtr0076706' 'FBtr0076585' 'FBtr0076011'
 'FBtr0075819' 'FBtr0333035' 'FBtr0333034' 'FBtr0075605' 'FBtr0075603'
 'FBtr0075101' 'FBtr0075112' 'FBtr0074940' 'FBtr0074946' 'FBtr0347089'
 'FBtr0345797' 'FBtr0088944' 'FBtr0088683' 'FBtr0087676' 'FBtr0087632'
 'FBtr0345792' 'FBtr0345793' 'FBtr0086745' 'FBtr0071834' 'FBtr0343014'
 'FBtr0071924' 'FBtr0330249' 'FBtr0072163' 'FBtr0072317' 'FBtr0070141'
 'FBtr0070368' 'FBtr0345714' 'FBtr0337067' 'FBtr0337066' 'FBtr0070634'
 'FBtr0070749' 'FBtr0071038' 'FBtr0071032' 'FBtr0345908' 'FBtr0071048'
 'FBtr0345982' 'FBtr0071143' 'FBtr0073675' 'FBtr0343649' 'FBtr0073763'
 'FBtr0073817' 'FBtr0074066' 'FBtr0074453' 'FBtr0078074' 'FBtr0077903'
 'FBtr0077832' 'FBtr0079052' 'FBtr0114511' 'FBtr0079253' 'FBtr0343161'
 'FBtr0079330' 'FBtr0079403' 'FBtr0079900' 'FBtr0079960' 'FBtr0080193'
 'FBtr0329904' 'FBtr0080306' 'FBtr0303164' 'FBtr0336864' 'FBtr0080845'
 'FBtr0080835' 'FBtr030324'
 
with correction:
'FBtr0078736' 'FBtr0082570' 'FBtr0083541' 'FBtr0083847' 'FBtr0085754'
 'FBtr0073317' 'FBtr0077157' 'FBtr0076706' 'FBtr0076585' 'FBtr0076011'
 'FBtr0333034' 'FBtr0075101' 'FBtr0075112' 'FBtr0074940' 'FBtr0074946'
 'FBtr0299876' 'FBtr0078549' 'FBtr0345797' 'FBtr0087676' 'FBtr0086745'
 'FBtr0071834' 'FBtr0343014' 'FBtr0071924' 'FBtr0330249' 'FBtr0072163'
 'FBtr0345982' 'FBtr0071143' 'FBtr0073922' 'FBtr0074066' 'FBtr0074453'
 'FBtr0078074' 'FBtr0077903' 'FBtr0077832' 'FBtr0114511' 'FBtr0079403'
 'FBtr0080193' 'FBtr0080306' 'FBtr0080398' 'FBtr0080845' 'FBtr0303249'
 
 
 percent overlap: 48.78% using my correction method.