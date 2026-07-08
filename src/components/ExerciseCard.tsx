import { useState } from "react";
import { Lightbulb, Check, X, RefreshCcw, Sparkles } from "lucide-react";
import type { Exercise } from "@/types";
import { cn } from "@/lib/utils";
import { useProgressStore } from "@/store/useProgressStore";

interface ExerciseCardProps {
  exercise: Exercise;
  exerciseIndex: number;
}

export default function ExerciseCard({ exercise, exerciseIndex }: ExerciseCardProps) {
  const [selected, setSelected] = useState<string | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [fillValue, setFillValue] = useState("");
  const markComplete = useProgressStore((s) => s.markExerciseComplete);
  const completed = useProgressStore((s) =>
    s.completedExercises.includes(exercise.id)
  );

  const isCorrect = () => {
    if (exercise.type === "fill-blank") {
      return fillValue.trim().toLowerCase() === exercise.answer.trim().toLowerCase();
    }
    return selected === exercise.answer;
  };

  const handleSubmit = () => {
    setSubmitted(true);
    if (isCorrect()) {
      markComplete(exercise.id);
    }
  };

  const handleReset = () => {
    setSelected(null);
    setSubmitted(false);
    setShowHint(false);
    setFillValue("");
  };

  return (
    <div className="rounded-2xl border border-ink-700 bg-ink-900/70 p-5 md:p-6">
      <div className="mb-3 flex items-center gap-2">
        <span className="inline-flex h-6 items-center rounded-full bg-vine-300/10 px-2.5 text-[11px] font-medium text-vine-300">
          练习 {exerciseIndex + 1}
        </span>
        {completed && (
          <span className="inline-flex h-6 items-center gap-1 rounded-full bg-vine-300/15 px-2 text-[11px] font-medium text-vine-300">
            <Check className="h-3 w-3" /> 已掌握
          </span>
        )}
      </div>

      <h3 className="text-lg font-semibold text-white font-display leading-snug">
        {exercise.question}
      </h3>

      {/* Body */}
      <div className="mt-4">
        {exercise.type === "fill-blank" || exercise.type === "predict-output" ? (
          <div>
            <input
              value={fillValue}
              onChange={(e) => setFillValue(e.target.value)}
              disabled={submitted}
              placeholder={
                exercise.type === "predict-output"
                  ? "在此输入预期输出…"
                  : "在此填入答案…"
              }
              className="w-full rounded-lg border border-ink-600 bg-ink-800/80 px-4 py-2.5 font-mono text-sm text-zinc-100 placeholder-zinc-500 outline-none focus:border-vine-300/60 focus:ring-1 focus:ring-vine-300/30 transition"
            />
          </div>
        ) : (
          <div className="space-y-2">
            {exercise.options?.map((opt, i) => {
              const isPicked = selected === opt;
              const isAnswer = opt === exercise.answer;
              return (
                <button
                  key={i}
                  disabled={submitted}
                  onClick={() => setSelected(opt)}
                  className={cn(
                    "flex w-full items-center gap-3 rounded-xl border px-4 py-3 text-left text-sm transition",
                    "border-ink-600 bg-ink-800/60 hover:border-vine-300/40 hover:bg-ink-800",
                    isPicked && !submitted && "border-vine-300/60 bg-vine-300/5",
                    submitted && isAnswer && "border-vine-300 bg-vine-300/10",
                    submitted && isPicked && !isAnswer && "border-rose-400/50 bg-rose-400/5"
                  )}
                >
                  <span
                    className={cn(
                      "flex h-6 w-6 shrink-0 items-center justify-center rounded-md border text-[11px] font-mono",
                      isPicked || (submitted && isAnswer)
                        ? "border-vine-300 bg-vine-300/20 text-vine-300"
                        : "border-ink-500 text-zinc-500"
                    )}
                  >
                    {String.fromCharCode(65 + i)}
                  </span>
                  <span className="text-zinc-200 font-mono text-[13.5px] flex-1">{opt}</span>
                  {submitted && isAnswer && <Check className="h-4 w-4 text-vine-300" />}
                  {submitted && isPicked && !isAnswer && (
                    <X className="h-4 w-4 text-rose-400" />
                  )}
                </button>
              );
            })}
          </div>
        )}
      </div>

      {/* Hint */}
      {showHint && !submitted && (
        <div className="mt-4 flex gap-2.5 rounded-lg border border-ember-400/20 bg-ember-400/[0.04] p-3.5 text-sm text-ember-300 animate-fade-in">
          <Lightbulb className="h-4 w-4 mt-0.5 shrink-0" />
          <span>{exercise.hint}</span>
        </div>
      )}

      {/* Result feedback */}
      {submitted && (
        <div
          className={cn(
            "mt-4 rounded-lg p-3.5 text-sm animate-fade-in",
            isCorrect()
              ? "border border-vine-300/30 bg-vine-300/[0.06] text-vine-200"
              : "border border-rose-400/30 bg-rose-400/[0.05] text-rose-200"
          )}
        >
          <div className="font-semibold mb-1.5 flex items-center gap-1.5">
            {isCorrect() ? (
              <>
                <Check className="h-4 w-4" /> 答对了！
              </>
            ) : (
              <>
                <X className="h-4 w-4" /> 还差一点，再想想
              </>
            )}
          </div>
          <div className="text-zinc-300/90 leading-relaxed">
            {exercise.explanation}
          </div>
        </div>
      )}

      {/* Actions */}
      <div className="mt-5 flex flex-wrap items-center gap-2">
        {!submitted && (
          <>
            <button
              onClick={() => setShowHint((s) => !s)}
              className="inline-flex items-center gap-1.5 rounded-md border border-ink-600 bg-ink-800/60 px-3 py-1.5 text-xs text-zinc-300 hover:border-ember-400/40 hover:text-ember-300 transition"
            >
              <Lightbulb className="h-3.5 w-3.5" />
              {showHint ? "隐藏提示" : "查看提示"}
            </button>
            <button
              onClick={handleSubmit}
              disabled={
                (exercise.type === "fill-blank" && !fillValue.trim()) ||
                (exercise.type !== "fill-blank" && !selected)
              }
              className="ml-auto inline-flex items-center gap-1.5 rounded-md bg-vine-300 px-4 py-1.5 text-xs font-semibold text-ink-950 shadow-glow-vine transition hover:bg-vine-200 disabled:opacity-40 disabled:shadow-none"
            >
              <Sparkles className="h-3.5 w-3.5" />
              提交答案
            </button>
          </>
        )}
        {submitted && (
          <button
            onClick={handleReset}
            className="ml-auto inline-flex items-center gap-1.5 rounded-md border border-ink-600 bg-ink-800/60 px-3 py-1.5 text-xs text-zinc-300 hover:bg-ink-700 transition"
          >
            <RefreshCcw className="h-3.5 w-3.5" />
            再试一次
          </button>
        )}
      </div>
    </div>
  );
}
