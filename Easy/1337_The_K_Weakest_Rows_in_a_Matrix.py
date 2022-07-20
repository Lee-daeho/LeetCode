###The K Weakeast Rows in a Matrix 22/7/21###

##mysolution
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    dt = {}
    for i in range(len(mat)):
        dt[i] = sum(mat[i])  # key: row, value: soldiers

    return list(dict(sorted(dt.items(), key=lambda item: item[1])).keys())[:k]



##solution using heap
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    minHeap=[]
    ans=[]
    heapq.heapify(minHeap)
    for row in range(len(mat)):
        soldiers=mat[row].count(1)
        heapq.heappush(minHeap,(soldiers,row))
    while k!=0:
        val,row=heapq.heappop(minHeap)
        ans.append(row)
        k-=1
    return ans

###another solution
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    rows = sorted(range(m), key=lambda i: (mat[i], i))
    del rows[k:]
    return rows

##one line solution
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

