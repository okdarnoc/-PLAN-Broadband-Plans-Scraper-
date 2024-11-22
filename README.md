# Broadband Plans Scraper 寬頻方案爬蟲工具

[English](#english) | [繁體中文](#繁體中文)

## English

### Overview
This Python script scrapes broadband plan information from findplanking.com. It collects plan details including titles, descriptions, pricing, and contact information, saving the data in multiple formats (CSV, JSON, and TXT) for easy analysis and processing.

### Features
- Headless browser automation using Selenium
- Concurrent scraping with multi-threading
- Data saved in multiple formats (CSV, JSON, TXT)
- Robust error handling
- Clean and documented code

### Requirements
- Python 3.6+
- ChromeDriver
- Required Python packages:
  ```
  selenium
  beautifulsoup4
  ```

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/broadband-plans-scraper.git
   cd broadband-plans-scraper
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download ChromeDriver and update the path in the script:
   - Download ChromeDriver from: https://sites.google.com/chromium.org/driver/
   - Update `CHROMEDRIVER_PATH` in the script

### Usage
Run the script:
```bash
python broadband_plans_scraper.py
```

### Output
The script generates three files:
- `broadband_plans.csv`: Data in CSV format
- `broadband_plans.json`: Data in JSON format
- `broadband_plans.txt`: Human-readable text format

### License
MIT License

---

## 繁體中文

### 概述
這個 Python 腳本用於爬取 findplanking.com 的寬頻方案資訊。它收集方案標題、描述、價格和聯絡資訊，並將數據以多種格式（CSV、JSON 和 TXT）保存，方便後續分析和處理。

### 功能特點
- 使用 Selenium 進行無頭瀏覽器自動化
- 使用多線程進行並發爬取
- 數據以多種格式保存（CSV、JSON、TXT）
- 強大的錯誤處理機制
- 清晰且有文檔說明的代碼

### 系統要求
- Python 3.6+
- ChromeDriver
- 必需的 Python 套件：
  ```
  selenium
  beautifulsoup4
  ```

### 安裝步驟
1. 克隆此專案：
   ```bash
   git clone https://github.com/yourusername/broadband-plans-scraper.git
   cd broadband-plans-scraper
   ```

2. 安裝必需套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 下載 ChromeDriver 並更新腳本中的路徑：
   - 從這裡下載 ChromeDriver：https://sites.google.com/chromium.org/driver/
   - 在腳本中更新 `CHROMEDRIVER_PATH`

### 使用方法
執行腳本：
```bash
python broadband_plans_scraper.py
```

### 輸出檔案
腳本會生成三個檔案：
- `broadband_plans.csv`：CSV 格式的數據
- `broadband_plans.json`：JSON 格式的數據
- `broadband_plans.txt`：人類可讀的文本格式

### 授權條款
MIT 授權
