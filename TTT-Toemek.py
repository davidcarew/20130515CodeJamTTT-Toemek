#! /usr/sbin/python
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#  C:\Python27\pdv\201305-CodeJam\TTT-Toemek.py
#  
#  This prg is based on Google Code Jam practice prob:
#     https://code.google.com/codejam/contest/2270488/dashboard  
#  It does not play TTT-Toemek.  It just recognizes winner or cat's game, or 
#  whether the game is still in progress.  Particular input is specified. 
#  Particular output is required. 
#    
#
#    DATE       WHO     DESCRIPTION
#    =========  ======= =======================================================
#    2013 May   Carew   created
#    2013 Jul   Carew   finished initial d.bug-- small-input-sample.txt passes
#                       
#------------------------------------------------------------------------------
#TODO:
#  Jul 5
#  Need to run it on "large" input. Also, could eliminate copy.deepcopy of the
#  scoring array-- ea function could remember modif's for 'T' and restore orig
#  value-- this would be faster than using copy.deepcopy, though the logic w/b
#  even more "flag-gy" and obscure. 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
import getopt
import copy

def main():
    """  """
    # init
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
            # check for winner across 'vertical' dimensions (4 checks)
            for dim in range(0,4):
                if (winnerFound): 
                    break
                winAry = copy.deepcopy(scorAry)   # copy scorAry 'cuz the function affects it
                reslt = vertWin(winAry, dim)
                if (reslt==4):
                    winnerFound = 1 
                    print ('Case #%d: X won' % (caseCntr))
                    break
                elif (reslt== -4):
                    winnerFound = 1 
                    print ('Case #%d: O won' % (caseCntr))
                    break
            # check for winner across 'horizontal' dimensions (4 more checks)
            for dim in range(0,4):
                if (winnerFound): 
                    break
                winAry = copy.deepcopy(scorAry)   # copy scorAry 'cuz the function affects it
                reslt = horzWin(winAry, dim)
                if (reslt==4):
                    winnerFound = 1 
                    print ('Case #%d: X won' % (caseCntr))
                    break
                elif (reslt== -4):
                    winnerFound = 1 
                    print ('Case #%d: O won' % (caseCntr))
                    break
            # check diagonal dimension "left to right"
            if (not winnerFound):
                winAry = copy.deepcopy(scorAry)   # copy scorAry 'cuz the function affects it
                reslt = diagnLeft2Rt(winAry)
                if (reslt==4):
                    winnerFound = 1 
                    print ('Case #%d: X won' % (caseCntr))
                elif (reslt== -4):
                    winnerFound = 1 
                    print ('Case #%d: O won' % (caseCntr))            
            # check diagonal dimension "right to left"            
            if (not winnerFound):
                winAry = copy.deepcopy(scorAry)   # copy scorAry 'cuz the function affects it
                reslt = diagnRt2Left(winAry)
                if (reslt==4):
                    winnerFound = 1 
                    print ('Case #%d: X won' % (caseCntr))
                elif (reslt== -4):
                    winnerFound = 1 
                    print ('Case #%d: O won' % (caseCntr))            
            #Check and print for "Game has not completed" or "Draw"
            if (not winnerFound):
                if (opnPositnsFound): 
                    print ('Case #%d: Game has not completed' % (caseCntr))
                else: 
                    print ('Case #%d: Draw' % (caseCntr))
    
#end main()

#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#                                                   
#                 1 2 3 4     9              X X X T
#                 | | | |      X X X T            /
#                 V V V V       \            . . . .
#             5-->X X X T      . . . .          /
#             6-->. . . .         \          O O . .
#             7-->O O . .      O O . .        /    
#             8-->. . . .           \        . . . .
#                              . . . .     10       
#                                                                
#                             
#   Here's how my recognizer works: there are 10 checks: 4 vertical, 4 
#   horizontal, and 2 diagonal. As input is read, a scorAry of numeric values
#   is built such that arithmetic total of 4 (for X) or -4 (for O) across any 
#   check dimension indicates a win. The 'T' value is adjusted at check-
#   dimension-time NOT build-the-array-time--The 'T' value takes the value of 
#   its predecessor in the check dimension (or successor if 'T' is found first 
#   in the dimension being checked. 'T' is recognized in the scorAry by its 
#   unique value of 10, set at build time. If after all 10 checks are done and
#   no winner has been found, then game state is "Draw" if there are no zeros
#   in scorAry. OTW state is "Game has not completed".
#
def vertWin(winAry, dim2ck):
    """ Form a 'winner check total' in a 'vertical' dimension
        [0][dim2ck] + [1][dim2ck]... + [3][dim2ck] in the scoring array
        If 'T' is encountered set its value before forming the total """        
    totl = 0
    if winAry[0][dim2ck]==10:
        winAry[0][dim2ck] = winAry[1][dim2ck]
    for x in range(0,4):
        if (winAry[x][dim2ck]==10):
            winAry[x][dim2ck] = winAry[x-1][dim2ck]
        totl = totl + winAry[x][dim2ck]
    return totl

def horzWin(winAry, dim2ck):        
    """ Form a 'winner check total' in a 'horizontal' dimension
        [dim2ck][0] + [dim2ck][1]... + [dim2ck][3] in the scoring array
        If 'T' is encountered set its value before forming the total """        
    totl = 0
    if (winAry[dim2ck][0]==10):
        winAry[dim2ck][0] = winAry[dim2ck][1]
    for x in range(0,4):
        if (winAry[dim2ck][x]==10):
            totl = totl + winAry[dim2ck][x-1]
        else:
            totl = totl + winAry[dim2ck][x]
    return totl

def diagnRt2Left(winAry):
    """ Form a 'winner check total' in a 'diagonal' dimension
        [0][3] + [1][2] + [2][1] + [3][0] in the scoring array
        If 'T' is encountered set its value before forming the total """
    totl = 0
    y = 3
    if (winAry[0][3]==10):
        winAry[0][3] = winAry[1][2]
    for x in range(0,4):
        if (winAry[x][y]==10):
            winAry[x][y] = winAry[x-1][y+1]
        totl = totl + winAry[x][y]
        y = y - 1
    return totl

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
    
def usage():
    """ print help information """
    sys.stderr.write('usage: ' + 'python ' + sys.argv[0] +\
        ' <input-file-spec>\n')
    sys.stderr.write('       '+\
        'Recognizes Tic-Tac-Toe-Toemek game completion\n')
    sys.stderr.write('       '+ '(Use file redirection to make outp file)\n')


if __name__ == '__main__':
    main()