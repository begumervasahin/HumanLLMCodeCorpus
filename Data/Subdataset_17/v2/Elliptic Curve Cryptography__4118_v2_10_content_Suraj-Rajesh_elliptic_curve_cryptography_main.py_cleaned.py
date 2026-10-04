from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def find_top_k_prime_orders(k=10, field_size=103):
    points_with_prime_orders = []
    gf = GaloisField(field_size)
    for a in range(gf.p):
        for b in range(gf.p):
            elliptic_curve = EllipticCurve(a, b, field_size)
            order = elliptic_curve.order_of_curve()
            if is_prime(order):
                points_with_prime_orders.append(((a, b), order))
    points_with_prime_orders.sort(key=lambda x: x[1], reverse=True)
    top_k_points_with_orders = points_with_prime_orders[:k]
    return top_k_points_with_orders
if __name__ == "__main__":
    top_k = 10
    field_size = 103
    top_k_prime_orders = find_top_k_prime_orders(top_k, field_size)
    for point, order in top_k_prime_orders:
        print(f"{point} : {order}")