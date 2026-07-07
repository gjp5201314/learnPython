import { Link, NavLink, useLocation } from "react-router-dom";
import { Home, Map, BarChart3, Code2, Github } from "lucide-react";
import { cn } from "@/lib/utils";

const navItems = [
  { to: "/", label: "首页", icon: Home, end: true },
  { to: "/learn", label: "学习路线", icon: Map },
  { to: "/practice", label: "练习中心", icon: Code2 },
  { to: "/progress", label: "学习进度", icon: BarChart3 },
];

interface SidebarProps {
  className?: string;
  onNavigate?: () => void;
}

export default function Sidebar({ className, onNavigate }: SidebarProps) {
  const location = useLocation();
  return (
    <aside
      className={cn(
        "flex h-full w-64 shrink-0 flex-col border-r border-ink-700/60 bg-ink-900/80 backdrop-blur",
        className
      )}
    >
      <Link
        to="/"
        onClick={onNavigate}
        className="flex items-center gap-3 px-5 py-5 group"
      >
        <div className="relative h-9 w-9 rounded-xl bg-gradient-to-br from-vine-300 to-vine-500 grid place-items-center text-ink-950 font-bold shadow-glow-vine">
          <span className="font-display">Py</span>
          <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-ember-400 ring-2 ring-ink-900 animate-pulse-dot" />
        </div>
        <div className="flex flex-col leading-tight">
          <span className="font-display text-lg font-semibold text-white tracking-tight">
            PyPath
          </span>
          <span className="text-[10px] uppercase tracking-[0.2em] text-vine-300/80">
            Learn · Code · Ship
          </span>
        </div>
      </Link>

      <nav className="px-3 py-2 flex flex-col gap-1">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              onClick={onNavigate}
              className={({ isActive }) =>
                cn(
                  "group relative flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all",
                  isActive
                    ? "bg-vine-300/10 text-vine-300"
                    : "text-zinc-400 hover:text-zinc-100 hover:bg-ink-800/80"
                )
              }
            >
              {({ isActive }) => (
                <>
                  {isActive && (
                    <span className="absolute left-0 top-1/2 h-5 w-[3px] -translate-y-1/2 rounded-r-full bg-vine-300" />
                  )}
                  <Icon className="h-4 w-4" />
                  <span>{item.label}</span>
                </>
              )}
            </NavLink>
          );
        })}
      </nav>

      <div className="mt-auto p-4">
        <div className="rounded-xl border border-ink-700/60 bg-ink-800/60 p-4">
          <div className="text-xs text-zinc-500 mb-1">当前路径</div>
          <div className="text-sm font-mono text-zinc-200 truncate">
            {location.pathname}
          </div>
        </div>
        <a
          href="https://github.com"
          target="_blank"
          rel="noreferrer"
          className="mt-3 flex items-center gap-2 text-xs text-zinc-500 hover:text-zinc-300 transition-colors"
        >
          <Github className="h-3.5 w-3.5" />
          <span>v1.0 · made for learners</span>
        </a>
      </div>
    </aside>
  );
}
