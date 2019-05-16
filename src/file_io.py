"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# this works on my Mac but this may not work on a windows machine
f = open('src/foo.txt', 'r')
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
b = open('src/bar.txt', 'w')
b.write("Too cool, I can create my own files.")
b.close()
bar = open('src/bar.txt', 'r')
print(bar.read())
bar.close()