def change(string, temp = ''):
    """eng -> thai"""
    str1 = '1234567890-=qwertyuiop[]asdfghjkl;\'zxcvbnm,./'
    str2 = 'ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฟหกดเ้่าสวงผปแอิืทมใฝ'
    str3 = '!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?'
    str4 = '+๑๒๓๔ู฿๕๖๗๘๙๐"ฎฑธํ๊ณฯญฐ,ฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ'
    for i in string:
        if i in str1:
            temp += str2[str1.find(i)]
        elif i in str2:
            temp += str1[str2.find(i)]
        elif i in str3:
            temp += str4[str3.find(i)]
        elif i in str4:
            temp += str3[str4.find(i)]
        else:temp += i
    print(temp)
change(input())
