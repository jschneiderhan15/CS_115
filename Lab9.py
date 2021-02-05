# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Jack Schneiderhan
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System
# Purpose : Writing a few hmmm functions to understand how this stuff works
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3 r1 r2
03 jgtzn r3 5
04 jltzn r3 7
05 write r1
06 halt
07 write r2
08 halt
"""

# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 ≥ 0
Power = """
00 read r1
01 read r2
02 setn r3 1
03 sub r2 r2 r3
04 copy r4 r1
05 mul r4 r4 r1
06 sub r2 r2 r3
07 jnezn r2 5
08 write r4
09 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 ≥ 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 jeqzn r1 9
02 setn r2 1
03 setn r5 1
04 add r3 r4 r2
05 copy r4 r2
06 copy r2 r3
07 sub r1 r1 r5
08 jnezn r1 03
09 write r4
10 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


