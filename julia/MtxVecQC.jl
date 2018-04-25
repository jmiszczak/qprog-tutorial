# base vectors for one qubit
k0 = [1; 0];
k1 = [0; 1];

# projectors
proj = a->kron(conj(transpose(a)), a);

# some one-qubit matrices
id = [1 0; 0 1];
sx = [0 1; 1 0];
h = 1/sqrt(2)*[1 1; 1 -1];

# controlled not operation
cnot = kron(proj(k0), id) + kron(proj(k1), sx);

print("File ", @__FILE__, " loaded.\n")
