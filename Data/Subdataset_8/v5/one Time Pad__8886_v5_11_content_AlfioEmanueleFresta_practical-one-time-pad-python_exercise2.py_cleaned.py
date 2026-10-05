
from cp_otp import strxor, intercept_in, intercept_out
original_message = intercept_in()
modified_message = original_message
intercept_out(modified_message)