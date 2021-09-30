import getpass

print('~Playfair Cipher Decrypter~')

text = input('復号化するテキストを入力：')
print('入力されたテキスト【'+text+'】')

keyword = getpass.getpass('キーワードを入力：')
print('入力されたキーワード【'+keyword+'】')
keyword = keyword.replace('j', 'i')
alphabet = keyword + 'abcdefghiklmnopqrstuvwxyz'
board = sorted(set(alphabet), key=alphabet.index)

decrypt = ''
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
        if one in xzero:
            done = one + 4
            dtwo = two - 1
        elif two in xzero:
            done = one - 1
            dtwo = two + 4
        elif one == two:
            if one in xzero:
                done = one + 4
                dtwo = two + 4
            else:
                done = one - 1
                dtwo = two - 1
        else:
            done = one - 1
            dtwo = two - 1
    elif one in yfive and two in yfive:
        if one in xzero:
            done = one + 4
            dtwo = two - 1
        elif two in xzero:
            done = one - 1
            dtwo = two + 4
        elif one == two:
            if one in xzero:
                done = one + 4
                dtwo = two + 4
            else:
                done = one - 1
                dtwo = two - 1
        else:
            done = one - 1
            dtwo = two - 1
    elif one in yten and two in yten:
        if one in xzero:
            done = one + 4
            dtwo = two - 1
        elif two in xzero:
            done = one - 1
            dtwo = two + 4
        elif one == two:
            if one in xzero:
                done = one + 4
                dtwo = two + 4
            else:
                done = one - 1
                dtwo = two - 1
        else:
            done = one - 1
            dtwo = two - 1
    elif one in yfifteen and two in yfifteen:
        if one in xzero:
            done = one + 4
            dtwo = two - 1
        elif two in xzero:
            done = one - 1
            dtwo = two + 4
        elif one == two:
            if one in xzero:
                done = one + 4
                dtwo = two + 4
            else:
                done = one - 1
                dtwo = two - 1
        else:
            done = one - 1
            dtwo = two - 1
    elif one in ytwenty and two in ytwenty:
        if one in xzero:
            done = one + 4
            dtwo = two - 1
        elif two in xzero:
            done = one - 1
            dtwo = two + 4
        elif one == two:
            if one in xzero:
                done = one + 4
                dtwo = two + 4
            else:
                done = one - 1
                dtwo = two - 1
        else:
            done = one - 1
            dtwo = two - 1
    elif one in xzero and two in xzero:
        if one in yzero:
            done = one + 20
            dtwo = two - 5
        elif two in yzero:
            done = one - 5
            dtwo = two + 20
        elif one == two:
            if one in yzero:
                done = one + 20
                dtwo = two + 20
            else:
                done = one - 5
                dtwo = two - 5
        else:
            done = one - 5
            dtwo = two - 5
    elif one in xone and two in xone:
        if one in yzero:
            done = one + 20
            dtwo = two - 5
        elif two in yzero:
            done = one - 5
            dtwo = two + 20
        elif one == two:
            if one in yzero:
                done = one + 20
                dtwo = two + 20
            else:
                done = one - 5
                dtwo = two - 5
        else:
            done = one - 5
            dtwo = two - 5
    elif one in xtwo and two in xtwo:
        if one in yzero:
            done = one + 20
            dtwo = two - 5
        elif two in yzero:
            done = one - 5
            dtwo = two + 20
        elif one == two:
            if one in yzero:
                done = one + 20
                dtwo = two + 20
            else:
                done = one - 5
                dtwo = two - 5
        else:
            done = one - 5
            dtwo = two - 5
    elif one in xthree and two in xthree:
        if one in yzero:
            done = one + 20
            dtwo = two - 5
        elif two in yzero:
            done = one - 5
            dtwo = two + 20
        elif one == two:
            if one in yzero:
                done = one + 20
                dtwo = two + 20
            else:
                done = one - 5
                dtwo = two - 5
        else:
            done = one - 5
            dtwo = two - 5
    elif one in xfour and two in xfour:
        if one in yzero:
            done = one + 20
            dtwo = two - 5
        elif two in yzero:
            done = one - 5
            dtwo = two + 20
        elif one == two:
            if one in yzero:
                done = one + 20
                dtwo = two + 20
            else:
                done = one - 5
                dtwo = two - 5
        else:
            done = one - 5
            dtwo = two - 5
    else:
        for i in range(5):
            for j in range (5):
                if one == yzero[i] and two == yfive[j]:
                    done = yzero[j]
                    dtwo = yfive[i]
                elif one == yzero[i] and two == yten[j]:
                    done = yzero[j]
                    dtwo = yten[i]
                elif one == yzero[i] and two == yfifteen[j]:
                    done = yzero[j]
                    dtwo = yfifteen[i]
                elif one == yzero[i] and two == ytwenty[j]:
                    done = yzero[j]
                    dtwo = ytwenty[i]
                elif one == yfive[i] and two == yzero[j]:
                    done = yfive[j]
                    dtwo = yzero[i]
                elif one == yfive[i] and two == yten[j]:
                    done = yfive[j]
                    dtwo = yten[i]
                elif one == yfive[i] and two == yfifteen[j]:
                    done = yfive[j]
                    dtwo = yfifteen[i]
                elif one == yfive[i] and two == ytwenty[j]:
                    done = yfive[j]
                    dtwo = ytwenty[i]
                elif one == yten[i] and two == yzero[j]:
                    done = yten[j]
                    dtwo = yzero[i]
                elif one == yten[i] and two == yfive[j]:
                    done = yten[j]
                    dtwo = yfive[i]
                elif one == yten[i] and two == yfifteen[j]:
                    done = yten[j]
                    dtwo = yfifteen[i]
                elif one == yten[i] and two == ytwenty[j]:
                    done = yten[j]
                    dtwo = ytwenty[i]
                elif one == yfifteen[i] and two == yzero[j]:
                    done = yfifteen[j]
                    dtwo = yzero[i]
                elif one == yfifteen[i] and two == yfive[j]:
                    done = yfifteen[j]
                    dtwo = yfive[i]
                elif one == yfifteen[i] and two == yten[j]:
                    done = yfifteen[j]
                    dtwo = yten[i]
                elif one == yfifteen[i] and two == ytwenty[j]:
                    done = yfifteen[j]
                    dtwo = ytwenty[i]
                elif one == ytwenty[i] and two == yzero[j]:
                    done = ytwenty[j]
                    dtwo = yzero[i]
                elif one == ytwenty[i] and two == yfive[j]:
                    done = ytwenty[j]
                    dtwo = yfive[i]
                elif one == ytwenty[i] and two == yten[j]:
                    done = ytwenty[j]
                    dtwo = yten[i]
                elif one == ytwenty[i] and two == yfifteen[j]:
                    done = ytwenty[j]
                    dtwo = yfifteen[i]
                else:
                    continue
    decrypt += ''.join(board[done])
    decrypt += ''.join(board[dtwo])

decrypt = decrypt.replace('axa', 'aa') 
decrypt = decrypt.replace('bxb', 'bb')
decrypt = decrypt.replace('cxc', 'cc')
decrypt = decrypt.replace('dxd', 'dd')
decrypt = decrypt.replace('exe', 'ee')
decrypt = decrypt.replace('fxf', 'ff')
decrypt = decrypt.replace('gxg', 'gg')
decrypt = decrypt.replace('hxh', 'hh')
decrypt = decrypt.replace('ixi', 'ii')
decrypt = decrypt.replace('kxk', 'kk')
decrypt = decrypt.replace('lxl', 'll')
decrypt = decrypt.replace('mxm', 'mm')
decrypt = decrypt.replace('nxn', 'nn')
decrypt = decrypt.replace('oxo', 'oo')
decrypt = decrypt.replace('pxp', 'pp')
decrypt = decrypt.replace('qxq', 'qq')
decrypt = decrypt.replace('rxr', 'rr')
decrypt = decrypt.replace('sxs', 'ss')
decrypt = decrypt.replace('txt', 'tt')
decrypt = decrypt.replace('uxu', 'uu')
decrypt = decrypt.replace('vxv', 'vv')
decrypt = decrypt.replace('wxw', 'ww')
decrypt = decrypt.replace('xxx', 'xx')
decrypt = decrypt.replace('yxy', 'yy')
decrypt = decrypt.replace('zxz', 'zz')

print('暗号化されたテキスト【'+decrypt+'】※i(j)')