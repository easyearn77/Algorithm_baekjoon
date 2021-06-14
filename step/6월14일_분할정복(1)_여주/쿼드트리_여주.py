n = int(input())
image = [input() for _ in range(n)]

def quadtree(x1, y1, x2, y2, n):
  if(n == 1):
    return image[y1][x1]
  
  d = n // 2

  s1 = quadtree(x1, y1, x1+d, y1+d, d)
  s2 = quadtree(x1+d, y1, x1+d, y1+d, d)
  s3 = quadtree(x1, y1+d, x1+d, y1+d, d)
  s4 = quadtree(x1+d, y1+d, x1+d, y1+d, d)

  if s1==s2==s3==s4 and len(s1) == 1:
    return s1
  
  return '(' + s1 + s2 + s3 + s4 + ')'

print(quadtree(0,0,n,n,n))
