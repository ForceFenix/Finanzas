def safe_series(data, index):
    import pandas as pd
    if hasattr(data, 'shape') and len(data.shape) == 2 and data.shape[1] == 1:
        return pd.Series(data.flatten(), index=index)
    return pd.Series(data, index=index)
