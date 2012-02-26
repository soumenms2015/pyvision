from vision import cluster

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cluster.setup('quickstep')

while True:
    token, problem, _ = cluster.getproblem()
    result = isprime(problem[0])
    cluster.solveproblem(token, result)