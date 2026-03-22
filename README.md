# Quantitative Portfolio Analysis

Quantitative analysis of a diversified investment portfolio over a two-year period, benchmarked against the FTSE Global All Cap Index. Evaluated key performance metrics including total return, maximum drawdown, and Sharpe ratio. The portfolio follows a long-term buy-and-hold strategy with rebalancing triggered by the 5/25 rule.

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
│   └── raw
├── figures
│   ├── cumr_and_drawdown.png
│   └── metrics.tex
├── notebooks
│   └── portfolio_analysis.ipynb
├── pyproject.toml
├── README.md
├── src
│   ├── __pycache__
│   │   └── portfolio_weights.cpython-312.pyc
│   └── portfolio_weights.py
└── uv.lock
```

### Privacy Notice

The actual portfolio data is not included in this repository for privacy reasons.
