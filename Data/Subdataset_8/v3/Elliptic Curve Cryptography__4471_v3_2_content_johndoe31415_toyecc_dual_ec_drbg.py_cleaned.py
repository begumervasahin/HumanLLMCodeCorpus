from toyecc import getcurvebyname, ECPrivateKey
def check_backdoor(curve, has_backdoor):
    if not has_backdoor:
        P = ECPrivateKey.generate(curve).pubkey.point
        Q = ECPrivateKey.generate(curve).pubkey.point
        print("Dual_EC_DBRG implementation is not backdoored")
    else:
        P = ECPrivateKey.generate(curve).pubkey.point
        d = 987654321
        Q = d * P
        dinv = pow(d, -1, curve.n)
        print("Dual_EC_DBRG implementation is backdoored (d = %d, d^{-1} = %d)" % (d, dinv))
        print("Backdoor prerequisite: Q = d P")
    return P, Q, dinv
def print_points(P, Q):
    print("P:", P)
    print("Q:", Q)
    print()
def perform_state_transformation(curve, P, Q, t):
    print("Initial state:", hex(t))
    s = int((t * P).x)
    print("s            :", hex(s))
    t = int((s * P).x)
    sQ = s * Q
    r = int(sQ.x)
    print("sQ           :", sQ)
    print("New state    :", hex(t))
    print("Output       :", hex(r))
    return r
def recover_point(curve, has_backdoor, r, dinv):
    if has_backdoor:
        print()
        print("Recovered point from r:")
        (A, B) = curve.getpointwithx(r)
        print(A * dinv)
        print(B * dinv)
curve = getcurvebyname("secp112r1")
print("Selected curve:", curve)
has_backdoor = True
P, Q, dinv = check_backdoor(curve, has_backdoor)
print_points(P, Q)
t = 0x123456789
r = perform_state_transformation(curve, P, Q, t)
recover_point(curve, has_backdoor, r, dinv)