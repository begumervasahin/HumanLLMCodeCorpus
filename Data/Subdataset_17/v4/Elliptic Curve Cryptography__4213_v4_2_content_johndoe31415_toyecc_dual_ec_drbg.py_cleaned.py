from toyecc import getcurvebyname, ECPrivateKey
def generate_points(curve, has_backdoor=True, d=987654321):
    P = ECPrivateKey.generate(curve).pubkey.point
    if has_backdoor:
        Q = d * P
        dinv = pow(d, -1, curve.n)
        print(f"Dual_EC_DBRG implementation is backdoored (d = {d}, d^{{-1}} = {dinv})")
        print("Backdoor prerequisite: Q = d P")
        return P, Q, dinv
    else:
        Q = ECPrivateKey.generate(curve).pubkey.point
        print("Dual_EC_DBRG implementation is not backdoored")
        return P, Q, None
def generate_initial_state(P, t_value=0x123456789):
    t = t_value
    print("Initial state:", hex(t))
    s = int((t * P).x)
    print("s            :", hex(s))
    t = int((s * P).x)
    sQ = s * Q
    r = int(sQ.x)
    return t, s, sQ, r
def recover_point(r, dinv, curve):
    A, B = curve.getpointwithx(r)
    return A * dinv, B * dinv
def main():
    curve = getcurvebyname("secp112r1")
    print("Selected curve:", curve)
    has_backdoor = True
    P, Q, dinv = generate_points(curve, has_backdoor)
    print(f"P: {P}")
    print(f"Q: {Q}")
    print()
    t, s, sQ, r = generate_initial_state(P)
    print(f"sQ           : {sQ}")
    print(f"New state    : {hex(t)}")
    print(f"Output       : {hex(r)}")
    if has_backdoor:
        print("\nRecovered point from r:")
        recovered_A, recovered_B = recover_point(r, dinv, curve)
        print(recovered_A)
        print(recovered_B)
if __name__ == "__main__":
    main()