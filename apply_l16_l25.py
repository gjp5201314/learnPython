#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为 lessons.ts 中 l16-l25 补充到 50 道题
- 保留每章原 ex-x-1
- 追加 49 道题 (ex-x-2 ~ ex-x-50)
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, r'e:\fastload\learnPython')
from gen_exercises import (
    L16_DATA, L17_DATA, L18_DATA, L19_DATA, L20_DATA,
    L21_DATA, L22_DATA, L23_DATA, L24_DATA, L25_DATA,
    with_idx, build_block
)

FILE = Path(r'e:\fastload\learnPython\src\data\lessons.ts')

# 保留原 ex-x-1 字符串
KEEPS = {
    16: '''    {
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
    }''',
    17: '''    {
      id: "ex-17-1",
      type: "fill-blank",
      question: "捕获除零错误的异常名是 ______DivisionError。",
      answer: "Zero",
      hint: "Zero + Division + Error。",
      explanation: "ZeroDivisionError 表示除以零。",
    }''',
    18: '''    {
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
    }''',
    19: '''    {
      id: "ex-19-1",
      type: "fill-blank",
      question: "把 Python 对象转成 JSON 字符串用 json.______。",
      answer: "dumps",
      hint: "dump + s = string。",
      explanation: "json.dumps 把对象序列化为字符串。",
    }''',
    20: '''    {
      id: "ex-20-1",
      type: "multiple-choice",
      question: "\\\\d 在正则中表示？",
      options: ["任意字符", "数字", "字母", "空白"],
      answer: "数字",
      hint: "d = digit。",
      explanation: "\\\\d 匹配任意一个数字字符。",
    }''',
    21: '''    {
      id: "ex-21-1",
      type: "predict-output",
      question: "如果 target=63，guess=50，输出？",
      answer: "50 太小了",
      hint: "50 < 63。",
      explanation: "50 小于 63，程序输出「太小了」。",
    }''',
    22: '''    {
      id: "ex-22-1",
      type: "fill-blank",
      question: "Python 中创建匿名函数的关键字是 ______。",
      answer: "lambda",
      hint: "希腊字母 λ。",
      explanation: "lambda 用于创建单行匿名函数。",
    }''',
    23: '''    {
      id: "ex-23-1",
      type: "multiple-choice",
      question: "列表的 append 方法返回新列表吗？",
      options: ["是", "否，原地修改", "取决于类型", "返回 None"],
      answer: "否，原地修改",
      hint: "看 append 的返回值。",
      explanation: "append 是 in-place 操作，返回 None。",
    }''',
    24: '''    {
      id: "ex-24-1",
      type: "fill-blank",
      question: "[x*x for x in range(5)] 这种写法叫 ______ 推导式。",
      answer: "列表",
      hint: "用 [] 包裹的推导式。",
      explanation: "用 [] 包裹的推导式叫列表推导式。",
    }''',
    25: '''    {
      id: "ex-25-1",
      type: "multiple-choice",
      question: "解析 HTML 最常用的库是？",
      options: ["requests", "BeautifulSoup", "numpy", "pandas"],
      answer: "BeautifulSoup",
      hint: "beautiful + soup。",
      explanation: "BeautifulSoup 用于从 HTML/XML 中提取数据。",
    }''',
}

DATA = {
    16: L16_DATA, 17: L17_DATA, 18: L18_DATA, 19: L19_DATA, 20: L20_DATA,
    21: L21_DATA, 22: L22_DATA, 23: L23_DATA, 24: L24_DATA, 25: L25_DATA,
}


def apply_replacement(text, lesson_num, keep, new_items):
    block = build_block(keep, new_items)
    pattern = re.compile(
        r'  exercises: \[\n    \{\n      id: "ex-' + str(lesson_num) + r'-1",[\s\S]*?\n  \],',
        re.MULTILINE
    )
    new_text, n = pattern.subn(block, text)
    if n != 1:
        raise RuntimeError(f"L{lesson_num} pattern matched {n} times")
    return new_text


def main():
    text = FILE.read_text(encoding='utf-8')
    for num in [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
        keep = KEEPS[num]
        items = with_idx(num, DATA[num])
        text = apply_replacement(text, num, keep, items)
        print(f"L{num}: 已写入 {len(items)} 新题 (合计 50)")

    FILE.write_text(text, encoding='utf-8')
    print("完成！")


if __name__ == '__main__':
    main()
