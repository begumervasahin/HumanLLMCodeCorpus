from cp_otp import strxor, intercept_in, intercept_out
def main():
    intercepted_data = intercept_in()
    processed_data = intercepted_data
    intercept_out(processed_data)
if __name__ == "__main__":
    main()