import { Link } from "react-router-dom";
import { ArrowRight, Sparkles, Zap, Code2, Trophy } from "lucide-react";
import StageCard from "@/components/StageCard";
import { stages, lessonMap } from "@/data/lessons";
import { useProgressStore } from "@/store/useProgressStore";
import { useEffect, useState } from "react";

const codeLines = [
  { color: "tok-kw", text: "def" },
  { color: "tok-fn", text: " " },
  { color: "tok-fn", text: "greet" },
  { color: "", text: "(" },
  { color: "tok-builtin", text: "name" },
  { color: "", text: "):" },
  { color: "tok-com", text: "    # 让 Python 为你工作" },
  { color: "tok-kw", text: "    return" },
  { color: "", text: " f" },
  { color: "tok-str", text: "'Hello, " },
  { color: "", text: "{" },
  { color: "tok-builtin", text: "name" },
  { color: "", text: "}! " },
  { color: "tok-str", text: "🐍'" },
  { color: "", text: "" },
  { color: "", text: "" },
  { color: "tok-builtin", text: "print" },
  { color: "", text: "(" },
  { color: "tok-fn", text: "greet" },
  { color: "", text: "(" },
  { color: "tok-str", text: "'PyPath'" },
  { color: "", text: "))" },
];

export default function Home() {
  const completed = useProgressStore((s) => s.completedLessons);
  const codeRuns = useProgressStore((s) => s.totalCodeRuns);
  const streak = useProgressStore((s) => s.streakDays);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div className="space-y-20 md:space-y-28">
      {/* HERO */}
      <section className="relative -mt-2">
        {/* background ornaments */}
        <div className="pointer-events-none absolute inset-0 -z-10">
          <div className="absolute top-10 left-1/2 -translate-x-1/2 h-[420px] w-[820px] rounded-full bg-vine-300/[0.07] blur-3xl" />
          <div className="absolute top-40 right-10 h-40 w-40 rounded-full bg-ember-400/[0.08] blur-3xl" />
        </div>

        <div className="grid lg:grid-cols-[1.1fr_1fr] gap-10 lg:gap-16 items-center">
          <div className={mounted ? "animate-fade-in" : "opacity-0"}>
            <div className="inline-flex items-center gap-2 rounded-full border border-ink-600 bg-ink-800/70 px-3 py-1 text-xs text-zinc-300 mb-6">
              <span className="relative flex h-1.5 w-1.5">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-vine-300 opacity-75" />
                <span className="relative inline-flex h-1.5 w-1.5 rounded-full bg-vine-300" />
              </span>
              <span className="font-mono tracking-wider">PYTHON 3.12 · 2026 EDITION</span>
            </div>

            <h1 className="font-display text-5xl md:text-6xl lg:text-7xl font-bold leading-[1.05] tracking-tight text-white">
              掌握 Python，<br />
              <span className="text-gradient-vine">从一行代码</span>开始。
            </h1>

            <p className="mt-6 max-w-xl text-lg text-zinc-400 leading-relaxed">
              一条从零基础到能写实战项目的完整学习路线。<br className="hidden md:block" />
              每一节都内置可运行示例、随堂练习与进度跟踪。
            </p>

            <div className="mt-8 flex flex-wrap items-center gap-3">
              <Link
                to="/learn/basics"
                className="group inline-flex items-center gap-2 rounded-xl bg-vine-300 px-5 py-3 text-sm font-semibold text-ink-950 shadow-glow-vine transition hover:shadow-[0_0_0_1px_rgba(126,231,135,0.6),0_10px_40px_-8px_rgba(126,231,135,0.7)] hover:-translate-y-0.5"
              >
                开始学习
                <ArrowRight className="h-4 w-4 transition group-hover:translate-x-1" />
              </Link>
              <Link
                to="/progress"
                className="inline-flex items-center gap-2 rounded-xl border border-ink-600 bg-ink-800/60 px-5 py-3 text-sm font-medium text-zinc-200 transition hover:border-ink-500 hover:bg-ink-800"
              >
                <Trophy className="h-4 w-4 text-ember-400" />
                查看我的进度
              </Link>
            </div>

            {/* quick stats */}
            <div className="mt-10 grid grid-cols-3 max-w-md gap-6">
              <Stat value="25" label="章节课程" />
              <Stat value="50+" label="随堂练习" />
              <Stat value="5" label="学习阶段" />
            </div>
          </div>

          {/* Hero code editor mock */}
          <div className={`relative ${mounted ? "animate-fade-in" : "opacity-0"}`} style={{ animationDelay: "200ms" }}>
            <div className="relative rounded-2xl border border-ink-700 bg-ink-900/80 shadow-2xl shadow-vine-300/5 overflow-hidden">
              <div className="flex items-center justify-between border-b border-ink-700/80 bg-ink-800/80 px-4 py-2.5">
                <div className="flex items-center gap-2">
                  <div className="flex gap-1.5">
                    <span className="h-2.5 w-2.5 rounded-full bg-rose-400/70" />
                    <span className="h-2.5 w-2.5 rounded-full bg-ember-400/70" />
                    <span className="h-2.5 w-2.5 rounded-full bg-vine-300/70" />
                  </div>
                  <span className="ml-2 font-mono text-[11px] text-zinc-500">welcome.py</span>
                </div>
                <span className="font-mono text-[10px] uppercase tracking-widest text-vine-300/80">live</span>
              </div>
              <div className="p-5 font-mono text-[13.5px] leading-[1.85] min-h-[260px]">
                {codeLines.map((line, i) => (
                  <div key={i} className="flex" style={{ animationDelay: `${i * 50}ms` }}>
                    <span className="w-7 shrink-0 text-right pr-3 text-zinc-600 select-none">{i + 1}</span>
                    <span className={line.color || "text-zinc-300"}>{line.text || "\u00A0"}</span>
                  </div>
                ))}
                <div className="mt-3 pl-7 text-vine-300">→ Hello, PyPath! 🐍</div>
              </div>
              {/* glow ring */}
              <div className="absolute -inset-px rounded-2xl pointer-events-none">
                <div className="absolute inset-0 rounded-2xl ring-1 ring-inset ring-vine-300/20" />
              </div>
            </div>

            {/* floating badges */}
            <div className="absolute -top-4 -right-2 hidden md:block animate-float">
              <div className="rounded-xl border border-ink-600 bg-ink-800/90 backdrop-blur px-3 py-2 shadow-xl">
                <div className="flex items-center gap-2 text-xs">
                  <Zap className="h-3.5 w-3.5 text-ember-400" />
                  <span className="font-mono text-zinc-200">Pyodide 在线运行</span>
                </div>
              </div>
            </div>
            <div className="absolute -bottom-3 -left-2 hidden md:block animate-float" style={{ animationDelay: "1.5s" }}>
              <div className="rounded-xl border border-ink-600 bg-ink-800/90 backdrop-blur px-3 py-2 shadow-xl">
                <div className="flex items-center gap-2 text-xs">
                  <Sparkles className="h-3.5 w-3.5 text-vine-300" />
                  <span className="font-mono text-zinc-200">5 阶段 · 25 节</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 实时数据 */}
      <section>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <LiveStatCard
            icon={<Code2 className="h-5 w-5" />}
            label="已运行代码"
            value={codeRuns}
            accent="vine"
          />
          <LiveStatCard
            icon={<Trophy className="h-5 w-5" />}
            label="已完成章节"
            value={completed.length}
            accent="ember"
          />
          <LiveStatCard
            icon={<Sparkles className="h-5 w-5" />}
            label="连续学习"
            value={streak}
            suffix="天"
            accent="sky"
          />
        </div>
      </section>

      {/* 5 阶段路线 */}
      <section>
        <SectionHeader
          eyebrow="Learning Path"
          title="完整学习路线"
          description="由浅入深，5 大阶段 25 个章节，构建你的 Python 知识体系。"
        />
        <div className="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {stages.map((stage, i) => (
            <StageCard
              key={stage.id}
              stage={stage}
              lessons={stage.lessonIds.map((id) => lessonMap[id]).filter(Boolean)}
              completedCount={stage.lessonIds.filter((id) => completed.includes(id)).length}
              index={i}
            />
          ))}
        </div>
      </section>

      {/* 价值主张 */}
      <section>
        <div className="grid lg:grid-cols-3 gap-5">
          <ValueProp
            icon="⚡"
            title="真正可运行"
            desc="所有示例代码都在浏览器内通过 Pyodide 真实执行，结果立即可见。"
          />
          <ValueProp
            icon="🎯"
            title="结构化路径"
            desc="5 个阶段 25 个章节，由浅入深，避免学完不知道下一步。"
          />
          <ValueProp
            icon="🏆"
            title="持续反馈"
            desc="随堂练习、运行统计、成就徽章，让你的努力被看见。"
          />
        </div>
      </section>

      {/* CTA */}
      <section className="relative rounded-3xl border border-ink-700 bg-gradient-to-br from-ink-800/80 via-ink-900 to-ink-900 px-6 md:px-12 py-12 md:py-16 overflow-hidden">
        <div className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-vine-300/10 blur-3xl" />
        <div className="pointer-events-none absolute -left-10 -bottom-10 h-56 w-56 rounded-full bg-ember-400/10 blur-3xl" />
        <div className="relative max-w-2xl">
          <h2 className="font-display text-3xl md:text-4xl font-bold text-white tracking-tight">
            准备好写下你的第一行 <span className="text-gradient-vine">Python</span> 了吗？
          </h2>
          <p className="mt-4 text-zinc-400 text-lg">
            从「入门基础」开始，每天 15 分钟，一个月后你就能独立写完整的小项目。
          </p>
          <Link
            to="/learn/basics"
            className="mt-7 inline-flex items-center gap-2 rounded-xl bg-vine-300 px-6 py-3 text-sm font-semibold text-ink-950 shadow-glow-vine transition hover:-translate-y-0.5"
          >
            进入第 1 阶段
            <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
      </section>
    </div>
  );
}

function Stat({ value, label }: { value: string; label: string }) {
  return (
    <div>
      <div className="font-mono text-3xl font-semibold text-white">{value}</div>
      <div className="text-xs text-zinc-500 mt-1 tracking-wider">{label}</div>
    </div>
  );
}

function SectionHeader({
  eyebrow,
  title,
  description,
}: {
  eyebrow: string;
  title: string;
  description: string;
}) {
  return (
    <div className="max-w-2xl">
      <div className="font-mono text-xs tracking-[0.25em] text-vine-300 uppercase mb-2">
        {eyebrow}
      </div>
      <h2 className="font-display text-3xl md:text-4xl font-bold text-white tracking-tight">
        {title}
      </h2>
      <p className="mt-3 text-zinc-400 leading-relaxed">{description}</p>
    </div>
  );
}

function LiveStatCard({
  icon,
  label,
  value,
  suffix,
  accent,
}: {
  icon: React.ReactNode;
  label: string;
  value: number;
  suffix?: string;
  accent: "vine" | "ember" | "sky";
}) {
  const colorMap = {
    vine: "text-vine-300 border-vine-300/25 from-vine-300/10",
    ember: "text-ember-300 border-ember-400/25 from-ember-400/10",
    sky: "text-sky-300 border-sky-300/25 from-sky-300/10",
  } as const;
  return (
    <div
      className={`card-glow rounded-2xl border bg-gradient-to-br to-transparent p-5 ${colorMap[accent]}`}
    >
      <div className="flex items-center justify-between mb-3">
        <span className="text-[11px] font-mono tracking-widest uppercase text-zinc-500">
          {label}
        </span>
        <div className={`rounded-lg border border-ink-700 bg-ink-800/60 p-1.5 ${colorMap[accent]}`}>
          {icon}
        </div>
      </div>
      <div className="font-mono text-3xl md:text-4xl font-semibold text-white">
        {value}
        {suffix && <span className="text-lg text-zinc-500 ml-1">{suffix}</span>}
      </div>
    </div>
  );
}

function ValueProp({ icon, title, desc }: { icon: string; title: string; desc: string }) {
  return (
    <div className="card-glow rounded-2xl border border-ink-700 bg-ink-900/60 p-6">
      <div className="text-2xl mb-3">{icon}</div>
      <h3 className="font-display text-lg font-semibold text-white mb-1.5">{title}</h3>
      <p className="text-sm text-zinc-400 leading-relaxed">{desc}</p>
    </div>
  );
}
