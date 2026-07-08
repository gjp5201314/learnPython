const fs = require('fs');
const ts = fs.readFileSync('src/data/lessons.ts', 'utf8');
const idRe = /id:\s*"(ex-(\d+)-(\d+))"/g;
const counts = {};
let m;
let total = 0;
const lessonIds = {};
while ((m = idRe.exec(ts)) !== null) {
  total++;
  const id = m[1];
  const lesson = m[2];
  if (!lessonIds[lesson]) lessonIds[lesson] = [];
  lessonIds[lesson].push(m[3]);
}
for (const lesson of Object.keys(lessonIds).sort()) {
  const arr = lessonIds[lesson];
  console.log('Lesson', lesson, 'count:', arr.length, 'min:', Math.min(...arr), 'max:', Math.max(...arr));
}
console.log('Total:', total);
