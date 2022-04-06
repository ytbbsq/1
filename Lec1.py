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

test_input()

# a 「Ctrl + / 」（行コメント）
# 「Shift + Alt + a 」（ブロックコメント)

"""
型の確認はtype()

  """