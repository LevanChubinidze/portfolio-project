# Gaming User Behavior Analysis - Portfolio Project

## 📊 Project Overview

This portfolio project demonstrates comprehensive data analysis skills through the examination of user behavior on a gaming platform. The analysis focuses on user segmentation, game performance metrics, and actionable business insights to drive revenue growth and user engagement.

## 🎯 Objectives

- **User Segmentation**: Identify and categorize users based on betting behavior and value
- **Revenue Analysis**: Understand revenue distribution across user segments and game types
- **Behavioral Insights**: Analyze user patterns to inform marketing and product strategies
- **Data Pipeline**: Demonstrate end-to-end data analysis workflow from SQL exploration to Python analysis

## 📁 Project Structure

```
portfolio-project/
├── 01_data_exploration.sql     # SQL queries for initial dataset exploration
├── 02_user_segmentation.py     # Python script for user segmentation analysis
├── 03_insights_report.md       # Narrative report with findings and recommendations
├── gaming.db                   # SQLite database containing users, bets, and sessions data
└── README.md                   # This file
```

### File Descriptions

- **`01_data_exploration.sql`**: Contains SQL queries for:
  - Dataset overview and summary statistics
  - User demographics and betting activity
  - Game performance metrics
  - Revenue analysis by user segments

- **`02_user_segmentation.py`**: Python script that:
  - Loads and processes the gaming dataset
  - Implements user segmentation logic
  - Generates visual summaries and statistical outputs
  - Supports downstream reporting

- **`03_insights_report.md`**: Narrative report with:
  - Executive summary and key observations
  - User segmentation insights
  - Game performance analysis
  - Business recommendations

- **`gaming.db`**: SQLite database included in the repository. It contains the core analysis tables:
  - `users`: user identifiers, signup details, country, and segment attributes
  - `bets`: bet records with user linkage, game type, amount, result, and timestamp
  - `sessions`: session records with user linkage, start/end times, duration, and device context
  - These tables support both the SQL exploration and Python segmentation workflows

## 🛠️ Technologies Used

- **SQL**: Data exploration and aggregation queries
- **Python**: Data processing and analysis
  - pandas: Data manipulation
  - matplotlib/seaborn: Data visualization
  - numpy: Numerical computations
- **Markdown**: Report generation and documentation

## 🚀 How to Run the Analysis

### Prerequisites

- Python 3.8 or later
- Required Python packages: `pandas`, `matplotlib`, `seaborn`, `numpy`
- `gaming.db` is included in the repository root and contains the dataset used by the analysis scripts

### Setup

1. **Navigate to the project directory**:
```bash
   cd portfolio-project
```

2. **Create a virtual environment** (if you don't have one):
```bash
   python -m venv .venv
   .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
   pip install pandas numpy scipy
```

### Execution Steps

1. **Inspect the database**:
   - `gaming.db` is included in the repository root and contains the dataset used for this analysis.
   - Use SQLite tooling or a database viewer to review table structure and sample records.

2. **Run the Python analysis**:
   ```bash
   python 02_user_segmentation.py
   ```
   - This script reads `gaming.db`, processes the data, and produces segmentation output.

3. **Review the report**:
   - Open `03_insights_report.md` to see the full analysis findings and recommendations.

## 📈 Summary of Insights

### User Segmentation
- The analysis categorizes users into distinct value segments to support targeted engagement.
- It highlights differences in activity patterns and revenue potential across user groups.

### Game Performance
- The project identifies games with the strongest engagement and revenue characteristics.
- It supports recommendations for product focus and marketing priorities.

## 💡 Skills Demonstrated

- **SQL Querying**: Complex joins, aggregations, and analytical functions
- **Data Analysis**: Statistical analysis and user segmentation techniques
- **Python Programming**: Data manipulation, analysis, and visualization
- **Business Intelligence**: Translating data insights into actionable recommendations
- **Technical Communication**: Clear documentation and reporting of findings

## 📊 Business Impact

This analysis provides actionable insights for:
- **Targeted Marketing**: Focus efforts on medium-value users for maximum ROI
- **Product Strategy**: Promote high-performing games like Roulette
- **User Engagement**: Develop strategies to convert low-value users
- **Revenue Optimization**: Identify key revenue drivers and growth opportunities

## 🔄 Future Enhancements

- Implement real-time user segmentation
- Add predictive modeling for user value
- Integrate with marketing automation tools
- Expand analysis to include time-series trends
- Add A/B testing framework for recommendations

---

*This project showcases practical data analysis skills applied to a real-world gaming industry scenario, demonstrating the ability to extract valuable business insights from user data.*

---

## 📄 Full Analysis

For complete findings and recommendations:
- See **`03_insights_report.md`**