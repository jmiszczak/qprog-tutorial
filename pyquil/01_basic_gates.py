from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE

qvm = get_qc('2q-qvm')  # connect to QVM with 2 quibts
prg = Program() # build the program
out = prg.declare('ro', 'BIT', 2) # declare classical memeory

# construct the code
prg += H(0)
prg += CNOT(0, 1)
prg += MEASURE(0, out[0])
print(prg)

# construct the intermediate representation
exe = qvm.compile(prg)
print(exe.program)

# run the code
res = qvm.run(exe)
print(res)