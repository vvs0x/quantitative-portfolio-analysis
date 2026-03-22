# Quantitative Portfolio Analysis

Quantitative analysis of a diversified investment portfolio over a two-year period, benchmarked against the FTSE Global All Cap Index (VT). The portfolio follows a long-term buy-and-hold strategy with rebalancing triggered by the 5/25 rule. All prices are converted to CHF. Portfolio positions are retrieved live from Interactive Brokers via the `ib_insync` API, and historical price data is sourced from Yahoo Finance.

## Portfolio Composition

| Asset Class | Allocation |
|---|---|
| Equity | ~75% |
| Fixed Income | ~5% |
| Alternatives | ~20% |

## Performance Metrics

| | My Portfolio | Benchmark |
|---|---|---|
| Total Return | 13.66% | 14.30% |
| Ann. Return | 6.46% | 6.76% |
| Ann. Volatility | 10.61% | 16.78% |
| Sharpe | 0.61 | 0.40 |
| Max Drawdown | -15.73% | -21.03% |

## Cumulative Returns & Drawdown

![Cumulative Returns and Drawdown](figures/cumr_and_drawdown.png)

## Project Structure

```
├── data
│   ├── processed
│   │   └── portfolio_weights.json
│   └── raw
├── figures
│   ├── cumr_and_drawdown.png
│   └── metrics.tex
├── notebooks
│   ├── get_portfolio_weights.ipynb
│   └── portfolio_analysis.ipynb
├── src
│   └── portfolio_weights.py
├── pyproject.toml
└── uv.lock
```

## Dependencies

- `ib-insync` -- Interactive Brokers API client
- `yfinance` -- Yahoo Finance historical data
- `pandas`, `numpy` -- data manipulation
- `matplotlib` -- visualization

Managed with `uv` (see `pyproject.toml`). Requires Python >= 3.12.

## Privacy Notice

The actual portfolio holdings and weights are not included in this repository. The data in `portfolio_weights.json` is from a paper trading account for demonstration purposes only.
