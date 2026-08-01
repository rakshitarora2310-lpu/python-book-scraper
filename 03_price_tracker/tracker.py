import random
import pandas as pd
from datetime import datetime

# Simulated Target Competitor Catalog
TARGET_PRODUCTS = [
    {"id": 101, "name": "Wireless Noise-Canceling Headphones", "target_price": 150.00},
    {"id": 102, "name": "Ergonomic Mechanical Keyboard", "target_price": 90.00},
    {"id": 103, "name": "Ultra-Wide Gaming Monitor", "target_price": 320.00},
]

def fetch_live_competitor_price(product_id):
    """Simulates fetching live price data from a competitor site or API."""
    base_prices = {101: 160.00, 102: 95.00, 103: 350.00}
    # Simulate market price fluctuation (-15% to +5%)
    fluctuation = random.uniform(-0.15, 0.05)
    current_price = round(base_prices[product_id] * (1 + fluctuation), 2)
    return current_price

def run_price_tracker():
    print("🔍 Running Competitor Price Monitoring Pipeline...\n")
    alerts = []
    log_entries = []
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in TARGET_PRODUCTS:
        current_price = fetch_live_competitor_price(item["id"])
        price_diff = round(current_price - item["target_price"], 2)
        
        status = "NORMAL"
        if current_price <= item["target_price"]:
            status = "🚨 ALERT: PRICE DROP"
            alerts.append(f"ALERT: '{item['name']}' dropped to ${current_price} (Target: ${item['target_price']})")
        
        log_entries.append({
            "Timestamp": timestamp,
            "Product": item["name"],
            "Target Price ($)": item["target_price"],
            "Current Price ($)": current_price,
            "Variance ($)": price_diff,
            "Status": status
        })
    
    # Save monitoring log to DataFrame
    df_log = pd.DataFrame(log_entries)
    print(df_log.to_string(index=False))
    
    print("\n--- Triggered Notifications ---")
    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No target thresholds breached during this check.")

if __name__ == "__main__":
    run_price_tracker()