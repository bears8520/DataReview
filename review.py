data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('讀取結束，共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均長度', sum_len/len(data))

new = []
for a in data:
	if len(a) < 100:
		new.append(a)
print('裡面有', len(new), '筆資料長度小於100')