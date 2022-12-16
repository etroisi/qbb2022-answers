# Week 1 Genome Assembly -- Feedback

1 + 0.75 + 0 + 0 + 0 + 1 + 1 + 0.33 + 0 + 0 = 4.08 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * good code, but it only is set up for the first question with 5x coverage. You can use sys.argv to pass the number of reads/coverage as an input argument or copy/paste your code and in the second code block increase the number of reads for 15x coverage --> +0.75

3. Question 1.2, 1.4 plotting script(s)

  * I don't see code for plotting --> +0

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * I don't see the plots; please add --> +0

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * don't see answers or code for this --> +0

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> don't see this answer + 0
  * how many insertions and deletions in assembly --> don't see this answer + 0

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> don't see this answer + 0
  * length of novel insertion --> don't see this answer + 0

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> don't see this answer + 0
  * secret message --> don't see this answer + 0


REGRADE 12/16/2023 -- Dylan

Great work getting this finished up! You addressed most of the points Kate made, but there are minor issues with the last part of the actual alignment.

1. Question 1.2, 1,4
 * Looks like you have the plots and code for both low and high coverage +2.25
2. Question 1.3, 1.4
 * I see your answer and code! +1
3. whole genome alignment
 * I see the longest alignment and the number of insertions and deletions +0.66
4. decoding the insertion
 * I have your answer for the position of the insertion, but I don't see your code. This is somewhat important as I'm not entirely sure the position lines up with what I was expecting (+0.25)
 * I have your answer for the length of the insertion, but it should be one base longer (maybe you accidently didn't include the end position in the calculation?) +0.5
5. Decoding the insertion cont
 * Your samtools faidx command is a little funky, as the positions you got from the previous section don't match the position your have here... +0.25
 * You did the right command, but given that the length and position of your insertion were a little funky, I'm not surprised you didn't get the correct decoded message +0.5

Overall, great work. Just make sure you that you're really clear with the commands you used. One minor comment: you put your code and answers in a `.py` file. That file ending is typically reserved for python files, and so it's not really correct to put plain text and bash commands in these files. We reccommend putting code and text in Markdown files, ending in `.md`, like `README.md`. There are a lot of tools that will actually render markdown files to be clearer to read as well.

Regrade: 9.5/10
