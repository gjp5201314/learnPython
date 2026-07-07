import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { Sparkles, Search, Trophy, ChevronRight } from "lucide-react";
import { stages, lessonMap, lessons } from "@/data/lessons";
import { useProgressStore } from "@/store/useProgressStore";
import ExerciseCard from "@/components/ExerciseCard";
import { cn } from "@/lib/utils";

export default function Practice() {
  const completedExercises = useProgressStore((s) => s.completedExercises);
  const [filter, setFilter] = useState<string>("all");
  const [query, setQuery] = useState("");

  // 收集所有练习，按 stage 分组
  const allExercises = useMemo(() => {
    return stages.map((stage) => ({
      stage,
      lessons: stage.lessonIds
        .map((id) => lessonMap[id])
        .filter(Boolean)
        .map((l) => ({
          lesson: l,
          exercises: l.exercises,
        })),
    }));
  }, []);

  const filtered = useMemo(() => {
    return allExercises
      .filter((g) => filter === "all" || g.stage.id === filter)
      .map((g) => ({
        ...g,
        lessons: g.lessons
          .map((lg) => ({
            ...lg,
            exercises: lg.exercises.filter((ex) => {
              if (!query) return true;
              return (
                ex.question.toLowerCase().includes(query.toLowerCase()) ||
                ex.hint.toLowerCase().includes(query.toLowerCase())
              );
            }),
          }))
          .filter((lg) => lg.exercises.length > 0),
      }))
      .filter((g) => g.lessons.length > 0);
  }, [allExercises, filter, query]);

  const totalExercises = lessons.reduce((sum, l) => sum + l.exercises.length, 0);
  const totalDone = completedExercises.length;
  const completionPct = totalExercises ? (totalDone / totalExercises) * 100 : 0;

  return (
    <div className="space-y-10">
      <header>
        <div className="font-mono text-xs tracking-[0.25em] text-vine-300 uppercase mb-2">
          Practice Center
        </div>
        <h1 className="font-display text-4xl md:text-5xl font-bold text-white tracking-tight">
          练习中心
        </h1>
        <p className="mt-3 text-zinc-400 max-w-2xl">
          把学到的知识用练习巩固。完成 {totalExercises} 道题，成为真正的 Python 玩家。
        </p>
      </header>

      {/* 进度概览 */}
      <div className="card-glow rounded-2xl border border-ink-700 bg-gradient-to-br from-vine-300/5 to-transparent p-5 flex items-center gap-5 flex-wrap">
        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-vine-300/10 text-vine-300 border border-vine-300/20">
          <Trophy className="h-5 w-5" />
        </div>
        <div className="flex-1 min-w-[200px]">
          <div className="font-mono text-2xl font-semibold text-white">
            {totalDone} <span className="text-zinc-500 text-base">/ {totalExercises}</span>
          </div>
          <div className="text-xs text-zinc-500">总完成度</div>
        </div>
        <div className="flex-1 min-w-[200px] h-2 overflow-hidden rounded-full bg-ink-700">
          <div
            className="h-full rounded-full bg-gradient-to-r from-vine-300 to-ember-400 transition-all duration-700"
            style={{ width: `${completionPct}%` }}
          />
        </div>
      </div>

      {/* 筛选 */}
      <div className="flex items-center gap-3 flex-wrap">
        <div className="relative flex-1 min-w-[200px]">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-zinc-500" />
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="搜索题目关键词…"
            className="w-full rounded-xl border border-ink-700 bg-ink-900/70 pl-10 pr-4 py-2.5 text-sm text-zinc-200 placeholder-zinc-500 outline-none focus:border-vine-300/40"
          />
        </div>
        <div className="flex items-center gap-1 rounded-xl border border-ink-700 bg-ink-900/60 p-1">
          <FilterPill active={filter === "all"} onClick={() => setFilter("all")}>
            全部
          </FilterPill>
          {stages.map((s) => (
            <FilterPill
              key={s.id}
              active={filter === s.id}
              onClick={() => setFilter(s.id)}
            >
              {s.title}
            </FilterPill>
          ))}
        </div>
      </div>

      {/* 练习列表 */}
      <div className="space-y-10">
        {filtered.length === 0 ? (
          <div className="rounded-2xl border border-ink-700 bg-ink-900/60 p-8 text-center text-zinc-500">
            没有匹配的练习
          </div>
        ) : (
          filtered.map((g) => (
            <section key={g.stage.id}>
              <div className="mb-4 flex items-center justify-between">
                <div>
                  <div className="font-mono text-[10px] tracking-widest text-vine-300 uppercase">
                    STAGE 0{g.stage.index}
                  </div>
                  <h2 className="font-display text-2xl font-semibold text-white">
                    {g.stage.title}
                  </h2>
                </div>
                <Link
                  to={`/learn/${g.stage.id}`}
                  className="inline-flex items-center gap-1 text-xs text-zinc-400 hover:text-vine-300 transition"
                >
                  返回章节 <ChevronRight className="h-3.5 w-3.5" />
                </Link>
              </div>
              <div className="space-y-4">
                {g.lessons.map((lg) => (
                  <div key={lg.lesson.id} className="space-y-3">
                    <div className="text-xs text-zinc-500 font-mono">
                      {lg.lesson.title}
                    </div>
                    {lg.exercises.map((ex, i) => (
                      <ExerciseCard key={ex.id} exercise={ex} exerciseIndex={i} />
                    ))}
                  </div>
                ))}
              </div>
            </section>
          ))
        )}
      </div>

      {filtered.length > 0 && (
        <div className="rounded-2xl border border-ink-700 bg-ink-900/60 p-5 flex items-center gap-3 text-sm text-zinc-400">
          <Sparkles className="h-4 w-4 text-ember-400" />
          提示：每答对一道题都会自动记录到你的进度中。
        </div>
      )}
    </div>
  );
}

function FilterPill({
  active,
  onClick,
  children,
}: {
  active: boolean;
  onClick: () => void;
  children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "rounded-lg px-3 py-1.5 text-xs font-medium transition",
        active
          ? "bg-vine-300/10 text-vine-300"
          : "text-zinc-400 hover:text-zinc-100"
      )}
    >
      {children}
    </button>
  );
}
