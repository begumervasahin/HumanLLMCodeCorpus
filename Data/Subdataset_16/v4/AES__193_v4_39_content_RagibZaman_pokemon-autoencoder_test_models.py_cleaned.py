import unittest
import torch
from torch.autograd import Variable
import models
class class1(unittest.TestCase):
    def fonk1(self):
        self.a1 = 32
        self.a2 = 64
        self.a3 = 128
        self.b1 = models.Encoder(self.a3, self.a2)
        self.b2 = Variable(2.0 * (torch.rand((self.a1, 3, self.a2, self.a2)) - 0.5))
    def fonk2(self):
        b3 = self.b1(self.b2)
        self.assertEqual(b3.size(), torch.Size([self.a1, self.a3]))
    def fonk3(self):
        b4 = self.b2.view(self.a1, -1)
        b5 = self.b1.hidden_layer(b4)
        self.assertEqual(b5.size(), torch.Size([self.a1, self.a3]))
        b3 = self.b1.output_layer(b5)
        self.assertEqual(b3.size(), torch.Size([self.a1, self.a3]))
class class2(unittest.TestCase):
    def fonk4(self):
        self.a1 = 32
        self.a2 = 64
        self.a3 = 128
        self.b6 = models.Decoder(self.a3, self.a2)
        self.b2 = Variable(2.0 * (torch.rand((self.a1, self.a3, 1, 1)) - 0.5))
    def fonk5(self):
        b3 = self.b6(self.b2)
        self.assertEqual(b3.size(), torch.Size([self.a1, 3, self.a2, self.a2]))
    def fonk6(self):
        b7 = self.b6.layer1(self.b2)
        self.assertEqual(b7.size(), torch.Size([self.a1, 128, 7, 7]))
        b8 = self.b6.layer2(b7)
        self.assertEqual(b8.size(), torch.Size([self.a1, 64, 15, 15]))
        b9 = self.b6.layer3(b8)
        self.assertEqual(b9.size(), torch.Size([self.a1, 64, 31, 31]))
        b10 = self.b6.layer4(b9)
        self.assertEqual(b10.size(), torch.Size([self.a1, 32, 63, 63]))
        b11 = self.b6.layer5(b10)
        self.assertEqual(b11.size(), torch.Size([self.a1, 3, self.a2, self.a2]))
if b12 = = '__main__':
    unittest.main()