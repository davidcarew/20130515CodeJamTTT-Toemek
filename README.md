20130515CodeJamTTT-Toemek
=========================

Proficiency Practice Python CodeJam 2013 problem.  Nothing of interest. 
Attempting to learn to use GitHub

         1         2         3         4         5         6         7         8
12345678901234567890123456789012345678901234567890123456789012345678901234567890
                                 Project Notes

                 Google Code Jam -- Practice in Python Problems
                 
Problem A. Tic-Tac-Toe-Tomek

https://code.google.com/codejam/contest/2270488/dashboard

For a problem stmt. 
I have put small sample input file into: 

file://C:\Python27\pdv\201305-CodeJam\TTToe-T-prjNotes.txt

Classic first step: use console-cmdline template to open and 'null proc' the
input

Then make the code "slurp" all the games and store each as a 
set of 4 strings in a gameList 'quasi' array
Then for games in gamelist
        form an array w numeric scores for for ea char in the input
        Call 10 chk-dimension functions
        After each call declare Winner IF score is +4 OR -4
              and continue to next game
        OTW (after all 10 checks)
            count zeros in array
            if none Call Cat's game
            ELSE 
                  Call incomplete game
See python code comments for scoring algor. details. 

Progress-- recognizer is flaggy and the flags are wrong

July 2013 - problem actually had to do with Python call-by-reference. 
The win evaluation functions were corrupting the scoring array-- I
coded it as though passing the scoring array made a copy of it-- not
so, of course. Quick fix was to import copy and use copy.deepcopy()
to preserve a copy of the scoring array. 

This was a good learning exercise, but took me way too long to debug. 
That is what I get for using pure procedural code-- OO w/h/been better.

OTOH learning how to "do it right" using "new-style" Python OO would 
probably take me approximately forever... I did not even know that 
Python had a "new style" OO (base class is an object) versus the old
style OO "classic classes"... (?!) 

AND OF COURSE--*that* is what I should do, now--i.e. re-write the same
basic solution (same recognizer design) using Classes and objects...

Someday... 
