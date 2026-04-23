import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load
income = {
    'Total Revenue':        [2971196000, 5632184000, 8269605000, 10626855000],
    'Operating Income':     [-364634000, 1030530000, 1972112000, 2871672000],
    'Interest Income':      [3555213000, 6439712000, 9631043000, 13434683000],
    'Interest Expense':     [1547903000, 2036925000, 2834859000, 4578680000],
    'Earnings Before Tax':  [-308901000, 1539078000, 2795198000, 3868419000],
    'Income Tax':           [55733000,   508548000,  823086000,  996747000],
    'Net Income':           [-364578000, 1030530000, 1972112000, 2868892000],
    'SGA Expenses':         [1428331000, 1137612000, 1439281000, 1611265000],
    'EPS':                  [-0.08,      0.22,       0.41,       0.59]
}

# Balance Sheet
balance = {
    'Total Assets':         [29934872000, 43345195000, 49931214000, 74893877000],
    'Total Liabilities':    [25044089000, 36938810000, 42284138000, 63572315000],
    'Stockholders Equity':  [4890783000,  6406385000,  7646289000,  11290948000],
    'Total Debt':           [605921000,   957218000,   577951000,   1897823000],
    'Cash':                 [6890816000,  13370862000, 13637271000, 20929905000],
    'Retained Earnings':    [64577000,    1276949000,  3420596000,  6412700000],
    'Accounts Receivable':  [8233123000,  12414101000, 12259276000, 18267904000]
}

# Cash Flow
cashflow = {
    'Operating Cash Flow':  [755573000,  1266189000, 2399044000, 3500464000],
    'Free Cash Flow':       [641267000,  1089186000, 2224054000, 3159695000],
    'Capital Expenditure':  [-114306000, -177003000, -174990000, -340769000],
    'End Cash Position':    [4172316000, 5923440000, 9185742000, 15003643000]
}

years = [2022, 2023, 2024, 2025]

df_income   = pd.DataFrame(income,   index=years).T
df_balance  = pd.DataFrame(balance,  index=years).T
df_cashflow = pd.DataFrame(cashflow, index=years).T

print(f"\nIncome Statement : {df_income.shape}")
print(f"Balance Sheet    : {df_balance.shape}")
print(f"Cash Flow        : {df_cashflow.shape}")

# profitability KPIs

kpis = pd.DataFrame(index=years)

# Margins
kpis['Net Profit Margin'] = df_income.loc['Net Income'] / df_income.loc['Total Revenue']
kpis['Operating Profit Margin'] = df_income.loc['Operating Income'] / df_income.loc['Total Revenue']

# Return on Assets and Equity
kpis['ROA'] = df_income.loc['Net Income'] / df_balance.loc['Total Assets']
kpis['ROE'] = df_income.loc['Net Income'] / df_balance.loc['Stockholders Equity']

# Net Interest Margin
kpis['NIM'] = (df_income.loc['Interest Income'] - df_income.loc['Interest Expense']) / df_balance.loc['Total Assets']

# Cost to income ratio
kpis['Cost to income ratio'] = df_income.loc['SGA Expenses'] / df_income.loc['Total Revenue']


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(kpis[['Net Profit Margin', 'Operating Profit Margin', 'ROA', 'ROE', 'NIM', 'Cost to income ratio']].round(4))

# Growth KPIs

kpis['Revenue Growth YoY'] = df_income.loc['Total Revenue'].pct_change()
kpis['Net Income Growth YoY'] = df_income.loc['Net Income'].pct_change()
kpis['Free Cash Flow Growth YoY'] = df_cashflow.loc['Free Cash Flow'].pct_change()
kpis['Assets Growth YoY'] = df_balance.loc['Total Assets'].pct_change()

print(kpis[['Revenue Growth YoY', 'Net Income Growth YoY', 'Free Cash Flow Growth YoY', 'Assets Growth YoY']].round(4))

# Financial

kpis['Debt-to-Equity Ratio'] = df_balance.loc['Total Debt'] / df_balance.loc['Stockholders Equity']
kpis['Equity Multiplier'] = df_balance.loc['Total Assets'] / df_balance.loc['Stockholders Equity']
kpis['Debt-to-Assets Ratio'] = df_balance.loc['Total Debt'] / df_balance.loc['Total Assets']
kpis['FCF-to-Net-Income Ratio'] = df_cashflow.loc['Free Cash Flow'] / df_income.loc['Net Income']

print(kpis[['Debt-to-Equity Ratio', 'Equity Multiplier', 'Debt-to-Assets Ratio', 'FCF-to-Net-Income Ratio']].round(4))

base = pd.DataFrame(index=years)

# Absolut
# Income Statement
base['Total Revenue']       = df_income.loc['Total Revenue']
base['Operating Income']    = df_income.loc['Operating Income']
base['Net Income']          = df_income.loc['Net Income']
base['Interest Income']     = df_income.loc['Interest Income']
base['Interest Expense']    = df_income.loc['Interest Expense']
base['EPS']                 = df_income.loc['EPS']

# Balance Sheet
base['Total Assets']        = df_balance.loc['Total Assets']
base['Total Liabilities']   = df_balance.loc['Total Liabilities']
base['Stockholders Equity'] = df_balance.loc['Stockholders Equity']
base['Total Debt']          = df_balance.loc['Total Debt']
base['Retained Earnings']   = df_balance.loc['Retained Earnings']
base['Cash']                = df_balance.loc['Cash']

# Cash Flow
base['Operating Cash Flow'] = df_cashflow.loc['Operating Cash Flow']
base['Free Cash Flow']      = df_cashflow.loc['Free Cash Flow']
base['Capital Expenditure'] = df_cashflow.loc['Capital Expenditure']

# Convertir valores absolutos a Billones USD
cols_billions = [
    'Total Revenue', 'Operating Income', 'Net Income',
    'Interest Income', 'Interest Expense',
    'Total Assets', 'Total Liabilities', 'Stockholders Equity',
    'Total Debt', 'Retained Earnings', 'Cash',
    'Operating Cash Flow', 'Free Cash Flow', 'Capital Expenditure'
]

base[cols_billions] = base[cols_billions] / 1e9

kpi_cols = [
    'Net Profit Margin', 'Operating Profit Margin', 'ROA', 'ROE', 'NIM',
    'Cost to income ratio', 'Revenue Growth YoY', 'Net Income Growth YoY',
    'Free Cash Flow Growth YoY', 'Assets Growth YoY', 'Debt-to-Equity Ratio',
    'Equity Multiplier', 'Debt-to-Assets Ratio', 'FCF-to-Net-Income Ratio'
]

kpis[kpi_cols] = kpis[kpi_cols].round(4)

final = pd.concat([base, kpis], axis=1)
final.index.name = 'Year'

final.to_csv(r'C:\Python\Project3\nu_financial_analysis.csv')
