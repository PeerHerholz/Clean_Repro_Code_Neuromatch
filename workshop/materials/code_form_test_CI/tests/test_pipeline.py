

# Import all necessary modules
import os
import shutil
import numpy as np
import torch
from emd_clust_cont_loss_sim_functions import create_output_paths, simulate_data, Encoder, train_encoder

# Define list of paths
test_paths = ["./test_outputs/", "./test_outputs/data", "./test_outputs/graphics", "./test_outputs/models"]


# Define the tests
def test_end_to_end_pipeline():
    # Step 1: Set up output directories
    create_output_paths(test_paths)
    for path in test_paths:
        assert os.path.isdir(path), f"Directory {path} was not created."

    # Step 2: Generate data
    data = simulate_data(size=(100, 50), save_path="./test_outputs/data/raw_data_sim.npy")
    assert isinstance(data, np.ndarray), "Expected output type np.ndarray"
    assert data.shape == (100, 50), "Expected output shape (100, 50)"
    
    # Step 3: Split data and prepare for model training
    data_train = torch.from_numpy(data[:80]).float()
    
    # Step 4: Initialize and train the Encoder model for a few epochs
    encoder = Encoder(input_dim=50, hidden_dim=25, embedding_dim=10)
    losses, _ = train_encoder(encoder, data_train, epochs=10)  # Limit epochs for a quick test
    
    # Check that the losses are recorded and decrease over epochs
    assert len(losses) == 10, "Expected 10 loss values, one for each epoch."
    assert losses[-1] < losses[0], "Expected the loss to decrease over training."
    

# Cleanup - remove generated outputs to keep the test environment clean
for path in reversed(test_paths):
        if os.path.isdir(path):
            shutil.rmtree(path)
