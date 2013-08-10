#! /usr/sbin/python
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#  C:\Python27\pdv\201305-CodeJam\Junit-subst-drvr-00.py
#  
#  LAME, but the best I can do right now: Use a degenerate version of the code
#  framework for my junit-style test driver.
#   
#  This unit test calculates and prints out the scoring array.  Array should 
#  match the input per the specif (see comments)of "How my recognizer works"
#  in the contest code (i.e. TTT-Toemek.py)
#  
#
#    DATE       WHO     DESCRIPTION
#    =========  ======= =======================================================
#    2013 May   Carew   created
#                       
#------------------------------------------------------------------------------
#TODO:
# 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
import getopt
import copy

def main():
    """  """
    # init and process cmd line args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "")
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    if len(args) == 0: 
        # print help information and exit:
        usage()
        sys.exit(2)       
    if args[0] in ('?','help','Help','HELP'):
        # print help information and exit:
        usage()
        sys.exit(2)
    try:
        opnfile = args[0]
        infile = open (opnfile, "r")
    except:
        print "error attempting to open " + args[0]
        print
        usage()
        sys.exit(2)
    # framework under test starts here
    # Process input file
    caseCntr = 0    
    row = 0    
    records = ''
    caseInstance = ['','','','']
    # init a fake 2D 'array'=list of lists, all zeroes
    scorAry = []
    for i in range(0,4):
      x = []
      for j in range(0,4):
        x.append(0)
      scorAry.append(x)
    # flags below (ugly)  
    skipHd = 1 
    opnPositnsFound = 0
    winnerFound = 0

    for records in infile:
        if skipHd:
            skipHd = 0
            continue
        if len(records) < 4:
            continue
        caseInstance[row] = records
        opnPositnsFound = 0    
        for i in range(0,4):
            if   records[i] == '.':
                scorAry[row][i] = 0
                opnPositnsFound += 1
            elif records[i] == 'X':
                scorAry[row][i] = 1
            elif records[i] == 'O':
                scorAry[row][i] = -1
            elif records[i] == 'T':
                scorAry[row][i] = 10
        row = row + 1
        if row > 3:
            row = 0
            winnerFound = 0
            caseCntr = caseCntr + 1
            print ('Case #%d: ' % (caseCntr))      #<--UNIT_ARTIF
            winAry = copy.deepcopy(scorAry)        # duplicate the array because we will corrupt it
            for x in range(0,4):                   #<--UNIT_ARTIF
                print winAry[x]                    #<--UNIT_ARTIF
def usage():
    """ print help information """
    sys.stderr.write('usage: ' + 'python ' + sys.argv[0] +\
        ' <input-file-spec>\n')
    sys.stderr.write('       '+\
        'Recognizes Tic-Tac-Toe-Toemek game completion (Google CodeJam2013)\n')
    sys.stderr.write('       '+ '(Use file redirection to make outp file)\n')
 
 
if __name__ == '__main__':
    main()