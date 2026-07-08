#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

text = open(r'e:\fastload\learnPython\src\data\lessons.ts', encoding='utf-8').read()

# Find simple match
pat1 = r'ex-9-1'
m1 = re.search(pat1, text)
print("ex-9-1 found at:", m1.start() if m1 else None)

# Try simpler pattern
pat2 = r'id: "ex-9-1",\n(?:.*\n){6}    \},'
m2 = re.search(pat2, text)
print("Pattern 2:", "Found" if m2 else "Not found")
if m2:
    print("Match:", repr(m2.group()))

# Try with DOTALL
pat3 = r'id: "ex-9-1",[\s\S]*?    \},'
m3 = re.search(pat3, text)
print("Pattern 3 (DOTALL):", "Found" if m3 else "Not found")
if m3:
    print("Match:", repr(m3.group()[:200]))
