# Quantitative Portfolio Analysis

Quantitative analysis of a diversified investment portfolio over a one-year period. This project evaluates performance metrics including risk-adjusted returns, maximum drawdown, and volatility analysis. Portfolio performance is benchmarked against the MSCI ACWI index.

### Portfolio Composition

| Asset Class | Allocation | Geographic Focus |
|------------|-----------|------------------|
| Equity | ~75% | Global Developed |
| Fixed Income | ~5% | US-Focused |
| Alternatives | ~20% | Emerging Markets |

### Project Structure

```
├── data
│   ├── processed
│   │   ├── nav_clean.csv
│   │   ├── open_positions_clean.csv
│   │   └── trades_clean.csv
│   └── raw
│       └── ibkr_data.csv
├── figures
├── notebooks
│   ├── data_cleaning.ipynb
│   └── exploratory_data_analysis.ipynb
├── pyproject.toml
├── README.md
├── src
└── uv.lock
```

### Privacy Notice

The actual portfolio data is not included in this repository for privacy reasons.
