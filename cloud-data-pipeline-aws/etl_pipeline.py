import pandas as pd

def extract():
    data = {"sales": [100, 200, 300]}
    df = pd.DataFrame(data)
    print("Extracted data from source")
    return df

def transform(df):
    df["tax"] = df["sales"] * 0.1
    print("Transformed data")
    return df

def load(df):
    df.to_csv("aws_pipeline_output.csv", index=False)
    print("Loaded data to simulated S3")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
