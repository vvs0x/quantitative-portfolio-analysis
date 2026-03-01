# Quantitative Portfolio Analysis

Quantitative analysis of a diversified investment portfolio over a one-year period. This project evaluates performance metrics including risk-adjusted returns, maximum drawdown, and volatility analysis. Portfolio performance is benchmarked against the MSCI ACWI index. The investment approach follows a long-term buy-and-hold strategy with portfolio rebalancing triggered by the 5/25 rule.

### Portfolio Composition

| Asset Class | Allocation |
|------------|-----------|
| Equity | ~75% |
| Fixed Income | ~5% |
| Alternatives | ~20% | 

### Project Structure

```
├── data
│   ├── processed
│   │   ├── nav_clean.csv
│   │   ├── open_positions_clean.csv
│   │   └── trades_clean.csv
│   └── raw
│       ├── data1.csv
│       ├── data2.csv
│       ├── data3.csv
│       └── info.txt
├── figures
│   └── performance.png
├── notebooks
│   ├── data_cleaning.ipynb
│   └── exploratory_data_analysis.ipynb
├── pyproject.toml
├── README.md
├── src
│   └── data_loader.py
└── uv.lock
```

### Privacy Notice

The actual portfolio data is not included in this repository for privacy reasons.
