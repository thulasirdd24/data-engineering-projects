import pandas as pd

def extract():
    # Simulated raw data
    data = {
        "item_id": [1, 2, 3],
        "inventory": [100, 50, 0],
        "supplier": ["A", "B", "C"]
    }
    df = pd.DataFrame(data)
    print("Data Extracted")
    return df

def transform(df):
    df["status"] = df["inventory"].apply(lambda x: "Low" if x < 50 else "OK")
    print("Data Transformed")
    return df

def load(df):
    df.to_csv("processed_supply_chain.csv", index=False)
    print("Data Loaded to CSV")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
