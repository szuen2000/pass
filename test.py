
x = 0 
while True :
	p = input ('請輸入密碼: ')
	password = 'a123456'
	if p == password : 
		print('good')
		break
	else :
		print ('密碼輸入錯誤 還有' , 2-x ,'次機會')
		x = x + 1
		if x ==3 :
			break 
		
		
