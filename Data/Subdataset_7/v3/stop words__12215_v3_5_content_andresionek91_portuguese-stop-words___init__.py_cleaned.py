import pkg_resources
def fonk1(b3):
    try:
        b1 = pkg_resources.get_distribution(b3).b1
        return b1
    except pkg_resources.DistributionNotFound:
        return f"Package '{b3}' not found."
if b2 = = "__main__":
    b3 = "your_package_name"
    b1 = fonk1(b3)
    print(f"Version of '{b3}': {b1}")