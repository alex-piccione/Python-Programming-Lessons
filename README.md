# Python-Programming-Lessons
Python programming lessons for beginners


# Topics

- Kata "Best travel"
- Take this blog post as an idea, https://blog.teowaki.com/2016/07/21/fun-with-theresa-mays-first-speech-as-mp-and-the-google-cloud-speech-and-natural-language-apis/, it is about Google Speech API.

# How to run the code

main.py: this is our "program"
test.py: this is the test that prove that the program works (or fail)

Both "main.py" and "test.py" can be runned.
If you run "main.py" it just execute the main() program that show ""

## PyCharm

(not immediate to set)
To "run" something you need to configure it in the "Configurations".
Both "main.py" and "test.py" can be run.
If you run "main.py" it just execute the main() prgram showing the wecome text and "Press any key to close".
If you run the test.py it executes all the test cases and esturn he result in the output console.

You have to create a configuration for "Python" and select "test.py" for 
tu run the test.py 

## Visual Studio Code

(super simple)
1. from the menu use the _open folder_ comand and select he path of your local project (the directory that contains _main.py_).
2. open _main.py_ or _test.py_
3. Press _F5_ (it is usually the shortcut for _run debug_)

## FAQ

Q. SourceTree returns an error when I try to commit/push my local changes.
A. Usually it happens because on the remote repository there are changes one one or more files that you have changed also locally.
   Because two different version cannot exists a "merge" of the changes should be done.
   This operation is called "Resolve Conflicts" and permits to select line by line (where the 2 files are different) if take the line of code from the file A or from the file B, or both.
   Another way to avoid conflict is to "revert" (or "discard" or "undo") all or part of the changes done. Sometime we have changes that we haven't done intentionally or that we want to cancel.
   It is possible to mix both the 2 ways to solve the conflicts: merge some files (resolve the conflicts choosing wich line will be selected for the final version) and delete some changes.