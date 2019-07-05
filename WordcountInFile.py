fname = input("Enter the file name:")
wc = 0
fp = open(fname, "w")
fp.write("My first line\n")
fp.write("This is the next line")
fp.close()
fp = open(fname, "r")
for line in fp:
    #print(line)
    word = line.split()
    wc=wc+len(word)
    #print(word)
print(wc)
