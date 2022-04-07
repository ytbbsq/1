# test

def test_if():
    a=100
    b=50
    if a > b:
        a -= b
    elif a < b:
        a += b
    else:
        pass
    print(a)
    c= None
    if not c:
        print(c)

def test_input():
    age = int(input("何歳ですか？"))
    casino_age = 18
    if age >= casino_age:
        print("どうぞお入りください")
    else:
        print("入場禁止です！！")

def test_list():
    fruits=["a","b",1]
    print(fruits[-1])
    #語尾に追加　fruits.append("c")
    #指定位置に追加(この例だと3番目にCが入る)　fruits.insert(3,"c")
    #削除　fruits.remove("a")
    #並べ替え　fruits.sort(reverse=True)
    #要素数を取得　len(fruits)
    #スライス 抜き出し fruits[開始:未満:ｽﾃｯﾌﾟ]
    #スライス 全部　fruits[:]
    #スライス 逆順にする fruits[::-1]
    #結合1　a(4次元) = a(1次元) + b(3次元)
    #結合2 a(1,3次元) = = a.append(b)

test_list()

# a 「Ctrl + / 」（行コメント）
# 「Shift + Alt + a 」（ブロックコメント)

"""
型の確認はtype()

  """