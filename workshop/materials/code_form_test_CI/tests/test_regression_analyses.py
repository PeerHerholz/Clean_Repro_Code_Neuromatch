
# Import all necessary modules
import os
import shutil
import numpy as np
import torch
from emd_clust_cont_loss_sim_functions import simulate_data, Encoder, train_encoder


# Define list of paths
test_paths = ["./test_outputs/", "./test_outputs/data", "./test_outputs/graphics", "./test_outputs/models"]


# Define regression test
def test_regression_workflow():
    # Part 1: Data Consistency Check
    # Generate test data and check shape and sample values
    data = simulate_data(size=(100, 100), save_path="./test_outputs/data/raw_data_sim.npy")
      
    # Verify data shape
    assert data.shape == (100, 100), "Data shape mismatch."

    # Part 2: Loss Consistency Check
    # Initialize the encoder and train it briefly, then check final loss
    input_dim = 100
    encoder = Encoder(input_dim=input_dim, hidden_dim=100, embedding_dim=50)
    data_train = torch.from_numpy(data).float()

    # Train the encoder for a few epochs
    losses, _ = train_encoder(encoder, data_train, epochs=10)

    # Check that the final loss is within the expected range
    final_loss = losses[-1]
    assert 0.01 < final_loss < 2.0, f"Final loss {final_loss} is outside the expected range (0.01, 2.0)."

    # Part 3: Model Output Consistency Check
    # Generate embeddings and verify their shape and sample values
    data_sample = torch.from_numpy(data[:10]).float()  # Take a sample of 10 rows for testing
    with torch.no_grad():
        embeddings = encoder(data_sample)

    # Verify output shape
    assert embeddings.shape == (10, 50), "Embedding shape mismatch."

    # Expected embedding sample values (replace with known values for regression testing)
    expected_embedding_sample = embeddings[0].numpy()[:5]  # Capture this once and use it as reference
    np.testing.assert_almost_equal(embeddings[0].numpy()[:5], expected_embedding_sample, decimal=6,
                                   err_msg="Embedding does not match expected sample values.")

# Cleanup - remove generated outputs to keep the test environment clean
for path in reversed(test_paths):
        if os.path.isdir(path):
            shutil.rmtree(path)
