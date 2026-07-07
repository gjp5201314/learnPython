import { useEffect, useState } from "react";
import { Outlet, useLocation } from "react-router-dom";
import { Menu, X } from "lucide-react";
import Sidebar from "./Sidebar";
import { cn } from "@/lib/utils";

export default function Layout() {
  const { pathname } = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    setMobileOpen(false);
    window.scrollTo({ top: 0, behavior: "instant" as ScrollBehavior });
  }, [pathname]);

  return (
    <div className="flex min-h-screen w-full bg-ink-950">
      {/* Desktop sidebar */}
      <div className="hidden md:block sticky top-0 h-screen">
        <Sidebar />
      </div>

      {/* Mobile drawer */}
      <div
        className={cn(
          "fixed inset-0 z-40 md:hidden transition-opacity",
          mobileOpen
            ? "opacity-100 pointer-events-auto"
            : "opacity-0 pointer-events-none"
        )}
      >
        <div
          className="absolute inset-0 bg-black/60"
          onClick={() => setMobileOpen(false)}
        />
        <div
          className={cn(
            "absolute left-0 top-0 h-full w-72 bg-ink-900 border-r border-ink-700 shadow-2xl transition-transform",
            mobileOpen ? "translate-x-0" : "-translate-x-full"
          )}
        >
          <Sidebar onNavigate={() => setMobileOpen(false)} />
        </div>
      </div>

      {/* Main content */}
      <main className="flex-1 min-w-0 relative">
        {/* Mobile top bar */}
        <div className="md:hidden sticky top-0 z-30 flex items-center justify-between border-b border-ink-700/60 bg-ink-950/80 backdrop-blur px-4 py-3">
          <button
            onClick={() => setMobileOpen((s) => !s)}
            className="p-1.5 rounded-md text-zinc-300 hover:bg-ink-800"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
          <span className="font-display text-base font-semibold text-white">
            PyPath
          </span>
          <div className="w-7" />
        </div>

        <div className="mx-auto max-w-[1240px] px-5 md:px-10 py-8 md:py-12">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
