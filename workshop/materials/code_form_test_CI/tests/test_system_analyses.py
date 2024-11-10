
import os
import shutil
import numpy as np
import torch
from emd_clust_cont_loss_sim_functions import main, Encoder, simulate_data, train_encoder

def test_system_workflow():
    # Set up paths for verification
    output_paths = ["./outputs/", "./outputs/data", "./outputs/graphics", "./outputs/models"]
    data_file = "./outputs/data/raw_data_sim.npy"
    plot_file = "./outputs/graphics/data_examples.png"
    model_file = "./outputs/models/encoder.pth"
    
    # Run the main function to execute the workflow
    main()
    
    # Check that output directories are created
    for path in output_paths:
        assert os.path.isdir(path), f"Expected directory {path} to be created."

    # Verify data file existence and format
    assert os.path.isfile(data_file), "Expected data file not found."
    data = np.load(data_file)
    assert isinstance(data, np.ndarray), "Data file is not in the expected .npy format."
    
    # Verify the plot file is created
    assert os.path.isfile(plot_file), "Expected plot file not found."

    # Verify the model file is created
    assert os.path.isfile(model_file), "Expected model file not found."
    
    # Step 1: Load and check model
    encoder = torch.load(model_file)
    assert isinstance(encoder, Encoder), "The loaded model is not an instance of the Encoder class."
    
    # Step 2: Evaluate model with sample data
    # Use a small subset of the data to generate embeddings and verify the output shape
    data_sample = torch.from_numpy(data[:10]).float()  # Take a sample of 10 for testing
    with torch.no_grad():
        embeddings = encoder(data_sample)
    
    # Check the output embeddings shape
    expected_shape = (10, encoder.layers[-1].out_features)
    assert embeddings.shape == expected_shape, f"Expected embeddings shape {expected_shape}, but got {embeddings.shape}."

    # Step 3: Check if training reduces loss over epochs
    # Train the model for a small number of epochs and confirm that loss decreases
    data_train = torch.from_numpy(data[:80]).float()
    initial_loss, final_loss = None, None
    encoder = Encoder(input_dim=100, hidden_dim=100, embedding_dim=50)  # Reinitialize the encoder for testing
    losses, _ = train_encoder(encoder, data_train, epochs=10)  # Train for a few epochs for quick testing
    
    # Capture initial and final losses
    initial_loss, final_loss = losses[0], losses[-1]
    
    # Verify that the final loss is lower than the initial loss
    assert final_loss < initial_loss, "Expected final loss to be lower than initial loss, indicating training progress."

    # Cleanup - remove generated outputs to keep the test environment clean
    for path in reversed(output_paths):
            if os.path.isdir(path):
                shutil.rmtree(path)
