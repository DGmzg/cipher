import re

letters = ["A", "B", "C", "D", "E", "F", "G",
           "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z"]


def sortKey(keys):
    """返回字母在字母表中的顺序"""
    sortList = []
    for k in str(keys).upper():
        try:
            st = letters.index(k)
            sortList.append(st)
        except ValueError:
            pass
    return sortList

def keyNum(lists):
    """根据字母表中出现的先后顺序返回一个列表"""
    keyLists = []
    numList = lists.copy()
    numList.sort()
    for sort in lists:
        num = numList.index(sort)
        keyLists.append(num)
    return keyLists

def turnMatrix(texts, keys):
    """切割文本生成矩阵"""
    reg = re.compile("[a-z]|[A-Z]")
    t = reg.findall(texts)
    newTexts = []
    for i in range(0, len(t), len(keys)):
        part = t[i:i + len(keys)]
        newTexts.append(part)
    return newTexts

def encrypt():
    """加密"""
    text = input("请输入需要加密的文本：")
    key = input("请输入你要使用的密钥：")
    keyList = keyNum(sortKey(key))
    matrix = turnMatrix(text, key)
    newText = []
    # 按照字母先后顺序进行置换
    for list in matrix:
        newList = [""]*len(key)
        for n in range(len(key)):
            try:
                newList[n] = list[keyList[n]]
            except IndexError:
                pass
        text = "".join(newList)
        newText.append(text)
    newText = "".join(newText)
    print(newText)

def decrypt():
    """解密"""
    text = input("请输入需要解密的文本：")
    key = input("请输入你要使用的密钥：")
    keyList = keyNum(sortKey(key))
    matrix = turnMatrix(text, key)
    newText = []
    # 按照字母先后顺序进行置换
    for list in matrix:
        newList = [""]*len(key)
        for n in range(len(key)):
            try:
                newList[keyList[n]] = list[n]
            except IndexError:
                pass
        text = "".join(newList)
        newText.append(text)
    newText = "".join(newText)
    print(newText)

def main():
    choose = int(input("请选择功能：1，加密；2，解密。（1/2）？"))
    if choose == 1:
        encrypt()
    elif choose == 2:
        decrypt()
    else:
        print("输入错误，没有对应的功能。")


main()
