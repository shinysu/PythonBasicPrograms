fp=open("file2.txt","w")#open a file2 in write mode
fp1=open("file1","r")#open a file1 in read mode
reading_file=fp1.read() #Read contents of a first file, store it in a string
fp.write(reading_file)#Write the string to second file
