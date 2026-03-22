import pandas as pd
from ib_insync import IB

def get_portfolio_weights(ib: IB):

    portfolio = ib.portfolio()
    
    if not portfolio:
        print("Portfolio is empty!")
        return pd.DataFrame()

    account_values = ib.accountValues()
    nav = next((float(v.value) for v in account_values if v.tag == 'NetLiquidation'), 0)
    
    data = []
    for item in portfolio:
        cost_basis = item.averageCost * abs(item.position)
        
        data.append({
            'symbol': item.contract.symbol,
            'position': item.position,
            'averageCost': item.averageCost,
            'costBasis': cost_basis,
            'marketPrice': item.marketPrice,
            'marketValue': item.marketValue,
            'unrealizedPNL': item.unrealizedPNL,
            'unrealizedPNL_pct': (item.unrealizedPNL / cost_basis * 100) if cost_basis != 0 else 0,
            'realizedPNL': item.realizedPNL
        })
    
    df = pd.DataFrame(data)
    
    df['weight_pct'] = (df['marketValue'] / nav * 100).round(2)
    
    df['unrealizedPNL_pct'] = df['unrealizedPNL_pct'].round(2)
    df['averageCost'] = df['averageCost'].round(2)
    df['costBasis'] = df['costBasis'].round(2)
    df['marketPrice'] = df['marketPrice'].round(2)
    df['marketValue'] = df['marketValue'].round(2)
    df['unrealizedPNL'] = df['unrealizedPNL'].round(2)
    
    df = df.sort_values('weight_pct', ascending=False).reset_index(drop=True)
    
    return df