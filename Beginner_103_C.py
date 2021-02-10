n = int(input())
alist = list(map(int, input().split()))
#m=a1*a2*a3*・・・とすると(m-1)modai=ai-1
print(sum(alist)-n)