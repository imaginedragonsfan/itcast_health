# ### 匹配分组 ()表达整体
import re
# (1)分组
print(re.findall('.*?_good','steven_good jack_good secret男_good'))  # ['steven_good', ' jack_good', ' secret男_good']
print(re.findall('(.*?)_good','steven_good jack_good secret男_good')) # ['steven', ' jack', ' secret男']

# (?:) 代表不优先显示分组里面的内容,只是显示正常匹配到的内容
print(re.findall('(?:.*?)_good','steven_good jack_good secret男_good')) # ['steven_good', ' jack_good', ' secret男_good']

# (2) | 代表或 , a|b 匹配字符a 或者 匹配字符b . 
strvar = "abceab"
lst = re.findall("a|b",strvar)
print(lst) # ['a', 'b', 'a', 'b']

# 注意点:把不容易匹配到的内容放到前面,把容易匹配到的内容放到后面
strvar = "abcdeabc234f"
lst = re.findall("abcd|abc",strvar)
print(lst)   # ['abcd', 'abc']

# (3) 练习
"""
.  可以匹配任意的字符,除了\n
\. 对.进行转义,表达.这个字符本身.

"""
# 匹配小数 
strvar = "3....  ....4  .3 ...3   1.3  9.89  10"
lst = re.findall(r"\d+\.\d+",strvar)
print(lst)  #['1.3', '9.89']

# 匹配小数和整数 
lst = re.findall(r"\d+\.\d+|\d+",strvar)
print(lst) # ['3', '4', '3', '3', '1.3', '9.89', '10']

# 使用分组改造
'''findall优先显示括号里的内容,需要加上?:取消优先显示,
按照匹配到的内容显示'''
lst = re.findall(r"\d+(?:\.\d+)?",strvar)
print(lst) # ['3', '4', '3', '3', '1.3', '9.89', '10']

# 匹配135或171的手机号 
strvar = "13566668888 17366669999 17135178392"
lst = re.findall(r"(?:135|171)\d{8}",strvar)
print(lst)  # ['13566668888', '17135178392']

# 优化,只能匹配出一个手机号
strvar = "13566668888"
lst = re.findall(r"^(?:135|171)\d{8}$",strvar)
print(lst)  # ['13566668888']
obj = re.search(r"^(135|171)\d{8}$",strvar)
print(obj) # <re.Match object; span=(0, 11), match='13566668888'>
print(obj.group())  # 13566668888
print(obj.groups()) # ('135',)

# 匹配www.baidu.com 或者 www.alibaba.com
"""
findall : 从左到右,匹配出所有的内容,返回到列表
		  问题是,匹配到的字符串和分组的内容不能同时显示;

search  : 从左到右,匹配到一组内容就直接返回,返回的是对象
		  优点是,可以让匹配到的内容和分组里的内容同时显示;
		  匹配不到内容时,返回的是None
		  
obj.group() : 获取匹配到的内容
obj.groups(): 获取分组里面的内容
"""
# findall
strvar = "www.baidu.com  www.alibaba.com  www.bilibili.com"
lst = re.findall(r"(?:www)\.(?:baidu|alibaba)\.(?:com)",strvar)
print(lst) # ['www.baidu.com', 'www.alibaba.com']

# search
strvar = "www.baidu.com  www.alibaba.com  www.bilibili.com"
obj = re.search(r"(www)\.(baidu|alibaba)\.(com)",strvar)
print(obj)  # <re.Match object; span=(0, 13), match='www.baidu.com'>

# 获取匹配到的内容
print(obj.group())  # www.baidu.com
# 获取分组里面的内容 (推荐)
print(obj.groups())  # ('www', 'baidu', 'com')

# 方法二,可以直接通过下标1来获取分组里面的第一个内容;
print(obj.group(1))
print(obj.group(2))
print(obj.group(3))

# search 练习 : 计算"5*6-7/3"结果  匹配 5*6 或者 7/3
strvar =  "5*6-7/3"
obj = re.search(r"\d+[*/]\d+",strvar)
res1 = obj.group()
print(res1 , type(res1)) # 5*6 <class 'str'>

# 计算结果
a,b = res1.split("*")
res2 = int(a) * int(b)
print(res2)

# 把30替换回原来的字符串中
strvar = strvar.replace(res1,str(res2))
print(strvar)

# 以此类推 ... 



