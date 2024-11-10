

import os
import shutil
import pytest
from emd_clust_cont_loss_sim_functions import create_output_paths 

# Define test paths (use temporary or unique paths to avoid overwriting real data)
test_paths = ["./test_outputs/", "./test_outputs/data", "./test_outputs/graphics", "./test_outputs/models"]

# Define tests
def test_create_output_paths():

    # Run the path creation function
    create_output_paths(test_paths)

    # Check if each path now exists
    for path in test_paths:
        assert os.path.isdir(path), f"Expected directory {path} to be created, but it was not."

    # Cleanup - remove the directories after the test to keep the environment clean
    for path in reversed(test_paths):  # Remove subdirectories before parent directory
        if os.path.isdir(path):
            os.rmdir(path)

# Cleanup - remove generated outputs to keep the test environment clean
for path in reversed(test_paths):
        if os.path.isdir(path):
            shutil.rmtree(path)
