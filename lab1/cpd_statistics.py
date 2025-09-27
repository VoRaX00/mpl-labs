import pandas as pd

def loan_statistics(path: str, keys: list[str]) -> pd.DataFrame: 
    df = pd.read_excel(path, header=None)
    categories = pd.Series(df[0])

    row_indices = []
    for key in keys:
        idx = categories[categories.str.contains(key, na=False)].index[0]
        row_indices.append(idx)

    dates = pd.to_datetime(df.iloc[0, 1:], errors='coerce')
    data = pd.DataFrame({'Дата': dates})
    for key, idx in zip(keys, row_indices):
        values = pd.to_numeric(df.iloc[idx, 1:], errors='coerce').values
        data[key] = values

    return data.dropna(subset=['Дата'])