"""
analyser.py — Student Grade Analyser
=====================================
Reads student exam scores from a CSV file, computes descriptive statistics,
assigns letter grades, and plots a histogram of the grade distribution.

Usage:
    python analyser.py scores.csv

Author: Anish Rana Magar
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


# ── Grade boundaries ──────────────────────────────────────────────────────────
GRADE_BANDS = [
    ("A", 90, 100),
    ("B", 80, 89),
    ("C", 70, 79),
    ("D", 60, 69),
    ("F",  0, 59),
]


def load_scores(filepath: str) -> pd.Series:
    """Load a CSV file and return the 'score' column as a Series.

    Args:
        filepath: Path to a CSV file with at least a 'score' column.

    Returns:
        A pandas Series of numeric scores.

    Raises:
        SystemExit: If the file cannot be read or is missing the 'score' column.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        sys.exit(f"Error: File '{filepath}' not found.")

    if "score" not in df.columns:
        sys.exit("Error: CSV must contain a 'score' column.")

    return pd.to_numeric(df["score"], errors="coerce").dropna()


def compute_statistics(scores: pd.Series) -> dict:
    """Compute descriptive statistics for a series of scores.

    Args:
        scores: A pandas Series of numeric values.

    Returns:
        A dictionary with keys: count, mean, median, std, min, max.
    """
    return {
        "count":  len(scores),
        "mean":   round(scores.mean(), 2),
        "median": round(scores.median(), 2),
        "std":    round(scores.std(), 2),
        "min":    int(scores.min()),
        "max":    int(scores.max()),
    }


def assign_grade_bands(scores: pd.Series) -> dict:
    """Count how many scores fall into each letter-grade band.

    Args:
        scores: A pandas Series of numeric values (0–100).

    Returns:
        A dictionary mapping grade letters to student counts.
    """
    counts = {}
    for grade, low, high in GRADE_BANDS:
        counts[grade] = int(((scores >= low) & (scores <= high)).sum())
    return counts


def print_report(stats: dict, bands: dict) -> None:
    """Print a formatted statistics report to stdout."""
    print("\n=== Grade Statistics ===")
    print(f"  Count   : {stats['count']}")
    print(f"  Mean    : {stats['mean']}")
    print(f"  Median  : {stats['median']}")
    print(f"  Std Dev : {stats['std']}")
    print(f"  Min     : {stats['min']}   Max: {stats['max']}")
    print("\nGrade Bands:")
    for grade, low, high in GRADE_BANDS:
        label = f"{grade} ({low}–{high})"
        print(f"  {label:<15}: {bands[grade]} students")
    print()


def plot_histogram(scores: pd.Series, output_path: str = "grade_distribution.png") -> None:
    """Plot and save a histogram of score distribution.

    Args:
        scores:      A pandas Series of numeric scores.
        output_path: Filename for the saved PNG image.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(scores, bins=10, range=(0, 100), color="#00a370", edgecolor="white", linewidth=0.8)
    ax.set_title("Grade Distribution", fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Score", fontsize=11)
    ax.set_ylabel("Number of Students", fontsize=11)
    ax.set_xlim(0, 100)
    ax.grid(axis="y", alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Histogram saved to '{output_path}'")


def main() -> None:
    """Entry point: parse arguments, run analysis, produce output."""
    if len(sys.argv) != 2:
        sys.exit("Usage: python analyser.py <scores.csv>")

    filepath = sys.argv[1]
    scores   = load_scores(filepath)
    stats    = compute_statistics(scores)
    bands    = assign_grade_bands(scores)

    print_report(stats, bands)
    plot_histogram(scores)


if __name__ == "__main__":
    main()
