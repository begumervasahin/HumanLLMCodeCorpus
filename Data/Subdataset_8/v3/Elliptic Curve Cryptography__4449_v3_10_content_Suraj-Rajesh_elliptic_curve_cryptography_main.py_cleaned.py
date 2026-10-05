from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def main():
    points = []
    orders = []
    top_k_points = []
    top_k_orders = []
    gf_103 = GaloisField(103)
    for a in range(gf_103.p):
        for b in range(gf_103.p):
            elliptic_curve = EllipticCurve(a, b, 103)
            order = elliptic_curve.order_of_curve()
            if is_prime(order):
                orders.append(order)
                points.append((a, b))
    for _ in range(10):
        maximum_order = max(orders)
        maximum_index = orders.index(maximum_order)
        top_k_orders.append(maximum_order)
        top_k_points.append(points[maximum_index])
        del orders[maximum_index]
        del points[maximum_index]
    for i in range(10):
        print("{} : {}".format(top_k_points[i], top_k_orders[i]))
if __name__ == "__main__":
    main()