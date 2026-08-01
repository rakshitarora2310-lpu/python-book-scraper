# 📚 Automated E-Commerce Catalog Scraper

> A production-ready Python scraping pipeline designed to extract, clean, and export structured product catalog data into formatted Excel spreadsheets.

---

## 💡 Overview

This project automates data collection from pagination-enabled e-commerce catalogs. Built with resilience in mind, it handles session management, rate limiting, dynamic character cleaning (such as non-standard currency encoding), and converts unstructured HTML into clean tabular data.

## ✨ Key Features

* **Automated Pagination:** Dynamically detects and traverses multi-page product listings.
* **Robust Data Sanitization:** Uses regular expressions (`re`) to clean currency symbols, extract numeric pricing, map star ratings, and normalize stock availability.
* **Polite Scraping:** Implements rate-limiting delays and custom `User-Agent` headers to ensure respectful server interactions.
* **Structured Data Export:** Outputs clean datasets directly into Excel (`.xlsx`) format using `pandas` and `openpyxl`.
* **Logging & Error Resilience:** Employs explicit logging levels (`INFO`, `WARNING`, `ERROR`) to track pipeline progress and catch network exceptions gracefully.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Web Scraping:** `BeautifulSoup4`, `requests`
* **Data Processing & Export:** `pandas`, `openpyxl`
* **Text Parsing:** `re` (Regular Expressions)

---

## 🚀 Getting Started

### 1. Installation & Setup

Clone the repository:
```bash
git clone https://github.com/rakshitarora2310-lpu/python-book-scraper.git
cd python-book-scraper