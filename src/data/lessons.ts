import type { Lesson, Stage } from "@/types";

/* =========================================================
   阶段 1：Python 入门基础
   ========================================================= */

const l1: Lesson = {
  id: "basics-01-variables",
  stage: "basics",
  order: 1,
  title: "变量与数据类型",
  subtitle: "Python 的记忆细胞",
  description: "理解变量、命名规范与五大基础类型：int / float / str / bool / None。",
  estimatedMinutes: 12,
  content: [
    {
      type: "text",
      body: "## 什么是变量？\n\n变量是程序用来**存储数据**的容器。你可以把它想象成一个带名字的盒子，盒子里装着值。Python 不需要显式声明类型，解释器会根据赋值自动推断。\n\n```\nname = 'Alice'   # 字符串\nage  = 28        # 整数\npi   = 3.14159   # 浮点数\nis_active = True # 布尔\nnothing = None   # 空值\n```",
    },
    {
      type: "note",
      body: "Python 变量名**区分大小写**，且不能以数字开头。推荐使用 `snake_case` 命名风格。",
    },
    {
      type: "code",
      caption: "查看变量类型",
      body: "name = 'PyPath'\nage = 1\nheight = 1.80\nis_cool = True\n\nprint(type(name))\nprint(type(age))\nprint(type(height))\nprint(type(is_cool))",
    },
    {
      type: "text",
      body: "## 类型转换\n\n使用 `int()`、`float()`、`str()`、`bool()` 可以在不同类型之间转换。",
    },
    {
      type: "code",
      caption: "类型转换示例",
      body: "x = '42'\ny = int(x)        # '42' -> 42\nz = float('3.5')  # '3.5' -> 3.5\ns = str(123)      # 123 -> '123'\nprint(y + 1)     # 43\nprint(s + '!')   # 123!",
    },
  ],
  exercises: [
    {
      id: "ex-1-1",
      type: "multiple-choice",
      question: "下列哪个是合法的 Python 变量名？",
      options: ["2nd_place", "_secret", "class", "my-name"],
      answer: "_secret",
      hint: "变量名可以以下划线开头，但不能以数字开头，也不能是关键字。",
      explanation: "`_secret` 合法；`2nd_place` 以数字开头；`class` 是关键字；`my-name` 包含连字符。",
    },
    {
      id: "ex-1-2",
      type: "fill-blank",
      question: "把字符串 '3.14' 转成浮点数：______('3.14')",
      answer: "float",
      hint: "Python 内置类型转换函数。",
      explanation: "使用 float() 函数。",
    },
  ],
};

const l2: Lesson = {
  id: "basics-02-operators",
  stage: "basics",
  order: 2,
  title: "运算符与表达式",
  subtitle: "让数字与逻辑起舞",
  description: "掌握算术、比较、逻辑运算符，理解表达式求值。",
  estimatedMinutes: 10,
  content: [
    {
      type: "text",
      body: "## 算术运算符\n\nPython 支持 `+ - * / // % **` 等运算符。其中 `//` 是整除，`%` 取余，`**` 是幂。",
    },
    {
      type: "code",
      caption: "算术运算",
      body: "print(7 + 3)    # 10\nprint(7 - 3)    # 4\nprint(7 * 3)    # 21\nprint(7 / 3)    # 2.333...\nprint(7 // 3)   # 2  整除\nprint(7 % 3)    # 1  取余\nprint(2 ** 10)  # 1024 幂",
    },
    {
      type: "text",
      body: "## 比较与逻辑\n\n比较运算符返回 `True/False`，可与 `and` / `or` / `not` 组合形成复合条件。",
    },
    {
      type: "code",
      caption: "逻辑判断",
      body: "age = 20\nhas_id = True\n\nif age >= 18 and has_id:\n    print('可以进入')\nelse:\n    print('禁止进入')",
    },
  ],
  exercises: [
    {
      id: "ex-2-1",
      type: "predict-output",
      question: "print(2 ** 3 ** 2) 的输出是？",
      answer: "512",
      hint: "** 是右结合，2 ** (3 ** 2) = 2 ** 9。",
      explanation: "3 ** 2 = 9，2 ** 9 = 512。",
    },
  ],
};

const l3: Lesson = {
  id: "basics-03-conditionals",
  stage: "basics",
  order: 3,
  title: "条件语句",
  subtitle: "让程序学会选择",
  description: "if / elif / else 的语法、缩进规则、嵌套条件。",
  estimatedMinutes: 10,
  content: [
    {
      type: "text",
      body: "## if 语句\n\nPython 使用**缩进**来组织代码块（通常 4 个空格）。",
    },
    {
      type: "code",
      caption: "基本条件",
      body: "score = 85\n\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelse:\n    grade = 'D'\n\nprint(f'你的等级是 {grade}')",
    },
    {
      type: "note",
      body: "f-string 是 Python 3.6+ 推荐的字符串格式化方式，比 `%` 和 `format()` 都更直观。",
    },
  ],
  exercises: [
    {
      id: "ex-3-1",
      type: "multiple-choice",
      question: "if 后面条件为假时，程序会执行什么？",
      options: ["跳过 if 块", "执行 if 块", "报错", "重启程序"],
      answer: "跳过 if 块",
      hint: "条件为假时，控制流会跳过 if 块。",
      explanation: "若条件为假，解释器跳过 if 块，继续向下检查 elif / else。",
    },
  ],
};

const l4: Lesson = {
  id: "basics-04-loops",
  stage: "basics",
  order: 4,
  title: "循环结构",
  subtitle: "重复的力量",
  description: "for 循环、while 循环、break / continue 的用法。",
  estimatedMinutes: 14,
  content: [
    {
      type: "text",
      body: "## for 循环\n\n`for` 用来遍历**可迭代对象**（如列表、字符串、range）。",
    },
    {
      type: "code",
      caption: "for 循环基础",
      body: "for i in range(5):\n    print(i, end=' ')\nprint()  # 换行\n\nfruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(f'I like {fruit}')",
    },
    {
      type: "text",
      body: "## while 循环\n\n`while` 在条件为真时反复执行。",
    },
    {
      type: "code",
      caption: "while 与 break",
      body: "n = 0\nwhile True:\n    n += 1\n    if n > 3:\n        break\n    print('n =', n)",
    },
  ],
  exercises: [
    {
      id: "ex-4-1",
      type: "predict-output",
      question: "for i in range(3): print(i) 的输出？",
      answer: "0\n1\n2",
      hint: "range(3) 产生 0, 1, 2。",
      explanation: "range(3) 包含 0、1、2，逐行打印。",
    },
  ],
};

const l5: Lesson = {
  id: "basics-05-functions",
  stage: "basics",
  order: 5,
  title: "函数基础",
  subtitle: "组织你的代码",
  description: "定义函数、参数、返回值、文档字符串。",
  estimatedMinutes: 13,
  content: [
    {
      type: "text",
      body: "## 定义函数\n\n使用 `def` 关键字。函数可以有参数和返回值。",
    },
    {
      type: "code",
      caption: "函数定义",
      body: "def greet(name, greeting='Hello'):\n    \"\"\"返回一个问候语。\"\"\"\n    return f'{greeting}, {name}!'\n\nprint(greet('PyPath'))\nprint(greet('World', greeting='Hi'))",
    },
    {
      type: "note",
      body: "参数 `greeting='Hello'` 是**默认参数**。调用时可以省略。",
    },
  ],
  exercises: [
    {
      id: "ex-5-1",
      type: "multiple-choice",
      question: "函数中使用什么关键字返回值？",
      options: ["yield", "return", "send", "result"],
      answer: "return",
      hint: "立即结束函数并把值传回调用方。",
      explanation: "return 用于把结果返回给调用方。",
    },
  ],
};

/* =========================================================
   阶段 2：数据结构
   ========================================================= */

const l6: Lesson = {
  id: "ds-01-list",
  stage: "data-structures",
  order: 1,
  title: "列表 List",
  subtitle: "有序、可变的序列",
  description: "列表的创建、索引、切片、常用方法。",
  estimatedMinutes: 12,
  content: [
    {
      type: "text",
      body: "## 创建与访问\n\n列表用 `[]` 定义，元素可以是不同类型。",
    },
    {
      type: "code",
      caption: "列表基础",
      body: "nums = [10, 20, 30, 40, 50]\nprint(nums[0])    # 10\nprint(nums[-1])   # 50\nprint(nums[1:4])  # [20, 30, 40]",
    },
    {
      type: "code",
      caption: "常用方法",
      body: "fruits = ['apple', 'banana']\nfruits.append('cherry')\nfruits.insert(1, 'blueberry')\nprint(fruits)\n\nfruits.remove('banana')\nlast = fruits.pop()\nprint('removed:', last, 'left:', fruits)",
    },
  ],
  exercises: [
    {
      id: "ex-6-1",
      type: "multiple-choice",
      question: "list.append(x) 的作用是？",
      options: [
        "在列表开头插入 x",
        "在列表末尾追加 x",
        "替换最后一个元素",
        "返回新列表",
      ],
      answer: "在列表末尾追加 x",
      hint: "append 字面意思是「附加」。",
      explanation: "append 把元素添加到列表末尾，in-place 修改。",
    },
  ],
};

const l7: Lesson = {
  id: "ds-02-tuple",
  stage: "data-structures",
  order: 2,
  title: "元组 Tuple",
  subtitle: "不可变的有序序列",
  description: "理解元组与列表的区别、解包与命名元组。",
  estimatedMinutes: 8,
  content: [
    {
      type: "text",
      body: "## 元组 vs 列表\n\n元组用 `()` 定义，**创建后不能修改**。这让它可以作为字典的 key、集合的元素。",
    },
    {
      type: "code",
      caption: "元组与解包",
      body: "point = (3, 4)\nx, y = point   # 解包\nprint(f'x={x}, y={y}')\n\nrgb = (255, 128, 0)\nr, g, b = rgb\nprint('R:', r, 'G:', g, 'B:', b)",
    },
  ],
  exercises: [
    {
      id: "ex-7-1",
      type: "fill-blank",
      question: "元组使用 ______ 括号定义。",
      answer: "圆",
      hint: "中文描述。",
      explanation: "元组使用圆括号 () 定义。",
    },
  ],
};

const l8: Lesson = {
  id: "ds-03-dict",
  stage: "data-structures",
  order: 3,
  title: "字典 Dict",
  subtitle: "键值对映射",
  description: "字典的增删改查、遍历、嵌套。",
  estimatedMinutes: 14,
  content: [
    {
      type: "text",
      body: "## 字典是映射\n\n字典存储 **key → value** 映射，key 必须是不可变类型。",
    },
    {
      type: "code",
      caption: "字典操作",
      body: "user = {'name': 'Alice', 'age': 28}\nuser['email'] = 'alice@example.com'\nprint(user.get('phone', 'N/A'))\n\nfor k, v in user.items():\n    print(f'{k} = {v}')",
    },
  ],
  exercises: [
    {
      id: "ex-8-1",
      type: "multiple-choice",
      question: "下列哪个不能作为字典的 key？",
      options: ["字符串", "元组", "列表", "整数"],
      answer: "列表",
      hint: "key 必须是不可变（hashable）对象。",
      explanation: "列表是可变对象，不能作为字典的 key。",
    },
  ],
};

const l9: Lesson = {
  id: "ds-04-set",
  stage: "data-structures",
  order: 4,
  title: "集合 Set",
  subtitle: "去重与集合运算",
  description: "集合的创建、交并差运算。",
  estimatedMinutes: 9,
  content: [
    {
      type: "code",
      caption: "集合运算",
      body: "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\n\nprint('并集', a | b)\nprint('交集', a & b)\nprint('差集', a - b)\nprint('对称差', a ^ b)",
    },
  ],
  exercises: [
    {
      id: "ex-9-1",
      type: "predict-output",
      question: "{1, 2, 2, 3} 的输出？",
      answer: "{1, 2, 3}",
      hint: "集合自动去重。",
      explanation: "集合中重复元素会被自动去除。",
    },
  ],
};

const l10: Lesson = {
  id: "ds-05-string",
  stage: "data-structures",
  order: 5,
  title: "字符串深入",
  subtitle: "文本处理利器",
  description: "字符串切片、常用方法、格式化。",
  estimatedMinutes: 11,
  content: [
    {
      type: "code",
      caption: "字符串方法",
      body: "s = '  PyPath is Awesome  '\nprint(s.strip())\nprint(s.lower())\nprint(s.upper())\nprint(s.replace('Awesome', 'Powerful'))\nprint(','.join(['a', 'b', 'c']))",
    },
  ],
  exercises: [
    {
      id: "ex-10-1",
      type: "fill-blank",
      question: "去除字符串首尾空格的函数是 ______()。",
      answer: "strip",
      hint: "首尾空白 = strip。",
      explanation: "str.strip() 去除首尾空白字符。",
    },
  ],
};

/* =========================================================
   阶段 3：面向对象
   ========================================================= */

const l11: Lesson = {
  id: "oop-01-class",
  stage: "oop",
  order: 1,
  title: "类与对象",
  subtitle: "面向对象的第一步",
  description: "类的定义、实例化、`__init__` 与实例属性。",
  estimatedMinutes: 15,
  content: [
    {
      type: "text",
      body: "## 定义类\n\n类（class）是创建对象的模板。`__init__` 是构造方法。",
    },
    {
      type: "code",
      caption: "第一个类",
      body: "class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age  = age\n\n    def bark(self):\n        return f'{self.name}: 汪汪！'\n\nd = Dog('旺财', 3)\nprint(d.bark())",
    },
  ],
  exercises: [
    {
      id: "ex-11-1",
      type: "multiple-choice",
      question: "Python 中类的构造方法是？",
      options: ["__init__", "__start__", "constructor", "new"],
      answer: "__init__",
      hint: "双下划线开头和结尾。",
      explanation: "Python 的构造方法是 __init__。",
    },
  ],
};

const l12: Lesson = {
  id: "oop-02-inheritance",
  stage: "oop",
  order: 2,
  title: "继承",
  subtitle: "代码复用的艺术",
  description: "单继承、方法重写、super() 的使用。",
  estimatedMinutes: 12,
  content: [
    {
      type: "code",
      caption: "继承示例",
      body: "class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return f'{self.name} 发出声音'\n\nclass Cat(Animal):\n    def speak(self):\n        return f'{self.name}: 喵~'\n\nprint(Cat('Tom').speak())",
    },
  ],
  exercises: [
    {
      id: "ex-12-1",
      type: "fill-blank",
      question: "调用父类方法的函数是 ______()。",
      answer: "super",
      hint: "在子类中常用。",
      explanation: "super() 返回父类的代理对象，可调用父类方法。",
    },
  ],
};

const l13: Lesson = {
  id: "oop-03-encapsulation",
  stage: "oop",
  order: 3,
  title: "封装与多态",
  subtitle: "隐藏细节，统一接口",
  description: "私有属性、property 装饰器、多态示例。",
  estimatedMinutes: 11,
  content: [
    {
      type: "code",
      caption: "封装",
      body: "class BankAccount:\n    def __init__(self, balance=0):\n        self._balance = balance\n    @property\n    def balance(self):\n        return self._balance\n    def deposit(self, amount):\n        if amount <= 0:\n            raise ValueError('必须为正数')\n        self._balance += amount\n\nacc = BankAccount(100)\nacc.deposit(50)\nprint('余额:', acc.balance)",
    },
  ],
  exercises: [
    {
      id: "ex-13-1",
      type: "multiple-choice",
      question: "Python 中约定表示「私有」的属性前缀是？",
      options: ["#", "@", "_", "$"],
      answer: "_",
      hint: "单下划线开头。",
      explanation: "单下划线 _ 是 Python 约定上的「内部使用」标记。",
    },
  ],
};

const l14: Lesson = {
  id: "oop-04-magic",
  stage: "oop",
  order: 4,
  title: "魔术方法",
  subtitle: "让对象支持运算符",
  description: "__str__、__repr__、__len__ 等魔术方法。",
  estimatedMinutes: 10,
  content: [
    {
      type: "code",
      caption: "魔术方法",
      body: "class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __repr__(self):\n        return f'Vector({self.x}, {self.y})'\n\nv = Vector(1, 2) + Vector(3, 4)\nprint(v)",
    },
  ],
  exercises: [
    {
      id: "ex-14-1",
      type: "fill-blank",
      question: "让 print() 输出友好字符串的魔术方法是 ________。",
      answer: "__str__",
      hint: "类似 Java 的 toString。",
      explanation: "__str__ 由 print() 调用。",
    },
  ],
};

const l15: Lesson = {
  id: "oop-05-modules",
  stage: "oop",
  order: 5,
  title: "模块与包",
  subtitle: "组织大型项目",
  description: "import 语法、`__name__ == '__main__'`、包结构。",
  estimatedMinutes: 9,
  content: [
    {
      type: "code",
      caption: "模块使用",
      body: "import math\nfrom random import randint\n\nprint(math.sqrt(16))\nprint(randint(1, 10))",
    },
  ],
  exercises: [
    {
      id: "ex-15-1",
      type: "multiple-choice",
      question: "如果模块是被直接运行，__name__ 的值是？",
      options: ["__main__", "module", "__init__", "self"],
      answer: "__main__",
      hint: "特殊的内置名字。",
      explanation: "直接运行脚本时，__name__ 会被设为 '__main__'。",
    },
  ],
};

/* =========================================================
   阶段 4：标准库
   ========================================================= */

const l16: Lesson = {
  id: "stdlib-01-io",
  stage: "stdlib",
  order: 1,
  title: "文件 I/O",
  subtitle: "读写外部世界",
  description: "open()、with 语句、读模式与写模式。",
  estimatedMinutes: 12,
  content: [
    {
      type: "code",
      caption: "读取文件",
      body: "# 注意：在浏览器中文件 I/O 是受限的，这里用内存中的字符串演示\ntext = '''line 1\nline 2\nline 3'''\n\nfor i, line in enumerate(text.splitlines(), 1):\n    print(f'{i}: {line}')",
    },
    {
      type: "code",
      caption: "写入字符串",
      body: "lines = ['first', 'second', 'third']\nbuffer = '\\n'.join(lines)\nprint('Buffer 长度:', len(buffer))\nprint(buffer)",
    },
  ],
  exercises: [
    {
      id: "ex-16-1",
      type: "multiple-choice",
      question: "with open('f.txt') as f: 的好处是？",
      options: [
        "代码更短",
        "自动关闭文件",
        "读取更快",
        "加密文件",
      ],
      answer: "自动关闭文件",
      hint: "with 是上下文管理器。",
      explanation: "with 会确保文件在使用完后自动关闭，避免资源泄露。",
    },
  ],
};

const l17: Lesson = {
  id: "stdlib-02-exceptions",
  stage: "stdlib",
  order: 2,
  title: "异常处理",
  subtitle: "优雅地处理错误",
  description: "try / except / else / finally 完整语法。",
  estimatedMinutes: 10,
  content: [
    {
      type: "code",
      caption: "异常处理",
      body: "def safe_div(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return '不能除以 0'\n    except TypeError:\n        return '类型错误'\n    finally:\n        print('done')\n\nprint(safe_div(10, 0))",
    },
  ],
  exercises: [
    {
      id: "ex-17-1",
      type: "fill-blank",
      question: "捕获除零错误的异常名是 ______DivisionError。",
      answer: "Zero",
      hint: "Zero + Division + Error。",
      explanation: "ZeroDivisionError 表示除以零。",
    },
  ],
};

const l18: Lesson = {
  id: "stdlib-03-datetime",
  stage: "stdlib",
  order: 3,
  title: "datetime 与 time",
  subtitle: "处理时间数据",
  description: "datetime 对象、时间差、格式化。",
  estimatedMinutes: 9,
  content: [
    {
      type: "code",
      caption: "日期时间",
      body: "from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint('现在:', now.strftime('%Y-%m-%d %H:%M:%S'))\n\ntomorrow = now + timedelta(days=1)\nprint('明天:', tomorrow.strftime('%Y-%m-%d'))",
    },
  ],
  exercises: [
    {
      id: "ex-18-1",
      type: "multiple-choice",
      question: "timedelta 用在什么场景？",
      options: [
        "表示时间间隔",
        "格式化日期",
        "解析字符串",
        "暂停程序",
      ],
      answer: "表示时间间隔",
      hint: "time + delta = 时间差。",
      explanation: "timedelta 用于表示两个时间之间的差值。",
    },
  ],
};

const l19: Lesson = {
  id: "stdlib-04-json",
  stage: "stdlib",
  order: 4,
  title: "JSON 处理",
  subtitle: "与 Web 数据对话",
  description: "json.dumps / loads、文件读写。",
  estimatedMinutes: 8,
  content: [
    {
      type: "code",
      caption: "JSON 编解码",
      body: "import json\n\ndata = {'name': 'PyPath', 'stars': 5, 'tags': ['python', 'learn']}\ns = json.dumps(data, ensure_ascii=False, indent=2)\nprint(s)\n\nback = json.loads(s)\nprint('name:', back['name'])",
    },
  ],
  exercises: [
    {
      id: "ex-19-1",
      type: "fill-blank",
      question: "把 Python 对象转成 JSON 字符串用 json.______。",
      answer: "dumps",
      hint: "dump + s = string。",
      explanation: "json.dumps 把对象序列化为字符串。",
    },
  ],
};

const l20: Lesson = {
  id: "stdlib-05-regex",
  stage: "stdlib",
  order: 5,
  title: "正则表达式",
  subtitle: "文本模式匹配",
  description: "re 模块常用函数与基础元字符。",
  estimatedMinutes: 13,
  content: [
    {
      type: "code",
      caption: "正则基础",
      body: "import re\n\ntext = '今天 2026-07-07 天气晴朗'\nmatch = re.search(r'\\d{4}-\\d{2}-\\d{2}', text)\nprint('找到日期:', match.group())\n\nemails = 'a@b.com, c@d.io'\nprint(re.findall(r'[\\w.]+@[\\w.]+', emails))",
    },
  ],
  exercises: [
    {
      id: "ex-20-1",
      type: "multiple-choice",
      question: "\\d 在正则中表示？",
      options: ["任意字符", "数字", "字母", "空白"],
      answer: "数字",
      hint: "d = digit。",
      explanation: "\\d 匹配任意一个数字字符。",
    },
  ],
};

/* =========================================================
   阶段 5：实战项目
   ========================================================= */

const l21: Lesson = {
  id: "proj-01-guess",
  stage: "projects",
  order: 1,
  title: "猜数字游戏",
  subtitle: "用循环与条件做个小游戏",
  description: "综合应用 input/循环/条件/随机数。",
  estimatedMinutes: 16,
  content: [
    {
      type: "text",
      body: "## 项目目标\n\n程序随机生成 1-100 的数字，玩家通过提示不断猜对。",
    },
    {
      type: "code",
      caption: "核心逻辑（浏览器版）",
      body: "import random\n\ntarget = random.randint(1, 100)\nattempts = 0\n# 模拟 3 次猜测\nfor guess in [50, 75, 63]:\n    attempts += 1\n    if guess < target:\n        print(f'{guess} 太小了')\n    elif guess > target:\n        print(f'{guess} 太大了')\n    else:\n        print(f'Bingo! 用 {attempts} 次猜中')\n        break",
    },
  ],
  exercises: [
    {
      id: "ex-21-1",
      type: "predict-output",
      question: "如果 target=63，guess=50，输出？",
      answer: "50 太小了",
      hint: "50 < 63。",
      explanation: "50 小于 63，程序输出「太小了」。",
    },
  ],
};

const l22: Lesson = {
  id: "proj-02-calc",
  stage: "projects",
  order: 2,
  title: "简易计算器",
  subtitle: "用函数组织你的工具",
  description: "加减乘除 + 错误处理。",
  estimatedMinutes: 12,
  content: [
    {
      type: "code",
      caption: "计算器",
      body: "def calc(a, op, b):\n    ops = {'+': lambda x, y: x + y,\n           '-': lambda x, y: x - y,\n           '*': lambda x, y: x * y,\n           '/': lambda x, y: x / y if y != 0 else None}\n    if op not in ops:\n        return '不支持的运算符'\n    return ops[op](a, b)\n\nprint(calc(10, '+', 5))\nprint(calc(10, '/', 0))",
    },
  ],
  exercises: [
    {
      id: "ex-22-1",
      type: "fill-blank",
      question: "Python 中创建匿名函数的关键字是 ______。",
      answer: "lambda",
      hint: "希腊字母 λ。",
      explanation: "lambda 用于创建单行匿名函数。",
    },
  ],
};

const l23: Lesson = {
  id: "proj-03-todo",
  stage: "projects",
  order: 3,
  title: "Todo List CLI",
  subtitle: "数据结构的实际应用",
  description: "用列表 + 字典管理待办。",
  estimatedMinutes: 14,
  content: [
    {
      type: "code",
      caption: "待办管理",
      body: "todos = []\n\ndef add(task):\n    todos.append({'task': task, 'done': False})\n\ndef complete(index):\n    if 0 <= index < len(todos):\n        todos[index]['done'] = True\n\ndef show():\n    for i, t in enumerate(todos):\n        mark = '✓' if t['done'] else '○'\n        print(f'{i} {mark} {t[\"task\"]}')\n\nadd('学习 Python 基础')\nadd('完成项目作品')\ncomplete(0)\nshow()",
    },
  ],
  exercises: [
    {
      id: "ex-23-1",
      type: "multiple-choice",
      question: "列表的 append 方法返回新列表吗？",
      options: ["是", "否，原地修改", "取决于类型", "返回 None"],
      answer: "否，原地修改",
      hint: "看 append 的返回值。",
      explanation: "append 是 in-place 操作，返回 None。",
    },
  ],
};

const l24: Lesson = {
  id: "proj-04-data",
  stage: "projects",
  order: 4,
  title: "数据分析入门",
  subtitle: "用 Python 看数据",
  description: "理解 csv/字典推导/统计函数。",
  estimatedMinutes: 15,
  content: [
    {
      type: "code",
      caption: "数据统计",
      body: "data = [\n    {'name': 'Alice', 'score': 88},\n    {'name': 'Bob',   'score': 92},\n    {'name': 'Cara',  'score': 79},\n]\n\nscores = [d['score'] for d in data]\nprint('平均分:', sum(scores) / len(scores))\nprint('最高分:', max(scores))\nprint('最低分:', min(scores))\nprint('>= 90:', [d['name'] for d in data if d['score'] >= 90])",
    },
  ],
  exercises: [
    {
      id: "ex-24-1",
      type: "fill-blank",
      question: "[x*x for x in range(5)] 这种写法叫 ______ 推导式。",
      answer: "列表",
      hint: "用 [] 包裹的推导式。",
      explanation: "用 [] 包裹的推导式叫列表推导式。",
    },
  ],
};

const l25: Lesson = {
  id: "proj-05-crawler",
  stage: "projects",
  order: 5,
  title: "Web 爬虫基础",
  subtitle: "从 HTML 中提取信息",
  description: "理解 requests/BeautifulSoup 思路。",
  estimatedMinutes: 13,
  content: [
    {
      type: "code",
      caption: "解析 HTML 片段",
      body: "html = '<p class=\"title\">PyPath</p><p>学习 Python</p>'\nimport re\n\n# 实际爬虫会用到 requests + BeautifulSoup，\n# 这里用正则演示匹配 <p> 标签中的文字\nfor m in re.findall(r'<p[^>]*>([^<]+)</p>', html):\n    print('匹配:', m)",
    },
  ],
  exercises: [
    {
      id: "ex-25-1",
      type: "multiple-choice",
      question: "解析 HTML 最常用的库是？",
      options: ["requests", "BeautifulSoup", "numpy", "pandas"],
      answer: "BeautifulSoup",
      hint: "beautiful + soup。",
      explanation: "BeautifulSoup 用于从 HTML/XML 中提取数据。",
    },
  ],
};

export const lessons: Lesson[] = [
  l1, l2, l3, l4, l5,
  l6, l7, l8, l9, l10,
  l11, l12, l13, l14, l15,
  l16, l17, l18, l19, l20,
  l21, l22, l23, l24, l25,
];

export const stages: Stage[] = [
  {
    id: "basics",
    index: 1,
    title: "入门基础",
    tagline: "Build Your Foundation",
    description: "从变量、运算符到控制流与函数，搭建你的 Python 知识地基。",
    accent: "vine",
    icon: "spark",
    lessonIds: ["basics-01-variables", "basics-02-operators", "basics-03-conditionals", "basics-04-loops", "basics-05-functions"],
  },
  {
    id: "data-structures",
    index: 2,
    title: "数据结构",
    tagline: "Tame The Data",
    description: "掌握 List / Tuple / Dict / Set / String，处理真实世界数据。",
    accent: "sky",
    icon: "stack",
    lessonIds: ["ds-01-list", "ds-02-tuple", "ds-03-dict", "ds-04-set", "ds-05-string"],
  },
  {
    id: "oop",
    index: 3,
    title: "面向对象",
    tagline: "Model The World",
    description: "用类与对象组织你的代码：继承、封装、多态与魔术方法。",
    accent: "ember",
    icon: "cube",
    lessonIds: ["oop-01-class", "oop-02-inheritance", "oop-03-encapsulation", "oop-04-magic", "oop-05-modules"],
  },
  {
    id: "stdlib",
    index: 4,
    title: "标准库",
    tagline: "Batteries Included",
    description: "Python 自带「电池」：文件、异常、日期、JSON、正则表达式。",
    accent: "rose",
    icon: "library",
    lessonIds: ["stdlib-01-io", "stdlib-02-exceptions", "stdlib-03-datetime", "stdlib-04-json", "stdlib-05-regex"],
  },
  {
    id: "projects",
    index: 5,
    title: "实战项目",
    tagline: "Ship Real Things",
    description: "把所学融合：游戏、计算器、Todo、数据分析、爬虫。",
    accent: "violet",
    icon: "rocket",
    lessonIds: ["proj-01-guess", "proj-02-calc", "proj-03-todo", "proj-04-data", "proj-05-crawler"],
  },
];

export const lessonMap: Record<string, Lesson> = lessons.reduce(
  (acc, l) => {
    acc[l.id] = l;
    return acc;
  },
  {} as Record<string, Lesson>
);

export const stageMap: Record<string, Stage> = stages.reduce(
  (acc, s) => {
    acc[s.id] = s;
    return acc;
  },
  {} as Record<string, Stage>
);
