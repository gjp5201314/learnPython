import { useState, useRef, useCallback, useEffect } from "react";
import { Play, Copy, RotateCcw, Check, Loader2, Terminal, Sparkles } from "lucide-react";
import { getPyodide, runPython } from "@/lib/pyodide";
import { highlightPython } from "@/lib/highlight";
import { useProgressStore } from "@/store/useProgressStore";
import { cn } from "@/lib/utils";

interface CodeRunnerProps {
  code: string;
  lessonId?: string;
  className?: string;
  /** 高度限制 */
  minHeight?: number;
}

export default function CodeRunner({ code: initialCode, lessonId, className, minHeight = 220 }: CodeRunnerProps) {
  const [code, setCode] = useState(initialCode);
  const [output, setOutput] = useState("");
  const [error, setError] = useState("");
  const [running, setRunning] = useState(false);
  const [copied, setCopied] = useState(false);
  const [loading, setLoading] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState("准备运行环境");
  const [showOutput, setShowOutput] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const highlightRef = useRef<HTMLPreElement>(null);
  const registerCodeRun = useProgressStore((s) => s.registerCodeRun);

  // 当传入的代码变化时（例如切换课程），重置编辑器
  useEffect(() => {
    setCode(initialCode);
    setOutput("");
    setError("");
    setShowOutput(false);
  }, [initialCode]);

  const handleRun = useCallback(async () => {
    setRunning(true);
    setShowOutput(true);
    setError("");
    setOutput("");
    try {
      if (!loading && !getPyodide.length) {
        // nothing
      }
      // 首次会加载 Pyodide
      setLoading(true);
      const py = await getPyodide((msg) => setLoadingMsg(msg));
      setLoading(false);
      const res = await runPython(code);
      setOutput(res.stdout);
      setError(res.stderr);
      registerCodeRun();
    } catch (e: any) {
      setError(e?.message || String(e));
    } finally {
      setRunning(false);
      setLoading(false);
    }
  }, [code, registerCodeRun, loading]);

  const handleCopy = useCallback(() => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  }, [code]);

  const handleReset = useCallback(() => {
    setCode(initialCode);
    setOutput("");
    setError("");
  }, [initialCode]);

  // 同步滚动：textarea 滚动时高亮 pre 跟随
  const syncScroll = () => {
    if (textareaRef.current && highlightRef.current) {
      highlightRef.current.scrollTop = textareaRef.current.scrollTop;
      highlightRef.current.scrollLeft = textareaRef.current.scrollLeft;
    }
  };

  return (
    <div className={cn("rounded-2xl border border-ink-700 bg-ink-900/70 overflow-hidden shadow-inner-soft", className)}>
      {/* Toolbar */}
      <div className="flex items-center justify-between border-b border-ink-700/80 bg-ink-800/80 px-4 py-2.5">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-rose-400/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-ember-400/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-vine-300/70" />
          </div>
          <span className="ml-2 font-mono text-[11px] text-zinc-500 tracking-wider">
            {lessonId ? `${lessonId}.py` : "main.py"}
          </span>
        </div>
        <div className="flex items-center gap-1">
          <button
            onClick={handleCopy}
            className="inline-flex items-center gap-1.5 rounded-md px-2.5 py-1.5 text-xs text-zinc-400 hover:text-zinc-100 hover:bg-ink-700/60 transition"
            title="复制代码"
          >
            {copied ? <Check className="h-3.5 w-3.5 text-vine-300" /> : <Copy className="h-3.5 w-3.5" />}
            <span>{copied ? "已复制" : "复制"}</span>
          </button>
          <button
            onClick={handleReset}
            className="inline-flex items-center gap-1.5 rounded-md px-2.5 py-1.5 text-xs text-zinc-400 hover:text-zinc-100 hover:bg-ink-700/60 transition"
            title="重置代码"
          >
            <RotateCcw className="h-3.5 w-3.5" />
            <span>重置</span>
          </button>
          <button
            onClick={handleRun}
            disabled={running}
            className={cn(
              "ml-1 inline-flex items-center gap-1.5 rounded-md px-3 py-1.5 text-xs font-semibold transition shadow-glow-vine",
              running
                ? "bg-vine-500/40 text-ink-950 cursor-wait"
                : "bg-vine-300 text-ink-950 hover:bg-vine-200"
            )}
          >
            {running ? (
              <Loader2 className="h-3.5 w-3.5 animate-spin" />
            ) : (
              <Play className="h-3.5 w-3.5 fill-current" />
            )}
            <span>{running ? "运行中" : "运行"}</span>
          </button>
        </div>
      </div>

      {/* Editor */}
      <div className="relative" style={{ minHeight }}>
        <pre
          ref={highlightRef}
          aria-hidden
          className="code-block absolute inset-0 m-0 !bg-transparent pointer-events-none whitespace-pre overflow-auto"
          style={{ minHeight, padding: "16px 18px 16px 48px" }}
          dangerouslySetInnerHTML={{ __html: highlightPython(code) + "\n" }}
        />
        <textarea
          ref={textareaRef}
          value={code}
          onChange={(e) => setCode(e.target.value)}
          onScroll={syncScroll}
          spellCheck={false}
          className="relative block w-full bg-transparent text-transparent caret-vine-300 font-mono text-[13.5px] leading-[1.7] outline-none resize-none p-4 pl-12 selection:bg-vine-300/30"
          style={{ minHeight, height: "auto" }}
        />
      </div>

      {/* Output panel */}
      <div className="border-t border-ink-700/80 bg-[#08090d]">
        <button
          onClick={() => setShowOutput((s) => !s)}
          className="flex w-full items-center justify-between px-4 py-2 text-xs text-zinc-400 hover:text-zinc-200 transition"
        >
          <span className="inline-flex items-center gap-2">
            <Terminal className="h-3.5 w-3.5" />
            <span>运行结果</span>
            {(output || error) && (
              <span className={cn(
                "h-1.5 w-1.5 rounded-full",
                error ? "bg-rose-400" : "bg-vine-300"
              )} />
            )}
          </span>
          <span className="font-mono text-[10px] text-zinc-500">
            {showOutput ? "收起 ▴" : "展开 ▾"}
          </span>
        </button>
        {showOutput && (
          <div className="border-t border-ink-700/60 px-4 py-3 font-mono text-[13px] leading-relaxed min-h-[80px] max-h-[260px] overflow-auto">
            {loading && (
              <div className="flex items-center gap-2 text-zinc-500">
                <Loader2 className="h-3.5 w-3.5 animate-spin" />
                <span>{loadingMsg}</span>
              </div>
            )}
            {!loading && !output && !error && (
              <div className="text-zinc-600 flex items-center gap-1.5">
                <Sparkles className="h-3.5 w-3.5" />
                点击「运行」执行上面的 Python 代码
              </div>
            )}
            {output && <pre className="text-zinc-200 whitespace-pre-wrap">{output}</pre>}
            {error && <pre className="text-rose-300 whitespace-pre-wrap">{error}</pre>}
          </div>
        )}
      </div>
    </div>
  );
}
