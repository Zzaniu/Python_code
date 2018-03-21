# coding=utf-8


import re


pattern = re.compile(r"\d+")
m = pattern.match(r"1234fsd")
print m.group()


str = "itcastheima"
pattern = "itcast"
# match 从左至右匹配,匹配成功返回一个对象，使用group()提取
result = re.match(pattern, str)
print result.group()

# "." 匹配任意一个字符，除了"\n"
# re.S:全文匹配  re.I:忽略大小写
print re.match(r"(.)(.)", "abc", re.I).span()

# "\d" 匹配数字，即0-9
print re.match(r"\d", "2")


# "\D" 匹配非数字，即不是数字
print re.match(r"\D", "@")


# "\s" 匹配空白，即空格，tab键，换行等，一检测非空格就返回None
print re.match(r"\s", "\na ")


# "\S" 匹配非空白，一检测到空格就返回None
print re.match(r"\S", " @")


# "\w" 匹配单词字符，即a-z、A-Z、0-9、_
print re.match(r"\w+", "a@a")


# "\W" 匹配非单词字符
print re.match(r"\W", "@a")



# "[]" 匹配[]中列举的字符, "^" 取反, "-" 范围值
print re.match(r"[34578]", "9")
print re.match(r"[^34578]", "9")
print re.match(r"[a-z3-8]", "s")
print "-----------"
print re.match(r"[0-9]+", "0132046").group()


# "*" 匹配之前出现的一个字符，出现0次或者无数次
print re.match(r"\d*", "9900")


# "+" 匹配之前出现的一个字符，出现至少有1次
print re.match(r"\d+", "aaa")


# "?" 匹配之前出现的一个字符，出现1次或者0次，即要么有1次，要么没有
print re.match(r"\d?[a-z]", "99a")


# {m} 匹配前一个字符出现m次 {m,} 匹配前一个字符出现至少m次 {m,n} 匹配前一个字符出现次数介于m到n之间
print re.match(r"\d{6}[a-z]", "999999a")

# "^" 匹配字符串开头  "$" 匹配字符串结尾
print re.match(r"^\w*l$", "strdgsjsl").group()


# \b 匹配一个单词的边界  \B 匹配单词非边界
print re.match(r"\w+ +(sl\w+sl\B)*", "fd sldsgfslj")
print "*"*50
print re.findall(r"\w+ +(\bsl\w+sl\B)*", "fd sldsgfslj")

# \num 引用分组num匹配到的字符串
print re.match(r"<(.+)><(.+)>(.+)</\2></\1>$", "<html><h1>你好，大爷</h1></html>").group(3)
print re.match(r"<(?P<key1>.+)><(?P<key2>.+)>(.+)</(?P=key2)></(?P=key1)>$", "<html><h1>你好，大爷</h1></html>").group()

print re.match(r"(.+)@(qq|163|126|gmail)\.(com|cn|net)$", "zzaniu@126.com").group()


a = re.match(r"\d*", "a").group()
print "" == a

str = "GET /fhdkj/gre 200\r\n"
a = re.match(r"\w+ +(/[^ ]*) +(\w+)", str)
b = re.match(r"\w+ +(/[^ ]*) ", str)
print a.group(1,2)
print b.group(1)


# 所有的正则表达式都是贪婪地，除非你用?关闭它
s = r"""<p>正则表达式通常用于在文本中查找匹配的字符串。Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪的则相反，总是尝试匹配尽可能少的字符。例如：正则表达式”ab*”如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。</p>

<p>注：我们一般使用非贪婪模式来提取。</p>

<p>与大多数编程语言相同，正则表达式里使用”\”作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符”\”，那么使用编程语言表示的正则表达式里将需要4个反斜杠”\\”：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。</p>

<p>Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r”\”表示。同样，匹配一个数字的”\d”可以写成r”\d”。有了原生字符串，写出来的表达式更加直观。</p>

<p>python的Re模块提供对正则表达式的支持，主要用到下列几种方法</p>

<p>我们传进一个原生字符串’hello’，通过compile方法编译出一个pattern对象，之后我们将用这个对象进行匹配。也就是说之后要做的事就是对要匹配的字符串与’hello’作比较。</p>

<p>下面我们看看刚才提到的re模块中的几种方法</p>

<p>这个方法从我们要匹配的字符串的头部开始，当匹配到string的尾部还没有匹配结束时，返回None; <br>
当匹配过程中出现了无法匹配的字母，返回None。 <br>
下面给出一组代码来进行具体认识</p>
<h2 id="2python的re模块">2.python的Re模块</h2>"""

# print re.sub(r"<.*?>", "", s)
# print re.sub(r"(<\w*?|/\w*?)", "", s)

s = "http://www.baidu.com/fndskj/gfsdg/dagenihao"


def pattern(str):
    a = str.group(1)
    return a


print re.sub(r"(http://.+?/).*", pattern, s)
print re.sub(r"(http://.+?/).*", lambda x: x.group(1), s)

s = "hello world ha ha"
print re.findall(r"\b[a-zA-Z]+\b", s)


