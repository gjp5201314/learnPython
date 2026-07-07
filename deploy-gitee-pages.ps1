# ============================================
#  Gitee Pages 一键部署脚本 (PowerShell)
#  用法: .\deploy-gitee-pages.ps1
#  自定义: .\deploy-gitee-pages.ps1 -RemoteUrl "https://gitee.com/xxx/yyy.git"
# ============================================

param(
    [string]$RemoteUrl = "https://gitee.com/ganjunpeiX/learn-python.git",
    [string]$Branch = "gh-pages",
    [string]$SourceBranch = "main"
)

$ErrorActionPreference = "Stop"

Write-Host "[1/6] 检查构建产物..." -ForegroundColor Cyan
if (-not (Test-Path "dist")) {
    Write-Host "    dist 目录不存在,正在执行 npm run build..." -ForegroundColor Yellow
    npm run build
    if ($LASTEXITCODE -ne 0) { throw "构建失败,请先修复错误" }
}

Write-Host "[2/6] 检查 git 状态..." -ForegroundColor Cyan
git status -s | Out-Null

Write-Host "[3/6] 临时保存当前分支..." -ForegroundColor Cyan
$currentBranch = git rev-parse --abbrev-ref HEAD
Write-Host "    当前分支: $currentBranch"

Write-Host "[4/6] 切换到 $Branch 分支..." -ForegroundColor Cyan
$branchExists = git show-ref --verify --quiet "refs/heads/$Branch"
if (-not $branchExists) {
    Write-Host "    $Branch 不存在,正在从 origin/$SourceBranch 创建..." -ForegroundColor Yellow
    git fetch origin
    git checkout -b $Branch "origin/$SourceBranch" 2>$null
    if ($LASTEXITCODE -ne 0) {
        # 远程分支不存在,直接从当前分支创建
        git checkout -b $Branch
    }
} else {
    git checkout $Branch
}

Write-Host "[5/6] 清空分支并拷贝 dist 内容..." -ForegroundColor Cyan
# 移除所有文件(保留 .git)
Get-ChildItem -Force | Where-Object { $_.Name -ne ".git" } | Remove-Item -Recurse -Force
Copy-Item -Path "dist\*" -Destination "." -Recurse -Force
Copy-Item -Path "dist\.gitignore" -Destination ".\.gitignore" -Force 2>$null

# 显示当前目录文件
Get-ChildItem | Select-Object Name | Format-Table -HideTableHeaders

Write-Host "[6/6] 提交并推送到 $Branch..." -ForegroundColor Cyan
git add -A
git commit -m "deploy: build $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" --allow-empty

Write-Host ""
Write-Host "准备推送到 Gitee..." -ForegroundColor Yellow
Write-Host "请输入 Gitee 用户名和密码(或 Personal Access Token 作为密码)" -ForegroundColor Yellow
Write-Host "    远程地址: $RemoteUrl" -ForegroundColor Gray
Write-Host "    目标分支: $Branch" -ForegroundColor Gray
Write-Host ""

git push origin $Branch --force

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "推送成功!" -ForegroundColor Green
    Write-Host ""
    Write-Host "============ 下一步 ============" -ForegroundColor Magenta
    Write-Host "1. 打开 Gitee 仓库: $RemoteUrl" -ForegroundColor White
    Write-Host "2. 点击顶部菜单 '服务' -> 'Gitee Pages'" -ForegroundColor White
    Write-Host "3. 点击 '启动' 按钮" -ForegroundColor White
    Write-Host "4. 部署分支选择: $Branch" -ForegroundColor White
    Write-Host "5. 部署目录留空(根目录)" -ForegroundColor White
    Write-Host "6. 点击 '启动部署'" -ForegroundColor White
    Write-Host "7. 等待 1-2 分钟后,Gitee 会分配一个访问地址,形如:" -ForegroundColor White
    Write-Host "   https://ganjunpeiX.gitee.io/learn-python" -ForegroundColor Green
    Write-Host ""
    Write-Host "注意: Gitee Pages 必须完成实名认证,仓库必须公开!" -ForegroundColor Red
} else {
    Write-Host "推送失败,请检查网络/凭证" -ForegroundColor Red
    Write-Host "常见原因: 仓库未公开 / 未完成实名认证 / 凭证错误" -ForegroundColor Red
}

# 切回原分支
Write-Host ""
Write-Host "切回原分支: $currentBranch" -ForegroundColor Cyan
git checkout $currentBranch
