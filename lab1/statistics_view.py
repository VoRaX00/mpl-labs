import matplotlib.pyplot as plt
import pandas as pd

def view_statistics_by_data(data: pd.DataFrame, keys: list[str], title: str, xlabel: str, ylable: str):
    plt.figure(figsize=(12, 6))

    for key in keys:
        if key in data.columns:
            plt.plot(data['Дата'], data[key], label=key, marker='o', markersize=2)
        else:
            print(f"Key: '{key}' does not exists in DateFrame")
            return

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylable)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()