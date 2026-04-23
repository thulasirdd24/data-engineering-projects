import pandas as pd

def extract():
    data = {
        "revenue": [1000, 2000, 3000],
        "cost": [400, 800, 1200]
    }
    return pd.DataFrame(data)

def transform(df):
    df["profit"] = df["revenue"] - df["cost"]
    df["margin"] = df["profit"] / df["revenue"]
    print("Calculated KPIs")
    return df

def load(df):
    df.to_csv("kpi_output.csv", index=False)
    print("Saved KPI data")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
