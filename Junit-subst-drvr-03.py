#! /usr/sbin/python
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#  C:\Python27\pdv\201305-CodeJam\Junit-subst-drvr-03.py
#  
#  LAME, but the best I can do right now: Use a degenerate version of the code
#  framework for my junit-style test driver.
#   This test validates diagonal check left to right - expected output is:
#         Case #1: 
#         Case #2: 
#         Case #3: 
#         Case #4: 
#         Case #5:
#         Case #6: O won
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
#-----------.
#           |  Code under test starts here 
# vvvvvvvvv v vv v vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            if (not winnerFound):
                winAry = copy.deepcopy(scorAry)   # copy scorAry 'cuz the function affects it
                reslt = diagnLeft2Rt(winAry)
                if (reslt==4):
                    winnerFound = 1 
                    print ('Case #%d: X won' % (caseCntr))
                elif (reslt== -4):
                    winnerFound = 1 
                    print ('Case #%d: O won' % (caseCntr))            
# ^^^^^^^^^ A ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#           |  Code under test ends here 
#-----------'
            if (not winnerFound):                      #<--UNIT_ARTIF
                print ('Case #%d: ' % (caseCntr))      #<--UNIT_ARTIF

#---.
#   |  Code under test starts here 
#vv v vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def diagnLeft2Rt(winAry):
    """ Form a 'winner check total' in a 'diagonal' dimension
        [0][0] + [1][1] + [2][2] + [3][3] in the scoring array
        If 'T' is encountered set its value before forming the total """
    totl = 0 
    if (winAry[0][0]==10):
        winAry[0][0] = winAry[1][1]
    for x in range(0,4):
        if (winAry[x][x]==10):
            winAry[x][x] = winAry[x-1][x-1]
        totl = totl + winAry[x][x]
    return totl
#^^ A ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   |  Code under test ends here 
#---'

def usage():
    """ print help information """
    sys.stderr.write('usage: ' + 'python ' + sys.argv[0] +\
        ' <input-file-spec>\n')
    sys.stderr.write('       '+\
        'Recognizes Tic-Tac-Toe-Toemek game completion (Google CodeJam2013)\n')
    sys.stderr.write('       '+ '(Use file redirection to make outp file)\n')
 
 
if __name__ == '__main__':
    main()