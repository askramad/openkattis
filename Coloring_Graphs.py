def R(): return map(int, raw_input().split())

n = R()[0]
adj = [R() for i in range(n)]

for i in range(n):
    assert all(i in adj[j] for j in adj[i])

maxColors = max(map(len, adj)) + 1
for k in range(2, maxColors + 1):
    allcolors = set(range(k))

    def color(C):
        v = next((i for i in range(n) if C[i] == None), -1)
        if v == -1:
            return True

        colorsleft = allcolors - set(C[vv] for vv in adj[v] if C[vv] != None)
        for c in colorsleft:
            C[v] = c
            if color(C):
                return True
            C[v] = None

        return False

    initial = [None] * n
    initial[0] = 0
    initial[adj[0][0]] = 1
    if color(initial):
        break

print k
