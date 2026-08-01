# 🚀 Python Data Science & Automation Portfolio

> A production-ready repository showcasing end-to-end Python projects spanning web scraping, data engineering, business intelligence, competitor analytics, and predictive machine learning.

---

## 📂 Repository Structure

```text
python-portfolio/
│
├── 01_catalog_scraper/        # Project A: Web Scraping Pipeline
├── 02_sales_dashboard/        # Project B: Interactive BI Analytics Dashboard
├── 03_price_tracker/          # Project C: Competitor Price Alert Engine
├── 04_churn_predictor/        # Project D: ML Customer Churn Predictor
├── screenshots/               # Visual outcomes & terminal execution logs
├── data/                      # Output datasets (Excel, CSV)
├── requirements.txt           # Environment dependencies
└── README.md                  # Project documentation hub

🛠️ Project Showcases
1️⃣ Project A: Automated E-Commerce Catalog Scraper
Folder: 01_catalog_scraper/

Tech Stack: Python, BeautifulSoup4, requests, pandas, openpyxl

Key Features:

Multi-page web crawler with automated pagination navigation.

RegEx (re) text sanitization to clean raw price strings, currency symbols, and stock status.

Rate-limiting and error handling for reliable HTTP requests.

Exports structured data directly into cleanly formatted Excel sheets (.xlsx).

📊 Execution Outcome:
2️⃣ Project B: Executive Sales & Revenue Analytics Dashboard
Folder: 02_sales_dashboard/

Tech Stack: Python, Streamlit, Plotly Express, pandas

Key Features:

Interactive Web UI built with Streamlit for real-time business metrics tracking.

High-level KPI summaries: Total Revenue, Units Sold, and Average Profit Margins.

Dynamic category performance visualizations and profit margin distribution charts powered by Plotly.

Category unit-share analysis via interactive donut breakdown.

📊 Execution Outcome:
3️⃣ Project C: Automated Competitor Price Tracker & Alert Engine
Folder: 03_price_tracker/

Tech Stack: Python, pandas, datetime

Key Features:

Real-time variance engine measuring live competitor pricing against baseline target thresholds.

Automated log formatting tracking product status (NORMAL vs. ALERT BREACH).

Automated notification trigger system whenever prices fall below target deal levels.

Structured terminal audit logging for continuous data monitoring.

📊 Execution Outcome:
4️⃣ Project D: Machine Learning Customer Churn Predictor
Folder: 04_churn_predictor/

Tech Stack: Python, scikit-learn, pandas, NumPy

Key Features:

End-to-End ML Pipeline: Complete data preprocessing, feature encoding, train/test split, and model evaluation workflow.

Classifier Model: Built using a Random Forest Classifier trained to detect customer attrition patterns based on tenure length, monthly spend (Monthly_Charges_$), and customer service interaction history (Support_Calls).

High Performance: Achieves 96.00% Test Accuracy on evaluation data.

Actionable Risk Tagging: Generates real-time churn probability scores alongside instant visual risk indicators (HIGH RISK 🚨 vs. RETAINED ✅) for customer success teams.

📊 Execution Outcome:
⚙️ Setup & Local Installation

1. clone repository

Bash
git clone [https://github.com/rakshitarora2310-lpu/python-book-scraper.git](https://github.com/rakshitarora2310-lpu/python-book-scraper.git)
cd python-book-scraper


2.Set Up Virtual Environment:

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

 
3.Install Master Dependencies:
PowerShell
pip install -r requirements.txt

4.Run Any Module:

PowerShell
python 01_catalog_scraper/main.py
streamlit run 02_sales_dashboard/app.py
python 03_price_tracker/tracker.py
python 04_churn_predictor/predictor.py