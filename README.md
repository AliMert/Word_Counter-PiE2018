# Word_Counter-PiE2018

This is the first assignment of the "Python in the Enterprise Lab." course.

The project is my own implementation of the (well known) Linux program WC (Word Counter).

Like in WC, this program allows to count words,lines, and characters of a given text.

There are three functions :

**count_chars(String data)**

**count_words(String data)**

**count_lines(String data)**


- After changing directory to project’s directory, project can be executed with the following commands : 

**python wc.py -h**

**python wc.py -wc \<directoryOfTheFile\>**\n
**python wc.py -lc \<directoryOfTheFile\>**

**python wc.py -cc \<directoryOfTheFile\>**

- For a quick test you can also use “testFile.txt”:

**python wc.py -wc testFile.txt**

**python wc.py -lc testFile.txt**

**python wc.py -cc testFile.txt**
