from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def find_top_k_prime_orders(k=10, field_size=103):
    points = []
    orders = []
    top_k_points = []
    top_k_orders = []
    gf = GaloisField(field_size)
    for a in range(gf.p):
        for b in range(gf.p):
            elliptic_curve = EllipticCurve(a, b, field_size)
            order = elliptic_curve.order_of_curve()
            if is_prime(order):
                orders.append(order)
                points.append((a, b))
    for _ in range(k):
        if not orders:
            break
        maximum = max(orders)
        max_index = orders.index(maximum)
        top_k_orders.append(maximum)
        top_k_points.append(points[max_index])
        del orders[max_index]
        del points[max_index]
    return list(zip(top_k_points, top_k_orders))
if __name__ == "__main__":
    top_k = 10
    field_size = 103
    top_k_prime_orders = find_top_k_prime_orders(top_k, field_size)
    for point, order in top_k_prime_orders:
        print(f"{point} : {order}")