# 凯撒密码的加密与解密
caeser = ["A", "B", "C", "D", "E", "F", "G",
          "H", "I", "J", "K", "L", "M", "N",
          "O", "P", "Q", "R", "S", "T", "U",
          "V", "W", "X", "Y", "Z"]

def useCaeser(texts):
    k = int(input("请输入密匙：")) % 26
    newText = ""
    for text in texts:
        m = caeser.index(str(text).upper())
        if m + k < len(caeser):
            newText += caeser[m + k].lower()
        else:
            newText += caeser[m + k - len(caeser)].lower()
    return print("您的密文为：%s" % newText)

def unCaeser(texts):
    k = int(input("请输入密匙：")) % 26
    newText = ""
    for text in texts:
        m = caeser.index(str(text).upper())
        newText += caeser[m - k].lower()
    return print("您的明文为：%s" % newText)


choose = int(input("请选择功能：1，加密；2，解密。（1/2)?"))
if choose == 1:
    useCaeser(input("请输入明文："))
elif choose == 2:
    unCaeser(input("请输入密文："))
else:
    print("所选项不存在。")
