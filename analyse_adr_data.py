"""Descriptive analysis of the synthetic ADR case dataset.

Run from the repository root:
    python src/analyse_adr_data.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "adr_cases.csv"
OUT = ROOT / "outputs"
FIG = OUT / "figures"
OUT.mkdir(exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

EXPECTED_COLUMNS = {
    "case_id", "age_years", "sex", "suspected_drug", "dose_as_reported",
    "route", "indication_as_reported", "reported_adr", "onset_days",
    "concomitant_medicine", "expectedness_as_reported",
    "seriousness_as_reported", "dechallenge", "rechallenge"
}

def main():
    df = pd.read_csv(DATA)
    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df["case_id"].duplicated().any():
        raise ValueError("Duplicate case IDs detected.")
    if df["onset_days"].isna().any() or (df["onset_days"] < 0).any():
        raise ValueError("Onset days must be present and non-negative.")

    summaries = {
        "cases_by_suspected_drug": df["suspected_drug"].value_counts().rename_axis("category").reset_index(name="count"),
        "cases_by_reported_adr": df["reported_adr"].value_counts().rename_axis("category").reset_index(name="count"),
        "cases_by_expectedness": df["expectedness_as_reported"].value_counts().rename_axis("category").reset_index(name="count"),
        "cases_by_seriousness": df["seriousness_as_reported"].value_counts().rename_axis("category").reset_index(name="count"),
        "cases_by_dechallenge": df["dechallenge"].value_counts().rename_axis("category").reset_index(name="count"),
        "cases_by_rechallenge": df["rechallenge"].value_counts().rename_axis("category").reset_index(name="count"),
    }
    all_rows = []
    for name, table in summaries.items():
        table.insert(0, "measure", name)
        all_rows.append(table)
    pd.concat(all_rows, ignore_index=True).to_csv(OUT / "summary_statistics.csv", index=False)

    # ADR frequency by suspected medicine
    counts = df["suspected_drug"].value_counts().sort_values(ascending=True)
    ax = counts.plot(kind="barh", figsize=(8, 5), title="Synthetic cases by suspected medicine")
    ax.set_xlabel("Number of cases")
    ax.set_ylabel("Suspected medicine")
    plt.tight_layout()
    plt.savefig(FIG / "adr_frequency_by_drug.png", dpi=180)
    plt.close()

    # Seriousness distribution
    counts = df["seriousness_as_reported"].value_counts()
    ax = counts.plot(kind="bar", figsize=(8, 5), title="Seriousness categories (as reported)")
    ax.set_xlabel("Seriousness category")
    ax.set_ylabel("Number of cases")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(FIG / "seriousness_distribution.png", dpi=180)
    plt.close()

    # Reported onset by case
    plot_df = df.sort_values("case_id")
    ax = plot_df.plot(x="case_id", y="onset_days", kind="bar", legend=False,
                      figsize=(11, 5), title="Reported time to onset by synthetic case")
    ax.set_xlabel("Case ID")
    ax.set_ylabel("Onset after treatment initiation (days)")
    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()
    plt.savefig(FIG / "onset_by_case.png", dpi=180)
    plt.close()

    print(f"Analysed {len(df)} synthetic cases.")
    print(f"Unique suspected medicines: {df['suspected_drug'].nunique()}")
    print(f"Unique reported ADRs: {df['reported_adr'].nunique()}")
    print(f"Outputs saved to: {OUT}")

if __name__ == "__main__":
    main()
