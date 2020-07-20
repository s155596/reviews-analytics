data = [] # 建立空清單
count = 0 
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0: # 如果數到1000的倍數
			print(len(data)) # 把data的筆數印出來
print(data[0])
print('---------')
print(data[1])