#aをリスト型で受け取り、小さい順に並べる
alist = sorted(list(map(int,input().split())))

#リストの2番目-1番目、3番目-2番目を足して出力は3番目-1番目と同意味
print(alist[2] - alist[0])
