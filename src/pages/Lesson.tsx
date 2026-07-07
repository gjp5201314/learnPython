import { Link, useParams, Navigate } from "react-router-dom";
import { useEffect, useMemo, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  Circle,
  Clock,
  Trophy,
  BookOpen,
  FlaskConical,
} from "lucide-react";
import { lessonMap, stageMap } from "@/data/lessons";
import { useProgressStore } from "@/store/useProgressStore";
import CodeRunner from "@/components/CodeRunner";
import ExerciseCard from "@/components/ExerciseCard";
import { renderMarkdown } from "@/lib/highlight";
import { cn } from "@/lib/utils";

type Tab = "lesson" | "playground" | "exercise";

export default function Lesson() {
  const { lessonId } = useParams();
  const lesson = lessonId ? lessonMap[lessonId] : undefined;
  const stage = lesson ? stageMap[lesson.stage] : undefined;

  const [tab, setTab] = useState<Tab>("lesson");
  const completed = useProgressStore((s) => s.completedLessons);
  const markLesson = useProgressStore((s) => s.markLessonComplete);

  // 当前阶段的所有课程
  const stageLessons = useMemo(
    () => (lesson ? stage?.lessonIds.map((id) => lessonMap[id]).filter(Boolean) || [] : []),
    [lesson, stage]
  );
  const currentIndex = stageLessons.findIndex((l) => l.id === lessonId);
  const prevLesson = currentIndex > 0 ? stageLessons[currentIndex - 1] : null;
  const nextLesson =
    currentIndex >= 0 && currentIndex < stageLessons.length - 1
      ? stageLessons[currentIndex + 1]
      : null;

  // 课程内的代码块（用于 playground）
  const codeExamples = useMemo(
    () => (lesson ? lesson.content.filter((s) => s.type === "code") : []),
    [lesson]
  );

  useEffect(() => {
    setTab("lesson");
  }, [lessonId]);

  if (!lesson || !stage) {
    return <Navigate to="/learn" replace />;
  }

  const isDone = completed.includes(lesson.id);

  const handleComplete = () => {
    markLesson(lesson.id);
  };

  return (
    <div className="grid lg:grid-cols-[260px_1fr] gap-8">
      {/* 左侧：阶段章节列表 */}
      <aside className="hidden lg:block">
        <div className="sticky top-4">
          <Link
            to={`/learn/${stage.id}`}
            className="inline-flex items-center gap-1.5 text-xs text-zinc-500 hover:text-vine-300 transition mb-5"
          >
            <ArrowLeft className="h-3.5 w-3.5" />
            {stage.title}
          </Link>
          <div className="font-display text-sm font-semibold text-white mb-3">
            章节导航
          </div>
          <div className="space-y-1">
            {stageLessons.map((l, i) => {
              const done = completed.includes(l.id);
              const active = l.id === lessonId;
              return (
                <Link
                  key={l.id}
                  to={`/lesson/${l.id}`}
                  className={cn(
                    "flex items-center gap-2.5 rounded-lg px-3 py-2 text-xs transition",
                    active
                      ? "bg-vine-300/10 text-vine-300"
                      : "text-zinc-400 hover:text-zinc-100 hover:bg-ink-800/80"
                  )}
                >
                  {done ? (
                    <CheckCircle2 className="h-3.5 w-3.5 text-vine-300 shrink-0" />
                  ) : (
                    <Circle className="h-3.5 w-3.5 text-zinc-600 shrink-0" />
                  )}
                  <span className="font-mono text-zinc-600 w-4 shrink-0">
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="truncate flex-1">{l.title}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </aside>

      {/* 主体 */}
      <article className="min-w-0">
        {/* breadcrumb */}
        <div className="mb-6 flex items-center gap-2 text-xs text-zinc-500">
          <Link to="/" className="hover:text-vine-300 transition">首页</Link>
          <span>/</span>
          <Link to={`/learn/${stage.id}`} className="hover:text-vine-300 transition">
            {stage.title}
          </Link>
          <span>/</span>
          <span className="text-zinc-300 truncate">{lesson.title}</span>
        </div>

        {/* header */}
        <header className="mb-8">
          <div className="flex items-center gap-2 mb-3">
            <span className="inline-flex h-6 items-center rounded-full bg-vine-300/10 px-2.5 text-[11px] font-medium text-vine-300">
              Stage 0{stage.index} · {stage.title}
            </span>
            <span className="inline-flex h-6 items-center gap-1 rounded-full border border-ink-700 bg-ink-800/60 px-2.5 text-[11px] text-zinc-400">
              <Clock className="h-3 w-3" />
              {lesson.estimatedMinutes} 分钟
            </span>
            {isDone && (
              <span className="inline-flex h-6 items-center gap-1 rounded-full bg-vine-300/15 px-2.5 text-[11px] font-medium text-vine-300">
                <Trophy className="h-3 w-3" /> 已完成
              </span>
            )}
          </div>
          <h1 className="font-display text-3xl md:text-4xl font-bold text-white tracking-tight">
            {lesson.title}
          </h1>
          <p className="mt-1 text-zinc-400">{lesson.subtitle}</p>
          <p className="mt-4 text-zinc-300/90 leading-relaxed">{lesson.description}</p>
        </header>

        {/* tabs */}
        <div className="mb-6 flex items-center gap-1 rounded-xl border border-ink-700 bg-ink-900/60 p-1 w-fit">
          <TabButton active={tab === "lesson"} onClick={() => setTab("lesson")}>
            <BookOpen className="h-3.5 w-3.5" /> 课程
          </TabButton>
          <TabButton
            active={tab === "playground"}
            onClick={() => setTab("playground")}
          >
            <FlaskConical className="h-3.5 w-3.5" /> 动手玩
            <span className="ml-1 text-[10px] text-zinc-500">
              {codeExamples.length}
            </span>
          </TabButton>
          <TabButton active={tab === "exercise"} onClick={() => setTab("exercise")}>
            <Trophy className="h-3.5 w-3.5" /> 随堂练习
            <span className="ml-1 text-[10px] text-zinc-500">
              {lesson.exercises.length}
            </span>
          </TabButton>
        </div>

        {/* tab content */}
        {tab === "lesson" && (
          <div className="prose-lesson animate-fade-in">
            {lesson.content.map((s, i) => (
              <SectionBlock key={i} section={s} lessonId={lesson.id} />
            ))}
          </div>
        )}

        {tab === "playground" && (
          <div className="space-y-5 animate-fade-in">
            {codeExamples.length === 0 ? (
              <div className="rounded-xl border border-ink-700 bg-ink-900/60 p-6 text-zinc-500 text-sm">
                本节没有可运行代码示例。
              </div>
            ) : (
              codeExamples.map((c, i) => (
                <div key={i}>
                  {c.caption && (
                    <div className="mb-2 text-xs uppercase tracking-wider text-zinc-500">
                      {c.caption}
                    </div>
                  )}
                  <CodeRunner code={c.body} lessonId={`${lesson.id}-${i + 1}`} />
                </div>
              ))
            )}
          </div>
        )}

        {tab === "exercise" && (
          <div className="space-y-5 animate-fade-in">
            {lesson.exercises.length === 0 ? (
              <div className="rounded-xl border border-ink-700 bg-ink-900/60 p-6 text-zinc-500 text-sm">
                本节暂无练习题。
              </div>
            ) : (
              lesson.exercises.map((ex, i) => (
                <ExerciseCard key={ex.id} exercise={ex} exerciseIndex={i} />
              ))
            )}
          </div>
        )}

        {/* footer nav */}
        <div className="mt-12 flex items-center justify-between gap-3 border-t border-ink-700/60 pt-6">
          {prevLesson ? (
            <Link
              to={`/lesson/${prevLesson.id}`}
              className="group inline-flex items-center gap-2 rounded-xl border border-ink-600 bg-ink-800/60 px-4 py-2.5 text-sm text-zinc-200 transition hover:bg-ink-800"
            >
              <ArrowLeft className="h-4 w-4 transition group-hover:-translate-x-0.5" />
              <span className="hidden sm:inline">{prevLesson.title}</span>
              <span className="sm:hidden">上一节</span>
            </Link>
          ) : (
            <span />
          )}

          <div className="flex items-center gap-2">
            {!isDone && (
              <button
                onClick={handleComplete}
                className="inline-flex items-center gap-1.5 rounded-xl border border-vine-300/40 bg-vine-300/10 px-4 py-2.5 text-sm font-medium text-vine-300 transition hover:bg-vine-300/20"
              >
                <CheckCircle2 className="h-4 w-4" />
                标记完成
              </button>
            )}
            {nextLesson ? (
              <Link
                to={`/lesson/${nextLesson.id}`}
                className="group inline-flex items-center gap-2 rounded-xl bg-vine-300 px-4 py-2.5 text-sm font-semibold text-ink-950 shadow-glow-vine transition hover:bg-vine-200"
              >
                <span className="hidden sm:inline">下一节 · {nextLesson.title}</span>
                <span className="sm:hidden">下一节</span>
                <ArrowRight className="h-4 w-4 transition group-hover:translate-x-0.5" />
              </Link>
            ) : (
              <Link
                to="/progress"
                className="inline-flex items-center gap-2 rounded-xl bg-vine-300 px-4 py-2.5 text-sm font-semibold text-ink-950 shadow-glow-vine"
              >
                <Trophy className="h-4 w-4" />
                查看进度
              </Link>
            )}
          </div>
        </div>
      </article>
    </div>
  );
}

function TabButton({
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
        "inline-flex items-center gap-1.5 rounded-lg px-3.5 py-1.5 text-xs font-medium transition",
        active
          ? "bg-ink-700 text-vine-300 shadow-inner-soft"
          : "text-zinc-400 hover:text-zinc-100"
      )}
    >
      {children}
    </button>
  );
}

function SectionBlock({ section, lessonId }: { section: any; lessonId: string }) {
  if (section.type === "code") {
    return (
      <div className="my-6">
        {section.caption && (
          <div className="mb-2 text-[11px] uppercase tracking-widest text-zinc-500 font-mono">
            {section.caption}
          </div>
        )}
        <CodeRunner code={section.body} lessonId={`${lessonId}-inline`} />
      </div>
    );
  }
  if (section.type === "note") {
    return (
      <div className="my-5 rounded-xl border border-ember-400/20 bg-ember-400/[0.05] px-4 py-3 text-ember-200 text-sm leading-relaxed flex gap-2.5">
        <span className="text-base leading-none mt-0.5">💡</span>
        <div dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }} />
      </div>
    );
  }
  return <div dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }} />;
}
