import { useMemo } from "react";

interface ProgressRingProps {
  value: number; // 0 - 100
  size?: number;
  stroke?: number;
  color?: string;
  label?: string;
  sublabel?: string;
}

export default function ProgressRing({
  value,
  size = 120,
  stroke = 10,
  color = "#7EE787",
  label,
  sublabel,
}: ProgressRingProps) {
  const v = Math.max(0, Math.min(100, value));
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = useMemo(() => circumference * (1 - v / 100), [circumference, v]);

  return (
    <div className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="rgba(255,255,255,0.06)"
          strokeWidth={stroke}
          fill="none"
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={color}
          strokeWidth={stroke}
          strokeLinecap="round"
          fill="none"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          style={{ transition: "stroke-dashoffset 0.8s ease" }}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <div className="font-mono text-2xl font-semibold text-white">{Math.round(v)}%</div>
        {label && <div className="text-[10px] uppercase tracking-widest text-zinc-500 mt-0.5">{label}</div>}
        {sublabel && <div className="text-[11px] text-zinc-400 mt-1">{sublabel}</div>}
      </div>
    </div>
  );
}
