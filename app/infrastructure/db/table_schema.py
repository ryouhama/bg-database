from enum import Enum


class TableSchema(str, Enum):
    # 異常
    ANOMALY = "anomaly"
    # ヒーロー
    HERO = "hero"
