from cp_otp import intercept_in, intercept_out
def process_intercepted_data(data):
    return data
def main():
    intercepted_data = intercept_in()
    processed_data = process_intercepted_data(intercepted_data)
    intercept_out(processed_data)
if __name__ == "__main__":
    main()