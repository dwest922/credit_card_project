# Credit Card Churn Project
A Group Project – Hackathon Data Challenge
This work was completed collaboratively by a multidisciplinary team, using Trello for planning and GitHub for shared repository management.
# Project Overview
This group project aims to analyse credit card customer data to understand churn behaviour and predict churn likelihood. The process includes ETL data preparation, exploratory analytics, predictive modelling, dashboard development and prototype functionality for churn scoring and retention support.
# The Dataset
The dataset for the project was sourced at Kaggle.  The dataset was kindly provided by Sakshi Goyal and can be accessed at the following link [Credit Card Customers](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

# Project Structure
## Project Planning
- Reviewed dataset variables, business problem and technical constraints
- Discussed compatible platforms (Power BI / Tableau / Streamlit / Python / Python Notebooks)
- Created GitHub repository for version control and online collaboration on the project
- Generated README skeleton and documentation guidelines
- Decided to use [Trello](https://trello.com/b/BSaLMmC0/hackathon-credit-card-churn) for project planning and management - picked the Kanban workflow
- Assigned team responsibilities and deliverables
## Data Cleaning/ETL Pipeline
Steps executed:
- 
## Exploratory Data Analysis (EDA)
Analysis components:
- 
## Modeling & Predictive Prototype

## Dashboard Development
A number of dashboards were developed by team members based on assigned resposibilities and individual preferred dashboard development platform.  Dashboards were developed using Power BI (Duncan) and Streamlit (Mohammed).  Mohammed has included his dashboard in the apps folder.
## Documentation
The project was properly documment with a comprehensive README.md file and supporting documents located in a number of folders.  Also included was the presentation powerpoint file.
# Team Roles and Responsibility Journal
Spending Patterns & Transaction Behaviour _Valeriia

During the analysis, we explored how customer behaviour metrics relate to churn risk. We visualised changes in spending, transaction counts, and utilisation patterns, comparing attrited versus existing customers across multiple distributions and scatter plots. This allowed us to identify clear behavioural differences and highlight which indicators are most predictive of attrition.

Customers who show a decline in total spending are significantly more likely to churn. Attrited customers cluster around lower spending change ratios (0.4–0.7), while retained clients show stable or increasing spend (0.7–1.1). Decreasing spend is a strong early predictor of attrition

Customers exhibiting a strong decline in transaction count are over-represented among attrited clients. Existing customers cluster around healthy transaction change levels. The distribution shows a clear behavioural separation:  lower transaction engagement strongly correlates with churn

Attrited customers form a dense cluster in the low-usage zone. Existing customers show a strong positive correlation between amount and count,  behavioural engagement predicts attrition.
The distribution of credit card utilization among attrited and existing customers is nearly identical. Сredit line usage is not a distinguishing factor between customers who churn and those who stay.

## Early Warning Indicators - Duncan
The aim is to identify customers likely to churn, analyse behavioural and financial early-warning indicators, and present the findings in an interactive Power BI dashboard that supports proactive customer retention.

### Dashboard Objective

* Identify customers likely to churn
* Detect early warning indicators of attrition
* Estimate short-term and medium-term churn risk
* Provide an interactive decision-support dashboard

---
* Created banded variables for interpretability:

  * Utilization_Band (from Avg_Utilization_Ratio)
  * Open_To_Buy_Band
  * Growth_Band (from Total_Ct_Chng_Q4_Q1)
* Encoded categorical fields
* Integrated Naive Bayes churn prediction outputs

### Key Columns Used

**Churn Indicator**

* Attrition_Flag

**Behavioural and Financial Variables**

* Avg_Utilization_Ratio
* Avg_Open_To_Buy
* Total_Ct_Chng_Q4_Q1
* Months_Inactive_12_mon
* Contacts_Count_12_mon

**Predictive Model Outputs**

* Naive_Bayes_Classifier_...Months_Inactive_12_mon_1
* Naive_Bayes_Classifier_...Months_Inactive_12_mon_2

---

### Measures Used (DAX)

The following measures were created in Power BI to support analysis and interaction:

**Churn & Population Metrics**

* Total Customers
* Attrited Customers
* Attrition Rate

**Behavioural Analysis Measures**

* Average Utilization
* Average Open To Buy
* Average Transaction Change
* Average Months Inactive

**Predictive Measures**

* Predicted Churn (Month 1)
* Predicted Churn (Month 2)

### Dashboard Visuals

* Attrition Rate by Utilization Band
* Attrition Rate by Open To Buy Band
* Attrition Rate by Growth Band
* Attrition Rate by Months Inactive
* Predicted Churn KPIs (Month 1 and Month 2)
* Key Influencers visual
* Interactive slicers for demographics and behavioural segments

---

### Key Findings

**Utilisation**

* Attrition increases noticeably in high utilisation segments (> ~0.8)
* Extreme utilisation (> ~0.98) shows the highest churn risk

**Open To Buy**

* Customers with Open_To_Buy in the 1k–2k range show attrition rates of ~20–21%

**Transaction Growth**

* Total_Ct_Chng_Q4_Q1 < 0.6 corresponds to ~36% attrition
* Stable or positive growth (≥ 1.0) shows attrition of ~4–8%

**Inactivity**

* Attrition increases after 3–4 inactive months
* Predicted churn rises from ~16% (Month 1) to ~84% (Month 2) under continued inactivity

---

### Segmentation & Decision Support

**High-Risk Customers**

* High utilisation
* Declining transaction growth
* Three or more months inactive
* High predicted churn probability

**Low-Risk Customers**

* Strong growth
* Low utilisation
* Active behaviour

---

### Dashboard Purpose

The dashboard functions as an early-warning and risk-scoring tool, enabling users to:

* Explore churn drivers interactively
* Identify high-risk customers
* Design proactive customer retention strategies

---
# Tech Stack
# Acknowledgements
