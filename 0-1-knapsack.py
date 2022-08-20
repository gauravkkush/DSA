def knapSack(K, P, V, N):
    if N == 0 or K == 0 :
        return 0
    if (P[N-1] > K):
        return knapSack(K, P, V, N-1)
    else:
        return max(V[N-1] + knapSack(K-P[N-1], P, V, N-1), knapSack(K, P, V, N-1))
        
N, K = map(int, input().split())
P = list(map(int, input().split()))
V = list(map(int, input().split()))
print (knapSack(K, P, V, N))