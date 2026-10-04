'''
Simple exponential smoothing
Created on 18.03.2019
@author: /dat
y_t = a * y_t + a * (1-a)^1 * y_t-1 + a * (1-a)^2 * y_t-2 + ... + a*(1-a)^n * y_t-n
'''
import numpy as np
import xlwings as xw
@xw.func
def expsmooth(st):
    data = []
    for values in st:
        data.append(values)
    sss = []
    a = []
    opt_a = []
    a2 = []
    sss2 = []
    def alpha_counting(alpha):
        global output
        eps = 0
        y = 0
        for i in data:
            if y == 0:
                b = alpha * i + (1 - alpha) * i
                y += 1
            else:
                c = (b - i) ** 2
                eps += c
                b = alpha * i + (1 - alpha) * b
        sigma = eps / (len(data))
        sss.append(sigma)
        a.append(alpha)
        y = 0
        if len(a) == 19:
            k = int(sss.index(min(sss)))
            opt_alpha = a[k]
            print(opt_alpha)
            for alp2 in np.arange(opt_alpha - 0.2, opt_alpha + 0.2, 0.001):
                opt_a.append(alp2)
            for q in opt_a:
                eps = 0
                y = 0
                for i in data:
                    if y == 0:
                        b = q * i + (1 - q) * i
                        y += 1
                    else:
                        c = (b - i) ** 2
                        eps += c
                        b = q * i + (1 - q) * b
                sigma = eps / (len(data))
                sss2.append(sigma)
                a2.append(q)
                y = 0
                if len(a2) == 400:
                    k2 = int(sss2.index(min(sss2)))
                    opt_alpha2 = a2[k2]
                    print(opt_alpha2)
                    for i in data:
                        if y == 0:
                            output = opt_alpha2 * i + (1 - opt_alpha2) * i
                            y += 1
                        else:
                            output = opt_alpha2 * i + (1 - opt_alpha2) * output
    for alp in np.arange(0.1, 2, 0.1):
        alpha_counting(alp)
    return output
if __name__ == '__expsmooth__':
    xw.Book().set_mock_caller()
    expsmooth()