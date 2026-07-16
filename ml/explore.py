import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "ml/data/creditcard.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    fraud = df["Class"].sum()
    normal = len(df) - fraud

    print(f"Normal transactions : {normal}")
    print(f"Fraud transactions  : {fraud}")

    counts = df["Class"].value_counts()

    plt.figure(figsize=(6, 4))

    bars = plt.bar(
        ["Normal", "Fraud"],
        counts.values
    )

    plt.title("Credit Card Transaction Distribution")
    plt.xlabel("Transaction Class")
    plt.ylabel("Number of Transactions")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height):,}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()