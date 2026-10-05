
def project_along(b, v, eps=1E-20):
    sigma = ((b * v) / (v * v)) if v * v > eps else 0
    return sigma * v
def project_orthogonal(b, vlist):
    for v in vlist:
        b = b - project_along(b, v)
    return b
def aug_project_orthogonal(b, vlist, eps=1E-20):
    alphadict = {len(vlist): 1}
    for i, v in enumerate(vlist):
        sigma = (b * v) / (v * v) if v * v > eps else 0
        alphadict[i] = sigma
        b = b - sigma * v
    return (b, alphadict)
def orthogonalize(vlist):
    assert isinstance(vlist, list)
    vstarlist = []
    for v in vlist:
        vstarlist.append(project_orthogonal(v, vstarlist))
    return vstarlist
def aug_orthogonalize(vlist):
    assert isinstance(vlist, list)
    vstarlist = []
    sigma_vecs = []
    D = set(range(len(vlist)))
    for v in vlist:
        (vstar, sigmadict) = aug_project_orthogonal(v, vstarlist)
        vstarlist.append(vstar)
        sigma_vecs.append(Vec(D, sigmadict))
    return vstarlist, sigma_vecs