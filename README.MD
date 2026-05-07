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
├── 01_data_exploration.sql     # SQL queries for initial data exploration
├── 02_user_segmentation.py     # Python script for user segmentation analysis
├── 03_insights_report.md       # Comprehensive analysis report with findings
└── README.MD                   # This file
```

### File Descriptions

- **`01_data_exploration.sql`**: Contains SQL queries for:
  - Dataset overview and summary statistics
  - User demographics and betting activity
  - Game performance metrics
  - Revenue analysis by user segments

- **`02_user_segmentation.py`**: Python script that:
  - Loads and processes the gaming data
  - Implements user segmentation logic
  - Generates visualizations and statistical summaries
  - Exports results for reporting

- **`03_insights_report.md`**: Detailed analysis report including:
  - Executive summary with key findings
  - User segmentation breakdown
  - Game performance analysis
  - Business recommendations

## 🛠️ Technologies Used

- **SQL**: Data exploration and aggregation queries
- **Python**: Data processing and analysis
  - pandas: Data manipulation
  - matplotlib/seaborn: Data visualization
  - numpy: Numerical computations
- **Markdown**: Report generation and documentation

## 🚀 How to Run the Analysis

### Prerequisites

- Python 3.8+
- SQLite or compatible database with gaming data
- Required Python packages: `pandas`, `matplotlib`, `seaborn`, `numpy`

### Setup

1. **Clone the repository** (if applicable)
2. **Navigate to the project directory**:
   ```bash
   cd portfolio-project
   ```

3. **Install dependencies** (if using virtual environment):
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

### Execution Steps

1. **Data Exploration** (SQL):
   - Run the queries in `01_data_exploration.sql` against your gaming database
   - Review the results to understand the dataset structure

2. **User Segmentation** (Python):
   ```bash
   python 02_user_segmentation.py
   ```
   - This will process the data and generate segmentation results
   - Check the output for user categories and statistics

3. **Review Insights**:
   - Open `03_insights_report.md` to review the complete analysis
   - Examine the findings and business recommendations

## 📈 Key Findings

### User Segmentation Results
- **High-Value Users** (25% of users): Generate 45.8% of total revenue
- **Medium-Value Users** (50% of users): Generate 49.7% of total revenue
- **Low-Value Users** (25% of users): Generate only 4.5% of total revenue

### Game Performance
- **Roulette**: Revenue leader with highest average bets ($115) and win rate (66.7%)
- **Poker**: Strong engagement but lower accessibility
- **Slots**: High volume but lower monetization potential

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