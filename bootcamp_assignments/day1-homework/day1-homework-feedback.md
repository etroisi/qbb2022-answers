Great work! A few notes: 

Exercise 1: 

You write that: "Error message means that awk does not accept nuc, because nuc is a bash command". This is really close. What's actually happening is that when awk sees a dollar sign, it is looking for a column/field number. So when awk sees `$nuc`, it's looking for the nuc-th column, which ofc makes no sense to the computer. Hence the error. 

Your use of -v to correctly bring in the variable into awk is great! 

Exercise 3:

This is *really* close. You get the right number of variants (10,293). 

For getting the number of genes, you use the following code: 

`cut -f 7 variantsgenes.bed | uniq -c > variantsgenes2.bed`

This gets you 731 unique genes, which is an overestimate – there are still some duplicate genes. There's something you need to do to the file after cutting out field 7, but before sorting so that you can ensure that you genuinely only get unique gene names. Can you please try modifying this line of code so that you get the count of unique genes? (Expect to see approximately 200 genes if all works well).

- Andrew 
