import math
def print_header(header_text):
    print("\n" + header_text)
    print("----------------------------------------")
def prompt_user(message):
    return float(input(message))
def calculate_predicted_mean(At, Bt, ut_, ut):
    return At * ut_ + Bt * ut
def calculate_predicted_covariance(At, Et_, Att, Qt):
    return At * Et_ * Att + Qt
def update_mean(pMean, pCo, kGain, zt, Ct):
    return pMean + kGain * (zt - Ct * pMean)
def update_covariance(pCo, kGain, Ct):
    return pCo - kGain * Ct * pCo
def kalman_filter():
    print_header("Prediction Steps")
    At = prompt_user("A: ")
    Bt = prompt_user("B: ")
    ut_ = prompt_user("Enter Prior Mean: ")
    ut = prompt_user("Enter Current Mean: ")
    pMean = calculate_predicted_mean(At, Bt, ut_, ut)
    print("Predicted Mean: ", pMean)
    Et_ = prompt_user("\nE(t-1): ")
    Att = prompt_user("A(T/t): ")
    Qt = prompt_user("Q(t): ")
    pCo = calculate_predicted_covariance(At, Et_, Att, Qt)
    print("Predicted Convariance: ", pCo)
    while True:
        print_header("Update Steps")
        Ctt = prompt_user("C(T/t): ")
        Ct = prompt_user("C/(t): ")
        Rt = prompt_user("Measurement Covariance: ")
        kGain = pCo * Ctt * math.pow((Ct * pCo * Ctt + Rt), (-1))
        print("Kalman Gain: ", kGain)
        zt = prompt_user("\nActual Measurement: ")
        uMean = update_mean(pMean, pCo, kGain, zt, Ct)
        print("Updated Mean: ", uMean)
        uCo = update_covariance(pCo, kGain, Ct)
        print("\nUpdated Covariance: ", uCo)
        print_header("Prediction Steps")
        At = prompt_user("A: ")
        Bt = prompt_user("B: ")
        ut = prompt_user("Enter Current Mean: ")
        pMean = calculate_predicted_mean(At, Bt, uMean, ut)
        print("Predicted Mean: ", pMean)
        Att = prompt_user("\nA(T/t): ")
        Qt = prompt_user("Q(t): ")
        pCo = calculate_predicted_covariance(At, uCo, Att, Qt)
        print("Predicted Convariance: ", pCo)
kalman_filter()