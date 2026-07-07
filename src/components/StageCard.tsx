import { Link } from "react-router-dom";
import { ArrowUpRight, BookOpen, Clock, Check } from "lucide-react";
import type { Lesson, Stage } from "@/types";
import { cn } from "@/lib/utils";

interface StageCardProps {
  stage: Stage;
  lessons: Lesson[];
  completedCount: number;
  index: number;
}

const accentMap: Record<string, { color: string; ring: string; bg: string; text: string; border: string }> = {
  vine: {
    color: "#7EE787",
    ring: "ring-vine-300/30",
    bg: "from-vine-300/15 to-vine-300/0",
    text: "text-vine-300",
    border: "border-vine-300/25",
  },
  sky: {
    color: "#7DD3FC",
    ring: "ring-sky-300/30",
    bg: "from-sky-300/15 to-sky-300/0",
    text: "text-sky-300",
    border: "border-sky-300/25",
  },
  ember: {
    color: "#FFB454",
    ring: "ring-ember-400/30",
    bg: "from-ember-400/15 to-ember-400/0",
    text: "text-ember-300",
    border: "border-ember-400/25",
  },
  rose: {
    color: "#FDA4AF",
    ring: "ring-rose-300/30",
    bg: "from-rose-300/15 to-rose-300/0",
    text: "text-rose-300",
    border: "border-rose-300/25",
  },
  violet: {
    color: "#C4B5FD",
    ring: "ring-violet-300/30",
    bg: "from-violet-300/15 to-violet-300/0",
    text: "text-violet-300",
    border: "border-violet-300/25",
  },
};

export default function StageCard({ stage, lessons, completedCount, index }: StageCardProps) {
  const accent = accentMap[stage.accent];
  const totalMin = lessons.reduce((sum, l) => sum + l.estimatedMinutes, 0);
  const progress = lessons.length ? (completedCount / lessons.length) * 100 : 0;
  const isDone = completedCount === lessons.length;

  return (
    <Link
      to={`/learn/${stage.id}`}
      className={cn(
        "card-glow group relative flex flex-col rounded-2xl border bg-ink-900/60 p-6 transition-all duration-300",
        "hover:-translate-y-1 hover:bg-ink-900/80",
        accent.border
      )}
      style={{ animationDelay: `${index * 80}ms` }}
    >
      {/* background gradient */}
      <div className={cn("absolute inset-0 rounded-2xl bg-gradient-to-br opacity-50 pointer-events-none", accent.bg)} />

      <div className="relative flex items-start justify-between mb-5">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className={cn("text-[11px] font-mono tracking-widest uppercase", accent.text)}>
              Stage 0{stage.index}
            </span>
            {isDone && (
              <span className="inline-flex h-5 items-center gap-1 rounded-full bg-vine-300/15 px-2 text-[10px] font-medium text-vine-300">
                <Check className="h-3 w-3" /> 已完成
              </span>
            )}
          </div>
          <h3 className="font-display text-2xl font-semibold text-white tracking-tight">
            {stage.title}
          </h3>
          <p className={cn("mt-1 text-xs font-mono tracking-wider", accent.text)}>
            {stage.tagline}
          </p>
        </div>
        <div
          className={cn(
            "flex h-11 w-11 items-center justify-center rounded-xl border bg-ink-800/80 transition group-hover:scale-110",
            accent.border,
            accent.text
          )}
        >
          <StageIcon icon={stage.icon} />
        </div>
      </div>

      <p className="relative text-sm text-zinc-400 leading-relaxed mb-5">
        {stage.description}
      </p>

      {/* Stats */}
      <div className="relative grid grid-cols-3 gap-2 mb-5 text-center">
        <div className="rounded-lg border border-ink-700 bg-ink-800/60 px-2 py-2">
          <div className="font-mono text-base text-white">{lessons.length}</div>
          <div className="text-[10px] text-zinc-500 tracking-wider">章节</div>
        </div>
        <div className="rounded-lg border border-ink-700 bg-ink-800/60 px-2 py-2">
          <div className="font-mono text-base text-white">{Math.round(totalMin / 60)}h</div>
          <div className="text-[10px] text-zinc-500 tracking-wider">总时长</div>
        </div>
        <div className="rounded-lg border border-ink-700 bg-ink-800/60 px-2 py-2">
          <div className={cn("font-mono text-base", accent.text)}>
            {completedCount}/{lessons.length}
          </div>
          <div className="text-[10px] text-zinc-500 tracking-wider">已完成</div>
        </div>
      </div>

      {/* Progress bar */}
      <div className="relative h-1.5 w-full overflow-hidden rounded-full bg-ink-700">
        <div
          className="h-full rounded-full transition-all duration-700"
          style={{ width: `${progress}%`, background: accent.color }}
        />
      </div>

      <div className="relative mt-4 flex items-center justify-between text-xs text-zinc-500">
        <span className="inline-flex items-center gap-1">
          <BookOpen className="h-3.5 w-3.5" />
          {lessons[0]?.title}
        </span>
        <span
          className={cn(
            "inline-flex items-center gap-1 transition group-hover:translate-x-0.5",
            accent.text
          )}
        >
          开始学习
          <ArrowUpRight className="h-3.5 w-3.5" />
        </span>
      </div>
    </Link>
  );
}

function StageIcon({ icon }: { icon: Stage["icon"] }) {
  const cls = "h-5 w-5";
  switch (icon) {
    case "spark":
      return (
        <svg viewBox="0 0 24 24" fill="none" className={cls} stroke="currentColor" strokeWidth="1.5">
          <path d="M12 2v6m0 8v6M4.93 4.93l4.24 4.24m5.66 5.66 4.24 4.24M2 12h6m8 0h6M4.93 19.07l4.24-4.24m5.66-5.66 4.24-4.24" strokeLinecap="round" />
        </svg>
      );
    case "stack":
      return (
        <svg viewBox="0 0 24 24" fill="none" className={cls} stroke="currentColor" strokeWidth="1.5">
          <path d="M12 3 2 8l10 5 10-5-10-5zM2 13l10 5 10-5M2 18l10 5 10-5" strokeLinejoin="round" strokeLinecap="round" />
        </svg>
      );
    case "cube":
      return (
        <svg viewBox="0 0 24 24" fill="none" className={cls} stroke="currentColor" strokeWidth="1.5">
          <path d="M12 2 3 7v10l9 5 9-5V7l-9-5z" strokeLinejoin="round" />
          <path d="M3 7l9 5 9-5M12 22V12" strokeLinejoin="round" />
        </svg>
      );
    case "library":
      return (
        <svg viewBox="0 0 24 24" fill="none" className={cls} stroke="currentColor" strokeWidth="1.5">
          <path d="M4 4h6v16H4zM14 4h6v16h-6z" strokeLinejoin="round" />
          <path d="M16 4v16M8 4v16" />
        </svg>
      );
    case "rocket":
      return (
        <svg viewBox="0 0 24 24" fill="none" className={cls} stroke="currentColor" strokeWidth="1.5">
          <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09zM12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" strokeLinejoin="round" />
          <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" />
        </svg>
      );
  }
}
