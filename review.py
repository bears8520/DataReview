data = []
count = 0
with open('reviews.txt' , 'r') as f: #讀取檔案
	for line in f:
		data.append(line) #每行作讀取
		count += 1
		if count % 1000 == 0:
			print(len(data)) #每千筆印出
print('讀取結束，共有', len(data), '筆資料')

wc = {} #字數計算字典
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #將蒐到值的數量加一
		else:
			wc[word] = 1 #新增KEY

print(len(wc))

while True:
	word = input('請問您想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word], '次')
	else:
		print('查無此字')

print('感謝使用')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均長度', sum_len/len(data)) #計算句子平均長度(總字數除以總筆數)


new = []
for a in data:
	if len(a) < 100: #每筆裡面的字小於100的話
		new.append(a) #把a加進new清單內
print('裡面有', len(new), '筆資料長度小於100')