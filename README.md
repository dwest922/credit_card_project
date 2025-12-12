# Credit Card Churn Project

A Group Project – Hackathon Data Challenge
This work was completed collaboratively by a multidisciplinary team, using Trello for planning and GitHub for shared repository management.

# Project Overview

This group project aims to analyse credit card customer data to understand churn behaviour and predict churn likelihood. The process includes ETL data preparation, exploratory analytics, predictive modelling, dashboard development and prototype functionality for churn scoring and retention support.

# The Dataset

The dataset for the project was sourced at Kaggle.  The dataset was kindly provided by Sakshi Goyal and can be accessed at the following link: [Credit Card Customers](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

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

A number of dashboards were developed by team members based on assigned resposibilities and individual preferred dashboard development platform.  Dashboards were developed using Power BI (Duncan, Helen) and Streamlit (Mohammed).  Mohammed has included his dashboard in the apps folder.

## Documentation

The project was properly documment with a comprehensive README.md file and supporting documents located in a number of folders.  Also included was the presentation powerpoint file.

# Team Roles and Responsibility Journal

## Attrition and Customer Characteristics - Mohammed

The goal was to determine how attrition or churn risk relate to customer characteristics.  To achieve this goal, we asked a number of questions:

- How does demographic category relate to attrition risk?
- Does age or number of dependent influence attrition risk?
- What role does the customers' months on the book play on attrition risk?

To answer these questions a number of visualizations were created using Python, Pandas and related libraries.  A cohort analysis was also conducted on the customers' months on the book to assess the attrition risk.  As cohort analysis uses time scale to analyse risks of attrition or retension, the months on book was converted into time by using bins or buckets.  Buckets of 1, 3, 6 or 12 months could be used depending on how grainer you want the analysis to be.  A bucket of 6 months was used in this analysis and was used to create a heatmap of months on the book against time.

A number of visualizations were created.  These include bar charts, histograms, boxplots, stacked bars and heatmaps.  The results of the visualizations can be found in the Jupyter Notebook, Streamlit Dashboard app and Power Point presentation of the Hackathon team project.

### The key findings of the data analysis are:

- Gender, graduate, high school, married, single, low income and blue card holders are the major drivers of churn.
- While gender and marital status show high attrition rates, there is not much difference between male and female or between married and single.  This implies other factors play more important roles in influencing the churn rates than gender or marital status.
- Graduate and High School leavers show the highest levels of churn rates within the education level sub-group.
- Low income earners and blue card holders show high attrition risks.
- Attrition rates are high among customers in the 38 to 52 years old range.  But the bulk of the customers, both existing and attrited, fall within the 40 and 52 years age range. This suggests age may not be a major driver of churn.  Other factors play more important roles.
- Families with 1 to 4 dependents show high attrition risks, with families with 2 or 3 dependents being the highest.
- Attrition rate is highest for customers with 36 months on book.  A cohort analysis of customers’ months on book versus attrition rate shows a fairly stable attrition rates from 15 to 52 months on book.  A cohort retention heatmap created by turning months on book into time using buckets of 6 months shows the retention rate highest at 12 months on book and attrition rate highest at 36 months on book.

### Recomendations

- A better understanding of the sub-demographic groups identified as high churn risk is needed to develop an effective strategy to reduce the churn rate.
- Further research is required to understand their particular needs and a strategy developed to address them in order to reduce their risks of attrition.
- Further study is suggested to understand why 36 months on book has the highest risk so that intervention can be triggered before customers reach their 36 months on book.
- A predictive model should be developed to indentify which demographic group and months on book have high attrition risks in the future.  This will enable to development of an effective strategy to mitigate the risks before they occur.

## Spending Patterns & Transaction Behaviour _Valeriia

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

## Helen Bliss – Relationship Depth & Engagement Analysis**

### **Focus Area**
Analysed customer **relationship depth** and **engagement behaviour** to understand key drivers of churn and identify at-risk segments within the existing customer base.

### **Power BI Dashboard**
[View the interactive dashboard](https://app.powerbi.com/links/K7R6jWh5PG?ctid=c233c072-135b-431d-af59-35e05babf941&pbi_source=linkShare)

---

## **Key Contributions**

### **1. Behavioural Feature Engineering**
Created new analytical fields to model customer engagement and stability:

- **Customer Lifestage** (New, Growing, Settled)  
- **Engagement Depth** (Low / Medium / High)  
- **Utilisation Tier** (No / Low / Moderate / High)  
- **Disengagement Indicator**  
- **Composite Risk Score**  
- **Z-Score Standardised Risk Measure**

These features enabled richer segmentation and more interpretable churn insights.
---

### **2. Power BI Data Modelling**
- Built dimensional lookup tables for engagement, utilisation, and lifecycle stage  
- Applied controlled sort orders for clear visual interpretation   
- Ensured stable one-to-many relationships for clean filtering and interactions  
---

### **3. Visual Analytics Development**
Delivered several core visuals for the dashboard:

- **Product Depth vs Retention**  
- **Contact Behaviour vs Inactivity**  
- **Inactivity Threshold Detection**  
- **Relationship Tier with Disengagement Trend**  
- **Engagement Depth vs Churn**  
- **Utilisation Tier vs Churn**  
- **Standardised Composite Risk Heatmap**

Added interactive slicers, tooltip pages, and multi-layer filtering to support deeper exploration.

—

### **4. Key Insights**
- Retention improves sharply once customers hold **3+ products**  
- Contact tends to be **reactive**, occurring after disengagement begins  
- Churn escalates after **3 months of inactivity**  
- Low engagement is the most consistent structural predictor of churn  
- The Z-score heatmap reveals two high-risk “tails”:  
  - **Low depth + high utilisation**  
  - **Low depth + no utilisation**
—

## **5. Conclusions**

Customer churn is driven by **relationship depth and behavioural disengagement** rather than contact frequency alone. Retention improves sharply once customers hold **three or more products**, while churn risk accelerates after **three months of inactivity**, particularly when combined with utilisation extremes or reactive contact. Behavioural composite risk measures effectively identify **at-risk existing customers**, enabling **proactive, prevention-led retention strategies**.
—

### **6. Recommended Actions**
- Promote early relationship deepening (encourage movement from 1–2 to 3+ products)  
- Trigger engagement interventions at **2 months inactive**  
- Shift from reactive to proactive contact strategies  
- Prioritise outreach to **low-engagement, high- or zero-utilisation** segments  

—

## **7. Future Development**

- **Predictive Modelling:**  
  Extend the project by exporting the cleaned dataset and building a churn prediction model using a train/test split in Python (Logistic Regression, Random Forest, Gradient Boosting). The resulting churn probability could be fed back into Power BI as a new risk metric.

- **Next Best Product:**  
  Use the strong link between product depth and retention to build a recommendation model for moving customers from 1–2 products toward 3+ products.

- **Behaviour Monitoring:**  
  Track changes in inactivity, utilisation, and spending momentum to detect early behaviour drift.

- **Operationalisation:**  
  Integrate model outputs into CRM systems to trigger proactive retention actions for high-risk customers.


## **Summary**
This work provided the team with a behavioural and relationship-driven view of churn, enabling early detection of at-risk customers and strengthening the strategic recommendations in our final Power BI dashboard.

## ** END OF HELEN'S SECTION**



# Tech Stack
# Acknowledgements

The team thanks Kaggle and [Sakshi Goyal](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers) for providing the dataset that was used for this Hackathon and John Anih of Code Institute for setting and judging the Hackathon team project.
