# Feedback day2-lunch

Overall, this looks great. I think you could use slightly fewer comments or compile them into blocks explaining multiple lines of code on their own line. This would make the code a little more readable. But that's just stylistic. The code itself appears to be functional and accomplish all that it was supposed to. I like how you use the entries in `field_types` for fields 9, 11, and  12 to hold the type for each nested list element. I think the only real comment I have is that there is lots of redundancy in how you handle the 3 complex fields. You split them all twice. You could store the results of the initial split in `fields` and then perform type conversion in the for loop. This would leave a single redundant type conversion of field 10 for the list length checks. Just food for thought for faster code. You seem to really get the concepts for this assignment. Great job and keep it up!