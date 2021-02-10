#sとtを入力値として受け取る
s = input()
t = input()

#sの長さを調べ、i文字目から読み始めてi文字目まで読む。tと合ったら修了。
for i in range(len(s)):
    if s[i:]+s[:i] == t:
        print("Yes")
        exit()
    else:
        continue
print("No")