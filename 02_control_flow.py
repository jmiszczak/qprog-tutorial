from pyquil.api import QVMConnection
from pyquil.quil import Program
from pyquil.gates import H, X, I, CNOT

import numpy as np

qvm = QVMConnection() # use the simulator
pr = 0 # we use quantum coins to make decisions
ar = 1 # the second register is for actual game
cregs = [ar, pr] # our classical registers

dec0 = Program(X(ar)) # flip
dec1 = Program(I(ar)) # do nothing

prog = Program()
prog.inst(X(ar))#, H(pr)) # initialize to heads
prog.inst(H(pr)) # for decision making
prog.inst(H(ar)) # flip
prog.measure(pr, pr)
prog.if_then(pr, dec1, dec0)
prog.inst(H(ar)) # undo the flip
prog.measure(ar,ar)

print(qvm.wavefunction(prog))

res = qvm.run(prog, cregs, trials = 10)
print(res)
