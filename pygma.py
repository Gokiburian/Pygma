import random
import sys

rotor=5 #ローターの数
check = True    #終了の確認

try:    #読み込みファイル名の取得
    file1 = sys.argv[1]
except:
    file1 = input("処理ファイル名 >")
if file1.find("pygma.py") != -1:
    input("pygma自体の暗号化を認識したため停止します >(enterで終了)")
    sys.exit()
    
try:    #シード値の設定
    random.seed(sys.argv[2])
except:
    random.seed(input("シード値 >"))

try:    #出力ファイル名の取得
    file2 = sys.argv[3]
    check = False
    if file2 == "o":
        file2 = file1
except:
    file2 = input("出力ファイル名 (無入力->上書き) >")
    if file2 == "":
        file2=file1
    
with open(file1,mode="rb")as f:  #ファイルの読み込みとバイナリデータの整理
    c = bytearray(f.read())



l = list(range(256))
ls = []
for i in range(rotor):
    ls.append(random.sample(l,len(l)))

for i in range(len(c)):
    if i%2**16==0:
        print(file2 + ": " + str(i*100//len(c)) + "%")
    b=c[i]
    for j in range(rotor):
        b=ls[j][b]
    if b%2==0:
        b+=1
    else:
        b-=1
    for j in range(rotor-1,-1,-1):
        b = ls[j].index(b)
        if i%256**j:
            ls[j].append(ls[j][0])
            del ls[j][0]
    c[i]=b


                
with open(file2,mode="wb")as f:  #ファイルへの書き込み
    f.write(c)
    
if check:    
    input(file2 + ": 100% >(enterで終了)")
else:
    print(file2 + ": 100%")
