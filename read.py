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