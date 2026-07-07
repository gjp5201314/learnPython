import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import {
  Trophy,
  Medal,
  Flame,
  Code2,
  Sparkles,
  CalendarDays,
  RotateCcw,
  Check,
  Lock,
} from "lucide-react";
import ProgressRing from "@/components/ProgressRing";
import { stages, lessonMap, lessons } from "@/data/lessons";
import { useProgressStore } from "@/store/useProgressStore";
import { cn } from "@/lib/utils";

const BADGES = [
  {
    id: "first-lesson",
    name: "初出茅庐",
    desc: "完成你的第 1 个章节",
    icon: "🌱",
    color: "from-vine-300/20 to-vine-500/0",
  },
  {
    id: "five-lessons",
    name: "小有所成",
    desc: "完成 5 个章节",
    icon: "🌿",
    color: "from-vine-300/20 to-vine-500/0",
  },
  {
    id: "all-rounder",
    name: "通关玩家",
    desc: "完成 15 个章节",
    icon: "🏆",
    color: "from-ember-400/20 to-ember-500/0",
  },
  {
    id: "first-run",
    name: "Hello World",
    desc: "首次运行代码",
    icon: "⚡",
    color: "from-sky-300/20 to-sky-500/0",
  },
  {
    id: "runner",
    name: "代码狂人",
    desc: "运行代码 10 次",
    icon: "🚀",
    color: "from-rose-300/20 to-rose-500/0",
  },
  {
    id: "quiz-novice",
    name: "答题新手",
    desc: "完成 5 道练习",
    icon: "✏️",
    color: "from-violet-300/20 to-violet-500/0",
  },
  {
    id: "quiz-master",
    name: "答题达人",
    desc: "完成 15 道练习",
    icon: "🎯",
    color: "from-ember-400/20 to-ember-500/0",
  },
];

export default function Progress() {
  const completed = useProgressStore((s) => s.completedLessons);
  const codeRuns = useProgressStore((s) => s.totalCodeRuns);
  const streak = useProgressStore((s) => s.streakDays);
  const studyLog = useProgressStore((s) => s.studyLog);
  const unlocked = useProgressStore((s) => s.unlockedBadges);
  const completedExercises = useProgressStore((s) => s.completedExercises);
  const reset = useProgressStore((s) => s.reset);

  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const overall = (completed.length / lessons.length) * 100;
  const totalMin = Object.values(studyLog).reduce((a: number, b: number) => a + (b as number), 0);

  return (
    <div className="space-y-12">
      <header className="flex items-end justify-between flex-wrap gap-4">
        <div>
          <div className="font-mono text-xs tracking-[0.25em] text-vine-300 uppercase mb-2">
            Your Progress
          </div>
          <h1 className="font-display text-4xl md:text-5xl font-bold text-white tracking-tight">
            学习进度
          </h1>
          <p className="mt-3 text-zinc-400 max-w-2xl">
            看看你已经走到哪一步。每完成一个章节 / 练习，你的努力都会被记录下来。
          </p>
        </div>
        <button
          onClick={() => {
            if (confirm("确定要重置全部学习进度吗？此操作不可撤销。")) {
              reset();
            }
          }}
          className="inline-flex items-center gap-1.5 rounded-lg border border-ink-600 bg-ink-800/60 px-3 py-2 text-xs text-zinc-400 hover:border-rose-400/40 hover:text-rose-300 transition"
        >
          <RotateCcw className="h-3.5 w-3.5" />
          重置进度
        </button>
      </header>

      {/* 总览 */}
      <section className="grid lg:grid-cols-[300px_1fr] gap-6">
        <div className="card-glow rounded-2xl border border-ink-700 bg-ink-900/60 p-6 flex flex-col items-center justify-center text-center">
          <ProgressRing
            value={overall}
            size={180}
            stroke={14}
            color="#7EE787"
            label="Overall"
          />
          <div className="mt-4">
            <div className="font-display text-2xl font-semibold text-white">
              {completed.length} <span className="text-zinc-500">/ {lessons.length}</span>
            </div>
            <div className="text-xs text-zinc-500 mt-1">已掌握章节</div>
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          <StatTile
            icon={<Trophy className="h-4 w-4" />}
            label="已完成章节"
            value={completed.length}
            sub={`/ ${lessons.length}`}
            color="vine"
          />
          <StatTile
            icon={<Medal className="h-4 w-4" />}
            label="已答对练习"
            value={completedExercises.length}
            color="ember"
          />
          <StatTile
            icon={<Code2 className="h-4 w-4" />}
            label="代码运行数"
            value={codeRuns}
            color="sky"
          />
          <StatTile
            icon={<Flame className="h-4 w-4" />}
            label="连续学习"
            value={streak}
            suffix="天"
            color="rose"
          />
          <div className="col-span-2 md:col-span-4 card-glow rounded-2xl border border-ink-700 bg-ink-900/60 p-5">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs text-zinc-500 font-mono uppercase tracking-widest">
                累计学习时长
              </span>
              <Sparkles className="h-3.5 w-3.5 text-vine-300" />
            </div>
            <div className="font-mono text-3xl font-semibold text-white">
              {totalMin} <span className="text-base text-zinc-500">分钟</span>
            </div>
            <div className="mt-1 text-xs text-zinc-500">
              约 {Math.max(1, Math.round(totalMin / 60))} 小时持续投入
            </div>
          </div>
        </div>
      </section>

      {/* 5 阶段进度 */}
      <section>
        <SectionTitle>分阶段进度</SectionTitle>
        <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-5">
          {stages.map((stage, i) => {
            const done = stage.lessonIds.filter((id) => completed.includes(id)).length;
            const pct = (done / stage.lessonIds.length) * 100;
            const accentMap: Record<string, string> = {
              vine: "#7EE787",
              sky: "#7DD3FC",
              ember: "#FFB454",
              rose: "#FDA4AF",
              violet: "#C4B5FD",
            };
            return (
              <Link
                key={stage.id}
                to={`/learn/${stage.id}`}
                className="card-glow group rounded-2xl border border-ink-700 bg-ink-900/60 p-5 transition hover:bg-ink-900/80"
              >
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-[10px] tracking-widest text-zinc-500">
                    STAGE 0{stage.index}
                  </span>
                  {done === stage.lessonIds.length && (
                    <Check className="h-3.5 w-3.5 text-vine-300" />
                  )}
                </div>
                <h3 className="font-display text-base font-semibold text-white">{stage.title}</h3>
                <div className="mt-3 flex items-center justify-between">
                  <ProgressRing
                    value={pct}
                    size={70}
                    stroke={6}
                    color={accentMap[stage.accent]}
                  />
                  <div className="text-right">
                    <div className="font-mono text-xl text-white">{done}/{stage.lessonIds.length}</div>
                    <div className="text-[10px] text-zinc-500">章节</div>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      {/* 学习日历 */}
      <section>
        <SectionTitle>
          <CalendarDays className="inline h-4 w-4 mr-1.5 -mt-0.5" />
          学习日历
        </SectionTitle>
        <div className="mt-6 card-glow rounded-2xl border border-ink-700 bg-ink-900/60 p-5">
          <HeatMap log={studyLog} />
        </div>
      </section>

      {/* 成就徽章 */}
      <section>
        <SectionTitle>成就徽章</SectionTitle>
        <div className="mt-6 grid gap-4 grid-cols-2 md:grid-cols-3 xl:grid-cols-4">
          {BADGES.map((b) => {
            const got = unlocked.includes(b.id);
            return (
              <div
                key={b.id}
                className={cn(
                  "card-glow relative overflow-hidden rounded-2xl border p-5 transition",
                  got
                    ? "border-vine-300/30 bg-gradient-to-br from-ink-900 to-ink-900"
                    : "border-ink-700 bg-ink-900/40 opacity-60"
                )}
              >
                {got && (
                  <div
                    className={cn(
                      "absolute inset-0 bg-gradient-to-br opacity-30 pointer-events-none",
                      b.color
                    )}
                  />
                )}
                <div className="relative flex items-start justify-between mb-3">
                  <div className="text-3xl">{b.icon}</div>
                  {got ? (
                    <span className="inline-flex h-5 items-center gap-1 rounded-full bg-vine-300/15 px-2 text-[10px] font-medium text-vine-300">
                      <Check className="h-2.5 w-2.5" /> 已解锁
                    </span>
                  ) : (
                    <Lock className="h-3.5 w-3.5 text-zinc-600" />
                  )}
                </div>
                <h3
                  className={cn(
                    "relative font-display text-sm font-semibold",
                    got ? "text-white" : "text-zinc-500"
                  )}
                >
                  {b.name}
                </h3>
                <p className="relative text-xs text-zinc-500 mt-1 leading-relaxed">
                  {b.desc}
                </p>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}

function SectionTitle({ children }: { children: React.ReactNode }) {
  return (
    <h2 className="font-display text-2xl font-semibold text-white tracking-tight">
      {children}
    </h2>
  );
}

function StatTile({
  icon,
  label,
  value,
  sub,
  suffix,
  color,
}: {
  icon: React.ReactNode;
  label: string;
  value: number;
  sub?: string;
  suffix?: string;
  color: "vine" | "ember" | "sky" | "rose";
}) {
  const colors = {
    vine: "text-vine-300 border-vine-300/20",
    ember: "text-ember-300 border-ember-400/20",
    sky: "text-sky-300 border-sky-300/20",
    rose: "text-rose-300 border-rose-300/20",
  } as const;
  return (
    <div className={cn("card-glow rounded-2xl border bg-ink-900/60 p-4", colors[color])}>
      <div className="flex items-center justify-between mb-2">
        <span className="text-[10px] font-mono tracking-widest uppercase text-zinc-500">
          {label}
        </span>
        <div className={cn("rounded-md border bg-ink-800/60 p-1", colors[color])}>{icon}</div>
      </div>
      <div className="font-mono text-2xl font-semibold text-white">
        {value}
        {suffix && <span className="text-sm text-zinc-500 ml-0.5">{suffix}</span>}
        {sub && <span className="text-base text-zinc-500 ml-1">{sub}</span>}
      </div>
    </div>
  );
}

/**
 * 学习日历 - 简易热力图
 */
function HeatMap({ log }: { log: Record<string, number> }) {
  // 生成最近 12 周
  const weeks: { date: string; minutes: number }[][] = [];
  const today = new Date();
  for (let w = 11; w >= 0; w--) {
    const week: { date: string; minutes: number }[] = [];
    for (let d = 0; d < 7; d++) {
      const d2 = new Date(today);
      d2.setDate(today.getDate() - (w * 7 + (6 - d)));
      const key = d2.toISOString().slice(0, 10);
      week.push({ date: key, minutes: (log[key] as number) || 0 });
    }
    weeks.push(week);
  }

  const max = Math.max(1, ...Object.values(log).map((v) => Number(v) || 0));

  const getColor = (m: number) => {
    if (!m) return "bg-ink-700/60";
    const ratio = m / max;
    if (ratio < 0.25) return "bg-vine-300/20";
    if (ratio < 0.5) return "bg-vine-300/40";
    if (ratio < 0.75) return "bg-vine-300/65";
    return "bg-vine-300";
  };

  return (
    <div>
      <div className="flex gap-1.5 overflow-x-auto pb-2">
        {weeks.map((week, wi) => (
          <div key={wi} className="flex flex-col gap-1.5">
            {week.map((cell) => (
              <div
                key={cell.date}
                title={`${cell.date} · ${cell.minutes} 分钟`}
                className={cn(
                  "h-4 w-4 rounded-sm transition",
                  getColor(cell.minutes),
                  "hover:ring-1 hover:ring-vine-300"
                )}
              />
            ))}
          </div>
        ))}
      </div>
      <div className="mt-4 flex items-center gap-2 text-[11px] text-zinc-500">
        <span>少</span>
        <span className="h-3 w-3 rounded-sm bg-ink-700/60" />
        <span className="h-3 w-3 rounded-sm bg-vine-300/20" />
        <span className="h-3 w-3 rounded-sm bg-vine-300/40" />
        <span className="h-3 w-3 rounded-sm bg-vine-300/65" />
        <span className="h-3 w-3 rounded-sm bg-vine-300" />
        <span>多</span>
      </div>
    </div>
  );
}
