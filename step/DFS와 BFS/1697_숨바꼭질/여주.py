#답지 참조, dfs로 문제를 풀 경우 무한 루프에 빠질 수 있음

from collections import deque 

def bfs(): 
  q = deque() 
  q.append(N) 
  while q: 
    v = q.popleft() 
    if v == K: 
      print(time[v]) 
      return 
    for next_step in (v-1, v+1, v*2): 
      if 0 <= next_step < MAX and not time[next_step]: 
        time[next_step] = time[v] + 1 
        q.append(next_step) 

MAX = 100001 #시간 초과 나지 않도록 max 제한
N, K = map(int, input().split()) 
time = [0]*MAX 
bfs()

#나는 코드는 답지 참고 안했는데, MAX설정을 100001로 안하고, 이론상 2*k로 했는데도 오류나더라;; 
#왜 그럴까? 알면 내 코드에 코멘트 남겨줘!ㅎㅎ
