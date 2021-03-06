# Using Python to Interact with the Operating System - Week 2

## Reading and Writing Files
### Programming with Files
File systems are usually organized in a __tree structure__ with directories and files nested under their parents.
* A relative paths use only a portion of a path to show where the resource is located in relation to the current working directory.
* An absolute path is a full path to the resource in the file system.

### Reading Files
When processing large chunks of data, it's a good idea to read that data from files.
* **readline method** reads a single line of a file and updates the current position in the file.
* **read method** reads from the current position until the end of the file instead of just one line.

The *open-use-close pattern* is a typical way of working with files in most programming languages. It's a good idea to close files after you've opened them for a few reasons.
1. When a file is opening a script, the file system usually lock it down and so no other programs or scripts can use it until it is closed.
2. There's a limited number of file descriptors that can be creates before file system runs out of them.
3. Leaving open files hanging around can lead to race conditions which occur when multiple processes try to modify and read from one resource at the same time and can cause unexpected behavior.

In Python, **file descriptor** is stored as an __attribute__ of the files object. This is a token generated by the OS that allows programs to do more operations with the file.

the "with" keyword creates a block of code with the code to be excuted inside of it. When we use a "with" block, __Python will automatically close the file__

The open-use-close approach vs. the "with" approach
* Using a "with" block is a good way to open and work on a single file then have the file automatically closed at the end of the block.
* Using open outside of a block means we can use a file object in other places in our code. So we're not restricted to just one single block. But when taking this approach, we need to remember to close it when we're finished.

### Iterating through Files
There are 2 ways to iterate a file object:
1. Iterate the file object like list or strings
2. Iterates the file object by reading the file lines into a list
    * When Python reads the file line by line, the line variable will always have a new line character at the end

The file has a new line character at the end of each line.
* Empty lines can be avoided by using strip method.

Python uses backlashes to display some of special symbols or operations:
* A newline character is displayed using "\n" symbol when printing a list of strings.
* 'tab' is displayed using \t.
* A single or double quote can be displayed using backlashes as well.

Be careful when reading the entire contents of a file into a variable of our programs:
If the file is large, it can take a lot of computer's memory to hold it, which can lead to poor performance. If a file is just a few kilobytes, it's more efficient to process it line by line.

### Writing Files
File objects can be opened in several different modes. A mode is similar to a file permission. It governs what can be done with the file.

| Character | Meaning |
|:-:|:-:|
| r | open for reading (default) |
| w | open for writing, truncating the file first |
| x | open for exclusive creation, failing if the file already exists |
| a | open for writing, appending to the end of the file if it exists |
| b | binary mode |
| t | text mode (default) |
| + | open for updating (reading and writing) |

---

## Managing Files and Directories
### Working with Files
**os module** provides a layer of abstraction between Python and the operating system which allows us to interact with the underlying system without us knowing whether we're working on a Windows, Mac, Linux, or any other operating system supported by Python.

Some of the functions available from the os module are: 
* remove function deletes a file
    * Trying to remove the file that doesn't exist, the function will raise an error.
* exists function checks whether a file exist
* rename function changes name of a file
    * The first parameter to rename function is the old name of the file and the second is new name.

### More File Informations
* getsize checks a file size and returns the file size in bytes.
* getmitime checks when the file was last modified and returns Unix timestamp.
* abspath function takes a filename and turns it into an absolute path.

**datetime module** provides a function to convert the Unix timestamp.

---

## Reading and Writing CSV Files


---
CSV Files Cheat Sheet
Check out the following links for more information:

https://docs.python.org/3/library/csv.html

https://realpython.com/python-csv/
