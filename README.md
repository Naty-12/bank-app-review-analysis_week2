# 📱 Bank App Review Analysis
A project for collecting and preprocessing Google Play Store reviews for bank apps as part of a sentiment analysis pipeline.

## 🚀 Project Objectives
- Scrape and preprocess user reviews from the Google Play Store to prepare text data for analysis.
- Apply NLP techniques to analyze review sentiment and identify key customer feedback themes.
- Design and implement a relational database schema in Oracle to store and manage review data.
- Derive actionable insights from analyzed data and create compelling visualizations for business stakeholders.
- Develop and present a data-driven report with recommendations for app improvement in a fintech context.
- Employ Git for version control and write unit tests to ensure the reliability of data processing scripts.
### 📁 Project Structure
```
Bank-app-review-analysis/
│
├── data/
│   └── bank_reviews.csv        # Clean dataset output
├── src/
│   └── scraper.py              # Review scraping and preprocessing script
│
├── .gitignore
├── requirements.txt
└── README.md
```
### Methods used 
- Sentiment analysis using Textblob, Vader and machine learning aproach
- Key word extraction using TF_IDF
- Clustering/grouping using Kmeans 
## Credit Scoring Business Understanding
### 1. Basel II Accord and the need for interpretable, well-documented models
The Basel II Capital Accord requires banks to establish rigorous internal systems for measuring credit risk to determine capital requirements. According to Basel II, "banks are encouraged to develop and use internal risk rating systems" and must provide regulators with transparent documentation on how risks are assessed ([Statistica, p.538](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf)). 

This regulatory context makes it critical to build **interpretable and well-documented models**. Using approaches like Logistic Regression with Weight of Evidence (WoE) allows institutions to justify risk estimates, satisfy audit requirements, and avoid regulatory capital add-ons. As highlighted by the World Bank: "models must be transparent and understandable by management" ([World Bank Guidelines, p.10](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)).

### 2. Importance and risks of creating a proxy default variable
Because we lack a direct "default" label in the data, we must engineer a **proxy variable**, for example by using overdue payments or segmentation from transaction behaviors. This is necessary to train a supervised learning model that can approximate credit risk.

However, this introduces business risks. The World Bank warns that "poorly designed proxy variables can lead to models that are statistically strong but economically meaningless" ([World Bank Guidelines, p.12](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)). This may result in rejecting good customers (lost revenue) or accepting risky ones (increased defaults), ultimately affecting profitability and capital adequacy.

### 3. Trade-offs: simple vs. complex models
There is a fundamental trade-off between **interpretability and predictive power**:

- **Simple, interpretable models** (like Logistic Regression with WoE) provide clarity on how each factor affects risk. They are easier to monitor and justify to regulators, aligning with Basel II principles requiring that "risk assessment methodologies must be documented and validated" ([Risk Officer](https://www.risk-officer.com/Credit_Risk.htm)).

- **Complex, high-performance models** (like Gradient Boosting) often achieve superior predictive accuracy, reducing expected credit losses. However, they can be opaque and harder to validate or explain, raising concerns in regulated environments. The HKMA notes that advanced techniques "must be transparent and subject to independent validation" to avoid systemic risks ([HKMA Paper, p.4](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)).

In practice, banks often combine approaches: using complex models for internal monitoring while relying on simpler models for final credit decisions and compliance reporting.

---

📚 **Key References:**
- [Basel II and Credit Risk Modelling (Statistica)](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf)
- [World Bank Credit Scoring Guidelines](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)
- [HKMA on Alternative Credit Scoring](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)
- [Risk Officer Credit Risk Notes](https://www.risk-officer.com/Credit_Risk.htm)
