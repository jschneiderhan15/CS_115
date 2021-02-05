# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name     : Jack Schneiderhan
# Pledge   : I pledge my honor that I have abided by the Stevens Honor System. 
# Purpose  : To use hmmm RECURSIVELY 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Power:
#  - Write a RECURSIVE hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  - Assumptions: No.1 is any integer, No.2 ≥ 0
#  - 0 ^ 0 can either be 0 or 1.
#  - Your function MUST be recursive.
#   No points will be given for solutions that
#   do not use the hmmm recursive/stack structure
#   See week9.pdf for more insight into that.
Power = """
00 setn r15 50
01 read r1
02 read r2
03 calln r14 6
04 write r13
05 halt
06 jnezn r2 9
07 setn r13 1
08 jumpr r14
09 pushr r1 r15
10 pushr r14 r15
11 addn r2 -1
12 calln r14 6
13 popr r14 r15
14 popr r1 r15
15 mul r13 r13 r1
16 jumpr r14
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Power  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()
