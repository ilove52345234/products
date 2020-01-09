#Produts 建立記帳小程式
#二維清單
#products[0][0]   
#索引 第0個清單內的清單第0個選項
#再次提醒 with 為自動關閉功能
#字串可以用加法跟乘法 
#減法跟除法不行
#.csv 常用儲存資料檔案 可用excel開啟 ,為分隔
import os # operating system
#讀取檔案
def read_file(mane):
    products = []
    with open(mane, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue ##從這跳到下個迴圈 這迴圈後面不執行
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products
##讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ' )
        if name == 'q':
            break
        price = input('請輸入價格: ')
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

##寫入檔案
def write_file(mane, products):
    with open(mane, 'w', encoding = 'utf-8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') 

def when_no_file():   #若無檔案則創立一個新的檔案
    with open('products.csv', 'w', encoding='utf-8') as f:
        f.write('商品, 價格\n')
    #注1:不可return，會產生錯誤  
def main():
    mane = 'products.csv'
    if os.path.isfile(mane):
        print('找到檔案, 開始讀取')
        products = read_file(mane)       
    else:
        print('未找到檔案, 將重新生成')
        products = when_no_file() #直接生成新檔案
      
    
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()