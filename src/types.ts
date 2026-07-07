export type StageId =
  | "basics"
  | "data-structures"
  | "oop"
  | "stdlib"
  | "projects";

export type LessonSectionType = "text" | "code" | "note";

export interface LessonSection {
  type: LessonSectionType;
  /** Markdown-style body for text/note; raw python code for 'code'. */
  body: string;
  /** Optional caption shown above code blocks. */
  caption?: string;
}

export type ExerciseType = "multiple-choice" | "fill-blank" | "predict-output";

export interface Exercise {
  id: string;
  type: ExerciseType;
  question: string;
  options?: string[];
  answer: string;
  hint: string;
  explanation: string;
}

export interface Lesson {
  id: string;
  stage: StageId;
  order: number;
  title: string;
  subtitle: string;
  description: string;
  estimatedMinutes: number;
  content: LessonSection[];
  exercises: Exercise[];
}

export interface Stage {
  id: StageId;
  index: number;
  title: string;
  tagline: string;
  description: string;
  accent: "vine" | "ember" | "sky" | "rose" | "violet";
  icon: "spark" | "stack" | "cube" | "library" | "rocket";
  lessonIds: string[];
}
