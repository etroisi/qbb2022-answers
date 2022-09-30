Really really great start! Your needleman-wunsch implementation is almost perfect, there are just a couple of minor issues:

When you're doing traceback, you need to be using `elif` statements, otherwise it could run mulitple sections at once, which we don't want (if you look at your AA output, I think it adds some nonsense to the beginning of the alignment). Other than that, this looks great.

For completion, you need to read in the fasta, scoring matrix, gap score, and output file as inputs. You also need to print the alignment stats we asked for: num gaps in each file, and the alignment score. Because you're reading everything you need from the command line, you should only have a single script that you can use to run both the AA alignment and the DNA alignment. (-3)

Everything else looks great!

7/10
