# Python Data Science & Automation Portfolio

A collection of practical Python projects covering web scraping, data visualization, price monitoring, and predictive modeling.

---

## Repository Structure

```text
python-book-scraper/
│
├── 01_catalog_scraper/        # Web Scraping Pipeline
├── 02_sales_dashboard/        # BI Analytics Dashboard
├── 03_price_tracker/          # Competitor Price Alert Engine
├── 04_churn_predictor/        # Customer Churn ML Predictor
├── screenshots/               # Project preview images
├── data/                      # Exported output files
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


Project Overview
1. Automated E-Commerce Catalog Scraper
Path: 01_catalog_scraper/

Tech Stack: Python, BeautifulSoup4, Requests, Pandas, OpenPyXL

Features:

Multi-page web scraper handling dynamic pagination.

Cleans raw price, currency, and stock strings using RegEx.

Implements rate-limiting and error handling to handle request limits safely.

Exports structured datasets directly to Excel (.xlsx).

Preview:

2. Sales & Revenue Analytics Dashboard
Path: 02_sales_dashboard/

Tech Stack: Python, Streamlit, Plotly, Pandas

Features:

Interactive web dashboard built with Streamlit.

Tracks high-level KPIs including revenue, units sold, and profit margins.

Plotly charts for sales distribution and category breakdowns.

Preview:

3. Competitor Price Tracker & Alert Engine
Path: 03_price_tracker/

Tech Stack: Python, Pandas, Datetime

Features:

Monitors live competitor pricing against baseline target prices.

Generates structured logs marking item statuses (NORMAL vs. ALERT BREACH).

Triggers notifications when prices drop below specified thresholds.

Preview:4. Customer Churn Machine Learning Predictor
Path: 04_churn_predictor/

Tech Stack: Python, Scikit-Learn, Pandas, NumPy

Features:

End-to-end ML workflow covering data preprocessing, feature encoding, and model evaluation.

Uses a Random Forest Classifier to predict churn based on tenure, spend, and support ticket history.

Achieves 96% accuracy on test data.

Outputs risk levels (HIGH RISK vs. RETAINED) with probability scores for customer success teams.

Preview:

Quickstart Guide


Clone the repository:

Bash
git clone [https://github.com/rakshitarora2310-lpu/python-book-scraper.git](https://github.com/rakshitarora2310-lpu/python-book-scraper.git)
cd python-book-scraper


Set up virtual environment:

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1


Install dependencies:

PowerShell
pip install -r requirements.txt


Run any project:

PowerShell
python 01_catalog_scraper/main.py
streamlit run 02_sales_dashboard/app.py
python 03_price_tracker/tracker.py
python 04_churn_predictor/predictor.py