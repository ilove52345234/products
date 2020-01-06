#Produts 建立記帳小程式
#二維清單


products = []
while True:
    name = input('請輸入商品名稱: ' )
    if name == 'q':
    	break
    price = input('請輸入價格: ')
    # np = []
    # np.append(name)
    # np.append(price)
    ## np = [name, price]
    ## products.append(np)
    products.append([name, price])
print(products)
#products[0][0]   
#索引 第0個清單內的清單第0個選項
for p in products:
	print(p[0], '的價格是', p[1])

#再次提醒 with 為自動關閉功能
#字串可以用加法跟乘法 
#減法跟除法不行
#.csv 常用儲存資料檔案 可用excel開啟 ,為分隔

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')