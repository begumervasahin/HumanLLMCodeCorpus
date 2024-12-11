import pkg_resources
def fonk1(b3):
    try:
        b1 = pkg_resources.get_distribution(b3).b1
        return b1
    except pkg_resources.DistributionNotFound:
        return "Package '{}' not found.".format(b3)
if b2 = = "__main__":
    b3 = "your_package_name"
    b1 = fonk1(b3)
    print("Version of '{}': {}".format(b3, b1))