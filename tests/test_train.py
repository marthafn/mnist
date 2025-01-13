import torch
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.project1.train import MyAwesomeModel


def test_train():
    # test that the model trains
    assert os.path.exists("reports/figures/training_statistics.png"), "Training statistics file does not exist"
    assert os.path.exists("models/model.pth"), "Model file does not exist"
