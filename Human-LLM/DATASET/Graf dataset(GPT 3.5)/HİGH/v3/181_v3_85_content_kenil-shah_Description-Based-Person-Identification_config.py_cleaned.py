import numpy as np
class class1:
    def fonk1(self):
        self.b1 = None
        self.a1 = 1
        self.a2 = 2
        self.a3 = 1000
        self.a4 = 50
        self.b2 = "resnet101"
        self.b3 = None
        self.b4 = [4, 8, 16, 32, 64]
        self.a5 = 1024
        self.a6 = 256
        self.a7 = 1
        self.b5 = (32, 64, 128, 256, 512)
        self.b6 = [0.5, 1, 2]
        self.a8 = 1
        self.a9 = 0.7
        self.a10 = 256
        self.a11 = 6000
        self.a12 = 2000
        self.a13 = 1000
        self.b7 = True
        self.b8 = (56, 56)
        self.b9 = "square"
        self.a14 = 800
        self.a15 = 1024
        self.a16 = 0
        self.a17 = 3
        self.b10 = np.array([123.7, 116.8, 103.9])
        self.a18 = 200
        self.a19 = 0.33
        self.a20 = 7
        self.a21 = 14
        self.b11 = [28, 28]
        self.a22 = 100
        self.b12 = np.array([0.1, 0.1, 0.2, 0.2])
        self.b13 = np.array([0.1, 0.1, 0.2, 0.2])
        self.a23 = 100
        self.a24 = 0.7
        self.a25 = 0.3
        self.a26 = 0.001
        self.a27 = 0.9
        self.a28 = 0.0001
        self.b14 = {
            "rpn_class_loss": 1.,
            "rpn_bbox_loss": 1.,
            "mrcnn_class_loss": 1.,
            "mrcnn_bbox_loss": 1.,
            "mrcnn_mask_loss": 1.
        }
        self.b15 = True
        self.b16 = False
        self.a29 = 5.0
        self.b17 = self.a2 * self.a1
        self.b18 = self.fonk2()
    def fonk2(self):
        if self.b9 = = "crop":
            return np.array([self.a14, self.a14, self.a17])
        else:
            return np.array([self.a15, self.a15, self.a17])
    def fonk3(self):
        print("\nConfigurations:")
        for attr_name in dir(self):
            if not attr_name.startswith("__") and not callable(getattr(self, attr_name)):
                print(f"{attr_name:30} {getattr(self, attr_name)}")
b19 = class1()
b19.fonk3()