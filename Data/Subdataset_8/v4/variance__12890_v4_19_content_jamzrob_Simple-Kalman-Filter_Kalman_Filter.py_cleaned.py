import math
def main():
    print("\nPrediction Steps")
    print("----------------------------------------")
    A_t = float(input("A: "))
    B_t = float(input("B: "))
    u_t_prior = float(input("Enter Prior Mean: "))
    u_t = float(input("Enter Current Mean: "))
    predicted_mean = A_t * u_t_prior + B_t * u_t
    print("Predicted Mean: ", predicted_mean)
    E_t_prior = float(input("\nE(t-1): "))
    A_T_t = float(input("A(T/t): "))
    Q_t = float(input("Q(t): "))
    predicted_covariance = A_t * E_t_prior * A_T_t + Q_t
    print("Predicted Covariance: ", predicted_covariance)
    while True:
        print("\nUpdate Steps")
        print("----------------------------------------")
        C_T_t = float(input("C(T/t): "))
        C_t = float(input("C/(t): "))
        R_t = float(input("Measurement Covariance: "))
        kalman_gain = predicted_covariance * C_T_t * math.pow((C_t * predicted_covariance * C_T_t + R_t), (-1))
        print("Kalman Gain: ", kalman_gain)
        z_t = float(input("\nActual Measurement: "))
        updated_mean = predicted_mean + kalman_gain * (z_t - C_t * predicted_mean)
        print("Updated Mean: ", updated_mean)
        updated_covariance = predicted_covariance - kalman_gain * C_t * predicted_covariance
        print("\nUpdated Covariance: ", updated_covariance)
        print("\nPrediction Steps")
        print("----------------------------------------")
        A_t = float(input("A: "))
        B_t = float(input("B: "))
        u_t = float(input("Enter Current Mean: "))
        predicted_mean = A_t * updated_mean + B_t * u_t
        print("Predicted Mean: ", predicted_mean)
        A_T_t = float(input("\nA(T/t): "))
        Q_t = float(input("Q(t): "))
        predicted_covariance = A_t * updated_covariance * A_T_t + Q_t
        print("Predicted Covariance: ", predicted_covariance)
if __name__ == "__main__":
    main()