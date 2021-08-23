# ### 正则表达式 - 匹配单个字符
import re
"""lst = re.findall(正则表达式,字符串)"""

# (1) 预定义字符集
# \d 匹配数字
strvar = "sdjfklj234&*(&1"
lst = re.findall("\d",strvar)
print(lst) # ['2', '3', '4', '1']

# \D 匹配非数字
strvar = "YWERsdf78_&"
lst = re.findall("\D",strvar)
print(lst) # ['Y', 'W', 'E', 'R', 's', 'd', 'f', '_', '&']

# \w 匹配字母或数字或下划线     (正则函数中,支持中文的匹配)
strvar = "sadf234_^&*%$^$%你好"
lst = re.findall("\w",strvar)
print(lst) # ['s', 'a', 'd', 'f', '2', '3', '4', '_', '你', '好']

# \W 匹配非字母或数字或下划线
strvar = "sadf234_^&*%$^$%你好"
lst = re.findall("\W",strvar)
print(lst) # ['^', '&', '*', '%', '$', '^', '$', '%']

# \s 匹配任意的空白符 ( " "  \t  \n \r )
strvar = " 		 \r "
lst = re.findall("\s",strvar)
print(lst) # [' ', '\t', '\t', ' ', '\r', ' ']

# \S 匹配任意非空白符
strvar = " 		 \r  123_*("
lst = re.findall("\S",strvar)
print(lst) # ['1', '2', '3', '_', '*', '(']

# \n 匹配一个换行符
strvar = """
假期结束了,兄弟们满载	而归,玩的	很困,尽	快调	整.
"""
lst = re.findall(r"\n",strvar)
print(lst) # ['\n', '\n']

# \t 匹配一个制表符
lst = re.findall(r"\t",strvar)
print(lst) # ['\t', '\t', '\t', '\t']

# (2) 字符组 [] 匹配出字符组当中列举的字符(默认选一个)
# lst = re.findall("[123]","a1b2c3d4")
# print(lst)

print(re.findall('a[abc]b','aab abb acb adb')) # aab abb acb
print(re.findall('a[0123456789]b','a1b a2b a3b acb ayb')) # a1b  a2b a3b
# 优化写法 0123456789  => 0-9
print(re.findall('a[0-9]b','a1b a2b a3b acb ayb')) 

print(re.findall('a[abcdefg]b','a1b a2b a3b acb ayb adb')) # acb adb
# 优化写法 abcdefg => a-g  表达所有的小写字母 a-z
print(re.findall('a[a-g]b','a1b a2b a3b acb ayb adb'))
print(re.findall('a[a-z]b','a1b a2b a3b acb ayb adb')) # acb adb ayb

print(re.findall('a[ABCDEFG]b','a1b a2b a3b  aAb aDb aYb')) # aAb aDb
# 优化写法 ABCDEFG => A-G  表达所有的大写字母 A-Z
print(re.findall('a[A-G]b','a1b a2b a3b  aAb aDb aYb')) # aAb aDb
print(re.findall('a[A-Z]b','a1b a2b a3b  aAb aDb aYb')) # aAb aDb aYb

# 注意点: 不能直接写A-z  中间ascii编码中包含了特殊的符号
print(re.findall('a[A-z]b','a1b a2b a3b acb ayb adb a[b'))
# 匹配所有的字母和数字
print(re.findall('a[a-zA-Z0-9]b','a1b a2b a3b acb ayb adb a[b'))


print(re.findall('a[0-9a-zA-Z]b','a-b aab aAb aWb aqba1b'))  #aab aAb aWb aqb a1b
print(re.findall('a[0-9][*#/]b','a1/b a2b a29b a56b a456b')) # a1/b

# ^ 在字符组开头的位置出现代表 除了...的意思
print(re.findall('a[^-+*/]b',"a%b ccaa*bda&bd")) #a%b a&b

# 匹配^-\等特殊字符时 ,需要前面加上\进行转义
strvar = "a^c a-c a\c"
lst = re.findall(r"a[\^\-\\]c",strvar)
print(lst) # ['a^c', 'a-c', 'a\\c']
print(lst[-1])


# 注意点:为了防止转义,在正则表达式中或者要匹配的字符串中,无脑加r实现匹配
strvar = r"a\b"
lst = re.findall(r"a\\b",strvar)
print(lst[0])


