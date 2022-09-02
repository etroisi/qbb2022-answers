import sys #tell python to use sys
filename = sys.argv[1] #tell python to refer to command line for info about file and how many lines the user wants it to read so that this info isn't hardcoded
n_lines = int(sys.argv[2]) #later on when i tell python i want it to consider a specific number of lines ("n_lines"), this step tells python to use the number of lines specified in the command line by user as well as makes it clear that that number is an integer
mylist = [] #tell python i want to make a list (to make sure the number of lines of a file is specific to the file and not hardcoded, make a list of all the lines in said file so the list contains all the lines of that file, no matter how long)(had some assistance for this part)
for i, line in enumerate(open(filename)): #define what i want the list to contain (number of lines in specified file)("i" is the lines it is going to print)(enumerate indicates that the actual line number is relevant)
    mylist.append(line) #actually add those lines to the list, use the for loop to add every line to the list
len(mylist) #define the length of the list as the number of lines in the list (you can print in the next line to double check if the length is what is expected)(this is important because it makes it so the code works for a file with any number of lines)
n = len(mylist) #i want to tell python to apply some parameters to what it prints. to do that, i have to tell it what to consider for "n"--the number of lines
for i, line in enumerate(mylist): #telling python i want it to do a for loop, specifically using lines from the list i just created
    if i >= n - n_lines and i < n: #specifically, i want it to look for lines that are greater than the total number of lines - 5 but less than the total number of lines
        print(line.strip('\r\n')) #print those lines please
    