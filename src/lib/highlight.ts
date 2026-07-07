import type { LessonSection } from "@/types";

const PY_KEYWORDS = new Set([
  "False","None","True","and","as","assert","async","await","break","class",
  "continue","def","del","elif","else","except","finally","for","from","global",
  "if","import","in","is","lambda","nonlocal","not","or","pass","raise","return",
  "try","while","with","yield","match","case",
]);

const PY_BUILTINS = new Set([
  "print","len","range","int","float","str","bool","list","tuple","dict","set",
  "type","isinstance","enumerate","zip","map","filter","sum","min","max","abs",
  "round","input","open","sorted","reversed","any","all","iter","next","super",
  "self","cls","__init__","__name__","__main__","__str__","__repr__",
]);

/**
 * 简易 Python 语法高亮 - 返回带 token span 的 HTML 字符串
 */
export function highlightPython(code: string): string {
  // 转义 HTML
  const escape = (s: string) =>
    s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

  // 组合正则：注释 -> 字符串 -> 数字 -> 标识符 -> 运算符
  const tokenRegex =
    /(\#[^\n]*)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_][A-Za-z0-9_]*\b)|([+\-*/%=<>!&|^~:,.()\[\]{}])|(\s+)|(.)/g;

  let result = "";
  let m: RegExpExecArray | null;
  while ((m = tokenRegex.exec(code)) !== null) {
    const [whole, comment, str, num, ident, op, ws, other] = m;
    if (comment) {
      result += `<span class="tok-com">${escape(comment)}</span>`;
    } else if (str) {
      result += `<span class="tok-str">${escape(str)}</span>`;
    } else if (num) {
      result += `<span class="tok-num">${escape(num)}</span>`;
    } else if (ident) {
      if (PY_KEYWORDS.has(ident)) {
        result += `<span class="tok-kw">${escape(ident)}</span>`;
      } else if (PY_BUILTINS.has(ident)) {
        result += `<span class="tok-builtin">${escape(ident)}</span>`;
      } else if (/^[A-Z]/.test(ident)) {
        result += `<span class="tok-cls">${escape(ident)}</span>`;
      } else if (code.slice(m.index + ident.length, m.index + ident.length + 1) === "(") {
        result += `<span class="tok-fn">${escape(ident)}</span>`;
      } else {
        result += escape(ident);
      }
    } else if (op) {
      result += `<span class="tok-op">${escape(op)}</span>`;
    } else if (ws) {
      result += ws;
    } else if (other) {
      result += escape(other);
    }
  }
  return result;
}

/**
 * 极简 Markdown 渲染（标题/列表/代码块/段落/行内代码/加粗）
 * 避免引入第三方依赖
 */
export function renderMarkdown(md: string): string {
  // 先抽取代码块并占位
  const codeBlocks: string[] = [];
  let processed = md.replace(/```(\w*)\n([\s\S]*?)```/g, (_m, _lang, code) => {
    const idx = codeBlocks.length;
    codeBlocks.push(code);
    return `\u0000CODEBLOCK_${idx}\u0000`;
  });

  // 转义 HTML
  const escape = (s: string) =>
    s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

  // 行内代码 -> 高亮（不抽离，只简单包一层）
  processed = processed.replace(/`([^`\n]+)`/g, (_m, c) => `<code>${escape(c)}</code>`);

  // 加粗
  processed = processed.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  // 标题
  processed = processed.replace(/^### (.+)$/gm, "<h3>$1</h3>");
  processed = processed.replace(/^## (.+)$/gm, "<h2>$1</h2>");

  // 列表（连续 - 开头）
  processed = processed.replace(/(^|\n)((?:[-*] .+(?:\n|$))+)/g, (_m, pre, block) => {
    const items = block
      .trim()
      .split(/\n/)
      .map((line: string) => `<li>${line.replace(/^[-*] /, "")}</li>`)
      .join("");
    return `${pre}<ul>${items}</ul>`;
  });

  // 段落
  const blocks = processed.split(/\n{2,}/);
  processed = blocks
    .map((b) => {
      const t = b.trim();
      if (!t) return "";
      if (t.startsWith("<h") || t.startsWith("<ul") || t.startsWith("\u0000CODEBLOCK_")) {
        return t;
      }
      // 处理换行
      return `<p>${t.replace(/\n/g, "<br/>")}</p>`;
    })
    .join("\n");

  // 还原代码块
  processed = processed.replace(/\u0000CODEBLOCK_(\d+)\u0000/g, (_m, i) => {
    const code = codeBlocks[Number(i)];
    return `<pre class="code-block"><code>${highlightPython(code)}</code></pre>`;
  });

  return processed;
}

/**
 * 把 lesson.content 渲染成 HTML 字符串
 */
export function renderLessonContent(sections: LessonSection[]): string {
  return sections
    .map((s) => {
      if (s.type === "text") {
        return renderMarkdown(s.body);
      }
      if (s.type === "note") {
        return `<div class="my-4 rounded-xl border border-ember-400/20 bg-ember-400/[0.04] px-4 py-3 text-ember-300 text-sm">💡 ${renderMarkdown(s.body)}</div>`;
      }
      if (s.type === "code") {
        const caption = s.caption
          ? `<div class="mb-2 text-xs uppercase tracking-wider text-zinc-500">${s.caption}</div>`
          : "";
        return `${caption}<pre class="code-block"><code>${highlightPython(s.body)}</code></pre>`;
      }
      return "";
    })
    .join("\n");
}
