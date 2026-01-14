import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1) Load data
FILE_PATH = "data/online_retail_II.xlsx"
df = pd.read_excel(FILE_PATH)

print("✅ Loaded dataset:", df.shape)
print(df.head())
print(df.columns)

# 2) Clean column names
df.columns = [c.strip().replace(" ", "_") for c in df.columns]

# Online Retail II common columns:
# Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID, Country
cust_col = "Customer_ID"
invoice_col = "Invoice"
date_col = "InvoiceDate"
qty_col = "Quantity"
price_col = "Price"

# Convert invoice to string
df[invoice_col] = df[invoice_col].astype(str)

# Drop missing customer id
df = df.dropna(subset=[cust_col])

# Remove cancelled invoices
df = df[~df[invoice_col].str.startswith("C")]

# Remove invalid qty/price
df = df[(df[qty_col] > 0) & (df[price_col] > 0)]

# Convert date
df[date_col] = pd.to_datetime(df[date_col])

print("✅ After cleaning:", df.shape)

# 3) Total Price
df["TotalPrice"] = df[qty_col] * df[price_col]

# 4) RFM Table
reference_date = df[date_col].max() + pd.Timedelta(days=1)

rfm = df.groupby(cust_col).agg({
    date_col: lambda x: (reference_date - x.max()).days,
    invoice_col: "nunique",
    "TotalPrice": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
print("✅ RFM created:", rfm.shape)

# 5) RFM Scoring
rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

rfm["R_Score"] = rfm["R_Score"].astype(int)
rfm["F_Score"] = rfm["F_Score"].astype(int)
rfm["M_Score"] = rfm["M_Score"].astype(int)

# 6) Segments
def segment_customer(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Champions"
    elif row["F_Score"] >= 4 and row["M_Score"] >= 3:
        return "Loyal Customers"
    elif row["R_Score"] >= 4 and row["F_Score"] >= 2:
        return "Potential Loyalists"
    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"
    elif row["R_Score"] <= 2 and row["F_Score"] <= 2:
        return "Lost"
    else:
        return "Need Attention"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)
print("\n✅ Segment counts:\n", rfm["Segment"].value_counts())

# 7) KMeans Clustering
X = rfm[["Recency", "Frequency", "Monetary"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(X_scaled)
print("\n✅ Cluster counts:\n", rfm["Cluster"].value_counts())

# 8) Export
OUTPUT_FILE = "output/segmented_customers.csv"
rfm.to_csv(OUTPUT_FILE, index=False)
print("\n✅ Exported:", OUTPUT_FILE)
