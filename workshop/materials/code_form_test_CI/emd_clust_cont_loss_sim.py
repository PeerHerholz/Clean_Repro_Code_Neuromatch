# Import all necessary modules and functions
import os
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.mixture import BayesianGaussianMixture
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
from joblib import dump
import matplotlib.pyplot as plt
import seaborn as sns

# Define paths for all to be generated outputs
output_path = "./outputs/"
output_path_data = "./outputs/data"
output_path_graphics = "./outputs/graphics"
output_path_models = "./outputs/models"

# For all output paths it should be checked if
# they exist and if not, they should be created
list_paths = [output_path, output_path_data, output_path_graphics,
              output_path_models]

# Loop over the list of paths that should be checked
for outputs in list_paths:

    # if path exists, all good
    if os.path.isdir(outputs):
        print(f"{outputs} exists.")
    # if not, path should be created
    else:
        print(f"{outputs} does not exist, creating it.")
        os.makedirs(outputs)

# Define seeds to address randomness
np.random.seed(42)
torch.manual_seed(42)

# Create, check and save simulated data
data = np.random.randn(2000, 100)
data.shape

np.save("./outputs/data/raw_data_sim.npy", data)

# Create a plot of the first 5 data samples
fig, axes = plt.subplots(5, 1, sharex=True, figsize=(16, 10))

for sample, ax in zip(np.arange(5), axes.flat):
    sns.heatmap(data[sample].reshape(-1, 100), cbar=False, annot=False,
                xticklabels=False, yticklabels=False, ax=ax)
    ax.set_title('data sample %s' % str(sample+1))

fig.savefig('./outputs/graphics/data_examples.png')

# Split the created data into train and test sets
# and create respective torchs
data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

data_train_torch = torch.from_numpy(data_train).float()
data_test_torch = torch.from_numpy(data_test).float()

# Define a class for the encoder


class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, embedding_dim):
        super(Encoder, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, embedding_dim)
        )

    # Define a forward function
    def forward(self, x):
        return self.layers(x)


# Create an encoder instance and print
# its parameters
encoder = Encoder(input_dim=100, hidden_dim=100, embedding_dim=50)

print(encoder)

# Define a loss function and optimization
loss_function = nn.MSELoss()
optimization = optim.SGD(encoder.parameters(), lr=0.001, momentum=0.9)

# Initiate empty lists for the loss and
# representations during the training
losses = []
representations_during_training = []

# Train the encoder for a given number
# of epochs, saving the loss and representations
for epoch in range(4000):
    optimization.zero_grad()
    outputs = encoder(data_train_torch)
    loss = loss_function(outputs, data_train_torch[:, :50])
    loss.backward()
    optimization.step()

    # save the loss
    losses.append(loss.item())

    # Save the representations of every 1000th epoch
    if epoch % 1000 == 0:
        with torch.no_grad():
            representations = encoder(data_train_torch)
            representations_during_training.append(
                representations.cpu().numpy())

# Save the trained encoder
torch.save(encoder, './outputs/models/encoder.pth')

# Create a plot to visualize the loss
# during training and save it
fig, ax = plt.subplots()

sns.lineplot(losses, ax=ax)
sns.despine(offset=10, ax=ax)
plt.title("Loss of Encoder")
plt.xlabel("Epoch number")
plt.ylabel("Training loss")

fig.savefig('./outputs/graphics/loss_training.png')

# Plot the learned representations for the first
# 5 data samples and save the graphic
representations_training = representations_during_training[3]

fig, axes = plt.subplots(1, 5, sharex=True, figsize=(10, 2))

for sample, ax in zip(np.arange(5), axes.flat):
    sns.heatmap(representations_training[sample].reshape(-1, 5),
                cbar=False, annot=False, xticklabels=False, yticklabels=False,
                ax=ax)
    ax.set_title('Sample %s' % str(sample+1))

fig.savefig('./outputs/graphics/data_representations_examples.png')

# Define and fit the Bayesian Gaussian Mixture
# clustering and save the fitted estimator
dpgmm = BayesianGaussianMixture(
        n_components=10, covariance_type='full',
        weight_concentration_prior_type="dirichlet_process",
        weight_concentration_prior=0.1, random_state=42)
dpgmm.fit(representations_during_training[3])

dump(dpgmm, './outputs/models/dpgmm.joblib')

# Predict cluster assignments of the learned
# representations in the training data
cluster_assignments_train = dpgmm.predict(representations_during_training[3])

clusters = []
for i in range(cluster_assignments_train.max() + 1):
    clusters.append(
        representations_during_training[3][cluster_assignments_train == i])

# Create pairs of data samples based on their
# cluster assignment
#
# positive pairs: pairs of samples in the sample cluster
# negative pairs: pairs of samples from different clusters
positive_pairs = []
negative_pairs = []

for i, cluster in enumerate(clusters):
    for j in range(len(cluster)):
        for k in range(j+1, len(cluster)):
            positive_pairs.append((cluster[j], cluster[k]))

    for j in range(len(cluster)):
        for k in range(i+1, len(clusters)):
            for m in range(len(clusters[k])):
                negative_pairs.append((cluster[j], clusters[k][m]))

positive_pairs_torch = torch.from_numpy(np.array(positive_pairs)).float()
negative_pairs_torch = torch.from_numpy(np.array(negative_pairs)).float()

# Create a class for the MLP and define
# its architecture


class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim)
        )

    # define a forward function
    def forward(self, x):
        return self.layers(x)


# Initiate the MLP and a respective optimizer
contrastive_model = MLP(input_dim=50, hidden_dim=50)

optimizer_contrastive = optim.Adam(contrastive_model.parameters(), lr=0.001)

# Create a class for the contrastive loss function
# and initiate it


class ContrastiveLoss(nn.Module):
    def __init__(self, margin):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    # define a forward function
    def forward(self, output1, output2, label):
        euclidean_distance = (output1 - output2).pow(2).sum(1)
        loss_contrastive = torch.mean((1-label) * euclidean_distance + (
            label) * torch.clamp(self.margin - euclidean_distance, min=0.0))
        return loss_contrastive


contrastive_loss = ContrastiveLoss(margin=1.0)


# Train the MLP with the defined loss function
# based on assigned pairs and save the trained
# MLP
losses_contrastive = []

for epoch in range(200):
    optimizer_contrastive.zero_grad()
    positive_pair_rep_1 = contrastive_model(positive_pairs_torch[:, 0])
    positive_pair_rep_2 = contrastive_model(positive_pairs_torch[:, 1])
    negative_pair_rep_1 = contrastive_model(negative_pairs_torch[:, 0])
    negative_pair_rep_2 = contrastive_model(negative_pairs_torch[:, 1])
    loss_positive = contrastive_loss(
        positive_pair_rep_1, positive_pair_rep_2, 0)
    loss_negative = contrastive_loss(
        negative_pair_rep_1, negative_pair_rep_2, 1)
    loss = loss_positive + loss_negative
    loss.backward()
    optimizer_contrastive.step()

    losses_contrastive.append(loss.item())

torch.save(contrastive_model, './outputs/models/contrastive_model.pth')

# Create and save a plot of the training loss
fig, ax = plt.subplots()

sns.lineplot(losses_contrastive, ax=ax)
sns.despine(offset=10, ax=ax)
plt.title("Loss of MLP with contrastive learning")
plt.xlabel("Epoch number")
plt.ylabel("Training loss")

fig.savefig('./outputs/graphics/loss_training_MLP_cont_learn.png')

# Apply the trained encoder to the test set
encoder_embeddings_test = encoder(data_test_torch)

# Create a plot of the first few test sample representations
# and save the graphic
fig, axes = plt.subplots(1, 5, sharex=True, figsize=(10, 2))

for sample, ax in zip(np.arange(5), axes.flat):
    sns.heatmap(
        encoder_embeddings_test.detach().numpy()[sample].reshape(-1, 5),
        cbar=False, annot=False,
        xticklabels=False, yticklabels=False, ax=ax)
    ax.set_title('Sample %s' % sample)

# Predict clusters in the test set using the
# fitted estimator
cluster_assignments_test = dpgmm.predict(
    encoder_embeddings_test.detach().numpy())

# Apply TSNE to the encoder representations of the test dataset, coloring
# samples based on their predicted cluster, create a plot and save it
tsne = TSNE(n_components=2, verbose=1, perplexity=40,
            n_iter=300, random_state=42)
tsne_results = tsne.fit_transform(encoder_embeddings_test.detach().numpy())

df_subset = pd.DataFrame()

df_subset['t-SNE dim 1'] = tsne_results[:, 0]
df_subset['t-SNE dim 2'] = tsne_results[:, 1]
df_subset['cluster'] = cluster_assignments_test

plt.figure(figsize=(16, 10))
sns.scatterplot(
    x="t-SNE dim 1", y="t-SNE dim 2",
    palette=sns.color_palette("hls", 10),
    data=df_subset, hue=df_subset['cluster'],
    legend="full",
    alpha=0.3
)
sns.despine(offset=10)
plt.savefig('./outputs/graphics/tsne_rep_clust_train.png')

# Apply the trained MLP with contrastive learning function
# to the test set
contrastive_representations_test = contrastive_model(encoder_embeddings_test)


# Apply TSNE to the MLP representations of the test dataset, coloring
# samples based on their predicted cluster, create a plot and save it
tsne = TSNE(n_components=2, verbose=1, perplexity=40,
            n_iter=300, random_state=42)
tsne_results = tsne.fit_transform(
    contrastive_representations_test.detach().numpy())

df_subset = pd.DataFrame()

df_subset['t-SNE dim 1'] = tsne_results[:, 0]
df_subset['t-SNE dim 2'] = tsne_results[:, 1]
df_subset['cluster'] = cluster_assignments_test

plt.figure(figsize=(16, 10))
sns.scatterplot(
    x="t-SNE dim 1", y="t-SNE dim 2",
    palette=sns.color_palette("hls", 10),
    data=df_subset, hue=df_subset['cluster'],
    legend="full",
    alpha=0.3
)
sns.despine(offset=10)
plt.savefig('./outputs/graphics/tsne_rep_clust_test.png')
