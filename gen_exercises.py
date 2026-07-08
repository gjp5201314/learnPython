#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为 lessons.ts 中 l9, l10, l16-l25 补充到 50 道题
格式: (etype, question, answer, hint, explanation, options_for_mc_or_None)
"""
import re
import json
from pathlib import Path

FILE = Path(r'e:\fastload\learnPython\src\data\lessons.ts')

def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')

def build_one(idx, lesson, etype, q, ans, hint, exp, opts):
    lines = ["    {"]
    lines.append(f'      id: "ex-{lesson}-{idx}",')
    lines.append(f'      type: "{etype}",')
    lines.append(f'      question: "{esc(q)}",')
    if etype == "multiple-choice":
        lines.append('      options: [')
        for o in opts:
            lines.append(f'        "{esc(o)}",')
        lines.append('      ],')
    lines.append(f'      answer: "{esc(ans)}",')
    lines.append(f'      hint: "{esc(hint)}",')
    lines.append(f'      explanation: "{esc(exp)}",')
    lines.append("    }")
    return "\n".join(lines)

def gen(lesson, items):
    """items: list of (etype, q, ans, hint, exp, opts)"""
    out = []
    for etype, q, ans, hint, exp, opts in items:
        out.append(build_one(0, lesson, etype, q, ans, hint, exp, opts))
    return out

# 一次性为每个 item 加上 idx
def with_idx(lesson, items):
    out = []
    for i, (etype, q, ans, hint, exp, opts) in enumerate(items, start=2):
        out.append(build_one(i, lesson, etype, q, ans, hint, exp, opts))
    return out


# =========================================================
# L9: 集合 Set  (保留 ex-9-1)
# =========================================================
L9_DATA = [
    ("multiple-choice", "下列哪个是创建空集合的正确写法？", "set()",
     "{} 创建的是空字典。", "{} 表示空字典，空集合必须用 set()。",
     ["[]", "{}", "set()", "dict()"]),

    ("fill-blank", "把列表 [1,2,2,3,3] 转为集合后元素个数是 ______。", "3",
     "集合自动去重。", "去重后剩 1, 2, 3 共 3 个元素。", None),

    ("predict-output", "{1, 2, 3} & {2, 3, 4} 的结果是？", "{2, 3}",
     "& 是交集。", "交集为两个集合共同的元素 {2, 3}。", None),

    ("multiple-choice", "Python 中集合的并集运算符是？", "|",
     "管道符像把两个集合连起来。", "| 是并集，& 是交集，- 是差集，^ 是对称差。",
     ["|", "&", "-", "^"]),

    ("fill-blank", "向集合 s 添加单个元素 'x' 的方法是 s.______('x')。", "add",
     "set 用 add 添加。", "set.add(x) 把 x 加入集合；append 是列表的方法。", None),

    ("predict-output", "{1, 2, 3} - {2, 3, 4} 的结果是？", "{1}",
     "- 是差集。", "差集 = a 中有、b 中没有的：{1}。", None),

    ("multiple-choice", "s.remove(x) 与 s.discard(x) 在 x 不存在时的区别是？",
     "remove 报错，discard 静默忽略",
     "discard 更安全。",
     "remove 抛 KeyError，discard 不抛异常。",
     ["完全相同", "remove 报错，discard 静默忽略", "discard 更快", "remove 删除最后一个"]),

    ("fill-blank", "清空集合 s 的方法是 s.______()。", "clear",
     "clear = 清空。", "s.clear() 移除集合的所有元素。", None),

    ("predict-output", "{1, 2, 3} ^ {2, 3, 4} 的结果是？", "{1, 4}",
     "^ 是对称差。", "对称差是只在一个集合中出现的元素。", None),

    ("multiple-choice", "Python 集合（set）是有序的吗？", "否，无序",
     "set 是无序容器。", "set 是无序的，元素顺序不保证。",
     ["是", "否，无序", "按插入顺序", "按字母顺序"]),

    ("fill-blank", "不可变的集合类型叫 ______set。", "frozen",
     "frozen 意为冰冻。", "frozenset 是不可变集合，可作为 dict 的 key。", None),

    ("predict-output", "{x for x in range(6) if x % 2 == 0} 的结果是？", "{0, 2, 4}",
     "集合推导式。", "range(6) 中偶数为 0,2,4。", None),

    ("multiple-choice", "len({1, 2, 3, 3, 2}) 的结果是？", "3",
     "集合去重。", "去重后剩 1, 2, 3，len 为 3。",
     ["5", "3", "4", "2"]),

    ("fill-blank", "判断集合 a 是否为 b 的子集用 a._______(b)。", "issubset",
     "is + subset。", "a.issubset(b) 当 a 中所有元素都在 b 中时返回 True。", None),

    ("predict-output", "{1, 2}.issubset({1, 2, 3}) 的结果是？", "True",
     "1 和 2 都在大集合里。", "{1,2} 的元素都出现在 {1,2,3} 中。", None),

    ("multiple-choice", "集合中的元素必须满足什么条件？", "可哈希（hashable）",
     "不可哈希对象不能放入集合。", "集合元素必须可哈希，如 int、str、tuple。",
     ["可变", "可哈希（hashable）", "任意类型", "必须是数字"]),

    ("fill-blank", "set('hello') 得到的集合大小是 ______。", "4",
     "h, e, l, o 四个不同字符。", "'hello' 拆字符后去重剩 h, e, l, o。", None),

    ("predict-output", "遍历集合时元素的顺序是？", "无固定顺序",
     "set 是无序容器。", "集合遍历顺序由内部 hash 决定，不保证。", None),

    ("multiple-choice", "把另一个可迭代对象的所有元素加入集合用哪个方法？", "update",
     "update = 批量更新。", "s.update(iter) 把可迭代对象中的元素批量加入。",
     ["add", "extend", "update", "merge"]),

    ("fill-blank", "{1,2,3}.isdisjoint({4,5}) 的返回值是 ______。", "True",
     "没有公共元素。", "两集合无交集，isdisjoint 返回 True。", None),

    ("predict-output", "frozenset 与 set 的关键区别是？", "不可变",
     "frozen 意为冰冻。", "frozenset 不可变，没有 add/remove 等修改方法。", None),

    ("multiple-choice", "复制集合 s 用哪个方法？", "copy",
     "copy = 复制。", "s.copy() 返回集合的浅拷贝。",
     ["dup", "copy", "clone", "repeat"]),

    ("fill-blank", "len(set([1,1,2,2,3,3])) 的结果是 ______。", "3",
     "去重后剩 3 个。", "集合去重后只保留 1, 2, 3。", None),

    ("predict-output", "集合支持下标访问（如 s[0]）吗？", "不支持",
     "set 无序。", "集合无序，不支持下标或切片访问。", None),

    ("multiple-choice", "判断两个集合是否相等用哪个运算符？", "==",
     "Python 等值比较。", "集合相等与顺序无关，{1,2,3} == {3,2,1} 为 True。",
     ["is", "==", "equals", "eq"]),

    ("fill-blank", "s.pop() 从集合中弹出元素后返回值的常见类型是 ______。", "int",
     "set 中元素通常是 int/str。", "pop 返回集合中的某个元素对象。", None),

    ("predict-output", "集合中查找元素的平均时间复杂度是？", "O(1)",
     "set 基于哈希表。", "哈希表查找平均 O(1)。", None),

    ("multiple-choice", "求集合 {3,1,2} 的最大值用哪个函数？", "max",
     "Python 内置 max。", "max(set) 返回集合中的最大元素。",
     ["largest", "top", "max", "maximum"]),

    ("fill-blank", "max({1, 5, 3}) 的结果是 ______。", "5",
     "max 取最大。", "{1,5,3} 中最大的是 5。", None),

    ("predict-output", "下列哪个对象不能放入集合？", "[1, 2]",
     "列表可变不可哈希。", "列表不可哈希，不能作为集合元素。", None),

    ("multiple-choice", "删除元素 x，元素不存在也不报错的集合方法是？", "discard",
     "discard 安全删除。", "s.discard(x) 删除 x，不存在则忽略。",
     ["remove", "discard", "delete", "pop"]),

    ("fill-blank", "sorted({3, 1, 2}) 的结果是 ______。", "[1, 2, 3]",
     "sorted 返回排序后的列表。", "sorted 把集合转成有序列表。", None),

    ("predict-output", "s.update([1, 2]) 的效果等价于？", "s.add(1); s.add(2)",
     "update 是批量添加。", "update 内部等价于依次 add 每个元素。", None),

    ("multiple-choice", "用集合对句子中的单词去重，用什么函数？", "set",
     "set() 把列表转集合。", "set(words) 自动去除重复单词。",
     ["unique", "distinct", "set", "dedup"]),

    ("fill-blank", "set('abab') | set('cd') 的结果是 ______。", "{'a', 'b', 'c', 'd'}",
     "并集。", "{a,b} 并 {c,d} = {a,b,c,d}。", None),

    ("predict-output", "Python 集合内部是用什么数据结构实现的？", "哈希表",
     "查找快靠哈希。", "set 与 dict 都基于哈希表。", None),

    ("multiple-choice", "求集合 s 中元素个数用哪个函数？", "len",
     "len() 是长度函数。", "len(s) 返回集合中元素个数。",
     ["size", "count", "len", "length"]),

    ("fill-blank", "{1, 2, 3} == {3, 2, 1} 的结果是 ______。", "True",
     "集合无序，比较与顺序无关。", "两个含相同元素的集合相等。", None),

    ("predict-output", "集合中的元素需要实现哪个魔术方法？", "__hash__",
     "可哈希对象必须实现 __hash__。", "集合要求元素实现 __hash__ 和 __eq__。", None),

    ("multiple-choice", "判断元素 'a' 是否在集合 s 中用哪个运算符？", "in",
     "in 是成员运算符。", "'a' in s 返回布尔值。",
     ["has", "contains", "in", "include"]),

    ("fill-blank", "'a' in {'a', 'b', 'c'} 的结果是 ______。", "True",
     "成员检查。", "'a' 是集合的元素之一。", None),

    ("predict-output", "set.union 与 set.update 的关键区别是？", "union 返回新集合，update 原地修改",
     "看是否返回新对象。", "union 返回新集合；update 修改原集合，返回 None。", None),

    ("multiple-choice", "求两个集合的差集用哪个方法或运算符？",
     "a.difference(b) 或 a - b",
     "difference 是差集方法名。", "a.difference(b) 或 a - b 都返回 a 中有 b 中没有的元素。",
     ["a.difference(b) 或 a - b", "a.subtract(b)", "a.minus(b)", "a.remove(b)"]),

    ("fill-blank", "{1, 2, 3} - set() 的结果是 ______。", "{1, 2, 3}",
     "任何集合减空集合等于其自身。", "差集为空集时返回原集合。", None),

    ("predict-output", "下列哪个是合法的集合推导式？", "{x for x in range(3)}",
     "{} + 推导式 = 集合推导式。", "{} 包推导式是集合；[] 是列表；() 是生成器。", None),

    ("multiple-choice", "求两个集合的交集用哪个方法？", "intersection",
     "intersection = 交集。", "a.intersection(b) 返回公共元素集合。",
     ["join", "intersection", "meet", "common"]),

    ("fill-blank", "{1, 2, 3}.intersection({2, 3, 4}) 的结果是 ______。", "{2, 3}",
     "交集。", "两个集合共有元素是 2 和 3。", None),

    ("predict-output", "下列哪个不是 set 的内置方法？", "append",
     "append 是列表的方法。", "set 没有 append；列表才有 append。", None),

    ("multiple-choice", "下列哪个不是 Python 的内置容器类型？", "graph",
     "graph 不是 Python 内置。", "list/tuple/dict/set 都是内置；graph 不是。",
     ["list", "tuple", "set", "graph"]),
]


# =========================================================
# L10: 字符串深入  (保留 ex-10-1)
# =========================================================
L10_DATA = [
    ("multiple-choice", "字符串是不可变的吗？", "是",
     "str 是不可变类型。", "Python 字符串一旦创建就不能修改，重新赋值会创建新对象。",
     ["是", "否", "只对短字符串是", "只对长字符串是"]),

    ("fill-blank", "把字符串 s 转成全大写的方法是 s.______()。", "upper",
     "upper = 大写。", "s.upper() 返回全大写副本。", None),

    ("predict-output", "'Hello'.lower() 的结果是？", "hello",
     "lower 转小写。", "'Hello'.lower() 返回 'hello'。", None),

    ("multiple-choice", "去除字符串首尾空格用哪个方法？", "strip",
     "strip = 剥去。", "str.strip() 去除首尾空白字符。",
     ["trim", "strip", "chomp", "clean"]),

    ("fill-blank", "把列表 ['a','b','c'] 用逗号连成字符串：','.______(['a','b','c'])。", "join",
     "join = 拼接。", "','.join(['a','b','c']) 返回 'a,b,c'。", None),

    ("predict-output", "len('你好') 的结果是？", "2",
     "len 按字符数算。", "Python 3 字符串是 Unicode，'你好' 长度为 2。", None),

    ("multiple-choice", "取字符串 'Python' 的前 3 个字符用哪种切片？", "'Python'[:3]",
     "切片语法。", "s[:3] 或 s[0:3] 都得到 'Pyt'。",
     ["'Python'[0:3]", "'Python'[1:3]", "'Python'[3:]", "'Python'[:3]"]),

    ("fill-blank", "'Python'[::-1] 的结果是 ______。", "nohtyP",
     "负步长 = 反转。", "[::-1] 步长为 -1，反转字符串。", None),

    ("predict-output", "'Hello,World'.split(',') 的结果是？", "['Hello', 'World']",
     "split 按分隔符切。", "按逗号切分为两个元素的列表。", None),

    ("multiple-choice", "判断字符串是否以某个前缀开头用哪个方法？", "startswith",
     "starts with = 以...开始。", "str.startswith(prefix) 返回布尔值。",
     ["startswith", "beginswith", "hasprefix", "prefix"]),

    ("fill-blank", "'Hello'.replace('l', 'L') 的结果是 ______。", "HeLLo",
     "replace 替换字符。", "把所有 'l' 替换为 'L'。", None),

    ("predict-output", "'  abc  '.strip() 的结果是？", "abc",
     "strip 去首尾空白。", "去除两端空格后只剩 'abc'。", None),

    ("multiple-choice", "字符串居中并填充字符用哪个方法？", "center",
     "center = 居中。", "str.center(width, fillchar) 居中并用 fillchar 填充。",
     ["center", "middle", "align", "pad"]),

    ("fill-blank", "判断 'a' 是否在字符串 'hello' 中：'a' ______ 'hello'。", "in",
     "in 是成员运算符。", "返回 False，因为 'a' 不在 'hello' 中。", None),

    ("predict-output", "'hello'.find('e') 的结果是？", "1",
     "find 找子串索引。", "'e' 在索引 1 位置。", None),

    ("multiple-choice", "find 与 index 的区别是？",
     "find 找不到返回 -1，index 找不到抛异常",
     "找不到时的行为不同。", "find 返回 -1，index 抛 ValueError。",
     ["完全相同", "find 找不到返回 -1，index 找不到抛异常", "index 更快", "find 支持正则"]),

    ("fill-blank", "'Python'.count('o') 的结果是 ______。", "1",
     "count 统计出现次数。", "'Python' 中 'o' 出现 1 次。", None),

    ("predict-output", "f'1+1={1+1}' 的结果是？", "1+1=2",
     "f-string 表达式插值。", "f-string 在 {} 中执行表达式。", None),

    ("multiple-choice", "字符串拼接 '+' 和 join 哪个更高效？", "join",
     "join 一次性分配。", "+ 拼接会反复创建新字符串；join 一次分配更高效。",
     ["+", "join", "一样", "看心情"]),

    ("fill-blank", "判断字符串是否全为字母的方法是 s.________()。", "isalpha",
     "is + alpha。", "s.isalpha() 当所有字符都是字母时返回 True。", None),

    ("predict-output", "'123'.isdigit() 的结果是？", "True",
     "isdigit 判断数字。", "全是数字字符返回 True。", None),

    ("multiple-choice", "把字符串首字母大写用哪个方法？", "capitalize",
     "capitalize = 首字母大写。", "str.capitalize() 把首字母大写其余小写。",
     ["capitalize", "title", "upper", "head"]),

    ("fill-blank", "每个单词首字母大写用 s.______()。", "title",
     "title = 标题格式。", "s.title() 把每个单词首字母大写。", None),

    ("predict-output", "'a b c'.split() 的结果是？", "['a', 'b', 'c']",
     "默认按空白切。", "split() 默认按任意空白切分。", None),

    ("multiple-choice", "把多个字符串拼接的最快方式是？", "''.join(lst)",
     "join 一次性分配。", "join 避免反复创建新对象，是最快的方式。",
     ["s = ''; for x in lst: s += x", "''.join(lst)", "reduce(lambda a,b: a+b, lst)", "f-string"]),

    ("fill-blank", "判断字符串是否以 '.py' 结尾：s._______('.py')。", "endswith",
     "ends with = 以...结束。", "s.endswith('.py') 返回布尔值。", None),

    ("predict-output", "'abcabc'.index('a') 的结果是？", "0",
     "index 返回首次出现位置。", "'a' 首次出现在索引 0。", None),

    ("multiple-choice", "下列哪个不是 Python 字符串方法？", "sort",
     "sort 是列表的方法。", "字符串没有 sort；列表才有 sort。",
     ["upper", "lower", "sort", "strip"]),

    ("fill-blank", "字符串 'a\\nb\\nc' 用 split('\\n') 切分后长度为 ______。", "3",
     "三段。", "切分后是 ['a', 'b', 'c']，长度 3。", None),

    ("predict-output", "'Hello'.startswith('He') 的结果是？", "True",
     "startswith 检查前缀。", "'Hello' 以 'He' 开头。", None),

    ("multiple-choice", "判断字符串是否全为小写用哪个方法？", "islower",
     "is + lower。", "str.islower() 当所有字母都是小写时返回 True。",
     ["islower", "lower", "islow", "issmall"]),

    ("fill-blank", "把字符串 s 居中宽度 10 填充 '*'：s._______(10, '*')。", "center",
     "center 居中填充。", "s.center(10, '*') 返回居中后的字符串。", None),

    ("predict-output", "'abc'.ljust(5, '-') 的结果是？", "abc--",
     "ljust 左对齐填充。", "左对齐，右侧用 '-' 填充至宽度 5。", None),

    ("multiple-choice", "rjust 与 ljust 的区别是？", "rjust 右对齐，ljust 左对齐",
     "对齐方向不同。", "rjust 右对齐并填充；ljust 左对齐并填充。",
     ["完全相同", "rjust 右对齐，ljust 左对齐", "rjust 更快", "ljust 只对数字"]),

    ("fill-blank", "把字符串中所有 tab 替换为空格：s._______('\\t', ' ')。", "replace",
     "replace 替换子串。", "str.replace(old, new) 替换所有匹配。", None),

    ("predict-output", "'  hello  '.lstrip() 的结果是？", "hello  ",
     "lstrip 去左空白。", "只去除左端空白，右端保留。", None),

    ("multiple-choice", "Python 字符串默认编码是？", "Unicode (str)",
     "Python 3 str 是 Unicode。", "Python 3 的 str 是 Unicode 字符串，bytes 才是字节串。",
     ["ASCII", "UTF-8", "Unicode (str)", "GBK"]),

    ("fill-blank", "将列表 ['1','2','3'] 转为字符串 '1,2,3' 用 ','._______(lst)。", "join",
     "join 拼接字符串列表。", "分隔符.join(列表) 拼接为字符串。", None),

    ("predict-output", "len('\\n') 的结果是？", "1",
     "转义字符算一个字符。", "转义字符 '\\n' 算 1 个字符。", None),

    ("multiple-choice", "下列哪个是格式化字符串的现代写法？", "f'{x}'",
     "f-string 最直观。", "Python 3.6+ 的 f-string 性能与可读性最佳。",
     ["'%s' % x", "f'{x}'", "str.format()", "str.template"]),

    ("fill-blank", "判断字符串 s 是否为空：len(s) == ______。", "0",
     "空字符串长度为 0。", "空字符串 '' 的 len 是 0。", None),

    ("predict-output", "'PyThOn'.swapcase() 的结果是？", "pYtHoN",
     "swapcase 大小写互换。", "把小写变大写，大写变小写。", None),

    ("multiple-choice", "translate 与 replace 的区别是？",
     "translate 支持字符映射表，可一次替换多个字符",
     "translate 用表批量替换。", "translate 用翻译表批量替换，replace 替换固定子串。",
     ["完全相同", "translate 支持字符映射表，可一次替换多个字符", "replace 更快", "translate 只对 ASCII"]),

    ("fill-blank", "用 maketrans 配合 translate 时，先建映射表：str.__________(a, b)。", "maketrans",
     "make + trans。", "str.maketrans(a, b) 创建字符映射表。", None),

    ("predict-output", "'hello'.zfill(8) 的结果是？", "000hello",
     "zfill 左侧补零。", "zfill 用 '0' 在左侧填充到指定宽度。", None),

    ("multiple-choice", "判断字符串是否只包含空白用哪个方法？", "isspace",
     "is + space。", "str.isspace() 当所有字符都是空白且非空时返回 True。",
     ["isblank", "isspace", "isempty", "iswhite"]),

    ("fill-blank", "把字符串 s 按行切分用 s._______() 或 s.splitlines()。", "split",
     "split + lines。", "split('\\n') 或 splitlines() 都按行切分。", None),

    ("predict-output", "判断 'Hello123'.isalnum() 的结果是？", "True",
     "isalnum 判断字母或数字。", "只含字母和数字返回 True。", None),

    ("multiple-choice", "Python 字符串底层存储是？", "不可变字节序列",
     "str 不可变。", "Python str 是不可变的 Unicode 字节序列。",
     ["字符数组", "不可变字节序列", "链表", "堆栈"]),
]


# =========================================================
# L16: 文件 I/O
# =========================================================
L16_DATA = [
    ("multiple-choice", "在 Python 中读文件最推荐的方式是？", "with open() as f",
     "with 是上下文管理器。", "with 语句会自动关闭文件，避免资源泄露。",
     ["f = open(); f.close()", "with open() as f", "try/except", "input()"]),

    ("fill-blank", "以只读模式打开文件用 open('f.txt', '______')。", "r",
     "read = r。", "默认就是 'r' 模式，可省略。", None),

    ("predict-output", "open('f.txt', 'w') 的 'w' 模式效果是？", "写入并清空原文件",
     "w = write。", "'w' 模式打开文件会清空原内容用于写入。", None),

    ("multiple-choice", "'a' 模式打开文件的效果是？", "追加写入，保留原内容",
     "a = append。", "'a' 模式从文件末尾追加写入，不清空原内容。",
     ["清空后写入", "追加写入，保留原内容", "只读", "二进制"]),

    ("fill-blank", "读取文件中所有行的方法 f._______()。", "readlines",
     "read + lines。", "f.readlines() 返回每行组成的列表。", None),

    ("predict-output", "读取文件整个内容用哪个方法？", "f.read()",
     "read 一次读完。", "f.read() 返回文件全部内容的字符串。", None),

    ("multiple-choice", "with open() as f: 的好处是？", "自动关闭文件",
     "with 是上下文管理器。", "with 语句确保文件使用完后自动关闭。",
     ["代码更短", "自动关闭文件", "读取更快", "加密文件"]),

    ("fill-blank", "按行遍历文件对象 f 用 for line in ______:。", "f",
     "文件可迭代。", "open() 返回的对象是可迭代的，每次返回一行。", None),

    ("predict-output", "'a' 与 'rb' 模式的关键区别是？", "rb 以二进制读取",
     "b = binary。", "'a' 是文本追加；'rb' 是二进制读取。", None),

    ("multiple-choice", "'x' 模式打开文件时若文件已存在会？", "报错 FileExistsError",
     "x = exclusive。", "'x' 模式是排他创建，文件已存在会抛异常。",
     ["覆盖", "追加", "报错 FileExistsError", "不操作"]),

    ("fill-blank", "写入字符串到文件用 f.______('hello')。", "write",
     "write 写入。", "f.write(s) 把字符串 s 写入文件。", None),

    ("predict-output", "f.writelines(['a', 'b']) 会自动加换行吗？", "不会",
     "writelines 不加分隔符。", "writelines 仅按顺序写入列表中的字符串，不自动加换行。", None),

    ("multiple-choice", "二进制模式与文本模式的区别是？", "返回/写入 bytes 而非 str",
     "b = bytes。", "二进制模式读写的是 bytes 对象。",
     ["更快", "返回/写入 bytes 而非 str", "支持中文", "不能跨平台"]),

    ("fill-blank", "判断文件是否可读 f.______()。", "readable",
     "readable 判断。", "f.readable() 返回文件是否可读。", None),

    ("predict-output", "f.seek(0) 的作用是？", "回到文件开头",
     "seek 移动指针。", "f.seek(0) 把文件指针移动到开头。", None),

    ("multiple-choice", "f.tell() 返回什么？", "当前文件指针位置",
     "tell 报告位置。", "f.tell() 返回当前文件指针的字节位置。",
     ["文件总大小", "当前文件指针位置", "下一行内容", "文件名"]),

    ("fill-blank", "关闭文件用 f.______()。", "close",
     "close 关闭。", "f.close() 关闭文件，释放资源。", None),

    ("predict-output", "文件关闭后再读会怎样？", "抛 ValueError",
     "关闭后不可读。", "ValueError: I/O operation on closed file。", None),

    ("multiple-choice", "以下哪个不是合法的 open mode？", "k",
     "没有 k 模式。", "open mode 包括 r/w/a/x/b/t/+ 等，没有 k。",
     ["r", "w", "a", "k"]),

    ("fill-blank", "同时读写模式用 'r______' 或 'w______'。", "+",
     "+ 表示扩展。", "'r+' 可读可写；'w+' 可写可读，会清空原内容。", None),

    ("predict-output", "'r+' 模式打开文件后指针位置？", "文件开头",
     "r+ 从头开始。", "'r+' 模式打开后文件指针在开头。", None),

    ("multiple-choice", "os.path.exists(path) 的作用是？", "判断路径是否存在",
     "exists 检查存在。", "os.path.exists() 返回路径是否存在。",
     ["读取文件", "判断路径是否存在", "创建目录", "删除文件"]),

    ("fill-blank", "获取文件名后缀用 os.path._______。", "splitext",
     "split + ext。", "os.path.splitext('a.txt') 返回 ('a', '.txt')。", None),

    ("predict-output", "os.path.join('a', 'b', 'c.txt') 的结果是？", "a/b/c.txt",
     "join 拼路径。", "在不同系统上分隔符可能不同，Linux 上为 'a/b/c.txt'。", None),

    ("multiple-choice", "Pathlib 相比 os.path 的优势是？", "面向对象，跨平台",
     "Pathlib 用类表示路径。", "pathlib.Path 提供面向对象的路径操作。",
     ["更快", "面向对象，跨平台", "只能读文本", "只支持 Linux"]),

    ("fill-blank", "用 pathlib 写 Path('a.txt').read______() 读文本。", "text",
     "read_text。", "Path.read_text() 读取文件全部文本内容。", None),

    ("predict-output", "open() 默认 encoding 是？", "locale-dependent (utf-8 in most)",
     "默认与平台相关。", "Python 默认 encoding 依赖系统 locale，现代系统多为 UTF-8。", None),

    ("multiple-choice", "读大文件时推荐用？", "逐行迭代 f",
     "避免一次性加载。", "用 for line in f 逐行处理，避免大文件占内存。",
     ["f.read()", "逐行迭代 f", "f.readlines()", "f.readline() 多次"]),

    ("fill-blank", "用 with 同时打开多个文件用逗号分隔：with open(a) as fa, open(b) as ______:。", "fb",
     "as 多个变量。", "多个 with 上下文可以用逗号分隔。", None),

    ("predict-output", "Path('a/../b.txt').resolve() 简化后是？", "b.txt",
     "resolve 解析 ..。", "'a/../b.txt' 解析为 'b.txt'。", None),

    ("multiple-choice", "以下哪个语句正确关闭文件？", "with open('f') as f: ... 自动关闭",
     "with 自动 close。", "用 with 块离开时自动调用 f.close()。",
     ["f = open()", "f.close() 必写", "with open('f') as f: ... 自动关闭", "不用关闭"]),

    ("fill-blank", "读取单行用 f._________()。", "readline",
     "read + line。", "f.readline() 一次读取一行（包括换行符）。", None),

    ("predict-output", "对大文件 f.read() 与迭代 f 哪个省内存？", "迭代 f",
     "迭代不一次性加载。", "迭代 f 逐行读取，内存占用小。", None),

    ("multiple-choice", "写文件时 flush 的作用是？", "强制把缓冲区数据写入磁盘",
     "flush 刷盘。", "f.flush() 强制将缓冲区的数据写入底层文件。",
     ["关闭文件", "强制把缓冲区数据写入磁盘", "删除文件", "读取文件"]),

    ("fill-blank", "Python 中表示文件路径最现代的库是 ______lib。", "path",
     "pathlib。", "pathlib 是 Python 3.4+ 的现代路径库。", None),

    ("predict-output", "用 'w' 模式打开不存在的文件会？", "创建新文件",
     "w 自动创建。", "'w' 模式打开的文件不存在时会被创建。", None),

    ("multiple-choice", "'r' 模式打开不存在的文件会？", "抛 FileNotFoundError",
     "r 不创建。", "'r' 模式打开不存在的文件会抛 FileNotFoundError。",
     ["创建空文件", "抛 FileNotFoundError", "返回 None", "等待输入"]),

    ("fill-blank", "删除文件用 os.______('f.txt')。", "remove",
     "remove 删除。", "os.remove(path) 删除指定路径的文件。", None),

    ("predict-output", "文件迭代 f 是否会保留换行符？", "会",
     "迭代返回原行。", "for line in f 每次返回包含换行符的一行。", None),

    ("multiple-choice", "shutil 模块主要用于？", "高级文件/目录操作",
     "shutil = shell util。", "shutil 提供复制、移动、删除等高级操作。",
     ["网络请求", "高级文件/目录操作", "日期处理", "正则匹配"]),

    ("fill-blank", "shutil.______(src, dst) 复制文件。", "copy",
     "copy 复制。", "shutil.copy(src, dst) 复制文件并保留权限。", None),

    ("predict-output", "shutil.copytree('a', 'b') 当 b 存在时会？", "抛 FileExistsError",
     "copytree 不覆盖。", "目标已存在时 shutil.copytree 会抛异常。", None),

    ("multiple-choice", "用 pickle 保存对象时文件模式是？", "'wb'",
     "pickle 是二进制。", "pickle 序列化需要二进制写入 'wb'。",
     ["'w'", "'wb'", "'a'", "'r'"]),

    ("fill-blank", "读取 pickle 文件用 pickle.________(f)。", "load",
     "load 反序列化。", "pickle.load(f) 从文件读取并反序列化对象。", None),

    ("predict-output", "pickle 能保存哪些对象？", "几乎所有 Python 对象",
     "pickle 通用。", "pickle 能序列化大多数 Python 对象（函数、类等有局限）。", None),

    ("multiple-choice", "以下哪个不是 open() 的合法 mode？", "rw",
     "rw 不存在。", "合法 mode 组合：r/w/a/x + b/t/+。",
     ["rb", "wb", "rw", "ab"]),

    ("fill-blank", "Path('.').iterdir() 的作用是？", "列出当前目录内容",
     "iterdir 迭代目录。", "iterdir() 返回目录中所有项的迭代器。", None),

    ("predict-output", "Path('a.txt').suffix 的结果是？", ".txt",
     "suffix 是后缀。", "Path('a.txt').suffix 返回 '.txt'。", None),

    ("multiple-choice", "临时文件用哪个模块？", "tempfile",
     "tempfile。", "tempfile 提供创建临时文件/目录的工具。",
     ["os", "sys", "tempfile", "shutil"]),
]


# =========================================================
# L17: 异常处理
# =========================================================
L17_DATA = [
    ("multiple-choice", "捕获所有异常的写法是？", "except Exception as e",
     "Exception 是基类。", "except Exception as e 可捕获大多数异常。",
     ["except:", "except Exception as e", "except All:", "catch:"]),

    ("fill-blank", "try/except 中 else 块在 ______ 发生时不执行。", "异常",
     "else 在成功时执行。", "else 在 try 块没有异常时执行。", None),

    ("predict-output", "finally 块在什么时候执行？", "无论如何都执行",
     "finally 必执行。", "finally 块无论是否有异常都会执行。", None),

    ("multiple-choice", "raise 的作用是？", "主动抛出异常",
     "raise = 抛异常。", "raise 主动抛出指定异常。",
     ["捕获异常", "主动抛出异常", "忽略异常", "打印异常"]),

    ("fill-blank", "自定义异常通常继承自 ______。", "Exception",
     "Exception 基类。", "自定义异常类通常继承 Exception。", None),

    ("predict-output", "try 中 return 后 finally 还会执行吗？", "会",
     "finally 必执行。", "即使 try 中 return，finally 也会执行。", None),

    ("multiple-choice", "except 子句的顺序应该是？", "从具体到宽泛",
     "具体异常先捕获。", "先捕获具体异常，再捕获通用 Exception。",
     ["从宽到窄", "从具体到宽泛", "任意顺序", "按字母"]),

    ("fill-blank", "捕获除零异常用 except ______Error:。", "ZeroDivision",
     "Zero Division。", "ZeroDivisionError 表示除数为零。", None),

    ("predict-output", "ValueError 通常在什么场景出现？", "类型转换或值错误",
     "值不合法。", "int('abc') 等会抛 ValueError。", None),

    ("multiple-choice", "TypeError 表示？", "类型错误",
     "type 不匹配。", "操作或函数应用于不适当类型时抛 TypeError。",
     ["值错误", "类型错误", "键错误", "索引错误"]),

    ("fill-blank", "访问不存在的字典键抛 ______Error。", "Key",
     "Key Error。", "KeyError 表示字典中没有该键。", None),

    ("predict-output", "list = []; list[0] 抛什么异常？", "IndexError",
     "索引越界。", "访问空列表第一个元素会抛 IndexError。", None),

    ("multiple-choice", "KeyboardInterrupt 在什么情况下触发？", "用户按 Ctrl+C",
     "Ctrl+C 触发。", "用户按 Ctrl+C 终止程序时抛 KeyboardInterrupt。",
     ["程序崩溃", "用户按 Ctrl+C", "磁盘满", "内存溢出"]),

    ("fill-blank", "with 语句内部用 ______ 协议处理资源。", "上下文管理",
     "__enter__/__exit__。", "with 协议通过 __enter__ 和 __exit__ 方法管理资源。", None),

    ("predict-output", "assert 1 == 2 会发生？", "抛 AssertionError",
     "断言失败。", "assert 条件为 False 时抛 AssertionError。", None),

    ("multiple-choice", "异常链用哪个关键字？", "from",
     "from 链接异常。", "raise X from Y 表示 X 是由 Y 引起的。",
     ["from", "with", "as", "raise"]),

    ("fill-blank", "except 后用 ______ as e 获取异常对象。", "as",
     "as 绑定变量。", "except Exception as e 把异常绑定到 e。", None),

    ("predict-output", "不存在的属性访问抛 ______Error。", "Attribute",
     "属性错误。", "AttributeError 表示对象没有该属性。", None),

    ("multiple-choice", "以下哪个是 BaseException 的子类？", "KeyboardInterrupt",
     "Ctrl+C 也是异常。", "KeyboardInterrupt 直接继承 BaseException。",
     ["ValueError", "KeyError", "KeyboardInterrupt", "TypeError"]),

    ("fill-blank", "try 块必须有 except 或 ______。", "finally",
     "至少要有一个。", "try 后必须有 except 或 finally。", None),

    ("predict-output", "except: 捕获所有异常吗？", "是，包括 SystemExit",
     "裸 except 很强。", "裸 except 会捕获 BaseException 及其所有子类。", None),

    ("multiple-choice", "import 不存在的模块抛？", "ModuleNotFoundError",
     "模块找不到。", "import 不存在的模块会抛 ModuleNotFoundError（ImportError 子类）。",
     ["NameError", "ModuleNotFoundError", "ImportWarning", "TypeError"]),

    ("fill-blank", "递归过深会抛 ______Error。", "Recursion",
     "Recursion Error。", "RecursionError 表示超出最大递归深度。", None),

    ("predict-output", "str.join(123) 会抛？", "TypeError",
     "类型不对。", "join 需要可迭代的字符串序列，传 int 会抛 TypeError。", None),

    ("multiple-choice", "finally 块中 return 会？", "覆盖 try 中的 return",
     "finally 最后执行。", "finally 中 return 会覆盖 try/except 中的 return。",
     ["报错", "覆盖 try 中的 return", "不影响", "先于 except"]),

    ("fill-blank", "traceback.print_exc() 的作用是？", "打印异常堆栈",
     "traceback 打印。", "traceback.print_exc() 把当前异常的堆栈打印到 stderr。", None),

    ("predict-output", "用 with open() 读不存在的文件会？", "抛 FileNotFoundError",
     "with 不创建。", "open 只读模式不创建文件，抛 FileNotFoundError。", None),

    ("multiple-choice", "logging.exception(e) 的作用是？", "记录异常堆栈",
     "logging 异常。", "logging.exception() 在 ERROR 级别记录并附带堆栈。",
     ["忽略异常", "记录异常堆栈", "抛出异常", "捕获异常"]),

    ("fill-blank", "Python 内置的警告类别基类是 ______。", "Warning",
     "Warning 基类。", "所有警告继承自 Warning（间接自 Exception）。", None),

    ("predict-output", "warnings.warn('msg') 的默认行为是？", "打印一次警告",
     "warn 提示。", "同一警告默认只显示一次。", None),

    ("multiple-choice", "上下文管理器协议需要实现？", "__enter__ 和 __exit__",
     "双方法。", "__enter__ 进入时调用，__exit__ 离开时调用。",
     ["__init__ 和 __del__", "__enter__ 和 __exit__", "__new__ 和 __init__", "__str__ 和 __repr__"]),

    ("fill-blank", "@contextmanager 装饰器来自 ______lib 模块。", "context",
     "contextlib。", "@contextmanager 可以把生成器函数转为上下文管理器。", None),

    ("predict-output", "with 块中 __exit__ 收到异常会怎样？", "返回 True 抑制异常",
     "返回 True 吞掉。", "__exit__ 返回 True 抑制异常，否则异常继续传播。", None),

    ("multiple-choice", "自定义异常通常放在？", "单独的 exceptions 模块",
     "集中管理。", "项目级异常常放在专门的 exceptions.py 中。",
     ["与业务代码混在一起", "单独模块", "main.py", "随便放"]),

    ("fill-blank", "except 后接元组可一次捕获多种异常：except (E1, E2) as ______:。", "e",
     "as 绑定。", "except (E1, E2) as e 同时捕获多种异常。", None),

    ("predict-output", "try 内出现 SyntaxError 会捕获吗？", "不会，编译期异常",
     "语法错误是编译期。", "SyntaxError 在编译期抛出，try 捕获不到运行期才有效。", None),

    ("multiple-choice", "try-except 嵌套时内层异常未被捕获会？", "传给外层",
     "内层未捕获则外层。", "内层 except 没匹配会继续向外传播。",
     ["自动忽略", "传给外层", "程序终止", "内存泄露"]),

    ("fill-blank", "Python 异常的根类是 ______。", "BaseException",
     "所有异常的基类。", "BaseException 是所有内建异常的根类。", None),

    ("predict-output", "在 except 中再次抛出会怎样？", "重新抛出当前异常",
     "raise 单独使用。", "except 中仅写 raise 会重新抛出当前正在处理的异常。", None),

    ("multiple-choice", "以下哪个不是 Python 内建异常？", "NetworkError",
     "没有 NetworkError。", "网络相关错误由 socket/OSError 等表示，没有 NetworkError。",
     ["OSError", "IOError", "NetworkError", "RuntimeError"]),

    ("fill-blank", "捕获 IO 错误用 except ______Error:。", "IO",
     "IO Error。", "IOError 在 Python 3 是 OSError 的别名。", None),

    ("predict-output", "open() 第二个参数错误会抛？", "ValueError",
     "参数错误。", "open 收到非法 mode 时抛 ValueError。", None),

    ("multiple-choice", "try-except 影响性能吗？", "未抛异常时影响极小",
     "正常路径几乎无开销。", "不抛异常时 try 几乎没有性能开销。",
     ["严重影响", "未抛异常时影响极小", "完全没影响", "CPU 翻倍"]),

    ("fill-blank", "sys.exc_info() 返回什么？", "(type, value, traceback) 三元组",
     "当前异常信息。", "sys.exc_info() 返回当前正在处理的异常信息。", None),

    ("predict-output", "with open('f') as f: 内 f.closed 离开 with 后是？", "True",
     "with 后自动关闭。", "with 块结束后 f.closed 为 True。", None),

    ("multiple-choice", "AssertionError 通常用于？", "开发期断言",
     "assert 调试用。", "assert 用于开发期检查，失败抛 AssertionError。",
     ["用户输入校验", "开发期断言", "生产异常处理", "语法检查"]),

    ("fill-blank", "except 块可以省略异常类型吗？", "可以",
     "裸 except 合法。", "裸 except 捕获所有 BaseException 子类。", None),

    ("predict-output", "Python 中哪种异常无法被 try 捕获？", "SystemExit",
     "SystemExit 是 BaseException。", "SystemExit 继承 BaseException，不会被 except Exception 捕获。", None),

    ("multiple-choice", "调试时常用的 'pdb' 是？", "Python 调试器",
     "pdb = Python debugger。", "pdb 是 Python 自带的交互式调试器。",
     ["数据库", "Python 调试器", "性能分析器", "网络库"]),

    ("fill-blank", "进入 pdb 调试用 import pdb; pdb.set_______()。", "trace",
     "set_trace 断点。", "pdb.set_trace() 设置断点，进入交互调试。", None),
]


# =========================================================
# L18: datetime 与 time
# =========================================================
L18_DATA = [
    ("multiple-choice", "获取当前时间用？", "datetime.now()",
     "now 是当前。", "datetime.now() 返回当前本地时间。",
     ["datetime.today()", "datetime.now()", "datetime.current()", "time.now()"]),

    ("fill-blank", "datetime 对象的格式化方法 strf______。", "time",
     "strftime = format time。", "strftime 用格式代码把 datetime 转字符串。", None),

    ("predict-output", "datetime.now().year 返回？", "当前年（int）",
     "year 是属性。", "now().year 是当前年份的整数。", None),

    ("multiple-choice", "timedelta 用在什么场景？", "表示时间间隔",
     "time + delta = 时间差。", "timedelta 表示两个时间之间的差值。",
     ["表示时间间隔", "格式化日期", "解析字符串", "暂停程序"]),

    ("fill-blank", "datetime.now() - datetime(2020,1,1) 的类型是？", "timedelta",
     "差值是 timedelta。", "两个 datetime 相减得到 timedelta。", None),

    ("predict-output", "datetime(2026, 7, 8).strftime('%Y') 的结果是？", "2026",
     "%Y 是 4 位年。", "%Y 输出 4 位年份 2026。", None),

    ("multiple-choice", "%m 在 strftime 中表示？", "月份（01-12）",
     "m = month。", "%m 是 2 位月份，01-12。",
     ["分钟", "月份（01-12）", "毫秒", "周一"]),

    ("fill-blank", "strftime 中表示日的代码是 ______。", "%d",
     "d = day。", "%d 是 2 位日期，01-31。", None),

    ("predict-output", "datetime(2026, 1, 1).weekday() 返回 0 表示？", "周一",
     "周一是 0。", "weekday() 返回 0 是周一，6 是周日。", None),

    ("multiple-choice", "isoformat 的输出格式是？", "YYYY-MM-DDTHH:MM:SS",
     "ISO 8601 标准。", "isoformat 输出 ISO 8601 格式字符串。",
     ["MM/DD/YYYY", "YYYY-MM-DDTHH:MM:SS", "DD-MM-YYYY HH:MM", "epoch 秒数"]),

    ("fill-blank", "把字符串解析为 datetime 用 datetime.__________。", "strptime",
     "strptime = parse time。", "strptime(date_string, format) 解析字符串。", None),

    ("predict-output", "datetime(2026, 7, 8) + timedelta(days=1) 的日期是？", "2026-07-09",
     "加一天。", "2026-07-08 加一天得到 2026-07-09。", None),

    ("multiple-choice", "时间戳（timestamp）表示？", "自 1970-01-01 起的秒数",
     "Unix 时间戳。", "timestamp 是自 epoch（1970-01-01 UTC）起的秒数。",
     ["字符串", "自 1970-01-01 起的秒数", "本地时间", "年"]),

    ("fill-blank", "datetime.now().timestamp() 返回值的类型是 ______。", "float",
     "timestamp 是 float。", "timestamp 返回 float，表示带小数的秒数。", None),

    ("predict-output", "datetime.fromtimestamp(0) 的结果基于？", "UTC 1970-01-01",
     "fromtimestamp 用本地时区。", "fromtimestamp 把时间戳转本地时间 datetime。", None),

    ("multiple-choice", "UTC 时间用哪个方法？", "datetime.utcnow()",
     "UTC = 世界标准时。", "datetime.utcnow() 返回当前 UTC 时间（Python 3.12+ 已废弃）。",
     ["datetime.now()", "datetime.utcnow()", "datetime.today()", "datetime.local()"]),

    ("fill-blank", "datetime 中时区对象用 ______ 模块构造。", "datetime",
     "datetime.timezone。", "datetime.timezone.utc 可作为时区参数。", None),

    ("predict-output", "datetime(2026,1,1) > datetime(2025,1,1) 的结果是？", "True",
     "支持比较。", "datetime 对象支持比较运算。", None),

    ("multiple-choice", "time.sleep(1) 的作用是？", "暂停 1 秒",
     "sleep 休眠。", "time.sleep(s) 让程序暂停 s 秒。",
     ["睡眠 1 小时", "暂停 1 秒", "立刻返回", "结束进程"]),

    ("fill-blank", "time.time() 返回 ______。", "当前时间戳",
     "time.time 时间戳。", "time.time() 返回当前时间戳（float）。", None),

    ("predict-output", "time.time() 的两次调用结果之差是？", "两次调用的间隔秒数",
     "time 差值。", "两次 time.time() 调用之差是经过的秒数。", None),

    ("multiple-choice", "perf_counter 用于？", "高精度性能计时",
     "perf = performance。", "time.perf_counter() 返回高精度性能计数器。",
     ["日期格式化", "高精度性能计时", "睡眠", "解析"]),

    ("fill-blank", "把 timestamp 转 datetime 用 datetime.____________。", "fromtimestamp",
     "from + timestamp。", "datetime.fromtimestamp(ts) 把时间戳转 datetime。", None),

    ("predict-output", "datetime(2026, 7, 8).isocalendar() 返回？", "(年, 周号, 周几)",
     "ISO 日历。", "isocalendar 返回 ISO 格式 (year, week, weekday)。", None),

    ("multiple-choice", "calendar 模块用于？", "日历相关操作",
     "calendar。", "calendar 提供日历打印、月份天数等功能。",
     ["时间戳", "日历相关操作", "性能分析", "日志"]),

    ("fill-blank", "calendar.________(2026) 打印 2026 年的日历。", "prcal",
     "prcal = print cal。", "calendar.prcal(year) 打印整年日历。", None),

    ("predict-output", "calendar.isleap(2024) 的结果是？", "True",
     "2024 是闰年。", "2024 能被 4 整除且不被 100 整除，是闰年。", None),

    ("multiple-choice", "dateutil 相比 datetime 的优势是？", "更灵活的解析和时区",
     "dateutil 增强。", "dateutil 提供更强大的日期解析和相对时间。",
     ["更快", "更灵活的解析和时区", "更轻量", "不需要安装"]),

    ("fill-blank", "dateutil 中解析字符串用 dateutil.______.parse(s)。", "parser",
     "parser 模块。", "dateutil.parser.parse(s) 能自动识别多种日期格式。", None),

    ("predict-output", "datetime.now().microsecond 返回？", "微秒部分（0-999999）",
     "microsecond 微秒。", "microsecond 返回当前时间的微秒部分。", None),

    ("multiple-choice", "%H 在 strftime 中表示？", "24 小时制小时（00-23）",
     "H = Hour 24。", "%H 是 24 小时制小时数，00-23。",
     ["12 小时制小时", "24 小时制小时（00-23）", "毫秒", "时区"]),

    ("fill-blank", "%M 在 strftime 中表示 ______（00-59）。", "分钟",
     "M = Minute。", "%M 是 2 位分钟数。", None),

    ("predict-output", "datetime(2026,7,8).strftime('%A') 返回？", "星期几的英文名",
     "%A = full weekday。", "%A 是完整英文星期名（如 Wednesday）。", None),

    ("multiple-choice", "%p 在 strftime 中表示？", "AM/PM",
     "p = PM。", "%p 输出 AM 或 PM。",
     ["时区", "AM/PM", "百分号", "上午"]),

    ("fill-blank", "获取时间戳对应的本地 datetime 用 datetime._____________。", "fromtimestamp",
     "from + timestamp。", "fromtimestamp 是把时间戳转本地 datetime 的方法。", None),

    ("predict-output", "datetime(2026,1,1).timestamp() 在不同时区下？", "相同（UTC 时间戳）",
     "timestamp 与时区无关。", "timestamp 内部始终是 UTC 时刻。", None),

    ("multiple-choice", "时间运算 datetime + timedelta 的结果是？", "datetime",
     "类型保持。", "datetime + timedelta 还是 datetime。",
     ["str", "datetime", "timedelta", "int"]),

    ("fill-blank", "两个 datetime 相减得到 ______。", "timedelta",
     "差值。", "datetime - datetime = timedelta。", None),

    ("predict-output", "datetime.now() - datetime.now() 的结果是？", "极小 timedelta",
     "两次调用间隔。", "两次调用间隔非常小，结果是接近 0 的 timedelta。", None),

    ("multiple-choice", "如何让 datetime 带时区信息？", "用 timezone.utc 创建",
     "tzinfo。", "datetime.now(tz=timezone.utc) 创建带时区的 datetime。",
     ["加 timezone.utc", "不可能", "用 str", "import zone"]),

    ("fill-blank", "datetime.replace(tzinfo=...) 的作用是？", "替换时区信息",
     "replace 替换字段。", "replace 可替换 datetime 的任意字段，包括时区。", None),

    ("predict-output", "datetime(2026,7,8).timetuple() 返回？", "time.struct_time",
     "struct_time 元组。", "timetuple() 返回 time.struct_time。", None),

    ("multiple-choice", "struct_time 主要用于？", "time 模块函数",
     "time 模块接口。", "time 模块的很多函数使用 struct_time。",
     ["性能分析", "time 模块函数", "字符串解析", "网络"]),

    ("fill-blank", "time.__________() 返回 UTC 时间 struct_time。", "gmtime",
     "gm = Greenwich Mean。", "time.gmtime() 返回当前 UTC 时间的 struct_time。", None),

    ("predict-output", "time.localtime() 与 time.gmtime() 差几小时？", "取决于时区",
     "localtime 包含时区偏移。", "差值等于本地与 UTC 时区差。", None),

    ("multiple-choice", "时间字符串 '2026-07-08' 解析用？",
     "datetime.strptime(s, '%Y-%m-%d')",
     "strptime 解析。", "strptime 配合格式串解析日期字符串。",
     ["datetime(s)", "strptime(s, '%Y-%m-%d')", "dateutil.now(s)", "parse(s)"]),

    ("fill-blank", "格式化 '%Y-%m-%d %H:%M:%S' 输出 '2026-07-08 14:30:00'。", "示例",
     "常见格式。", "这是最常见的日期时间格式串。", None),

    ("predict-output", "datetime(2026,2,29) 会抛？", "ValueError（2026 非闰年）",
     "2026 不是闰年。", "2026 不能被 4 整除，2 月只有 28 天。", None),

    ("multiple-choice", "获取当前时间戳的函数是？", "time.time()",
     "time.time 经典。", "time.time() 是获取 Unix 时间戳最常用方式。",
     ["datetime.now()", "time.time()", "time.now()", "date.now()"]),
]


# =========================================================
# L19: JSON 处理
# =========================================================
L19_DATA = [
    ("multiple-choice", "把 Python 对象转 JSON 字符串用？", "json.dumps",
     "dump + s。", "json.dumps(obj) 把对象序列化为字符串。",
     ["json.to_str", "json.dumps", "json.stringify", "json.encode"]),

    ("fill-blank", "把 JSON 字符串解析为 Python 用 json.______。", "loads",
     "load + s。", "json.loads(s) 把字符串反序列化为 Python 对象。", None),

    ("predict-output", "json.dumps({\"a\": 1}) 的结果是？", "{\"a\": 1}",
     "dumps 默认输出。", "json.dumps 序列化为 JSON 字符串。", None),

    ("multiple-choice", "json.dumps 默认 ensure_ascii 是？", "True",
     "默认转义非 ASCII。", "ensure_ascii=True 把非 ASCII 转成 \\uXXXX。",
     ["True", "False", "None", "空"]),

    ("fill-blank", "要正常输出中文需设置 ensure_ascii=______。", "False",
     "关闭 ASCII 转义。", "ensure_ascii=False 直接输出原字符。", None),

    ("predict-output", "json.dumps({\"a\": 1}, indent=2) 的输出含？", "换行和缩进",
     "indent 美化。", "indent 控制美化输出。", None),

    ("multiple-choice", "json.load(f) 与 json.loads(s) 的区别是？",
     "load 从文件读，loads 从字符串读",
     "load/loads 区别。", "load 从文件对象读，loads 从字符串读。",
     ["完全相同", "load 从文件读，loads 从字符串读", "loads 更快", "load 支持中文"]),

    ("fill-blank", "把对象写入 JSON 文件用 json.______(obj, f)。", "dump",
     "dump 写文件。", "json.dump(obj, f) 直接写入文件。", None),

    ("predict-output", "json.dumps({1, 2, 3}) 会抛？", "TypeError",
     "set 不可 JSON 化。", "set 不是 JSON 可序列化类型。", None),

    ("multiple-choice", "JSON 中布尔值对应 Python 的？", "True/False",
     "true/false → True/False。", "JSON 的 true/false 解析为 Python 的 True/False。",
     ["1/0", "True/False", "yes/no", "on/off"]),

    ("fill-blank", "JSON 中 null 对应 Python 的 ______。", "None",
     "null → None。", "JSON 的 null 解析为 Python 的 None。", None),

    ("predict-output", "json.loads('null') 的结果是？", "None",
     "null → None。", "JSON null 解析为 Python None。", None),

    ("multiple-choice", "json.dumps 处理 datetime 对象会？", "抛 TypeError",
     "datetime 不是 JSON 原生类型。", "需要自定义 encoder 才能序列化 datetime。",
     ["转字符串", "抛 TypeError", "忽略", "转时间戳"]),

    ("fill-blank", "自定义 JSON 编码器继承 json.__________。", "JSONEncoder",
     "JSONEncoder 基类。", "继承 json.JSONEncoder 并重写 default() 方法。", None),

    ("predict-output", "json.dumps([1, 2, 3]) 的结果是？", "[1, 2, 3]",
     "列表 → JSON 数组。", "Python 列表序列化为 JSON 数组。", None),

    ("multiple-choice", "json.dumps 默认分隔符是？", "', ' 和 ': '",
     "默认带空格。", "默认 separators=(', ', ': ')，带空格。",
     ["',', ':'", "', ' 和 ': '", "无分隔符", "', ' 和 ':'"]),

    ("fill-blank", "压缩 JSON 用 separators=(',', ':') 表示 ______ 空格。", "无",
     "最小化输出。", "separators 控制是否插入空格。", None),

    ("predict-output", "json.dumps({'a': 1}, sort_keys=True) 会？", "按键排序",
     "sort_keys 排序。", "sort_keys=True 时输出按键名排序。", None),

    ("multiple-choice", "json.dump 默认 ensure_ascii=True 时中文会？", "转成 \\uXXXX",
     "中文被转义。", "默认把中文转成 \\u 开头的 Unicode 转义。",
     ["正常显示", "转成 \\uXXXX", "报错", "丢失"]),

    ("fill-blank", "json._____ 模块提供工具函数。", " ",
     "json 就是模块。", "import json 后直接使用其函数。", None),

    ("predict-output", "json.loads('[1, 2, 3]')[1] 的结果是？", "2",
     "解析数组并取索引。", "loads 把 JSON 数组解析为 Python list，索引 1 是 2。", None),

    ("multiple-choice", "JSON 数字与 Python 哪种类型对应？", "int 和 float",
     "JSON 数字 → int/float。", "JSON 数字解析为 Python 的 int 或 float。",
     ["Decimal", "int 和 float", "str", "complex"]),

    ("fill-blank", "Python 的 tuple 序列化后会变成 JSON 的 ______。", "array",
     "tuple → array。", "JSON 没有 tuple，序列化为数组。", None),

    ("predict-output", "json.dumps((1, 2)) 的结果是？", "[1, 2]",
     "tuple 变 array。", "tuple 序列化为 JSON 数组。", None),

    ("multiple-choice", "json.dumps 的 default 参数用于？", "处理不可序列化对象",
     "default 回调。", "遇到不可序列化对象时调用 default() 处理。",
     ["处理编码错误", "处理不可序列化对象", "压缩 JSON", "格式化"]),

    ("fill-blank", "json.______(s) 解析 JSON 字符串。", "loads",
     "loads 解析字符串。", "json.loads(s) 把字符串解析为 Python 对象。", None),

    ("predict-output", "json.dumps({'a': float('inf')}) 默认会？", "符合规范但 Python 默认 strict 会抛",
     "inf 默认抛错。", "默认 allow_nan=True 写入 'Infinity'，解析会还原。", None),

    ("multiple-choice", "json.tool 命令用于？", "格式化 JSON 文件",
     "json.tool 格式化。", "python -m json.tool 可美化 JSON。",
     ["压缩", "格式化 JSON 文件", "加密", "验证"]),

    ("fill-blank", "验证 JSON 是否合法用 json.______()。", "loads",
     "loads 失败会抛。", "json.loads 解析失败会抛 JSONDecodeError。", None),

    ("predict-output", "json.loads('{\"a\": 1, }') 会抛？", "JSONDecodeError",
     "尾部多余逗号。", "JSON 规范不允许尾部多余逗号。", None),

    ("multiple-choice", "json 解析失败抛？", "JSONDecodeError",
     "JSONDecodeError 解析异常。", "解析失败抛 json.JSONDecodeError。",
     ["ValueError", "JSONDecodeError", "TypeError", "KeyError"]),

    ("fill-blank", "将类实例序列化到 JSON 通常需要重写 ______ 方法。", "__dict__",
     "返回实例字典。", "自定义 default 返回 obj.__dict__。", None),

    ("predict-output", "json.dumps({'a': 1, 'b': [1,2]}) 的结果含？", "a, b 两个键",
     "嵌套结构。", "嵌套 dict 与 list 都被序列化。", None),

    ("multiple-choice", "JSON 顶层可以是？", "对象/数组/标量",
     "JSON 顶层类型。", "JSON 顶层可以是 object、array、string、number 等。",
     ["只能是对象", "只能是数组", "对象/数组/标量", "只能是字符串"]),

    ("fill-blank", "Python 的 dict 序列化后变成 JSON 的 ______。", "object",
     "dict → object。", "Python dict 对应 JSON object。", None),

    ("predict-output", "json.dumps(True) 的结果是？", "true",
     "True → true。", "Python True 序列化为 JSON true（小写）。", None),

    ("multiple-choice", "用 orjson 库的好处是？", "更快且原生支持更多类型",
     "orjson 高性能。", "orjson 是用 Rust 写的 JSON 库，速度极快。",
     ["更安全", "更快且原生支持更多类型", "体积小", "支持 XML"]),

    ("fill-blank", "json.______ 抛出解析异常。", "JSONDecodeError",
     "JSONDecodeError。", "解析错误时抛 json.JSONDecodeError。", None),

    ("predict-output", "json.dumps({'a': None}) 的结果是？", "{\"a\": null}",
     "None → null。", "Python None 序列化为 JSON null。", None),

    ("multiple-choice", "解析 JSON 后得到 dict，如何安全获取键？", "dict.get(key)",
     "get 安全。", "用 dict.get(key, default) 避免 KeyError。",
     ["dict[key]", "dict.get(key)", "dict.find(key)", "dict.lookup(key)"]),

    ("fill-blank", "JSON 字符串必须使用 ______ 引号。", "双",
     "JSON 规范要求双引号。", "JSON 字符串必须是双引号。", None),

    ("predict-output", "json.loads('true') 的类型是？", "bool",
     "true → bool。", "JSON true 解析为 Python 的 True（bool 类型）。", None),

    ("multiple-choice", "Python 的 set 可直接 json.dumps 吗？", "不能",
     "set 不是 JSON 原生。", "set 会抛 TypeError，需要先转 list。",
     ["能", "不能", "看版本", "能但是空集合才行"]),

    ("fill-blank", "用 json.dumps 处理 NaN 需要 allow_nan=______。", "True",
     "allow_nan 控制。", "allow_nan=True 时 NaN/Infinity 会被写入（不严格符合 JSON）。", None),

    ("predict-output", "json.dumps(float('nan'), allow_nan=True) 的结果是？", "NaN",
     "NaN 字符串。", "输出 'NaN'（非严格 JSON）。", None),

    ("multiple-choice", "json.dumps 的 skipkeys 参数用于？", "跳过不可序列化的 key",
     "skipkeys 跳过。", "skipkeys=True 时遇到非 str/基本类型 key 会跳过。",
     ["跳过 None", "跳过不可序列化的 key", "跳过空对象", "跳过数字"]),

    ("fill-blank", "Python 字典的键通常是 ______ 类型才能 JSON 序列化。", "str",
     "JSON 键必须字符串。", "JSON object 的 key 必须是字符串。", None),

    ("predict-output", "json.dumps({1: 'a'}) 默认会？", "抛 TypeError",
     "int 键不被允许。", "默认 int 作为 key 抛 TypeError。", None),

    ("multiple-choice", "Python 解析 JSON 后 datetime 字段会变？", "str",
     "JSON 没有 datetime。", "解析后 datetime 字段通常变为字符串。",
     ["str", "datetime", "int", "None"]),
]


# =========================================================
# L20: 正则表达式
# =========================================================
L20_DATA = [
    ("multiple-choice", "正则中 \\d 表示？", "数字",
     "d = digit。", "\\d 匹配任意一个数字字符。",
     ["任意字符", "数字", "字母", "空白"]),

    ("fill-blank", "正则中 \\w 表示单词字符（字母数字下划线）用 \\______。", "w",
     "w = word。", "\\w 匹配 [A-Za-z0-9_]。", None),

    ("predict-output", "正则中 \\s 匹配？", "空白字符",
     "s = space。", "\\s 匹配空白字符（空格、tab、换行）。", None),

    ("multiple-choice", "正则中 . 默认匹配？", "除换行外的任意字符",
     "点匹配任意字符。", "默认 . 不匹配换行；用 DOTALL 标志可匹配换行。",
     ["任意字符包括换行", "除换行外的任意字符", "仅数字", "仅字母"]),

    ("fill-blank", "正则中 * 表示前面的元素出现 ______ 次或多次。", "0",
     "* 表示 0+。", "* 表示 0 或多次。", None),

    ("predict-output", "正则中 + 表示？", "1 次或多次",
     "+ 表示 1+。", "+ 表示 1 或多次。", None),

    ("multiple-choice", "正则中 ? 表示？", "0 次或 1 次",
     "? = 0 or 1。", "? 表示 0 或 1 次。",
     ["0 次或 1 次", "至少 1 次", "0 次或多次", "恰好 1 次"]),

    ("fill-blank", "正则中 {m,n} 表示前面的元素出现 m 到 n ______。", "次",
     "{m,n} 区间。", "{m,n} 表示 m 到 n 次。", None),

    ("predict-output", "正则中 ^ 的作用是？", "匹配字符串开头",
     "^ 开头锚点。", "^ 匹配字符串开头（或行首，多行模式下）。", None),

    ("multiple-choice", "正则中 $ 匹配？", "字符串结尾",
     "$ 结尾锚点。", "$ 匹配字符串结尾。",
     ["字符串开头", "字符串结尾", "任意位置", "单词边界"]),

    ("fill-blank", "正则中 \\b 表示 ______ 边界。", "单词",
     "b = boundary。", "\\b 匹配单词字符与非单词字符之间的位置。", None),

    ("predict-output", "正则 [a-z] 表示？", "a 到 z 之间的任意字符",
     "字符范围。", "[a-z] 是字符类，匹配 a 到 z 的任一字符。", None),

    ("multiple-choice", "正则 [^0-9] 表示？", "非数字字符",
     "^ 在 [] 内取反。", "字符类内 ^ 表示取反。",
     ["数字字符", "非数字字符", "字母", "空字符串"]),

    ("fill-blank", "re.______ 模块函数用于在字符串开头匹配。", "match",
     "match 从头开始。", "re.match(pattern, string) 从字符串开头尝试匹配。", None),

    ("predict-output", "re.search 与 re.match 的区别是？", "search 任意位置，match 仅开头",
     "search 任意位置。", "search 找第一个匹配位置；match 仅在开头。", None),

    ("multiple-choice", "re.findall 返回？", "所有匹配的列表",
     "findall 全部返回。", "re.findall 返回所有非重叠匹配的列表。",
     ["第一个匹配", "所有匹配的列表", "match 对象", "迭代器"]),

    ("fill-blank", "re.________ 替换匹配的子串。", "sub",
     "sub = substitute。", "re.sub(pattern, repl, string) 替换。", None),

    ("predict-output", "re.split(r'\\s+', 'a b  c') 的结果是？", "['a', 'b', 'c']",
     "按空白切分。", "按一个或多个空白切分。", None),

    ("multiple-choice", "正则中 | 的作用是？", "或",
     "| = or。", "| 在正则中表示或（分支）。",
     ["与", "或", "非", "异或"]),

    ("fill-blank", "正则中 () 用于 ______。", "分组捕获",
     "() = group。", "() 把多个字符组合成子组并捕获。", None),

    ("predict-output", "re.match(r'(\\d+)', '123abc').group(1) 的结果是？", "123",
     "第 1 组捕获。", "group(1) 返回第一个捕获组。", None),

    ("multiple-choice", "非贪婪匹配用？", "*? 或 +?",
     "? 表示非贪婪。", "在量词后加 ? 表示非贪婪（最小匹配）。",
     ["*?", "+?", "*? 或 +?", "?!"]),

    ("fill-blank", "正则中 .* 默认是 ______ 匹配。", "贪婪",
     "默认贪婪。", "默认量词是贪婪的（最大匹配）。", None),

    ("predict-output", "re.findall(r'\\d+', 'a1b22c333') 的结果是？", "['1', '22', '333']",
     "findall 提取所有数字。", "匹配所有连续数字片段。", None),

    ("multiple-choice", "re.IGNORECASE 标志用于？", "忽略大小写",
     "re.I 忽略大小写。", "re.IGNORECASE 或 re.I 使匹配忽略大小写。",
     ["忽略大小写", "多行模式", "匹配换行", "Unicode 模式"]),

    ("fill-blank", "re.MULTILINE 标志让 ^ 和 $ 匹配每行 ______。", "首尾",
     "多行模式。", "re.MULTILINE 让 ^/$ 匹配每行首尾。", None),

    ("predict-output", "re.findall(r'\\b\\w+\\b', 'Hello, world!') 的结果是？", "['Hello', 'world']",
     "提取单词。", "\\b\\w+\\b 提取所有单词。", None),

    ("multiple-choice", "命名分组用？", "(?P<name>...)",
     "?P<name> 命名。", "命名分组的语法是 (?P<name>...)。",
     ["(?name...)", "(?P<name>...)", "(?<name>...)", "(?name=...)"]),

    ("fill-blank", "re.__________ 预编译正则返回 Pattern 对象。", "compile",
     "compile 编译。", "re.compile(pattern) 返回可复用的 Pattern 对象。", None),

    ("predict-output", "Pattern.findall 与 re.findall 的关系是？", "等价但前者更快（复用）",
     "Pattern 复用。", "Pattern.findall 等价于 re.findall，但预编译更快。", None),

    ("multiple-choice", "re.sub 的 count 参数控制？", "替换次数",
     "count 限制次数。", "count 控制最大替换次数。",
     ["匹配次数", "替换次数", "捕获组数", "None"]),

    ("fill-blank", "正则中 (?=...) 是 ______ 先行断言。", "正向",
     "正向 lookahead。", "(?=...) 是正向先行断言（lookahead）。", None),

    ("predict-output", "(?<=@)\\w+ 在 'a@b.com' 中匹配？", "b",
     "后顾断言。", "(?<=@) 是后顾，匹配 @ 后的 \\w+。", None),

    ("multiple-choice", "正则中 (?!...) 是？", "负向先行断言",
     "负向 lookahead。", "(?!...) 表示负向先行断言。",
     ["正向断言", "负向先行断言", "后顾", "非捕获"]),

    ("fill-blank", "Python 的 re 模块用 ______ 语言实现的？", "C",
     "re 模块底层 C。", "标准库 re 是 C 实现的。", None),

    ("predict-output", "re.match(r'a.b', 'a\\nb') 的默认结果是？", "None",
     ". 不匹配换行。", ". 默认不匹配换行，返回 None。", None),

    ("multiple-choice", "使用 re.VERBOSE 可以？", "在正则中加注释和空白",
     "re.X 注释。", "re.VERBOSE 或 re.X 允许正则中加注释和空白。",
     ["加速", "在正则中加注释和空白", "支持 Unicode", "禁用贪婪"]),

    ("fill-blank", "raw 字符串 r'...' 在正则中用于避免 ______ 转义。", "反斜杠",
     "raw 字符串。", "r'\\d' 避免 \\\\d 双重转义。", None),

    ("predict-output", "len(re.findall(r'.', 'abc')) 的结果是？", "3",
     "3 个字符。", "'abc' 有 3 个字符，. 匹配每个。", None),

    ("multiple-choice", "re.finditer 返回？", "match 迭代器",
     "finditer 迭代。", "re.finditer 返回 match 对象的迭代器。",
     ["列表", "match 迭代器", "count", "None"]),

    ("fill-blank", "match.______() 返回完整匹配字符串。", "group",
     "group(0)。", "match.group() 等同于 group(0)，返回完整匹配。", None),

    ("predict-output", "re.sub(r'\\d', '*', 'a1b2') 的结果是？", "a*b*",
     "替换数字。", "把每个数字替换为 *。", None),

    ("multiple-choice", "正则中 \\D 匹配？", "非数字字符",
     "D = not digit。", "\\D 匹配非数字字符。",
     ["数字", "非数字字符", "字母", "空白"]),

    ("fill-blank", "\\W 表示 ______ 字符。", "非单词",
     "W = not word。", "\\W 匹配非单词字符 [\\W]。", None),

    ("predict-output", "re.match(r'\\d+', 'abc') 的结果是？", "None",
     "开头不匹配。", "开头不是数字，match 返回 None。", None),

    ("multiple-choice", "如何匹配点号本身？", "\\.",
     "转义点。", "点 . 是元字符，要匹配字面量需 \\.。",
     [".", "\\.", "[.]", "*."]),

    ("fill-blank", "[^abc] 表示除 a、b、c 之外的 ______。", "任意字符",
     "字符类取反。", "[^abc] 是字符类取反，匹配 a、b、c 之外的任意字符。", None),

    ("predict-output", "re.findall(r'[A-Z]', 'aBcDe') 的结果是？", "['B', 'D']",
     "找大写字母。", "[A-Z] 匹配大写字母 B 和 D。", None),

    ("multiple-choice", "正则中 (?i) 标志表示？", "忽略大小写",
     "内联 i。", "(?i) 是内联标志，忽略大小写。",
     ["多行", "忽略大小写", "DOTALL", "Unicode"]),
]


# =========================================================
# L21: 猜数字游戏
# =========================================================
L21_DATA = [
    ("multiple-choice", "Python 中生成随机整数用？", "random.randint(a, b)",
     "randint 闭区间。", "random.randint(a, b) 返回 [a, b] 区间的整数。",
     ["random.random()", "random.randint(a, b)", "random.int(a, b)", "rand.int(a, b)"]),

    ("fill-blank", "生成 [0, 1) 之间随机小数用 random.______()。", "random",
     "random() 半开区间。", "random.random() 返回 [0, 1) 的浮点数。", None),

    ("predict-output", "random.randint(1, 3) 的可能值？", "1, 2 或 3",
     "randint 闭区间。", "randint(a, b) 包含两端。", None),

    ("multiple-choice", "random.choice(seq) 的作用是？", "随机选一个元素",
     "choice 单选。", "random.choice 从非空序列随机选一个元素。",
     ["排序", "随机选一个元素", "洗牌", "采样多个"]),

    ("fill-blank", "random.________(seq) 打乱原序列顺序。", "shuffle",
     "shuffle 洗牌。", "shuffle 原地打乱。", None),

    ("predict-output", "random.choice([1,2,3]) 的可能值？", "1, 2 或 3",
     "choice 选一个。", "从列表中随机选一个。", None),

    ("multiple-choice", "random.sample(seq, k) 的作用是？", "无重复随机采样 k 个",
     "sample 无放回。", "sample 返回不重复的 k 个样本。",
     ["有重复采样", "无重复随机采样 k 个", "全排列", "排序"]),

    ("fill-blank", "设置随机种子用 random.______。", "seed",
     "seed 种子。", "random.seed(n) 设置随机种子以便复现。", None),

    ("predict-output", "random.random() 总是返回？", "[0, 1) 浮点数",
     "半开区间。", "random.random 返回 [0, 1) 的浮点数。", None),

    ("multiple-choice", "if 后面跟 elif 的作用是？", "否则如果",
     "elif = else if。", "elif 在前一个条件不满足时检查另一个条件。",
     ["否则", "否则如果", "结束", "循环"]),

    ("fill-blank", "while 循环的条件为 ______ 时停止。", "False",
     "条件为假停止。", "while 条件为 False 时停止。", None),

    ("predict-output", "break 在循环中的作用是？", "立即终止循环",
     "break 跳出。", "break 立即终止当前循环。", None),

    ("multiple-choice", "continue 的作用是？", "跳过本轮，进入下一轮",
     "continue 跳本轮。", "continue 跳过本轮剩余代码，进入下一轮。",
     ["终止循环", "跳过本轮，进入下一轮", "重启循环", "无作用"]),

    ("fill-blank", "input() 返回值的类型是 ______。", "str",
     "input 都是字符串。", "input() 始终返回字符串，需要手动转换。", None),

    ("predict-output", "input('guess: ') 的返回值类型？", "str",
     "input 是字符串。", "不管用户输入什么，input 都返回 str。", None),

    ("multiple-choice", "将字符串转 int 用？", "int(s)",
     "int 转换。", "int('123') 把字符串转为整数。",
     ["int(s)", "str(s)", "float(s)", "num(s)"]),

    ("fill-blank", "try/except 中用 except ______Error: 捕获值错误。", "Value",
     "ValueError。", "int('abc') 抛 ValueError。", None),

    ("predict-output", "while True: 是？", "无限循环",
     "True 永不停止。", "while True 配合 break 形成可控无限循环。", None),

    ("multiple-choice", "if/elif/else 的 else 块在？", "所有条件都不满足时执行",
     "else 是兜底。", "else 是所有 if/elif 都不匹配时执行。",
     ["第一个 if 不满足时", "所有条件都不满足时执行", "总是执行", "不会执行"]),

    ("fill-blank", "用 f-string 嵌入变量：f'答案是 {______}'。", "answer",
     "变量替换。", "f-string 在 {} 中放变量名。", None),

    ("predict-output", "1 < 2 < 3 的结果是？", "True",
     "链式比较。", "Python 支持链式比较，等价于 1 < 2 and 2 < 3。", None),

    ("multiple-choice", "and / or / not 是？", "逻辑运算符",
     "布尔运算。", "and/or/not 是 Python 的逻辑运算符。",
     ["算术", "逻辑运算符", "位运算", "赋值"]),

    ("fill-blank", "表示「大于等于」用 ______。", ">=",
     ">= 大于等于。", ">= 运算符。", None),

    ("predict-output", "True and False 的结果是？", "False",
     "and 都真才真。", "True and False = False。", None),

    ("multiple-choice", "True or False 的结果是？", "True",
     "or 一真就真。", "True or False = True。",
     ["True", "False", "None", "Error"]),

    ("fill-blank", "not True 的结果是 ______。", "False",
     "not 取反。", "not True = False。", None),

    ("predict-output", "max(1, 5, 3) 的结果是？", "5",
     "max 取最大。", "max 返回最大元素 5。", None),

    ("multiple-choice", "min(1, 5, 3) 的结果是？", "1",
     "min 取最小。", "min 返回最小元素 1。",
     ["1", "3", "5", "avg"]),

    ("fill-blank", "abs(-5) 的结果是 ______。", "5",
     "abs 绝对值。", "abs 返回参数的绝对值。", None),

    ("predict-output", "round(3.7) 的结果是？", "4",
     "round 四舍五入。", "round(3.7) = 4。", None),

    ("multiple-choice", "print 多个参数默认用什么分隔？", "空格",
     "print 默认空格。", "print(a, b) 默认用空格分隔。",
     ["逗号", "空格", "无分隔符", "换行"]),

    ("fill-blank", "print 默认以 ______ 结尾。", "换行",
     "默认 end='\\n'。", "print 的默认 end 参数是 '\\n'。", None),

    ("predict-output", "print('a', end='') 的效果是？", "不换行",
     "end='' 不换行。", "end='' 关闭末尾换行。", None),

    ("multiple-choice", "用 sys.exit() 的作用是？", "退出程序",
     "sys.exit 退出。", "sys.exit() 终止 Python 解释器。",
     ["暂停", "退出程序", "重启", "无作用"]),

    ("fill-blank", "import ______ as rd 引入 random。", "random",
     "import random。", "import random as rd。", None),

    ("predict-output", "random.uniform(1, 5) 返回？", "[1, 5] 之间浮点数",
     "uniform 区间。", "uniform(a, b) 返回 [a, b] 之间的浮点数。", None),

    ("multiple-choice", "实现猜数字游戏中统计猜测次数用？", "计数器变量",
     "attempts += 1。", "用 attempts 变量累加猜测次数。",
     ["len()", "计数器变量", "sum()", "count()"]),

    ("fill-blank", "退出 while 循环用 ______ 关键字。", "break",
     "break 跳出。", "猜中后用 break 退出循环。", None),

    ("predict-output", "for i in range(3): print(i) 输出？", "0 1 2",
     "range(3)。", "range(3) 产生 0,1,2。", None),

    ("multiple-choice", "range(2, 10, 2) 的值是？", "2, 4, 6, 8",
     "step=2。", "从 2 开始到 10 之前，步长 2。",
     ["1,2,3", "2, 4, 6, 8", "0,2,4,6,8", "2,3,4"]),

    ("fill-blank", "想要猜数字 1-100，随机数用 random.______(1, 100)。", "randint",
     "randint 闭区间。", "random.randint(1, 100) 包含两端。", None),

    ("predict-output", "如果 target=50，guess=70，输出？", "70 太大了",
     "70 > 50。", "70 大于 50，输出「太大了」。", None),

    ("multiple-choice", "input() 引发 EOFError 通常因为？", "无输入或流关闭",
     "没有输入。", "input() 在无输入时抛 EOFError。",
     ["网络问题", "无输入或流关闭", "权限", "语法错"]),

    ("fill-blank", "把 guess 转整数：int(______)。", "guess",
     "变量名。", "int(guess) 把字符串转整数。", None),

    ("predict-output", "如果猜了 3 次才中，attempts 最终值？", "3",
     "attempts 累加。", "每次猜测 attempts += 1，3 次后为 3。", None),

    ("multiple-choice", "猜数字游戏常用模块是？", "random + input",
     "random + input。", "random 生成数，input 获取用户输入。",
     ["os + sys", "random + input", "json + csv", "math + os"]),

    ("fill-blank", "在浏览器中 input() 通常被替换为 ______ input。", "弹窗",
     "prompt。", "浏览器环境 input 会用 prompt 弹窗模拟。", None),

    ("predict-output", "用 random.seed(0) 后多次运行结果？", "相同序列",
     "种子可复现。", "相同种子下 random 序列可复现。", None),

    ("multiple-choice", "猜数字游戏中「再玩一次」常用模式是？", "外层 while True",
     "外层循环。", "外层 while True 包裹游戏逻辑，猜中后询问是否继续。",
     ["if/else", "外层 while True", "递归", "for 循环"]),

    ("fill-blank", "把猜测次数与上限比较用 ______ 限制最大尝试。", "if",
     "if 限制。", "if attempts >= max_tries 触发结束条件。", None),
]


# =========================================================
# L22: 简易计算器
# =========================================================
L22_DATA = [
    ("multiple-choice", "Python 中创建匿名函数的关键字是？", "lambda",
     "λ。", "lambda 用于创建单行匿名函数。",
     ["def", "lambda", "function", "fn"]),

    ("fill-blank", "lambda x, y: x + y 创建一个 ______ 函数。", "匿名",
     "匿名函数。", "lambda 表达式返回匿名函数对象。", None),

    ("predict-output", "(lambda x: x * 2)(3) 的结果是？", "6",
     "调用 lambda。", "lambda 接收 3 返回 3*2 = 6。", None),

    ("multiple-choice", "add = lambda x, y: x + y; add(2, 3) 的结果是？", "5",
     "lambda 赋值。", "add(2, 3) = 2 + 3 = 5。",
     ["6", "5", "23", "lambda"]),

    ("fill-blank", "将函数作为参数传给 sorted 的 key 参数用 ______ 函数。", "lambda",
     "key 常用 lambda。", "sorted(key=lambda x: ...) 用 lambda。", None),

    ("predict-output", "sorted([3, 1, 2], key=lambda x: -x) 的结果是？", "[3, 2, 1]",
     "降序排序。", "key 用负值实现降序。", None),

    ("multiple-choice", "map(func, iterable) 的作用是？", "对每个元素应用 func",
     "map 映射。", "map 把 func 应用于 iterable 每个元素。",
     ["过滤", "对每个元素应用 func", "求和", "排序"]),

    ("fill-blank", "filter(func, iterable) 保留 func 返回 ______ 的元素。", "True",
     "filter 过滤。", "filter 保留 func 返回 True 的元素。", None),

    ("predict-output", "list(filter(lambda x: x % 2 == 0, [1,2,3,4])) 的结果是？", "[2, 4]",
     "过滤偶数。", "只保留偶数 2, 4。", None),

    ("multiple-choice", "reduce(func, seq) 首次调用 func 时？", "用 seq 的前两个元素",
     "reduce 第一次用前两个。", "reduce 把前两个元素传给 func。",
     ["用全部元素", "用 seq 的前两个元素", "用第一个元素 + 初始值", "随机"]),

    ("fill-blank", "Python 3 中 reduce 移到 ______ 模块。", "functools",
     "reduce 在 functools。", "from functools import reduce。", None),

    ("predict-output", "functools.reduce(lambda a, b: a + b, [1, 2, 3, 4]) 的结果是？", "10",
     "累加。", "1+2+3+4 = 10。", None),

    ("multiple-choice", "以下哪个是合法的 lambda？", "lambda x: x * 2",
     "lambda 语法。", "lambda 参数列表: 表达式。",
     ["lambda x: x * 2", "lambda(x): x * 2", "def lambda x: x * 2", "lambda x -> x * 2"]),

    ("fill-blank", "lambda 体只能是 ______ 个表达式。", "一",
     "lambda 单表达式。", "lambda 不能包含语句，只能是单个表达式。", None),

    ("predict-output", "(lambda: 42)() 的结果是？", "42",
     "无参 lambda。", "lambda: 42 返回常数 42。", None),

    ("multiple-choice", "以下哪个是字典映射运算符的实现方式？", "dict[key]",
     "dict[key] 映射。", "字典用 [key] 访问。",
     ["dict.get", "dict[key]", "dict.find", "dict.lookup"]),

    ("fill-blank", "字典中安全取值的字典方法是 d.______(key, default)。", "get",
     "get 默认值。", "d.get(key, default) 找不到时返回 default。", None),

    ("predict-output", "d = {'+': lambda a,b: a+b}; d['+'](2,3) 的结果是？", "5",
     "字典存函数。", "字典可以存可调用对象，按键调用。", None),

    ("multiple-choice", "用字典实现计算器的优点是？", "分支少、易扩展",
     "映射 vs if/elif。", "用 dict[op] 替代 if/elif 链，扩展性更好。",
     ["更快", "分支少、易扩展", "更安全", "更小"]),

    ("fill-blank", "检测除零错误用 Zero________Error。", "Division",
     "ZeroDivision。", "ZeroDivisionError 是除数为零的异常。", None),

    ("predict-output", "10 / 0 会抛？", "ZeroDivisionError",
     "/ 0 报错。", "除法运算除以 0 抛 ZeroDivisionError。", None),

    ("multiple-choice", "Python 整数除法 // 的结果是？", "向下取整的整数",
     "// 整除。", "// 是 floor division，结果是整数（向下取整）。",
     ["浮点", "向下取整的整数", "向上取整", "四舍五入"]),

    ("fill-blank", "10 % 3 的结果是 ______。", "1",
     "% 取余。", "10 除 3 余 1。", None),

    ("predict-output", "2 ** 3 的结果是？", "8",
     "** 幂。", "2 的 3 次方 = 8。", None),

    ("multiple-choice", "input() 返回字符串，比较两个数字前需要？", "int() 转换",
     "int() 转换。", "input() 返回 str，比较前需要 int() / float() 转换。",
     ["直接比较", "int() 转换", "str 排序", "加引号"]),

    ("fill-blank", "eval('1 + 2') 的结果是 ______。", "3",
     "eval 求值。", "eval 执行字符串表达式。", None),

    ("predict-output", "eval('3 * 4') 的结果是？", "12",
     "eval 求值。", "eval('3 * 4') = 12。", None),

    ("multiple-choice", "eval 的安全风险来自？", "执行任意输入",
     "eval 可执行任意代码。", "eval 会执行任意字符串，可能被注入。",
     ["语法错误", "执行任意输入", "类型不匹配", "慢"]),

    ("fill-blank", "ast.literal_eval 用于 ______ 求值。", "安全",
     "literal_eval 安全。", "ast.literal_eval 只能解析字面量，更安全。", None),

    ("predict-output", "ast.literal_eval('[1, 2, 3]') 的结果是？", "[1, 2, 3]",
     "literal_eval 解析字面量。", "解析为 Python 列表。", None),

    ("multiple-choice", "Python 中实现简单的 switch/case 常用？", "dict 映射",
     "dict 代替 switch。", "Python 没有 switch，常用 dict 模拟。",
     ["switch/case 关键字", "dict 映射", "match 关键字", "if/else 链"]),

    ("fill-blank", "Python 3.10+ 引入 match-case 语法关键字是 ______。", "match",
     "match 关键字。", "Python 3.10+ 的 match 关键字。", None),

    ("predict-output", "float('inf') 表示？", "正无穷",
     "inf = infinity。", "float('inf') 表示正无穷大。", None),

    ("multiple-choice", "如何优雅处理非法输入？", "try/except ValueError",
     "try/except。", "用 try/except 捕获 ValueError 并提示重新输入。",
     ["if 嵌套", "try/except ValueError", "os.system", "sys.exit"]),

    ("fill-blank", "try/except 后重新获取输入用 ______ 回到循环顶。", "continue",
     "continue 重新循环。", "except 后 continue 回到输入循环。", None),

    ("predict-output", "len('hello') 的结果是？", "5",
     "len 字符串长度。", "'hello' 长度 5。", None),

    ("multiple-choice", "在函数中返回多个值用？", "元组",
     "元组/解包。", "Python 函数可以 return a, b 返回元组。",
     ["数组", "元组", "字典", "字符串"]),

    ("fill-blank", "def calc(a, op, b): 中 op 通常是 ______ 类型。", "str",
     "op 是字符串。", "运算符用字符串如 '+', '-' 表示。", None),

    ("predict-output", "True + True 的结果是？", "2",
     "bool 是 int 子类。", "True 等价于 1，1+1=2。", None),

    ("multiple-choice", "Python 算术运算 * 与列表配合表示？", "重复",
     "* 重复。", "[1,2] * 3 = [1,2,1,2,1,2]。",
     ["复制", "重复", "乘法", "拼接"]),

    ("fill-blank", "定义函数用 ______ 关键字。", "def",
     "def 定义函数。", "def 关键字定义函数。", None),

    ("predict-output", "def f(x): return x*2; f(5) 的结果是？", "10",
     "调用函数。", "f(5) = 5*2 = 10。", None),

    ("multiple-choice", "默认参数在函数签名中放在？", "必需参数之后",
     "默认参数在后。", "默认参数必须放在必需参数之后。",
     ["任意位置", "必需参数之后", "最前", "最后"]),

    ("fill-blank", "def f(x, y=10): 中 y=10 是 ______ 参数。", "默认",
     "默认值。", "带默认值的形参。", None),

    ("predict-output", "f(5) 调用 def f(x, y=10): print(x+y) 的输出？", "15",
     "默认参数补全。", "y 默认 10，5+10=15。", None),

    ("multiple-choice", "异常处理时获取异常对象用？", "except ... as e",
     "as e 绑定。", "except ValueError as e 可绑定异常对象。",
     ["except e", "except ... as e", "catch e", "raise e"]),

    ("fill-blank", "自定义异常类通常继承 ______。", "Exception",
     "Exception 基类。", "class MyError(Exception): pass。", None),

    ("predict-output", "def add(a, b=2): return a+b; add(3) 的结果是？", "5",
     "默认参数。", "b 默认 2，3+2=5。", None),

    ("multiple-choice", "Python 中 ** 运算符的优先级高于 * 吗？", "是",
     "** 优先级高。", "** 优先级高于 *，先做幂运算。",
     ["是", "否", "相同", "看情况"]),

    ("fill-blank", "在 REPL 中按 ______ 退出交互式 Python。", "Ctrl+D",
     "Ctrl+D 退出。", "Linux/macOS 下 Ctrl+D，Windows 下 Ctrl+Z + Enter。", None),
]


# =========================================================
# L23: Todo List CLI
# =========================================================
L23_DATA = [
    ("multiple-choice", "列表的 append 方法返回新列表吗？", "否，原地修改",
     "append 原地。", "append 修改原列表并返回 None。",
     ["是", "否，原地修改", "取决于类型", "返回 None"]),

    ("fill-blank", "向列表 lst 末尾添加元素用 lst.______。", "append",
     "append 追加。", "lst.append(x) 把 x 加到末尾。", None),

    ("predict-output", "[1, 2, 3].append(4) 后列表是？", "[1, 2, 3, 4]",
     "append 末尾。", "append 把 4 加到列表末尾。", None),

    ("multiple-choice", "list.insert(i, x) 的作用是？", "在索引 i 处插入 x",
     "insert 任意位置。", "insert 在指定位置插入元素。",
     ["末尾追加", "在索引 i 处插入 x", "替换", "删除"]),

    ("fill-blank", "删除列表中第一次出现的 x 用 lst.______(x)。", "remove",
     "remove 按值。", "lst.remove(x) 删除第一个匹配的 x。", None),

    ("predict-output", "[1, 2, 3].remove(2) 后列表是？", "[1, 3]",
     "remove 删除。", "2 被删除，剩 [1, 3]。", None),

    ("multiple-choice", "list.pop() 不带参数时？", "删除并返回最后一个元素",
     "pop 默认末尾。", "pop() 默认弹栈顶（最后一个）。",
     ["删第一个", "删除并返回最后一个元素", "报错", "返回第一个"]),

    ("fill-blank", "list.pop(i) 删除并返回索引 i 处的 ______。", "元素",
     "pop 返回元素。", "pop(i) 删除索引 i 处并返回该元素。", None),

    ("predict-output", "[1, 2, 3].pop() 的返回值是？", "3",
     "pop 末尾。", "弹出最后一个元素 3。", None),

    ("multiple-choice", "list.extend(other) 的作用是？", "把 other 元素追加到列表",
     "extend 合并。", "extend 接受可迭代对象并逐个追加。",
     ["返回新列表", "把 other 元素追加到列表", "替换列表", "排序"]),

    ("fill-blank", "[1,2] + [3,4] 得到新列表 ______。", "[1, 2, 3, 4]",
     "+ 拼接。", "列表 + 列表 = 新列表。", None),

    ("predict-output", "list[0] 的作用是？", "访问第一个元素",
     "索引访问。", "list[0] 访问索引 0 的元素。", None),

    ("multiple-choice", "list[-1] 表示？", "最后一个元素",
     "负索引。", "负数索引从末尾计数，-1 是最后一个。",
     ["第一个", "最后一个元素", "报错", "None"]),

    ("fill-blank", "list[1:4] 是列表的 ______。", "切片",
     "切片操作。", "[1:4] 切片返回子列表。", None),

    ("predict-output", "[1,2,3,4,5][1:4] 的结果是？", "[2, 3, 4]",
     "切片 1-4。", "切片 [1,4) = [2,3,4]。", None),

    ("multiple-choice", "list.index(x) 的作用是？", "返回 x 第一次出现的索引",
     "index 找位置。", "index 返回第一个匹配 x 的索引。",
     ["计数", "返回 x 第一次出现的索引", "替换", "删除"]),

    ("fill-blank", "list.______(x) 统计 x 出现次数。", "count",
     "count 计数。", "list.count(x) 返回 x 出现次数。", None),

    ("predict-output", "[1, 2, 2, 3].count(2) 的结果是？", "2",
     "count 2 出现 2 次。", "[1,2,2,3] 中 2 出现 2 次。", None),

    ("multiple-choice", "list.sort() 与 sorted(list) 的区别是？",
     "sort 原地修改，sorted 返回新列表",
     "sort vs sorted。", "sort 修改原列表；sorted 返回新列表。",
     ["完全相同", "sort 原地修改，sorted 返回新列表", "sort 更快", "sorted 更慢"]),

    ("fill-blank", "list.______(key=...) 接受 key 函数排序。", "sort",
     "sort with key。", "list.sort(key=func) 按 func 结果排序。", None),

    ("predict-output", "sorted([3, 1, 2]) 的结果是？", "[1, 2, 3]",
     "sorted 升序。", "sorted 默认升序。", None),

    ("multiple-choice", "list.reverse() 的作用是？", "原地反转列表",
     "reverse 反转。", "reverse 原地反转列表元素顺序。",
     ["返回新列表", "原地反转列表", "排序", "清空"]),

    ("fill-blank", "list._______() 清空列表。", "clear",
     "clear 清空。", "list.clear() 删除所有元素。", None),

    ("predict-output", "len([1, 2, 3]) 的结果是？", "3",
     "len 长度。", "list 有 3 个元素。", None),

    ("multiple-choice", "'in' 运算符检查？", "元素是否在列表中",
     "成员检查。", "'x' in lst 返回 x 是否在列表中。",
     ["索引", "元素是否在列表中", "长度", "类型"]),

    ("fill-blank", "'for x in lst:' 会遍历列表中的每个 ______。", "元素",
     "迭代元素。", "for 循环依次访问列表的每个元素。", None),

    ("predict-output", "for i, x in enumerate(['a','b']): print(i, x) 的输出？", "0 a\\n1 b",
     "enumerate 给索引。", "enumerate 返回 (index, value) 元组。", None),

    ("multiple-choice", "enumerate(iter) 的作用是？", "同时返回索引和元素",
     "enumerate 索引+值。", "enumerate 把索引和元素配对返回。",
     ["排序", "同时返回索引和元素", "过滤", "统计"]),

    ("fill-blank", "zip(['a','b'], [1,2]) 的结果是？", "[('a', 1), ('b', 2)]",
     "zip 配对。", "zip 把多个可迭代对象按位置配对。", None),

    ("predict-output", "list(zip([1,2], ['a','b'])) 的结果是？", "[(1, 'a'), (2, 'b')]",
     "zip 转列表。", "zip 返回迭代器，list 转列表。", None),

    ("multiple-choice", "用字典表示 Todo 状态：'task' 与 'done' 通常是？", "键",
     "dict 的键。", "字典用 'task' 和 'done' 作为键。",
     ["值", "键", "方法", "类型"]),

    ("fill-blank", "枚举字典的 key-value 用 dict.________。", "items",
     "items 方法。", "dict.items() 返回 (key, value) 视图。", None),

    ("predict-output", "{'a': 1, 'b': 2}.items() 的类型是？", "dict_items",
     "dict_items 视图。", "items 返回 dict_items 视图对象。", None),

    ("multiple-choice", "删除字典键 d.pop('k', default) 的作用是？",
     "删除 k 并返回值，无则返回 default",
     "pop 带默认值。", "pop 删除并返回值，缺键时返回 default。",
     ["仅删除", "删除 k 并返回值，无则返回 default", "取最后一个", "排序"]),

    ("fill-blank", "判断键 k 是否在字典 d 中用 ______。", "k in d",
     "成员检查。", "'k' in d 判断键是否存在。", None),

    ("predict-output", "{'a': 1, 'b': 2}['a'] 的结果是？", "1",
     "按键取值。", "d['a'] = 1。", None),

    ("multiple-choice", "用 if 完成 Todo 的 done 状态用？", "todos[i]['done'] = True",
     "修改 done 字段。", "用 todos[i]['done'] = True 标记完成。",
     ["todos = True", "todos[i]['done'] = True", "todos.append(True)", "todos.done(True)"]),

    ("fill-blank", "把任务保存为文件用 json.______。", "dump",
     "dump 写文件。", "json.dump(data, f) 把列表写为 JSON。", None),

    ("predict-output", "json.dumps([{'task': 'x'}]) 的结果是？", "[{\"task\": \"x\"}]",
     "序列化为 JSON。", "列表含字典被序列化为 JSON 数组。", None),

    ("multiple-choice", "CLI 程序主循环用？", "while True",
     "主循环。", "while True + 条件分支 + break 是常见模式。",
     ["if 链", "while True", "for 循环", "递归"]),

    ("fill-blank", "退出主循环用 ______ 关键字。", "break",
     "break 退出。", "用户选择退出时 break。", None),

    ("predict-output", "在循环中用 'continue' 会？", "跳过本轮进入下一轮",
     "continue 跳本轮。", "continue 立即进入下一次迭代。", None),

    ("multiple-choice", "input().strip() 的作用是？", "去除首尾空白",
     "strip 去空白。", "input() 后 strip 去掉首尾换行/空格。",
     ["转为数字", "去除首尾空白", "分割", "小写"]),

    ("fill-blank", "if not lst: 表示列表为 ______。", "空",
     "空列表为假。", "空列表在布尔上下文中是 False。", None),

    ("predict-output", "bool([]) 的结果是？", "False",
     "空列表 falsy。", "空列表是 False。", None),

    ("multiple-choice", "用 enumerate 遍历时同时拿到？", "索引和元素",
     "enumerate。", "enumerate(iter) 返回 (index, value)。",
     ["仅索引", "索引和元素", "仅元素", "长度"]),

    ("fill-blank", "Python 中所有非空列表都被视为 ______。", "True",
     "truthy。", "非空列表在布尔上下文中是 True。", None),

    ("predict-output", "用列表存储 5 个任务后 len() 等于？", "5",
     "任务数。", "len 等于列表元素个数。", None),

    ("multiple-choice", "保存 Todo 到文件推荐格式？", "JSON",
     "JSON 易读写。", "JSON 是最常用的简单数据交换格式。",
     ["纯文本", "JSON", "PDF", "二进制"]),
]


# =========================================================
# L24: 数据分析入门
# =========================================================
L24_DATA = [
    ("multiple-choice", "[x*x for x in range(5)] 的写法叫？", "列表推导式",
     "List Comprehension。", "用 [] 包裹的推导式叫列表推导式。",
     ["生成器", "列表推导式", "字典推导式", "集合推导式"]),

    ("fill-blank", "{k: v for k, v in items} 叫 ______ 推导式。", "字典",
     "Dict Comprehension。", "{} 包 (k, v) 的推导式是字典推导式。", None),

    ("predict-output", "[x*2 for x in range(3)] 的结果是？", "[0, 2, 4]",
     "列表推导式。", "0*2=0, 1*2=2, 2*2=4。", None),

    ("multiple-choice", "[x for x in range(10) if x % 2 == 0] 的结果是？", "[0, 2, 4, 6, 8]",
     "筛选偶数。", "0 到 9 中的偶数。",
     ["[1, 3, 5, 7, 9]", "[0, 2, 4, 6, 8]", "[0, 2, 4, 6, 8, 10]", "[]"]),

    ("fill-blank", "(x for x in range(3)) 叫 ______ 表达式。", "生成器",
     "生成器表达式。", "() 包的是生成器表达式，惰性求值。", None),

    ("predict-output", "sum(x for x in range(5)) 的结果是？", "10",
     "生成器求和。", "0+1+2+3+4 = 10。", None),

    ("multiple-choice", "sum([1, 2, 3]) 的结果是？", "6",
     "sum 求和。", "1+2+3 = 6。",
     ["5", "6", "123", "avg"]),

    ("fill-blank", "max([3, 1, 4, 1, 5]) 的结果是 ______。", "5",
     "max 最大值。", "列表中最大是 5。", None),

    ("predict-output", "min([3, 1, 4, 1, 5]) 的结果是？", "1",
     "min 最小值。", "列表中最小是 1。", None),

    ("multiple-choice", "len([10, 20, 30]) 的结果是？", "3",
     "len 长度。", "列表有 3 个元素。",
     ["3", "60", "30", "10"]),

    ("fill-blank", "计算平均值的常用写法 sum(data) / ______。", "len(data)",
     "总和 / 个数。", "平均值 = sum / len。", None),

    ("predict-output", "sum([10, 20, 30]) / len([10, 20, 30]) 的结果是？", "20.0",
     "平均数。", "60 / 3 = 20.0。", None),

    ("multiple-choice", "统计函数中位数用？", "statistics.median",
     "median 中位数。", "statistics.median() 返回中位数。",
     ["mean()", "median()", "average()", "mid()"]),

    ("fill-blank", "用 statistics.______ 计算标准差。", "stdev",
     "stdev 标准差。", "statistics.stdev(data) 计算样本标准差。", None),

    ("predict-output", "[x for x in [1, 2, 3] if x > 1] 的结果是？", "[2, 3]",
     "过滤大于 1。", "保留 2 和 3。", None),

    ("multiple-choice", "用 csv 模块读取 CSV 文件用？", "csv.reader",
     "csv.reader。", "csv.reader(f) 返回每行列表的迭代器。",
     ["csv.read", "csv.reader", "csv.open", "csv.parse"]),

    ("fill-blank", "写入 CSV 文件用 csv._______。", "writer",
     "csv.writer。", "csv.writer(f) 返回 writer 对象。", None),

    ("predict-output", "sum([]) 的结果是？", "0",
     "空和为 0。", "空列表求和返回 0。", None),

    ("multiple-choice", "以下哪个不是 statistics 模块的函数？", "variance_user",
     "没有此函数。", "statistics 提供 mean/median/stdev/variance 等。",
     ["mean", "median", "stdev", "variance_user"]),

    ("fill-blank", "statistics.______ 计算平均值。", "mean",
     "mean 平均值。", "statistics.mean(data) 返回算术平均。", None),

    ("predict-output", "sorted([3, 1, 2])[:2] 的结果是？", "[1, 2]",
     "排序后取前 2。", "sorted 升序，[:2] 取前两个 1,2。", None),

    ("multiple-choice", "用 Counter 统计列表元素出现次数用？", "collections.Counter",
     "Counter 计数。", "Counter 是 dict 子类，专门用于计数。",
     ["dict.Counter", "collections.Counter", "count.counter", "itertools.Counter"]),

    ("fill-blank", "Counter({'a': 3, 'b': 1}).most_common(1) 返回？", "[('a', 3)]",
     "most_common。", "返回出现次数最多的元素。", None),

    ("predict-output", "collections.Counter('aab').most_common() 的结果是？", "[('a', 2), ('b', 1)]",
     "统计字符。", "'a' 出现 2 次，'b' 出现 1 次。", None),

    ("multiple-choice", "以下哪个是 numpy 的核心对象？", "ndarray",
     "ndarray 多维数组。", "numpy 的核心是 ndarray（N 维数组）。",
     ["ndarray", "DataFrame", "Series", "Matrix"]),

    ("fill-blank", "pandas 读取 CSV 用 pd._________。", "read_csv",
     "read_csv。", "pd.read_csv('f.csv') 读取 CSV 为 DataFrame。", None),

    ("predict-output", "len([1, 2, 3, 4, 5]) 的结果是？", "5",
     "len 长度。", "5 个元素。", None),

    ("multiple-choice", "过滤列表中大于 5 的元素用？", "列表推导式 + if",
     "filter。", "用 [x for x in lst if x > 5] 过滤。",
     ["map", "filter", "列表推导式 + if", "reduce"]),

    ("fill-blank", "max([], default=0) 的结果是 ______。", "0",
     "default 防止空。", "空序列 max 设置 default 返回 0。", None),

    ("predict-output", "max([1, 5, 3], key=lambda x: -x) 的结果是？", "1",
     "key 取最小。", "key 把元素取负后取最大，等价于取最小。", None),

    ("multiple-choice", "Counter 之间可以用 + 运算吗？", "可以",
     "Counter 支持 +。", "Counter + Counter 把计数相加。",
     ["可以", "不可以", "会报错", "只支持整数"]),

    ("fill-blank", "数据分析中常用 pandas 的 ______ 对象表示表格。", "DataFrame",
     "DataFrame 表格。", "DataFrame 是 pandas 的二维表格数据结构。", None),

    ("predict-output", "sum(range(1, 6)) 的结果是？", "15",
     "1+2+3+4+5。", "1 到 5 之和 = 15。", None),

    ("multiple-choice", "用 Python 处理 CSV 的标准库是？", "csv",
     "csv 标准库。", "csv 是 Python 标准库的一部分。",
     ["pandas", "csv", "openpyxl", "xlsx"]),

    ("fill-blank", "用 dict.________ 排序键用 sorted(d.keys())。", "keys",
     "dict.keys。", "d.keys() 返回所有键的视图。", None),

    ("predict-output", "sorted({'b': 1, 'a': 2}.keys()) 的结果是？", "['a', 'b']",
     "按字母排序。", "字典键排序后是 ['a', 'b']。", None),

    ("multiple-choice", "用 filter 与 lambda 实现过滤的写法是？",
     "filter(lambda x: x > 0, lst)",
     "filter 接受函数。", "filter(func, iterable) 保留 func 返回 True 的元素。",
     ["map", "filter(lambda x: x > 0, lst)", "reduce", "lambda 自身过滤"]),

    ("fill-blank", "statistics.________(data) 返回样本方差。", "variance",
     "variance 方差。", "statistics.variance 计算样本方差。", None),

    ("predict-output", "math.sqrt(16) 的结果是？", "4.0",
     "sqrt 平方根。", "math.sqrt(16) = 4.0。", None),

    ("multiple-choice", "numpy.mean(arr) 与 sum(arr)/len(arr) 相比？", "等价但 numpy 更高效",
     "numpy 优化。", "numpy 对数组运算做了底层优化。",
     ["更快", "等价但 numpy 更高效", "更精确", "不同结果"]),

    ("fill-blank", "用 pandas 读取 Excel 用 pd._________。", "read_excel",
     "read_excel。", "pd.read_excel('f.xlsx') 读 Excel。", None),

    ("predict-output", "len(set([1, 1, 2, 3])) 的结果是？", "3",
     "去重后长度。", "{1,2,3} 含 3 个元素。", None),

    ("multiple-choice", "在 Python 中画图常用？", "matplotlib",
     "matplotlib。", "matplotlib 是 Python 最常用的绘图库。",
     ["numpy", "matplotlib", "pandas", "scipy"]),

    ("fill-blank", "matplotlib.pyplot 别名通常是 ______。", "plt",
     "plt 约定。", "import matplotlib.pyplot as plt 是惯例。", None),

    ("predict-output", "plt.plot([1, 2, 3]) 默认画？", "折线图",
     "plot 折线。", "plt.plot 默认画折线图。", None),

    ("multiple-choice", "在 DataFrame 中按列筛选用？", "df[df['col'] > 0]",
     "布尔索引。", "df[条件] 返回满足条件的行。",
     ["df.select", "df[df['col'] > 0]", "df.filter(col)", "df.where"]),

    ("fill-blank", "用 pandas 描述统计用 df._________。", "describe",
     "describe 描述。", "df.describe() 返回各列统计信息。", None),

    ("predict-output", "df.describe() 默认会计算？", "count/mean/std/min/25%/50%/75%/max",
     "describe 字段。", "describe 给出计数、均值、标准差等。", None),

    ("multiple-choice", "数据清洗中处理缺失值常用？", "fillna/dropna",
     "fillna 填充。", "fillna 填充缺失值，dropna 删除缺失。",
     ["fillna/dropna", "append", "sort", "merge"]),
]


# =========================================================
# L25: Web 爬虫基础
# =========================================================
L25_DATA = [
    ("multiple-choice", "解析 HTML 最常用的库是？", "BeautifulSoup",
     "beautiful + soup。", "BeautifulSoup 用于从 HTML/XML 中提取数据。",
     ["requests", "BeautifulSoup", "numpy", "pandas"]),

    ("fill-blank", "用 requests 发送 GET 请求用 requests.______。", "get",
     "get 拉取。", "requests.get(url) 发送 GET 请求。", None),

    ("predict-output", "requests.get(url).status_code == 200 表示？", "请求成功",
     "200 = OK。", "HTTP 200 表示请求成功。", None),

    ("multiple-choice", "BeautifulSoup 解析 HTML 用？", "BeautifulSoup(html, 'html.parser')",
     "构造时指定解析器。", "构造时传入 HTML 和解析器。",
     ["bs.parse(html)", "BeautifulSoup(html, 'html.parser')", "soup(html)", "bs4.html(html)"]),

    ("fill-blank", "soup.find('a') 返回 ______ 个匹配元素。", "1",
     "find 返回首个。", "find 返回第一个匹配的 Tag。", None),

    ("predict-output", "soup.find_all('a') 的类型是？", "ResultSet（Tag 列表）",
     "find_all 列表。", "find_all 返回 ResultSet，可索引。", None),

    ("multiple-choice", "soup.select('div.title') 用于？", "CSS 选择器查找",
     "select CSS。", "select 用 CSS 选择器查找元素。",
     ["按 id", "CSS 选择器查找", "按属性", "按文本"]),

    ("fill-blank", "获取 Tag 的文本内容用 tag.______ 或 tag.get_text()。", "text",
     "text 属性。", "tag.text 返回标签内的文本。", None),

    ("predict-output", "tag.get('href') 的作用是？", "获取属性 href 的值",
     "get 取属性。", "tag.get('href') 返回 href 属性的值。", None),

    ("multiple-choice", "requests 与 urllib 相比？", "requests 更简洁",
     "requests 易用。", "requests 封装更好，API 更直观。",
     ["更快", "requests 更简洁", "urllib 更现代", "一样"]),

    ("fill-blank", "requests 响应对象的 text 属性是 ______。", "str",
     "text 是 str。", "response.text 返回解码后的字符串。", None),

    ("predict-output", "requests.get(url).text 返回？", "响应体字符串",
     "text 响应体。", "response.text 返回 HTML 等文本内容。", None),

    ("multiple-choice", "response.content 与 response.text 的区别是？",
     "content 是 bytes，text 是 str",
     "bytes vs str。", "content 是字节，text 是解码后的字符串。",
     ["完全相同", "content 是 bytes，text 是 str", "text 更快", "content 自动解码"]),

    ("fill-blank", "requests 发送带参数的 GET 用 params=______。", "dict",
     "params 是字典。", "requests.get(url, params={'q': 'python'})。", None),

    ("predict-output", "response.json() 的作用是？", "把 JSON 响应解析为 Python 对象",
     "json 解析。", "response.json() 用内置 JSON 解析。", None),

    ("multiple-choice", "爬虫中处理反爬常用？", "设置 headers / 限速",
     "反爬策略。", "设置 User-Agent、添加延时、限速等。",
     ["暴力抓取", "设置 headers / 限速", "分布式抓", "修改 DNS"]),

    ("fill-blank", "requests 默认 UA 是？", "python-requests/<version>",
     "默认 UA。", "不修改会被识别为 Python 爬虫。", None),

    ("predict-output", "自定义 header 用 requests.get(url, headers=...) 传入？", "字典",
     "headers 是 dict。", "headers 接受 dict 形式的请求头。", None),

    ("multiple-choice", "robots.txt 用于？", "告知爬虫可访问范围",
     "爬虫协议。", "robots.txt 声明哪些路径允许爬取。",
     ["加密", "告知爬虫可访问范围", "身份验证", "压缩"]),

    ("fill-blank", "BeautifulSoup 中获取所有链接的写法 soup._______('a')。", "find_all",
     "find_all。", "soup.find_all('a') 找所有 a 标签。", None),

    ("predict-output", "正则提取邮箱 r'[\\w.]+@[\\w.]+' 中 \\w 表示？", "单词字符",
     "\\w 单词字符。", "\\w 匹配字母数字下划线。", None),

    ("multiple-choice", "解析 JSON API 响应推荐用？", "response.json()",
     "内置 json。", "response.json() 直接解析为 Python 对象。",
     ["json.loads()", "response.json()", "json.read()", "json.parse()"]),

    ("fill-blank", "BeautifulSoup 解析 XML 也用同一个库，只要 parser 改为 ______。", "xml",
     "lxml/xml。", "传入 'xml' 或 'lxml' parser 即可解析 XML。", None),

    ("predict-output", "len(soup.find_all('a')) 的含义？", "页面中 a 标签的数量",
     "链接数。", "返回 a 标签的个数。", None),

    ("multiple-choice", "爬虫中处理登录常用？", "Session 对象 + POST",
     "session 会话。", "用 requests.Session 保持 cookie。",
     ["GET", "Session 对象 + POST", "PUT", "无"]),

    ("fill-blank", "requests.________() 创建会话。", "Session",
     "Session 类。", "requests.Session() 创建会话对象。", None),

    ("predict-output", "session.get(url) 与 requests.get(url) 的区别是？",
     "session 保持 cookies",
     "Session 状态。", "Session 在多个请求间共享 cookies/headers。", None),

    ("multiple-choice", "爬虫中限速常用？", "time.sleep()",
     "time.sleep 限速。", "每次请求后 sleep 一段时间。",
     ["os.system", "time.sleep()", "input()", "print()"]),

    ("fill-blank", "网页编码查看用 response.__________。", "encoding",
     "encoding 属性。", "response.encoding 显示猜测的编码。", None),

    ("predict-output", "response.encoding = 'utf-8' 的作用是？", "设置响应的解码编码",
     "手动设置编码。", "强制使用 UTF-8 解码 response.content。", None),

    ("multiple-choice", "BeautifulSoup 中 find 的 attrs 参数用于？", "按属性筛选",
     "attrs 字典。", "find('a', attrs={'class': 'link'})。",
     ["按文本", "按属性筛选", "按索引", "按父节点"]),

    ("fill-blank", "tag.______(class_='title') 按 class 筛选（class 是关键字）。", "find",
     "class_ 下划线。", "class 是 Python 关键字，参数名要加下划线。", None),

    ("predict-output", "tag.string 与 tag.text 的关系是？", "string 只在无子标签时可用",
     "string 严格。", "tag.string 仅在子节点为 NavigableString 时返回。", None),

    ("multiple-choice", "用 CSS 选择器选择 id='main' 的元素用？", "#main",
     "id 选择器。", "CSS 中 # 表示 id。",
     [".main", "#main", "main", "*main"]),

    ("fill-blank", "用 CSS 选择器选 class='link' 的元素用 ______link。", ".",
     ". = class。", ".link 选择 class 为 link 的元素。", None),

    ("predict-output", "soup.select('a')[0].get('href') 的作用是？", "取第一个链接的 href",
     "取链接地址。", "select 返回列表，索引 0 取首个 a 标签的 href。", None),

    ("multiple-choice", "BeautifulSoup 解析慢可换哪个解析器？", "lxml",
     "lxml 更快。", "lxml 是 C 实现的解析器，速度极快。",
     ["html.parser", "lxml", "html5lib", "re"]),

    ("fill-blank", "scrapy 是 Python 的 ______ 爬虫框架。", "专业",
     "scrapy 框架。", "scrapy 是工业级爬虫框架。", None),

    ("predict-output", "requests 抛 ConnectionError 通常因为？", "网络不通",
     "网络问题。", "ConnectionError 表示连接失败。", None),

    ("multiple-choice", "爬虫中被识别后的常见反制是？", "封 IP / 验证码",
     "反爬。", "网站常用 IP 封锁、验证码等反爬手段。",
     ["加速响应", "封 IP / 验证码", "发送邮件", "无"]),

    ("fill-blank", "爬虫中模拟浏览器常用设置 UA 到 headers 的 'User-______'。", "Agent",
     "User-Agent。", "User-Agent 标识客户端。", None),

    ("predict-output", "response.url 返回？", "最终响应的 URL",
     "url 属性。", "response.url 是最终响应的 URL（考虑重定向）。", None),

    ("multiple-choice", "BeautifulSoup 是哪个第三方库？", "bs4",
     "bs4 包。", "pip install beautifulsoup4，import as bs4。",
     ["bs4", "soup", "bs", "bs_4"]),

    ("fill-blank", "from bs4 import ______。", "BeautifulSoup",
     "导入类。", "from bs4 import BeautifulSoup。", None),

    ("predict-output", "len(soup.body.contents) 表示？", "body 的直接子节点数",
     "contents 子节点。", "body.contents 是子节点列表。", None),

    ("multiple-choice", "爬虫中存储大量数据常用？", "数据库/文件",
     "持久化。", "常用 SQLite、MySQL、MongoDB、CSV 等。",
     ["内存", "数据库/文件", "print", "GUI"]),

    ("fill-blank", "用 Python 操作 SQLite 用 sqlite3 ______ 模块。", " ",
     "sqlite3 内置。", "sqlite3 是标准库模块。", None),

    ("predict-output", "sqlite3.connect('data.db') 返回？", "Connection 对象",
     "Connection。", "connect 返回数据库连接对象。", None),

    ("multiple-choice", "BeautifulSoup 中 find_parent() 找？", "父节点",
     "父节点。", "find_parent 找直接父节点。",
     ["子节点", "父节点", "兄弟节点", "所有祖先"]),

    ("fill-blank", "tag._______ 返回父节点。", "parent",
     "parent 属性。", "tag.parent 返回父 Tag。", None),
]


# =========================================================
# 主流程
# =========================================================
def build_block(keep_first, new_items):
    parts = [keep_first] + new_items
    return "  exercises: [\n" + ",\n".join(parts) + ",\n  ],"


def apply_replacement(text, lesson_num, keep_first, new_items):
    block = build_block(keep_first, new_items)
    pattern = re.compile(
        '  exercises: \\[\\n    \\{\\n      id: "ex-' + str(lesson_num) + '-1",\\n[\\s\\S]*?    \\},',
        re.MULTILINE
    )
    new_text, n = pattern.subn(block, text)
    assert n == 1, f"L{lesson_num} pattern matched {n} times"
    return new_text


def main():
    text = FILE.read_text(encoding='utf-8')

    # L9
    l9_keep = '''    {
      id: "ex-9-1",
      type: "predict-output",
      question: "{1, 2, 2, 3} 的输出？",
      answer: "{1, 2, 3}",
      hint: "集合自动去重。",
      explanation: "集合中重复元素会被自动去除。",
    }'''
    l9_items = with_idx(9, L9_DATA)
    text = apply_replacement(text, 9, l9_keep, l9_items)

    # L10
    l10_keep = '''    {
      id: "ex-10-1",
      type: "fill-blank",
      question: "去除字符串首尾空格的函数是 ______()。",
      answer: "strip",
      hint: "首尾空白 = strip。",
      explanation: "str.strip() 去除首尾空白字符。",
    }'''
    l10_items = with_idx(10, L10_DATA)
    text = apply_replacement(text, 10, l10_keep, l10_items)

    FILE.write_text(text, encoding='utf-8')
    print(f"L9 + L10 已写入: L9={len(L9_DATA)} 新题, L10={len(L10_DATA)} 新题")


if __name__ == '__main__':
    main()
