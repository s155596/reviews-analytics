data = [] # 建立空清單
count = 0 
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0: # 如果數到1000的倍數
			print(len(data)) # 把data的筆數印出來
print('檔案讀取完了, 總共有', len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))