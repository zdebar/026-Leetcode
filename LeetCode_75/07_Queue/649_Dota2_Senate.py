from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    radiant: deque[int] = deque()
    dire: deque[int] = deque()
    for i, s in enumerate(senate):
        if s == 'R':
            radiant.append(i)
        else:
            dire.append(i)
    while radiant and dire:
        r_idx = radiant.popleft()
        d_idx = dire.popleft()
        if r_idx < d_idx:
            radiant.append(r_idx + n)
        else:
            dire.append(d_idx + n)
    return "Radiant" if radiant else "Dire"