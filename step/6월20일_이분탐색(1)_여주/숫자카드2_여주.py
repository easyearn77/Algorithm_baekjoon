from collections import Counter

n = int(input())
card_num = list(map(int, input().split()))
m = int(input())
card_count = list(map(int, input().split()))
card_num = Counter(card_num)

for i in card_count:
  print(card_num[i], end =' ')
