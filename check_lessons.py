import re
from collections import Counter

content = open(r'e:\fastload\learnPython\src\data\lessons.ts', encoding='utf-8').read()
matches = re.findall(r'id: "ex-(\d+)-(\d+)"', content)
c = Counter([m[0] for m in matches])
for k, v in sorted(c.items(), key=lambda x: int(x[0])):
    print(f'l{k}: {v}')

# Also count max ids per lesson
ids_per_lesson = {}
for lesson_id, num in matches:
    ids_per_lesson.setdefault(lesson_id, []).append(int(num))
for k in sorted(ids_per_lesson, key=lambda x: int(x)):
    nums = sorted(ids_per_lesson[k])
    print(f'l{k}: count={len(nums)}, max={max(nums)}, missing={[i for i in range(1, max(nums)+1) if i not in nums][:5]}...')
