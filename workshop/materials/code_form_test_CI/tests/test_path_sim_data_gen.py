

import os
import shutil
import numpy as np
import pytest
from emd_clust_cont_loss_sim_functions import create_output_paths, simulate_data

# Define temporary test paths to avoid overwriting real data
test_paths = ["./test_outputs/", "./test_outputs/data", "./test_outputs/graphics", "./test_outputs/models"]


def test_create_output_paths():
    # Run the path creation function
    create_output_paths(test_paths)
    
    # Check if each path now exists
    for path in test_paths:
        assert os.path.isdir(path), f"Expected directory {path} to be created, but it was not."


def test_simulate_data():
    # Generate test data
    data = simulate_data(size=(100, 50), save_path="./test_outputs/data/raw_data_sim.npy")
    
    # Check type and shape
    assert isinstance(data, np.ndarray), "Expected output type np.ndarray"
    assert data.shape == (100, 50), "Expected output shape (100, 50)"

    os.remove("./test_outputs/data/raw_data_sim.npy")


# Cleanup - remove generated outputs to keep the test environment clean
for path in reversed(test_paths):
        if os.path.isdir(path):
            shutil.rmtree(path)
