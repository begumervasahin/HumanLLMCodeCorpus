import numpy as np
class class1:
    b1 = None
    a1 = 1
    a2 = 2
    a3 = 1000
    a4 = 50
    b2 = "resnet101"
    b3 = None
    b4 = [4, 8, 16, 32, 64]
    a5 = 1024
    a6 = 256
    a7 = 1
    b5 = (32, 64, 128, 256, 512)
    b6 = [0.5, 1, 2]
    a8 = 1
    a9 = 0.7
    a10 = 256
    a11 = 6000
    a12 = 2000
    a13 = 1000
    b7 = True
    b8 = (56, 56)
    b9 = "square"
    a14 = 800
    a15 = 1024
    a16 = 0
    a17 = 3
    b10 = np.array([123.7, 116.8, 103.9])
    a18 = 200
    a19 = 0.33
    a20 = 7
    a21 = 14
    b11 = [28, 28]
    a22 = 100
    b12 = np.array([0.1, 0.1, 0.2, 0.2])
    b13 = np.array([0.1, 0.1, 0.2, 0.2])
    a23 = 100
    a24 = 0.7
    a25 = 0.3
    a26 = 0.001
    a27 = 0.9
    a28 = 0.0001
    b14 = {
        "rpn_class_loss": 1.,
        "rpn_bbox_loss": 1.,
        "mrcnn_class_loss": 1.,
        "mrcnn_bbox_loss": 1.,
        "mrcnn_mask_loss": 1.
    }
    b15 = True
    b16 = False
    a29 = 5.0
    def fonk1(self):
        self.b17 = self.a2 * self.a1
        if self.b9 = = "crop":
            self.b18 = np.array([self.a14, self.a14, self.a17])
        else:
            self.b18 = np.array([self.a15, self.a15, self.a17])
        self.b19 = 1 + 3 + 3 + 4 + 1 + self.a7
    def fonk2(self):
        print("\nConfigurations:")
        for attr_name in dir(self):
            if not attr_name.startswith("__") and not callable(getattr(self, attr_name)):
                print(f"{attr_name:30} {getattr(self, attr_name)}")
b20 = class1()
b20.fonk2()