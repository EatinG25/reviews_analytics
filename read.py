data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Read over, total is', len(data), 'data.')

# 每筆資料平均長度為？
sum_len = 0
for d in data:
	sum_len += len(d)
print('average length of reviews is', sum_len/len(data))

# 篩選機制
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆留言長度<100。')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆留言中提到good。')
print(good[0])