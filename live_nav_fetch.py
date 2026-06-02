import requests
import pandas as pd
import os

scheme_codes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw", exist_ok=True)

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)

    try:
        data = response.json()

        # ✅ important check
        if "data" in data and len(data["data"]) > 0:

            nav_df = pd.DataFrame(data["data"])

            file_name = f"data/raw/{fund_name}_NAV.csv"
            nav_df.to_csv(file_name, index=False)

            print(f"✅ Saved: {file_name}")

        else:
            print(f"❌ No NAV data found for {fund_name}")

    except Exception as e:
        print(f"❌ Error for {fund_name}: {e}")