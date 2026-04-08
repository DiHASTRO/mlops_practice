"""
Обучение модели на train.csv, сохранение в pickle (joblib).
"""
from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

ROOT = Path(__file__).resolve().parents[1]
PROC = ROOT / "data" / "processed"
MODELS = ROOT / "models"
MODELS.mkdir(parents=True, exist_ok=True)


def main() -> None:
    train = pd.read_csv(PROC / "train.csv")
    y = train["target"].values
    X = train.drop(columns=["target"]).values

    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)

    path = MODELS / "model.joblib"
    joblib.dump(clf, path)
    print(f"Модель сохранена: {path}")


if __name__ == "__main__":
    main()
