// Pyodide 浏览器内 Python 解释器封装
// 通过 CDN 加载，单例缓存

declare global {
  interface Window {
    loadPyodide?: (config?: { indexURL?: string }) => Promise<any>;
  }
}

let pyodideInstance: any = null;
let loadingPromise: Promise<any> | null = null;

const PYODIDE_VERSION = "0.26.4";
const PYODIDE_INDEX = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

function loadScript(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[data-pyodide-loader]`)) {
      resolve();
      return;
    }
    const script = document.createElement("script");
    script.src = src;
    script.async = true;
    script.setAttribute("data-pyodide-loader", "true");
    script.onload = () => resolve();
    script.onerror = () => reject(new Error("无法加载 Pyodide 脚本"));
    document.head.appendChild(script);
  });
}

export async function getPyodide(onProgress?: (msg: string) => void): Promise<any> {
  if (pyodideInstance) return pyodideInstance;
  if (loadingPromise) return loadingPromise;

  loadingPromise = (async () => {
    onProgress?.("正在加载 Python 解释器 (~10MB)...");
    await loadScript(`${PYODIDE_INDEX}pyodide.js`);
    if (!window.loadPyodide) {
      throw new Error("Pyodide 加载失败");
    }
    onProgress?.("初始化运行时...");
    const py = await window.loadPyodide({ indexURL: PYODIDE_INDEX });
    onProgress?.("就绪");
    pyodideInstance = py;
    return py;
  })();

  return loadingPromise;
}

export interface RunResult {
  ok: boolean;
  stdout: string;
  stderr: string;
}

export async function runPython(code: string): Promise<RunResult> {
  const py = await getPyodide();
  let stdout = "";
  let stderr = "";
  py.setStdout({
    batched: (s: string) => {
      stdout += s + "\n";
    },
  });
  py.setStderr({
    batched: (s: string) => {
      stderr += s + "\n";
    },
  });
  try {
    await py.runPythonAsync(code);
  } catch (e: any) {
    stderr += (e?.message || String(e)) + "\n";
  }
  return {
    ok: !stderr,
    stdout: stdout.trimEnd(),
    stderr: stderr.trimEnd(),
  };
}
