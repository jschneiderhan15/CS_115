from importlib import reload as Rfrsh
import hmmm

# Name: Jack Schneiderhan
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1 ■■■ f(5) = 5 ■■■ f(9) = 34
RecFibSeq = """ # You may not need all lines
00 setn r15 42
01 read r1
02 setn r2 1
03 calln r14 6
04 write r4
05 halt
06 jnezn r1 09
07 setn r13 0
08 jumpr r14
09 pushr r1 r15
10 pushr r14 r15
11 addn r1 -1
12 calln r14 6
13 add r13 r4 r2
14 copy r4 r2
15 copy r2 r13
16 popr r14 r15
17 popr r1 r15
18 jumpr r14
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = False

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
