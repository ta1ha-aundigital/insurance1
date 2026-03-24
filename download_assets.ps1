$ErrorActionPreference = "Continue"

$baseDir = "e:\Insurance Websites"
$htmlFiles = @(Get-ChildItem -Path $baseDir -Filter "*.html" | Where-Object { $_.FullName -notmatch "assets" })
$cssFiles = @(Get-ChildItem -Path $baseDir -Filter "*.css" | Where-Object { $_.FullName -notmatch "assets" })

$allFiles = $htmlFiles + $cssFiles

if (-not (Test-Path "$baseDir\assets\images")) {
    New-Item -ItemType Directory -Force -Path "$baseDir\assets\images" | Out-Null
}

$urlMap = @{}
$counter = 1

# 1. Extract URLs
foreach ($file in $allFiles) {
    if (-not $file) { continue }
    $content = Get-Content $file.FullName -Raw
    
    # Match any http/https URL that ends right before quotes, spaces, or closing parens.
    $matches = [regex]::Matches($content, 'https?://[^"''\)\s]+')
    
    foreach ($match in $matches) {
        $url = $match.Value
        
        # Skip CDNs for fonts and stylesheets
        if ($url -match "fonts\.googleapis" -or $url -match "bootstrap" -or $url -match "cloudflare" -or $url -match "jsdelivr") {
            continue
        }
        
        if (-not $urlMap.ContainsKey($url)) {
            $ext = ".jpg"
            if ($url -match "\.svg" -or $url -match "iconify\.design") { $ext = ".svg" }
            elseif ($url -match "\.png") { $ext = ".png" }
            elseif ($url -match "\.gif") { $ext = ".gif" }
            
            $filename = "img_$($counter.ToString('000'))$ext"
            $urlMap[$url] = $filename
            $counter++
            
            Write-Host "Downloading to $filename -> $url"
            try {
                Invoke-WebRequest -Uri $url -OutFile "$baseDir\assets\images\$filename" -UseBasicParsing -TimeoutSec 15
            } catch {
                Write-Host "Failed to download $url"
                # Remove from map so we don't accidentally replace it with a broken local path
                # Actually, let's keep it but output warning. If it fails, maybe it's dead, but we will let it gracefully fail.
            }
        }
    }
}

# 2. Replace in files
foreach ($file in $allFiles) {
    if (-not $file) { continue }
    $content = Get-Content $file.FullName -Raw
    $modified = $false
    
    foreach ($key in $urlMap.Keys) {
        $filename = $urlMap[$key]
        
        # Only replace if the file actually downloaded correctly (over 0 bytes)
        if (Test-Path "$baseDir\assets\images\$filename") {
            $fileInfo = Get-Item "$baseDir\assets\images\$filename"
            if ($fileInfo.Length -gt 0) {
                if ($content.Contains($key)) {
                    $content = $content.Replace($key, "assets/images/$filename")
                    $modified = $true
                }
            }
        }
    }
    
    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated $($file.Name) with local asset paths!"
    }
}
Write-Host "All downloads and replacements complete."
