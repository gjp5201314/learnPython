#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理 l9 和 l10 中重复的练习题
"""
import re
from pathlib import Path

FILE = Path(r'e:\fastload\learnPython\src\data\lessons.ts')

def find_lesson_block(text, lesson_id):
    """找到 l{lesson_id} 的整个对象"""
    # 找到 const lX: Lesson = { 开始
    pattern = re.compile(r'^const l' + str(lesson_id) + r': Lesson = \{', re.MULTILINE)
    m = pattern.search(text)
    if not m:
        return None, None
    start = m.start()

    # 找到对象结束 `^};`
    pattern_end = re.compile(r'^};', re.MULTILINE)
    end_matches = list(pattern_end.finditer(text, start))
    if not end_matches:
        return None, None
    end = end_matches[0].end()
    return start, end

def cleanup_lesson(lesson_id):
    text = FILE.read_text(encoding='utf-8')
    start, end = find_lesson_block(text, lesson_id)
    if start is None:
        print(f"L{lesson_id}: not found")
        return

    block = text[start:end]
    # 找到 exercises: [\n 之后到 \n  ], 之前
    ex_start = block.find('  exercises: [')
    if ex_start < 0:
        print(f"L{lesson_id}: exercises not found")
        return
    # 找 ], 闭合
    # 找到最后一个 ], 在 之后是 \n}
    # 从 ex_start 开始找 ]
    rest = block[ex_start:]
    # 找 ],
    close_pos = rest.rfind('\n  ],')
    if close_pos < 0:
        print(f"L{lesson_id}: close not found")
        return

    ex_content = rest[len('  exercises: ['):close_pos]
    # 分割练习
    exercises = re.findall(r'    \{\n(?:.*?\n)+?    \},', ex_content, re.DOTALL)
    print(f"L{lesson_id}: 找到 {len(exercises)} 个练习")

    if len(exercises) > 50:
        # 保留前 50
        # 注意: 第二批 ex-9-2 到 ex-9-49 的开头可能是 `    {\n      id: "ex-9-2",`
        # 保留前 50 个
        keep = exercises[:50]
        new_content = "\n".join(keep)
        new_exercises = '  exercises: [\n' + new_content + '\n  ],'
        new_block = block[:ex_start] + new_exercises
        new_text = text[:start] + new_block + text[end:]
        FILE.write_text(new_text, encoding='utf-8')
        print(f"L{lesson_id}: 已保留 50 个练习")
    else:
        print(f"L{lesson_id}: 数量正常，无需清理")

if __name__ == '__main__':
    cleanup_lesson(9)
    cleanup_lesson(10)
