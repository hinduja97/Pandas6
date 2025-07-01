import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df=store[store['amount']>500].drop_duplicates('customer_id')
    count=df['customer_id'].nunique()
    return pd.DataFrame({'rich_count':[count]})