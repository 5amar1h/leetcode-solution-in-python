from bisect import bisect_left

class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)

        # ---- run-length encode s ----
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((int(s[i]), i, j - 1))
            i = j

        numRuns = len(runs)
        runType  = [r[0] for r in runs]
        runStart = [r[1] for r in runs]
        runEnd   = [r[2] for r in runs]
        runLen   = [e - st + 1 for (_, st, e) in runs]

        totalOnes = sum(runLen[i] for i in range(numRuns) if runType[i] == 1)

        leftZero  = [0]*numRuns
        rightZero = [0]*numRuns
        for i in range(numRuns):
            if runType[i] == 1:
                leftZero[i]  = runLen[i-1] if i-1 >= 0 else 0
                rightZero[i] = runLen[i+1] if i+1 < numRuns else 0

        Aarr     = [runLen[i] if runType[i] == 1 else 0 for i in range(numRuns)]
        fullGain = [(leftZero[i] + rightZero[i]) if runType[i] == 1 else -1
                    for i in range(numRuns)]

        A_compact, G_compact = [], []
        onesBefore = [0]*(numRuns + 1)
        for i in range(numRuns):
            onesBefore[i+1] = onesBefore[i] + (1 if runType[i] == 1 else 0)
            if runType[i] == 1:
                A_compact.append(Aarr[i])
                G_compact.append(fullGain[i])

        zeroVal = [runLen[i] if runType[i] == 0 else 0 for i in range(numRuns)]

        def build_max(arr):
            m = len(arr)
            if m == 0: return []
            table = [arr[:]]
            j = 1
            while (1 << j) <= m:
                prev, half = table[-1], 1 << (j-1)
                table.append([max(prev[i], prev[i+half]) for i in range(m-(1<<j)+1)])
                j += 1
            return table

        def build_min(arr):
            m = len(arr)
            if m == 0: return []
            table = [arr[:]]
            j = 1
            while (1 << j) <= m:
                prev, half = table[-1], 1 << (j-1)
                table.append([min(prev[i], prev[i+half]) for i in range(m-(1<<j)+1)])
                j += 1
            return table

        def q_max(table, l, r):
            if l > r: return None
            k = (r - l + 1).bit_length() - 1
            return max(table[k][l], table[k][r - (1 << k) + 1])

        def q_min(table, l, r):
            if l > r: return None
            k = (r - l + 1).bit_length() - 1
            return min(table[k][l], table[k][r - (1 << k) + 1])

        zeroTable = build_max(zeroVal)
        Gtable    = build_max(G_compact)
        Atable    = build_min(A_compact)

        runEndArr = runEnd[:]
        def findRun(pos):
            return bisect_left(runEndArr, pos)

        NEG = float('-inf')
        ans = []
        for (l, r) in queries:
            runL, runR = findRun(l), findRun(r)

            if runL == runR:
                GMZ = (r - l + 1) if runType[runL] == 0 else 0
            else:
                GMZ = 0
                if runType[runL] == 0:
                    GMZ = max(GMZ, runEnd[runL] - l + 1)
                if runType[runR] == 0:
                    GMZ = max(GMZ, r - runStart[runR] + 1)
                if runR - 1 >= runL + 1:
                    gm = q_max(zeroTable, runL+1, runR-1)
                    if gm is not None:
                        GMZ = max(GMZ, gm)

            maxGain = NEG
            RA, RB = runL + 1, runR - 1
            if RA <= RB:
                if RA == RB:
                    if runType[RA] == 1:
                        Ai = Aarr[RA]
                        Lz = runEnd[runL] - l + 1
                        Rz = r - runStart[runR] + 1
                        cand = max(Lz + Rz, GMZ - Ai)
                        maxGain = max(maxGain, cand)
                else:
                    if runType[RA] == 1:
                        Ai = Aarr[RA]
                        Lz = runEnd[runL] - l + 1
                        Rz = rightZero[RA]
                        cand = max(Lz + Rz, GMZ - Ai)
                        maxGain = max(maxGain, cand)
                    if runType[RB] == 1:
                        Ai = Aarr[RB]
                        Rz = r - runStart[runR] + 1
                        Lz = leftZero[RB]
                        cand = max(Lz + Rz, GMZ - Ai)
                        maxGain = max(maxGain, cand)
                    if RA + 1 <= RB - 1:
                        k_lo = onesBefore[RA+1]
                        k_hi = onesBefore[RB] - 1
                        if k_lo <= k_hi:
                            gmax = q_max(Gtable, k_lo, k_hi)
                            amin = q_min(Atable, k_lo, k_hi)
                            cand = max(gmax, GMZ - amin)
                            maxGain = max(maxGain, cand)

            ans.append(totalOnes if maxGain == NEG else totalOnes + max(0, maxGain))

        return ans