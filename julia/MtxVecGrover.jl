# flat superposition on one qubit
sp = h*k0

# version for 2 qubit

needle2 = kron(k1,k1)
oracle2 = kron(id,id) - 2*proj(needle2)
diffuse2 = -1*(kron(id,id) - 2*proj(kron(sp,sp)))

# version for 3 qubits

needle3 = kron(k1,k1,k1)
oracle3 = kron(id,id,id) - 2*proj(needle3)
diffuse3 = -1*(kron(id,id,id) - 2*proj(kron(sp,sp,sp)))

# version for n qubits

needle(n) = foldl(kron,k1,[k1 for i in 1:n-1])
oracle(n) = foldl(kron,id,[id for i in 1:n-1]) - 2*proj(needle(n))
diffuse(n) = -1*(foldl(kron,id,[id for i in 1:n-1]) - 2*proj(foldl(kron,sp,[sp for i in 1:n-1])))

# some examples

testGrover(n,i) = grover(n)^i*groverInit(n);
testGrover(n) = grover(n)^Int(floor(sqrt(2^n)))*groverInit(n);
testGroverProbs(n,i) = map(x->abs(x)^2, testGrover(n,i));
testGroverProbs(n) = map(x->abs(x)^2, testGrover(n));

print("File ", @__FILE__, " loaded.\n")
