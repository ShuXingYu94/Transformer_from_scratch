import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.optim import Adam
from torch.utils.data import TensorDataset, DataLoader

import lightning as L

import tokenize
import BytesIO

token_to_id=tokenize.tokenize("waht is statquest?")
g = tokenize(BytesIO(s.encode('utf-8')).readline)
print(token_to_id)
#
# token_to_id={'what' :0}