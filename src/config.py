from __future__ import annotations
from pathlib import Path
import yaml
from pydantic import BaseModel

class Paths(BaseModel):
    train_dir: str
    test_dir: str
    sample_submission: str
    artifacts_dir: str
    submission_path: str

class FeatureCfg(BaseModel):
    gr_windows: list[int]
    typewell_neighbors: int

class CVCfg(BaseModel):
    n_splits: int
    group_col: str
    random_state: int

class ModelCfg(BaseModel):
    n_estimators: int
    learning_rate: float
    num_leaves: int
    subsample: float
    colsample_bytree: float
    min_child_samples: int
    reg_lambda: float
    random_state: int
    early_stopping_rounds: int

class MLflowCfg(BaseModel):
    experiment: str
    enabled: bool

class Config(BaseModel):
    paths: Paths
    features: FeatureCfg
    cv: CVCfg
    model: ModelCfg
    mlflow: MLflowCfg

def load_config(path: str | Path = "config.yaml") -> Config:
    with open(path, "r") as fh:
        raw= yaml.safe_load(fh)
    return Config(**raw)