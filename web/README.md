Run ./bin/runner to run it. You might have to cd into bin and run chmod +x runner to give it permission to run.


requirements.txt downloads extra stuff because I refactored an EECS485 project, but it should work. (I'll remove the extra stuff later)

Currently it should refresh if it is not given a valid link or errors in some way, and changes to the result page, it'll print a number. 
If you check your console you will see it printed a python array of the words it found.
Check views/index.py to see where this occurs. 
