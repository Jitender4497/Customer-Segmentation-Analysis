# Customer Segmentation Analysis (RFM + K-Means Clustering)

## 📌 Project Overview
This project performs **Customer Segmentation Analysis** using transactional retail data.  
Customers are segmented based on their purchasing behavior using:

✅ **RFM Analysis** (Recency, Frequency, Monetary)  
✅ **K-Means Clustering** (Machine Learning based segmentation)

An interactive **Tableau Dashboard** is created to visualize customer segments, revenue contribution, recency trends, and cluster distributions.

---

## 🎯 Objective
To group customers into meaningful categories such as:
- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

This helps businesses to:
- Run targeted marketing campaigns
- Improve customer retention
- Increase revenue using data-driven strategies

---

## 🗂 Dataset
Dataset used: **Online Retail II dataset (.xlsx)**  
Contains transaction-level data such as:
- Invoice number and date
- Customer ID
- Quantity and price
- Total transaction value

---

## ⚙️ Tools & Technologies Used
- **Python**
  - Pandas, NumPy
  - Scikit-learn (KMeans)
- **Tableau**
  - Interactive Dashboard for visualization

---

## 🧹 Data Cleaning Steps
✔ Removed missing Customer IDs  
✔ Removed cancelled invoices (`Invoice` starting with "C")  
✔ Removed negative quantity and price entries  
✔ Created `TotalPrice = Quantity * Price`

---

## 📊 Feature Engineering
### RFM Metrics
- **Recency:** Days since last purchase
- **Frequency:** Number of unique invoices/orders
- **Monetary:** Total spending

### RFM Scoring (1–5)
Customers are scored using quintiles:
- Higher score = better customer value

---

## 🤖 Machine Learning (K-Means)
Applied **K-Means clustering** on scaled RFM metrics:
- Recency
- Frequency
- Monetary

Clusters represent different customer purchasing behaviors.

---

## 📈 Tableau Dashboard
Dashboard includes:
✅ KPI Tiles (Total Revenue, Avg Revenue / Customer, Total Customers)  
✅ Segment Count  
✅ Revenue Contribution by Segment  
✅ Monetary vs Frequency Scatterplot  
✅ Avg Recency by Segment  
✅ Cluster Distribution  

Interactive feature:
- Clicking a segment filters the whole dashboard.

---

## 📌 Key Insights
- **Champions generate the highest revenue** → premium/loyalty offers recommended.
- **Lost segment contains high customer count** → reactivation campaigns needed.
- Majority customers belong to **Cluster 0**, indicating low/medium spenders → upsell opportunities exist.
- **Champions have low Recency**, showing high engagement and repeat buying behavior.

---

## 📂 Project Structure
