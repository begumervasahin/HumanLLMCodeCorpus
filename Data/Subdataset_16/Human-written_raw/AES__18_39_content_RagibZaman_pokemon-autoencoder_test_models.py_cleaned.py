import unittest
import torch
from torch.autograd import Variable
import models
class class1(unittest.TestCase):
    def fonk1(self):
        a1 = 32
        a2 = 64
        a3 = 128
        b1 = models.Encoder(a3, a2)
        b2 = Variable(2.0 * (torch.rand((a1, 3, a2, a2)) - 0.5))
        b3 = b1.forward(b2)
        self.assertEqual(b3.size(), torch.Size([a1, a3]))
    def fonk2(self):
        a1 = 32
        a2 = 64
        a3 = 128
        b1 = models.Encoder(a3, a2)
        b4 = Variable(2.0 * (torch.rand((a1, 3, a2, a2)) - 0.5))
        b4 = b4.view(b4.size()[0], -1)
        b4 = b1.hidden_layer(b4)
        self.assertEqual(b4.size(), torch.Size([a1, a3]))
        b4 = b1.output_layer(b4)
        self.assertEqual(b4.size(), torch.Size([a1, a3]))
class class2(unittest.TestCase):
    def fonk3(self):
        a1 = 32
        a2 = 64
        a3 = 128
        b5 = models.Decoder(a3, a2)
        b2 = Variable(2.0 * (torch.rand((a1, a3, 1, 1)) - 0.5))
        b3 = b5.forward(b2)
        self.assertEqual(b3.size(), torch.Size([a1, 3, a2, a2]))
    def fonk4(self):
        a1 = 32
        a2 = 64
        a3 = 128
        b5 = models.Decoder(a3, a2)
        b4 = Variable(2.0 * (torch.rand((a1, a3, 1, 1)) - 0.5))
        b4 = b5.layer1.forward(b4)
        self.assertEqual(b4.size(), torch.Size([a1, 128, 7, 7]))
        b4 = b5.layer2.forward(b4)
        self.assertEqual(b4.size(), torch.Size([a1, 64, 15, 15]))
        b4 = b5.layer3.forward(b4)
        self.assertEqual(b4.size(), torch.Size([a1, 64, 31, 31]))
        b4 = b5.layer4.forward(b4)
        self.assertEqual(b4.size(), torch.Size([a1, 32, 63, 63]))
        b4 = b5.layer5.forward(b4)
        self.assertEqual(b4.size(), torch.Size([a1, 3, a2, a2]))
if b6 = = '__main__':
    unittest.main()