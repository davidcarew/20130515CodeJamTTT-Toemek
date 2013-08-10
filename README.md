20130515CodeJamTTT-Toemek
=========================

Proficiency Practice Python CodeJam 2013 problem.  Nothing of interest. 
Attempting to learn to use GitHub

         1         2         3         4         5         6         7         8
12345678901234567890123456789012345678901234567890123456789012345678901234567890
                                 Project Notes

                 Google Code Jam -- Practice in Python Problems
                 
Problem A. Tic-Tac-Toe-Tomek
See: 
https://code.google.com/codejam/contest/2270488/dashboard

...For a problem stmt. 

I have put small sample input file into the GitHub repository:
a-small-practice.in

BELOW is my 'stream-of-development' project notes: 

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
--------------------------------------------------
For Anyone foolish enough to 'pull' this from GitHub (pointless tho'
that is), here is a bit of README-style user notes:

clone the repository. then set up python (2.7- this is not modern Python!)
in your path so that you can run from the clone directory.  Then the command:

python TTT-Toemek.py a-small-practice.in

... produces correct output from the CodeJam dashboard-specified small input
I have also included the "large input file" -- 1000 games. 
My code seems to process the large file OK -- my sample spot checks 
seem to validate correctness. 

HOWEVER I have *NOT* actually submitted either large or small output to 
CodeJam for "points"- presumably CodeJam would validate the large output
in some way.  I have *also* included 'j-unit' style tests for individual 
parts of the final TTT-Toemek.py "recognizer algorithm" code.

I was attempting to do 'TDD' (test driven development), but my "test 
framework" simply cloned the initialization and framework of the 
TTT-Toemek.py program itself-- calling out the recognizer code under
test with comments.  This is lame but the tests could still serve if I were
to (for example) modify the recognizer to NOT change the scoring array, a
potential optimization I considered. And of course it did serve my initial
development. 