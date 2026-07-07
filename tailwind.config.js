/** @type {import('tailwindcss').Config} */

export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    container: {
      center: true,
    },
    extend: {
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"],
        display: ["Space Grotesk", "Inter", "ui-sans-serif"],
        mono: ["JetBrains Mono", "ui-monospace", "SFMono-Regular", "monospace"],
      },
      colors: {
        ink: {
          950: "#0B0D12",
          900: "#10131A",
          800: "#161A23",
          700: "#1B1F27",
          600: "#22262F",
          500: "#2A2F3A",
        },
        vine: {
          50: "#E9FBE9",
          100: "#C8F4C8",
          200: "#A6EDA6",
          300: "#7EE787",
          400: "#5BD45D",
          500: "#3AB53C",
          600: "#2D8E2E",
        },
        ember: {
          300: "#FFD27A",
          400: "#FFB454",
          500: "#F39C32",
        },
      },
      boxShadow: {
        "glow-vine":
          "0 0 0 1px rgba(126,231,135,0.35), 0 8px 30px -10px rgba(126,231,135,0.45)",
        "glow-ember":
          "0 0 0 1px rgba(255,180,84,0.35), 0 8px 30px -10px rgba(255,180,84,0.45)",
        "inner-soft": "inset 0 1px 0 0 rgba(255,255,255,0.04)",
      },
      backgroundImage: {
        "grid-fade":
          "linear-gradient(to bottom, rgba(11,13,18,0) 0%, rgba(11,13,18,1) 80%), radial-gradient(circle at 1px 1px, rgba(255,255,255,0.05) 1px, transparent 0)",
        "noise":
          "url(\"data:image/svg+xml;utf8,<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.04 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
      },
      keyframes: {
        "fade-in": {
          "0%": { opacity: "0", transform: "translateY(8px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        "slide-in-left": {
          "0%": { opacity: "0", transform: "translateX(-16px)" },
          "100%": { opacity: "1", transform: "translateX(0)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        "pulse-dot": {
          "0%, 100%": { opacity: "1" },
          "50%": { opacity: "0.4" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-6px)" },
        },
      },
      animation: {
        "fade-in": "fade-in 0.6s ease-out both",
        "slide-in-left": "slide-in-left 0.5s ease-out both",
        shimmer: "shimmer 2.4s linear infinite",
        "pulse-dot": "pulse-dot 1.6s ease-in-out infinite",
        float: "float 4s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};
