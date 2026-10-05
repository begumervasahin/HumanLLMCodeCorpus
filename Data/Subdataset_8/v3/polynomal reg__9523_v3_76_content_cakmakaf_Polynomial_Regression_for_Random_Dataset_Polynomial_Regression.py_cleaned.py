import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
page_speeds = np.random.normal(3.0, 1.0, 100)
purchase_amount = np.random.normal(50.0, 30.0, 100) / page_speeds
plt.scatter(page_speeds, purchase_amount)
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Relationship between Page Speeds and Purchase Amount')
plt.show()
train_x, test_x = page_speeds[:80], page_speeds[80:]
train_y, test_y = purchase_amount[:80], purchase_amount[80:]
plt.scatter(train_x, train_y, label='Training Data')
plt.scatter(test_x, test_y, label='Testing Data')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Training and Testing Data Split')
plt.legend()
plt.show()
poly_fit = np.poly1d(np.polyfit(train_x, train_y, 7))
x_values = np.linspace(0, 7, 100)
plt.scatter(train_x, train_y, label='Training Data')
plt.plot(x_values, poly_fit(x_values), c='b', label='Fitted Model')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Fitted Polynomial Regression Model')
plt.legend()
plt.show()
r2_test = r2_score(test_y, poly_fit(test_x))
print("R-squared score for testing data:", r2_test)
r2_train = r2_score(train_y, poly_fit(train_x))
print("R-squared score for training data:", r2_train)