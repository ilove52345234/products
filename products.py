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