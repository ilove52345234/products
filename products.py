import os # operating system
#讀取檔案
products = []
if os.path.isfile('products.csv'):#
    print('找到檔案, 開始讀取')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue ##從這跳到下個迴圈 這迴圈後面不執行
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
else:
    print('未找到檔案, 將重新生成')
#Produts 建立記帳小程式
#二維清單
#讀取檔案
##讓使用者輸入
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

#印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])
#再次提醒 with 為自動關閉功能
#字串可以用加法跟乘法 
#減法跟除法不行
#.csv 常用儲存資料檔案 可用excel開啟 ,為分隔

##寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') 