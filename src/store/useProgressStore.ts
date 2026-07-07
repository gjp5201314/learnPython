import { create } from "zustand";
import { persist } from "zustand/middleware";

interface ProgressState {
  completedLessons: string[];
  completedExercises: string[];
  totalCodeRuns: number;
  streakDays: number;
  lastStudyDate: string;
  unlockedBadges: string[];
  studyLog: Record<string, number>; // yyyy-mm-dd -> minutes

  markLessonComplete: (lessonId: string) => void;
  markExerciseComplete: (exerciseId: string) => void;
  registerCodeRun: () => void;
  addStudyMinutes: (minutes: number) => void;
  unlockBadge: (badge: string) => void;
  reset: () => void;
}

const todayKey = () => new Date().toISOString().slice(0, 10);

export const useProgressStore = create<ProgressState>()(
  persist(
    (set, get) => ({
      completedLessons: [],
      completedExercises: [],
      totalCodeRuns: 0,
      streakDays: 0,
      lastStudyDate: "",
      unlockedBadges: [],
      studyLog: {},

      markLessonComplete: (lessonId) => {
        const { completedLessons, unlockedBadges } = get();
        if (completedLessons.includes(lessonId)) return;
        const next = [...completedLessons, lessonId];
        const newBadges = [...unlockedBadges];
        if (next.length === 1 && !newBadges.includes("first-lesson"))
          newBadges.push("first-lesson");
        if (next.length >= 5 && !newBadges.includes("five-lessons"))
          newBadges.push("five-lessons");
        if (next.length >= 15 && !newBadges.includes("all-rounder"))
          newBadges.push("all-rounder");
        set({ completedLessons: next, unlockedBadges: newBadges });
        get().addStudyMinutes(2);
      },

      markExerciseComplete: (exerciseId) => {
        const { completedExercises, unlockedBadges } = get();
        if (completedExercises.includes(exerciseId)) return;
        const next = [...completedExercises, exerciseId];
        const newBadges = [...unlockedBadges];
        if (next.length >= 5 && !newBadges.includes("quiz-novice"))
          newBadges.push("quiz-novice");
        if (next.length >= 15 && !newBadges.includes("quiz-master"))
          newBadges.push("quiz-master");
        set({ completedExercises: next, unlockedBadges: newBadges });
      },

      registerCodeRun: () => {
        const { totalCodeRuns, unlockedBadges } = get();
        const newBadges = [...unlockedBadges];
        if (totalCodeRuns + 1 >= 1 && !newBadges.includes("first-run"))
          newBadges.push("first-run");
        if (totalCodeRuns + 1 >= 10 && !newBadges.includes("runner"))
          newBadges.push("runner");
        set({ totalCodeRuns: totalCodeRuns + 1, unlockedBadges: newBadges });
      },

      addStudyMinutes: (minutes) => {
        const today = todayKey();
        const { studyLog, lastStudyDate, streakDays } = get();
        const updatedLog = { ...studyLog, [today]: (studyLog[today] || 0) + minutes };
        let newStreak = streakDays;
        if (lastStudyDate !== today) {
          const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
          newStreak = lastStudyDate === yesterday ? streakDays + 1 : 1;
        }
        set({
          studyLog: updatedLog,
          lastStudyDate: today,
          streakDays: newStreak,
        });
      },

      unlockBadge: (badge) =>
        set((s) =>
          s.unlockedBadges.includes(badge)
            ? s
            : { unlockedBadges: [...s.unlockedBadges, badge] }
        ),

      reset: () =>
        set({
          completedLessons: [],
          completedExercises: [],
          totalCodeRuns: 0,
          streakDays: 0,
          lastStudyDate: "",
          unlockedBadges: [],
          studyLog: {},
        }),
    }),
    {
      name: "pypath-progress",
    }
  )
);
