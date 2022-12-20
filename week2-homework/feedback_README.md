Really really great start! Your needleman-wunsch implementation is almost perfect, there are just a couple of minor issues:

When you're doing traceback, you need to be using `elif` statements, otherwise it could run mulitple sections at once, which we don't want (if you look at your AA output, I think it adds some nonsense to the beginning of the alignment). Other than that, this looks great.

For completion, you need to read in the fasta, scoring matrix, gap score, and output file as inputs. You also need to print the alignment stats we asked for: num gaps in each file, and the alignment score. Because you're reading everything you need from the command line, you should only have a single script that you can use to run both the AA alignment and the DNA alignment. (-3)

Everything else looks great!

7/10

REGRADE 12/20/22 -- Dylan

This was really well done Emma! That said, there are a couple of very minor issues:
1. When you're doing traceback you should be using `elif` statements instead of `if` statements. As it stands right now, if there's a tie between any of these, you'll actually step backwards through the traceback matrix twice, and update the alignment twice. (no points deducted)
2. Secondly, your while condition is `i!=0 and j!=0`, but that will actually terminate as soon as either i or j become 0, which is not what we want if there are leading gaps. Because of this (along with the previous error), your count for the number of gaps in the DNA alignment is slightly off (-0.25)

Overall though, great work! This looks awesome.

(9.75/10)
