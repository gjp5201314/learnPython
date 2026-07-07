# PyPath · Python 互动学习平台

> 掌握 Python，从一行代码开始。
> Master Python, one line at a time.

PyPath 是一款**纯前端**的 Python 互动学习平台，面向零基础到进阶学习者。通过 5 大阶段、25 个章节的**结构化学习路线**、**浏览器内可运行**的代码示例、**随堂练习**和**进度跟踪**，帮助用户系统掌握 Python 编程。

所有代码示例都通过 [Pyodide](https://pyodide.org/)（WebAssembly 版 Python 解释器）真实在浏览器内执行，无需任何后端服务。课程数据与用户进度全部存放在前端（`localStorage`），刷新不丢失。

---

## ✨ 核心特性

- **🎯 5 阶段 25 章节**：从入门语法 → 数据结构 → 面向对象 → 标准库 → 实战项目，构成一条完整的 Python 学习路径。
- **⚡ 浏览器内真实运行 Python**：内置代码运行器，示例代码通过 Pyodide 真正执行，结果立即可见。
- **📝 随堂练习即时反馈**：选择题 / 填空题 / 预测输出题，提交后立即判分并给出解析。
- **📈 进度可视化**：进度环、热力图、累计学习时长、连续打卡天数，全方位呈现学习成果。
- **🏆 成就徽章系统**：完成首章节、跑通 10 次代码、答对 15 道题等 7 个徽章，激励持续学习。
- **🎨 暗色 IDE 风格 UI**：深空黑 + 藤蔓绿（`#7EE787`）的开发者向审美，移动端自适应。

---

## 🧰 技术栈

| 类别 | 选型 |
|------|------|
| 前端框架 | React 18 + TypeScript |
| 构建工具 | Vite 6 |
| 样式方案 | TailwindCSS 3 + 自定义 CSS 变量 |
| 路由 | react-router-dom 7 |
| 状态管理 | Zustand 5（带 `persist` 中间件持久化到 localStorage）|
| Python 解释器 | Pyodide（CDN 加载，WebAssembly）|
| 图标 | lucide-react |
| 工具 | clsx、tailwind-merge |
| 字体 | Google Fonts — JetBrains Mono + Space Grotesk + Inter |

---

## 📂 项目结构

```
src/
├── components/              # 通用组件
│   ├── Layout.tsx           # 全局布局（侧边栏 + 主区 + 移动端抽屉）
│   ├── Sidebar.tsx          # 左侧导航
│   ├── CodeRunner.tsx       # 代码编辑器 + 运行 + 输出面板
│   ├── ExerciseCard.tsx     # 练习题卡片
│   ├── StageCard.tsx        # 阶段卡片
│   └── ProgressRing.tsx     # 进度环
├── pages/                   # 页面
│   ├── Home.tsx             # 首页（Hero + 学习路线 + 实时统计）
│   ├── Learn.tsx            # 阶段详情 / 章节列表
│   ├── Lesson.tsx           # 课程详情（知识点 + 代码 + 练习）
│   ├── Practice.tsx         # 练习中心
│   └── Progress.tsx         # 进度页（统计、徽章、热力图）
├── data/
│   └── lessons.ts           # 静态课程数据（25 章节 + 阶段定义）
├── store/
│   └── useProgressStore.ts  # Zustand 状态（含徽章解锁、连续打卡）
├── lib/
│   ├── pyodide.ts           # Pyodide 加载与执行封装
│   ├── highlight.ts         # Python 语法高亮
│   └── utils.ts             # cn / 工具函数
├── types.ts                 # 全局类型定义
├── App.tsx                  # 路由配置
└── main.tsx                 # 入口
```

---

## 🚀 快速开始

### 环境要求

- Node.js ≥ 18
- 现代浏览器（支持 WebAssembly 与 ES2020）

### 安装与运行

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 类型检查
npm run check

# 代码风格检查
npm run lint

# 生产构建
npm run build

# 本地预览生产包
npm run preview
```

启动后访问 `http://localhost:5173` 即可。

---

## 🗺️ 路由

| 路径 | 用途 |
|------|------|
| `/` | 首页：Hero、学习路线、实时统计 |
| `/learn` | 全部阶段总览 |
| `/learn/:stageId` | 单个阶段下的章节列表 |
| `/lesson/:lessonId` | 课程详情：知识点讲解 + 代码运行器 + 随堂练习 |
| `/practice` | 练习中心 |
| `/progress` | 进度页：统计、徽章、学习日历热力图 |

---

## 📚 学习路线

| 阶段 | 主题 | 章节数 |
|------|------|--------|
| 01 | Python 入门基础 | 5 |
| 02 | 数据结构 | 5 |
| 03 | 面向对象 | 5 |
| 04 | 标准库 | 5 |
| 05 | 实战项目 | 5 |

各阶段主题详见 [prd.md](./.trae/documents/prd.md)。

---

## 🏆 成就徽章

| ID | 名称 | 解锁条件 |
|----|------|----------|
| `first-lesson` | 初出茅庐 | 完成第 1 个章节 |
| `five-lessons` | 小有所成 | 完成 5 个章节 |
| `all-rounder` | 通关玩家 | 完成 15 个章节 |
| `first-run` | Hello World | 首次运行代码 |
| `runner` | 代码狂人 | 运行代码 10 次 |
| `quiz-novice` | 答题新手 | 完成 5 道练习 |
| `quiz-master` | 答题达人 | 完成 15 道练习 |

> 徽章在 `src/pages/Progress.tsx` 的 `BADGES` 数组中维护；解锁逻辑在 `src/store/useProgressStore.ts`。

---

## 🧠 数据持久化

学习进度通过 Zustand 的 `persist` 中间件写入 `localStorage`，key 为 `pypath-progress`：

```ts
{
  completedLessons: string[];        // 已完成章节 id
  completedExercises: string[];     // 已答对练习 id
  totalCodeRuns: number;             // 代码累计运行次数
  streakDays: number;                // 连续学习天数
  lastStudyDate: string;             // 最近学习日期 (yyyy-mm-dd)
  unlockedBadges: string[];          // 已解锁徽章 id
  studyLog: Record<string, number>;  // 每日学习分钟数（用于热力图）
}
```

在「学习进度」页可点击右上角「重置进度」清空全部记录。

---

## 🎨 设计语言

- **主色**：`#0B0D12`（深空黑）+ `#7EE787`（藤蔓绿，Python 经典色）+ `#FFB454`（暖橙，强调）
- **次色**：`#1B1F27`（石墨灰）、`#9CA3AF`（浅灰文本）、`#FFFFFF`（纯白）
- **字体**：标题 `Space Grotesk`、正文 `Inter`、代码 `JetBrains Mono`
- **风格**：圆角 12–16px、卡片化、细噪点纹理、悬停微光

---

## 📄 文档

- 产品需求：[`.trae/documents/prd.md`](./.trae/documents/prd.md)
- 技术架构：[`.trae/documents/tech-architecture.md`](./.trae/documents/tech-architecture.md)

---

## 📝 License

本项目为学习用途的演示项目，欢迎参考与二次开发。
