import getpass #to hide the keyword when enter

print('プレイフェア暗号') #title

text = input('暗号化するテキストを入力：') #get the text
print('入力されたテキスト【'+text+'】') #text check

text = text.replace(' ', '') #remove space
text = text.replace('j', 'i') #i == j
text = text.replace('aa', 'axa') 
text = text.replace('bb', 'bxb')
text = text.replace('cc', 'cxc')
text = text.replace('dd', 'dxd')
text = text.replace('ee', 'exe')
text = text.replace('ff', 'fxf')
text = text.replace('gg', 'gxg')
text = text.replace('hh', 'hxh')
text = text.replace('ii', 'ixi')
text = text.replace('kk', 'kxk')
text = text.replace('ll', 'lxl')
text = text.replace('mm', 'mxm')
text = text.replace('nn', 'nxn')
text = text.replace('oo', 'oxo')
text = text.replace('pp', 'pxp')
text = text.replace('qq', 'qxq')
text = text.replace('rr', 'rxr')
text = text.replace('ss', 'sxs')
text = text.replace('tt', 'txt')
text = text.replace('uu', 'uxu')
text = text.replace('vv', 'vxv')
text = text.replace('ww', 'wxw')
text = text.replace('xx', 'xxx')
text = text.replace('yy', 'yxy')
text = text.replace('zz', 'zxz')
if len(text) % 2 == 1: #if odd
    text = text + 'x' #add x

keyword = getpass.getpass("キーワードを入力：") #get the keyword
print('入力されたキーワード【'+keyword+'】') #keyword check lol
keyword = keyword.replace('j', 'i') #i == j
alphabet = keyword + 'abcdefghiklmnopqrstuvwxyz' #add alphabet
keyword = sorted(set(keyword), key=keyword.index) #delete duplicate
board = sorted(set(alphabet), key=alphabet.index) #board build 

encrypt = ''#encrypt reset
yzero = [0, 1, 2, 3, 4]
yfive = [5, 6, 7, 8, 9]
yten = [10, 11, 12, 13, 14]
yfifteen = [15, 16, 17, 18, 19]
ytwenty = [20, 21, 22, 23, 24]
xzero = [0, 5, 10, 15, 20]
xone = [1, 6, 11, 16, 21]
xtwo = [2, 7, 12, 17, 22]
xthree = [3, 8, 13, 18, 23]
xfour = [4, 9, 14, 19, 24]

for n in range(0, len(text), 2):
    for k in range(len(board)):
        if board[k] == text[n]: 
            one = k
        elif board[k] == text[n+1]: 
            two = k
        else:
            pass
    if one in yzero and two in yzero:
        if one in xfour:
            eone = one - 4
            etwo = two + 1
        elif two in xfour:
            eone = one + 1
            etwo = two - 4
        elif one == two:
            if one in xfour:
                eone = one - 4
                etwo = two - 4
            else:
                eone = one + 1
                etwo = two + 1
        else:
            eone = one + 1
            etwo = two + 1
    elif one in yfive and two in yfive:
        if one in xfour:
            eone = one - 4
            etwo = two + 1
        elif two in xfour:
            eone = one + 1
            etwo = two - 4
        elif one == two:
            if one in xfour:
                eone = one - 4
                etwo = two - 4
            else:
                eone = one + 1
                etwo = two + 1
        else:
            eone = one + 1
            etwo = two + 1
    elif one in yten and two in yten:
        if one in xfour:
            eone = one - 4
            etwo = two + 1
        elif two in xfour:
            eone = one + 1
            etwo = two - 4
        elif one == two:
            if one in xfour:
                eone = one - 4
                etwo = two - 4
            else:
                eone = one + 1
                etwo = two + 1
        else:
            eone = one + 1
            etwo = two + 1
    elif one in yfifteen and two in yfifteen:
        if one in xfour:
            eone = one - 4
            etwo = two + 1
        elif two in xfour:
            eone = one + 1
            etwo = two - 4
        elif one == two:
            if one in xfour:
                eone = one - 4
                etwo = two - 4
            else:
                eone = one + 1
                etwo = two + 1
        else:
            eone = one + 1
            etwo = two + 1
    elif one in ytwenty and two in ytwenty:
        if one in xfour:
            eone = one - 4
            etwo = two + 1
        elif two in xfour:
            eone = one + 1
            etwo = two - 4
        elif one == two:
            if one in xfour:
                eone = one - 4
                etwo = two - 4
            else:
                eone = one + 1
                etwo = two + 1
        else:
            eone = one + 1
            etwo = two + 1
    elif one in xzero and two in xzero:
        if one in ytwenty:
            eone = one - 20
            etwo = two + 5
        elif two in ytwenty:
            eone = one + 5
            etwo = two - 20
        elif one == two:
            if one in ytwenty:
                eone = one - 20
                etwo = two - 20
            else:
                eone = one + 5
                etwo = two + 5
        else:
            eone = one + 5
            etwo = two + 5
    elif one in xone and two in xone:
        if one in ytwenty:
            eone = one - 20
            etwo = two + 5
        elif two in ytwenty:
            eone = one + 5
            etwo = two - 20
        elif one == two:
            if one in ytwenty:
                eone = one - 20
                etwo = two - 20
            else:
                eone = one + 5
                etwo = two + 5
        else:
            eone = one + 5
            etwo = two + 5
    elif one in xtwo and two in xtwo:
        if one in ytwenty:
            eone = one - 20
            etwo = two + 5
        elif two in ytwenty:
            eone = one + 5
            etwo = two - 20
        elif one == two:
            if one in ytwenty:
                eone = one - 20
                etwo = two - 20
            else:
                eone = one + 5
                etwo = two + 5
        else:
            eone = one + 5
            etwo = two + 5
    elif one in xthree and two in xthree:
        if one in ytwenty:
            eone = one - 20
            etwo = two + 5
        elif two in ytwenty:
            eone = one + 5
            etwo = two - 20
        elif one == two:
            if one in ytwenty:
                eone = one - 20
                etwo = two - 20
            else:
                eone = one + 5
                etwo = two + 5
        else:
            eone = one + 5
            etwo = two + 5
    elif one in xfour and two in xfour:
        if one in ytwenty:
            eone = one - 20
            etwo = two + 5
        elif two in ytwenty:
            eone = one + 5
            etwo = two - 20
        elif one == two:
            if one in ytwenty:
                eone = one - 20
                etwo = two - 20
            else:
                eone = one + 5
                etwo = two + 5
        else:
            eone = one + 5
            etwo = two + 5
    else:
        for i in range(5):
            for j in range (5):
                if one == yzero[i] and two == yfive[j]:
                    eone = yzero[j]
                    etwo = yfive[i]
                elif one == yzero[i] and two == yten[j]:
                    eone = yzero[j]
                    etwo = yten[i]
                elif one == yzero[i] and two == yfifteen[j]:
                    eone = yzero[j]
                    etwo = yfifteen[i]
                elif one == yzero[i] and two == ytwenty[j]:
                    eone = yzero[j]
                    etwo = ytwenty[i]
                elif one == yfive[i] and two == yzero[j]:
                    eone = yfive[j]
                    etwo = yzero[i]
                elif one == yfive[i] and two == yten[j]:
                    eone = yfive[j]
                    etwo = yten[i]
                elif one == yfive[i] and two == yfifteen[j]:
                    eone = yfive[j]
                    etwo = yfifteen[i]
                elif one == yfive[i] and two == ytwenty[j]:
                    eone = yfive[j]
                    etwo = ytwenty[i]
                elif one == yten[i] and two == yzero[j]:
                    eone = yten[j]
                    etwo = yzero[i]
                elif one == yten[i] and two == yfive[j]:
                    eone = yten[j]
                    etwo = yfive[i]
                elif one == yten[i] and two == yfifteen[j]:
                    eone = yten[j]
                    etwo = yfifteen[i]
                elif one == yten[i] and two == ytwenty[j]:
                    eone = yten[j]
                    etwo = ytwenty[i]
                elif one == yfifteen[i] and two == yzero[j]:
                    eone = yfifteen[j]
                    etwo = yzero[i]
                elif one == yfifteen[i] and two == yfive[j]:
                    eone = yfifteen[j]
                    etwo = yfive[i]
                elif one == yfifteen[i] and two == yten[j]:
                    eone = yfifteen[j]
                    etwo = yten[i]
                elif one == yfifteen[i] and two == ytwenty[j]:
                    eone = yfifteen[j]
                    etwo = ytwenty[i]
                elif one == ytwenty[i] and two == yzero[j]:
                    eone = ytwenty[j]
                    etwo = yzero[i]
                elif one == ytwenty[i] and two == yfive[j]:
                    eone = ytwenty[j]
                    etwo = yfive[i]
                elif one == ytwenty[i] and two == yten[j]:
                    eone = ytwenty[j]
                    etwo = yten[i]
                elif one == ytwenty[i] and two == yfifteen[j]:
                    eone = ytwenty[j]
                    etwo = yfifteen[i]
                else:
                    continue

    encrypt += ''.join(board[eone])
    encrypt += ''.join(board[etwo])
print('暗号化されたテキスト【'+encrypt+'】') #output