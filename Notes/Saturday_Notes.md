# Saturday Notes 

*19AUG23 @ 1700 (Germany Time)*

Main Instructor: Shannon Landin  
Tech Guy: Gil  
PY4E instructor: Juan  

## From Juan's Notes

I hope everyone is doing well and getting started with this week’s exciting new topics in Python. First, this week we will have office hours as originally scheduled (Tuesday & Thursday, 7pm-9pm ET), 

- but starting next week, I’ll host **office hours Tuesday & Thursday 12pm-2pm ET** based on feedback from last class. 
  
As always, feel free to message me if you’d like to meet but can’t make it to those office hours.

- Last class we covered exercises in **lessons 4, 7, 9, 10, and 11**

There are multiple ways achieve the same outcome in programming. **"Pythonic"** code (also known as **"idiomatic"** code in other languages) refers to the most conventional way to code common patterns, such as how to loop through a list.
Guard clauses are a way of organizing your code to prevent deep indentation.
There are performance implications to the decisions we make in code. Some algorithms are simply more efficient than others, but most algorithms make a balance between readability, speed, and memory. We touched briefly on online/offline algorithms and time complexity.
Testing your assignment code,
You can use 'python3 -i assignment.py' in the terminal to run code in interactive mode, test your functions, and exit using `exit()`
Interacting with your terminal,
Press up arrow to re-use previously entered commands and tab to autocomplete
Use ‘ls’ to see your current folder contents, ‘cd’ to enter a folder, and ‘cd ..’ to exit a folder
Use ‘man’ to see the manual for different commands. E.g. ‘man cd’ will show the manual for the ‘cd’ command
And coding on your local machine
Using codespaces is perfectly fine for current exercises but if you’d like to use a different editor or work offline, you can use ‘git clone GITHUB_URL_HERE’ in the terminal to download a github repository to a folder on your computer. (Note: if you are on Windows and want to access the same type of terminal as used on codespaces, an easy way is to download Ubuntu directly from the Microsoft Store on your computer.)
This week you should:
Look out for announcements and to-dos on Google Classroom
Go through lessons 10 through 16 of the Python for Everybody course and record your progress on Jira.
and if anything visit office hours or contact me to schedule office hours at a different time
Next class we will meet to review lessons 10 through 16 and preview the next section which is IT Automation with Python.

I wish you all the best, reach me if anything on Google Classroom or juan@codecraftworks.com, and I'll see you next time.

```py
for line in fh:
# N lines in the file, M characters in each line
# Time: O(N * M)
# Space: O(M)
    do something...
```

```py
fstr = fh.read()
# N lines in the file, M characters in each line
# Time: O(N/2)
# Space: O(N)
```

Terminal 

- echo "mbox-short.txt" | py ex_0_0

1300 - 1400 break
