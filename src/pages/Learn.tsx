import { Link, useParams, Navigate } from "react-router-dom";
import { ArrowLeft, ArrowRight, Check, Circle, Clock, Trophy } from "lucide-react";
import { stages, lessonMap } from "@/data/lessons";
import { useProgressStore } from "@/store/useProgressStore";
import { cn } from "@/lib/utils";

export default function Learn() {
  const { stageId } = useParams();
  const stage = stageId ? stages.find((s) => s.id === stageId) : undefined;
  const completed = useProgressStore((s) => s.completedLessons);

  // 阶段总览（无 stageId）
  if (!stageId) {
    return (
      <div className="space-y-10">
        <div>
          <div className="font-mono text-xs tracking-[0.25em] text-vine-300 uppercase mb-2">
            Learning Path
          </div>
          <h1 className="font-display text-4xl md:text-5xl font-bold text-white tracking-tight">
            完整学习路线
          </h1>
          <p className="mt-3 text-zinc-400 max-w-2xl">
            选择一个阶段深入学习。每个阶段包含 5 个章节，建议按顺序完成。
          </p>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          {stages.map((s, i) => {
            const done = s.lessonIds.filter((id) => completed.includes(id)).length;
            return (
              <Link
                key={s.id}
                to={`/learn/${s.id}`}
                className="card-glow group flex items-center gap-5 rounded-2xl border border-ink-700 bg-ink-900/60 p-5 transition hover:bg-ink-900/80"
                style={{ animationDelay: `${i * 60}ms` }}
              >
                <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-vine-300/20 to-ember-400/10 font-display text-2xl font-bold text-white border border-ink-700">
                  0{s.index}
                </div>
                <div className="flex-1 min-w-0">
                  <h3 className="font-display text-xl font-semibold text-white">{s.title}</h3>
                  <p className="mt-0.5 text-xs text-zinc-500 font-mono">{s.tagline}</p>
                  <div className="mt-2 flex items-center gap-3 text-xs text-zinc-500">
                    <span>{s.lessonIds.length} 章节</span>
                    <span>·</span>
                    <span className="text-vine-300">{done} 已完成</span>
                  </div>
                </div>
                <ArrowRight className="h-5 w-5 text-zinc-500 transition group-hover:translate-x-1 group-hover:text-vine-300" />
              </Link>
            );
          })}
        </div>
      </div>
    );
  }

  if (!stage) {
    return <Navigate to="/learn" replace />;
  }

  const stageLessons = stage.lessonIds.map((id) => lessonMap[id]).filter(Boolean);
  const done = stage.lessonIds.filter((id) => completed.includes(id)).length;

  return (
    <div className="space-y-10">
      <div>
        <Link
          to="/learn"
          className="inline-flex items-center gap-1.5 text-xs text-zinc-500 hover:text-vine-300 transition mb-6"
        >
          <ArrowLeft className="h-3.5 w-3.5" />
          返回所有阶段
        </Link>

        <div className="flex items-start justify-between flex-wrap gap-4">
          <div>
            <div className="font-mono text-xs tracking-[0.25em] text-vine-300 uppercase mb-2">
              Stage 0{stage.index} · {stage.tagline}
            </div>
            <h1 className="font-display text-4xl md:text-5xl font-bold text-white tracking-tight">
              {stage.title}
            </h1>
            <p className="mt-3 text-zinc-400 max-w-2xl">{stage.description}</p>
          </div>
          <div className="rounded-2xl border border-ink-700 bg-ink-900/60 px-5 py-3 text-right">
            <div className="font-mono text-3xl font-semibold text-white">
              {done}/{stageLessons.length}
            </div>
            <div className="text-[10px] uppercase tracking-widest text-zinc-500">阶段进度</div>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {stageLessons.map((lesson, i) => {
          const isDone = completed.includes(lesson.id);
          return (
            <Link
              key={lesson.id}
              to={`/lesson/${lesson.id}`}
              className={cn(
                "card-glow group flex items-center gap-4 rounded-2xl border bg-ink-900/60 p-5 transition",
                isDone
                  ? "border-vine-300/30 hover:border-vine-300/60"
                  : "border-ink-700 hover:border-ink-500"
              )}
            >
              <div
                className={cn(
                  "flex h-12 w-12 shrink-0 items-center justify-center rounded-xl font-mono text-sm font-semibold border",
                  isDone
                    ? "bg-vine-300/15 text-vine-300 border-vine-300/30"
                    : "bg-ink-800 text-zinc-400 border-ink-700"
                )}
              >
                {isDone ? <Check className="h-5 w-5" /> : String(i + 1).padStart(2, "0")}
              </div>
              <div className="flex-1 min-w-0">
                <h3 className="font-display text-lg font-semibold text-white truncate">
                  {lesson.title}
                </h3>
                <p className="mt-0.5 text-sm text-zinc-400 line-clamp-1">{lesson.description}</p>
                <div className="mt-2 flex items-center gap-3 text-xs text-zinc-500">
                  <span className="inline-flex items-center gap-1">
                    <Clock className="h-3 w-3" />
                    {lesson.estimatedMinutes} 分钟
                  </span>
                  <span>·</span>
                  <span>{lesson.exercises.length} 个练习</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                {isDone && (
                  <span className="inline-flex items-center gap-1 rounded-full bg-vine-300/10 px-2.5 py-1 text-[10px] font-medium text-vine-300">
                    <Trophy className="h-3 w-3" /> 已完成
                  </span>
                )}
                {!isDone && i === done && (
                  <span className="inline-flex items-center gap-1 rounded-full bg-ember-400/10 px-2.5 py-1 text-[10px] font-medium text-ember-300">
                    <Circle className="h-3 w-3 fill-current" /> 下一个
                  </span>
                )}
                <ArrowRight className="h-5 w-5 text-zinc-500 transition group-hover:translate-x-1 group-hover:text-vine-300" />
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
