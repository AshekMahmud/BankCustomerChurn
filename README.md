# BankCustomerChurn
Visit the live app here: [Bank Customer Churn Streamlit App](https://bankcustomerchurn-hgvmdjfmqywmitqpz7iywy.streamlit.app/)

---
This dataset contains account information for 10,000 customers from a European bank. It includes key details such as customers' credit scores, account balances, the number of products they use, and whether they have churned (left the bank). This dataset is an ideal resource for conducting churn analysis and building predictive models for customer retention.

#### Key Analysis Opportunities:
1. **Churn Attributes:** Identify attributes that are more common among churners compared to retained customers. Can we predict customer churn using these variables?
2. **Customer Demographics:** Analyze the overall demographics of the bank’s customers, including gender, age groups, and geographic distribution.
3. **Country-Specific Behavior:** Explore differences in account behavior between customers from Germany, France, and Spain.
4. **Customer Segmentation:** Discover segments within the bank’s customer base to understand different behavioral patterns and trends.

This dataset is valuable for building data-driven insights on customer retention strategies and predictive modeling for churn prediction.

---

### Data Analysis Process

I conducted a detailed analysis of the **Bank Customer Churn Dataset** to extract meaningful insights and answer key questions about customer churn patterns. The following steps were taken in the analysis process:

1. **Data Cleaning & Preparation:**
   - Removed any missing or irrelevant data.
   - Segmented customers based on various attributes such as age, credit score, balance, and churn status.
   - Standardized the dataset for ease of analysis.

2. **Exploratory Data Analysis (EDA):**
   - Conducted a thorough EDA to understand the overall distribution of the data and key variables like churn rate, balance distribution, and credit score segments.
   - Visualized trends using bar charts, histograms, and scatter plots for attributes like gender, age group, balance, and credit score.

3. **Demographic and Behavioral Analysis:**
   - Analyzed the customer demographics by country, gender, and age group.
   - Investigated customer behavior across German, French, and Spanish customers to detect any country-specific patterns in churn and retention rates.
   - Explored the relationship between credit score and churn rate to identify risk segments.

4. **Churn Prediction Insights:**
   - Evaluated which customer attributes (e.g., credit score, age, balance) were more common among churned customers.
   - Highlighted which segments were more likely to churn and the attributes that indicated high retention probability.

---

### Analysis Report

**Overall Views:**
- **Total Customer Count:** 10,000
  - **Male:** 46.70%
  - **Female:** 53.30%
- **Churned Customers:** 20.40%
- **Retained Customers:** 79.60%

**1. Key Attributes Among Churners:**
- **Age:** 66% of churned customers fall within the 45-64 age group, whereas younger customers (18-44) tend to have higher retention rates.
- **Credit Score:** Customers with lower credit scores are more likely to churn. Specifically:
  - **300-579 (High Risk):** 28.9% churn rate
  - **580-669 (Moderate Risk):** 32.4% churn rate
  - **670-739 (Low Risk):** 22.5% churn rate
  - Higher credit scores (740-850) show lower churn rates.
- **Balance:** Customers with balances under $100k have a lower churn rate, while those with balances over $200k exhibit a 100% churn rate.

**2. Demographics Analysis:**
- **Country-wise Customer Count:**
  - **France:** 48.2% of the total customers, with the lowest churn rate (15.98%).
  - **Germany and Spain:** Higher churn rates compared to France, with Spain showing a churn rate of 28.96%.
- **Gender-Based Retention:**
  - Males tend to have slightly higher retention rates, especially in younger age groups.
- **Age Group Patterns:**
  - In France, both males and females aged 18-34 have the highest retention rates, with near 100% retention for those aged 18-24.

**3. Country-Specific Differences:**
- **France:** Largest customer base with the lowest churn rates.
- **Germany and Spain:** Display higher churn rates, suggesting differences in customer behavior that may require targeted retention strategies.

**4. Customer Segmentation:**
- Identified customer segments based on age, credit score, and balance:
  - **High Risk:** Older customers (45-64) with lower credit scores.
  - **Low Risk:** Younger customers with higher credit scores and balances under $100k.
