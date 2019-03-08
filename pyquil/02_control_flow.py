from pyquil import Program, get_qc
from pyquil.gates import H, X, I, CNOT
import numpy as np

qvm = get_qc('2q-qmv') # use the QVM simulator, 2 qubits
prg = Program() # main program
cond = prg.declare('ro', 'BIT', 1) # classical memory for condition

pr = 0 # we use quantum coins to make decisions
ar = 1 # the second register is for actual game

# two branches
dec0 = Program(X(ar)) # flip
dec1 = Program(I(ar)) # do nothing

# construct the main program
prg.inst(X(ar)) # initialize to heads
prg.inst(H(pr)) # for decision making

# make the decision
prg.measure(pr, out).if_then(out, dec1, dec0)

exe = qvm.compile(prg)
res = qvm.run(exe)
print(res)
