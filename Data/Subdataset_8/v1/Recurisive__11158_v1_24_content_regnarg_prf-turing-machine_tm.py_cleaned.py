
def LIST(*args):
    return list(args)
def pair(x, y):
    return (x, y)
def list3(x, y, z):
    return [x, y, z]
TM_STAY = 0
TM_LEFT = 1
TM_RIGHT = 2
def tm_init_conf(tm, inp):
    pass
def tm_dump_conf(conf):
    pass
def tm_conf_is_final(tm, conf):
    pass
def tm_step(tm, conf):
    pass
def tm_exec(tm, inp):
    pass
if __name__ == '__main__':
    inp = LIST(1, 1, 2, 2, 1)
    conf = tm_init_conf(TM_PARITY, inp)
    tm_dump_conf(conf)
    while not tm_conf_is_final(TM_PARITY, conf):
        conf = tm_step(TM_PARITY, conf)
        tm_dump_conf(conf)
    tm_dump_conf(tm_exec(TM_PARITY, inp))