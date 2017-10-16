import torch
from torch import nn


class LayerNorm(nn.Module):

    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.gamma = nn.Parameter(torch.ones(features))
        self.beta = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(0, keepdim=True)
        std = x.std(0, keepdim=True)
        return self.gamma * (x - mean) / (std + self.eps) + self.beta
