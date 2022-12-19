Great work! This is almost done, just a couple of minor comments:

1. I need your commands for Question 3C (-0.5 point)
2. For Step 3/Question 4A, I like what you're going for but I don't think it's working quite the way you intended. In your while loop, you're grepping for `p` instead of for `$p`. Which means you're just trying to find contigs with the letter "p" in the taxonomy somewhere. If you want to loop through the contig names, you can do something like `for contig in $(grep ">" bin.1.fa); do ...; done` (-1 point)

Good job so far!

(8.5/10)
