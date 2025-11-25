# Predicting Price Moves with News Sentiment — Week 1 Challenge

Analyze the relationship between financial news sentiment and stock price movements to provide actionable insights for Nova Financial Solutions.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [Dataset Overview](#dataset-overview)
- [Folder Structure](#folder-structure)
- [Setup & Installation](#setup--installation)
- [Tasks Completed](#tasks-completed)
- [Technologies Used](#technologies-used)
- [Key Insights](#key-insights)

---

## Project Overview

This project covers end-to-end analysis of financial news and stock prices:

- Exploratory Data Analysis (EDA) of news headlines, publishers, and publishing times
- Sentiment analysis of news headlines
- Technical indicators computation using TA-Lib and PyNance
- Correlation analysis between sentiment scores and stock price movements
- Development workflow using Git branches and CI/CD

---

## Business Objective

Nova Financial Solutions aims to strengthen predictive analytics by combining qualitative news sentiment with quantitative stock metrics.

The project focuses on:

- Measuring sentiment in financial news
- Linking sentiment to stock returns
- Highlighting actionable signals for investment strategies

---

## Dataset Overview

**Financial News and Stock Price Integration Dataset (FNSPID)**:

| Column    | Description                     |
| --------- | ------------------------------- |
| headline  | News article title              |
| url       | Link to full article            |
| publisher | Publisher name or domain        |
| date      | Publication date & time (UTC-4) |
| stock     | Stock ticker symbol             |

**Stock Price Dataset**:

- Open, High, Low, Close (OHLC)
- Volume
- Daily returns

---


## Setup & Installation

### Clone the repository:

```bash
git clone https://github.com/<username>/fintech-sentiment-analysis.git
cd fintech-sentiment-analysis

Create a Python virtual environment and activate it:
```

```bash
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Linux/Mac)
source venv/bin/activate
```

### Upgrade pip and install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Launch Jupyter notebooks:

```bash
jupyter notebook
```

## Tasks Completed

### Task 1: Git & Environment Setup

- Repository initialized with branches and CI workflow
- Python virtual environment created
- Exploratory Data Analysis (EDA) of news headlines, publishers, and publishing times
---
Based on the data above the following conclusions were reached:
- Keywords such as stocks, week, shares and trading are the most frequently words mentioned in the news headlines with over 6000 mentions across different publishers.
- Starting from 2020 onwards, more articles were published daily.
- Top 5 publishers inlcuded Benzinga Newsdek, Lisa Levin,, ETF Professor, Paul Quintaro, and Benzinga Insights.


### Task 2: Technical Indicators & Market Analysis

- Stock price data cleaned and prepared
- Technical indicators computed (SMA, EMA, RSI, MACD)
- Visualizations for trends and volume

### Task 3: Sentiment vs Stock Movement Correlation

- Sentiment scores generated from news headlines
- Daily stock returns calculated
- Pearson correlation analysis between sentiment and returns
- Visualizations for patterns and regression

---

## Technologies Used

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- TA-Lib, PyNance
- NLTK, TextBlob
- Jupyter Notebook
- Git & GitHub Actions

---

## Key Insights

- Negative news sentiment often precedes short-term price drops
- Certain publishers have strong positive or negative bias
- Sentiment combined with technical indicators improves predictive power
- Publishing spikes align with major financial events