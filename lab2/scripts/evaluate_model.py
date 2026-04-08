"""
Загрузка модели и оценка качества на тестовых данных.
"""
from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score

ROOT = Path(__file__).resolve().parents[1]
PROC = ROOT / "data" / "processed"
MODELS = ROOT / "models"


def main() -> None:
    model = joblib.load(MODELS / "model.joblib")
    test = pd.read_csv(PROC / "test.csv")
    y_true = test["target"].values
    X = test.drop(columns=["target"]).values

    y_pred = model.predict(X)
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average="weighted")

    print("=== Метрики на тесте ===")
    print(f"Accuracy: {acc:.4f}")
    print(f"F1 (weighted): {f1:.4f}")
    print(classification_report(y_true, y_pred, digits=4))
    # Одна строка для логов CI/Jenkins
    print(f"Model test accuracy is: {acc:.4f}")


if __name__ == "__main__":
    main()
