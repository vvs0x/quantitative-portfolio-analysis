# Quantitative Portfolio Analysis

Quantitative analysis of a diversified investment portfolio over a two-year period, benchmarked against the FTSE Global All Cap Index. Evaluated key performance metrics including total return, maximum drawdown, and Sharpe ratio. The portfolio follows a long-term buy-and-hold strategy with rebalancing triggered by the 5/25 rule.

Portfolio Composition:

| Asset Class | Allocation |
|------------|-----------|
| Equity | ~75% |
| Fixed Income | ~5% |
| Alternatives | ~20% |

Performance Metrics:

| | My Portfolio | Benchmark |
|---|---|---|
| Total Return | 13.66% | 14.30% |
| Ann. Return | 6.46% | 6.76% |
| Ann. Volatility | 10.61% | 16.78% |
| Sharpe | 0.61 | 0.40 |
| Max Drawdown | -15.73% | -21.03% |

### Project Structure

```
├── data
│   ├── processed
│   │   └── portfolio_weights.json
│   └── raw
├── figures
│   ├── cumr_and_drawdown.png
│   └── metrics.tex
├── notebooks
│   ├── get_portfolio_weights.ipynb
│   └── portfolio_analysis.ipynb
├── pyproject.toml
├── README.md
├── src
│   ├── __pycache__
│   │   └── portfolio_weights.cpython-312.pyc
│   └── portfolio_weights.py
└── uv.lock
```

### Dependencies

`ib-insync` — Interactive Brokers API client
`yfinance` — Yahoo Finance historical data
`pandas`, `numpy` — data manipulation
`matplotlib` — visualization

Managed via `uv` (see `pyproject.toml`).

### Privacy Notice

The actual portfolio data is not included in this repository for privacy reasons.
