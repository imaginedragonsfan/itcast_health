# ### 正则函数
import re
# search   通过正则匹配出第一个对象返回，通过group取出对象中的值
strvar = "3+4 6*4"
obj = re.search(r"(\d+[+*]\d+)",strvar)
print(obj)

# 获取匹配到的内容
print(obj.group()) # 3+4
# 获取分组当中的内容 (返回元组)
print(obj.groups()) # ('3+4',)

# match    验证用户输入内容 (了解)
"""search在正则表达式的前面加上^ 等价于 match ,其他用法上一模一样"""
strvar = "a17366668888"
strvar = "17366668888"
# obj = re.search(r"^\d+",strvar)
# obj = re.match(r"\d+",strvar)
# print(obj.group())
print(obj)


# split    切割
strvar = "steven|jack_xboyww@risky"
lst = re.split("[|_@]",strvar)
print(lst) # ['steven', 'jack', 'xboyww', 'risky']

strvar = "steven2341273894jack234234xboyww11111risky"
lst = re.split("\d+",strvar)
print(lst) # ['steven', 'jack', 'xboyww', 'risky']


# sub      替换 
strvar = "steven|jack_xboyww@risky"
"""
strvar = strvar.replace("|","&")
strvar = strvar.replace("_","&")
strvar = strvar.replace("@","&")
print(strvar)
"""
# sub(正则,替换的字符,原字符串[,替换的次数])
res = re.sub("[|_@]","&",strvar)
res = re.sub("[|_@]","&",strvar,1)
print(res) # steven&jack_xboyww@risky

# subn     替换  (用法上与sub相同,只是返回值不同)
res = re.subn("[|_@]","&",strvar) # ('steven&jack&xboyww&risky', 3)
res = re.subn("[|_@]","&",strvar,2) # ('steven&jack&xboyww@risky', 2)
print(res)

# finditer 匹配字符串中相应内容,返回迭代器
"""返回的是迭代器,迭代器中包含了对象 对象.group来获取匹配到的值"""
from collections import Iterator, Iterable
strvar = "sdf23647fdgdfg()*()*23423423"
it = re.finditer("\d+",strvar)
print(isinstance(it,Iterator))

for obj in it:
	print(obj.group())
# 23647
# 23423423

# compile  指定一个统一的匹配规则
"""
正常情况下,正则表达式编译一次,执行一次
为了避免反复编译,节省时间空间,可以使用compile统一规则
编译一次,终身受益
"""
strvar = "asdfs234sdf234"
pattern = re.compile("\d+")

obj = pattern.search(strvar)
print(obj.group()) # 234

lst = pattern.findall(strvar)
print(lst) # ['234', '234']

# 修饰符 
# re.I 使匹配对大小写不敏感
strvar = "<h1>大标题</H1>"
pattern = re.compile("<h1>(.*?)</h1>" , flags=re.I)
obj = pattern.search(strvar)
print(obj.group()) # <h1>大标题</H1>


# re.M 使每一行都能够单独匹配(多行匹配)，影响 ^ 和 $
"""单行独立匹配,而不是整体匹配"""
strvar = """
<p>111</p>
<a>222</a>
<strong>333</strong>
"""

pattern = re.compile("^<.*?>(?:.*?)<.*?>$" , flags=re.M)
lst = pattern.findall(strvar)
print(lst) # ['<p>111</p>', '<a>222</a>', '<strong>333</strong>']

# re.S 使 . 匹配包括换行在内的所有字符
strvar = """
give
sdfsdfmefive
"""
# 多个修饰符一起使用通过|拼接
pattern = re.compile(".*?mefive" , flags = re.S|re.I|re.M )
obj = pattern.search(strvar)
print(obj.group())
"""

give
sdfsdfmefive
"""
