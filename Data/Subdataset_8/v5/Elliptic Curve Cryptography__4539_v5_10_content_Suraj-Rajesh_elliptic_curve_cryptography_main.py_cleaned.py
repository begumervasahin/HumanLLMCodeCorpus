from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def find_top_k_points(elliptic_curve, k=10):
    points = []
    orders = []
    for a in range(elliptic_curve.field.p):
        for b in range(elliptic_curve.field.p):
            order = elliptic_curve.order_of_curve(a, b)
            if is_prime(order):
                orders.append(order)
                points.append((a, b))
    top_k_points = []
    top_k_orders = []
    for _ in range(k):
        maximum = max(orders)
        maximum_index = orders.index(maximum)
        top_k_orders.append(maximum)
        top_k_points.append(points[maximum_index])
        del orders[maximum_index]
        del points[maximum_index]
    return top_k_points, top_k_orders
def main():
    gf_103 = GaloisField(103)
    elliptic_curve = EllipticCurve(gf_103)
    top_k_points, top_k_orders = find_top_k_points(elliptic_curve)
    for i in range(10):
        print("{} : {}".format(top_k_points[i], top_k_orders[i]))
if __name__ == "__main__":
    main()