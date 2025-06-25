#!/sur/bin/env python3
import sys
if len(sys.argv) != 2:
    print("None")
else:
    u_ipt= input("What was the parameter? ")
    if u_ipt == sys.argv[1]:
        print("Good Job! ")
    else:
        print("Nope, Sorry...")