from prf import *
from pairs import *
from lists import *
from dicts import *
TM_STAY = 0
TM_LEFT = 1
TM_RIGHT = 2
TM_PARITY = LIST(
    0,
    LIST(2, 3),
    LIST(
        pair(pair(0, 1), LIST(1, 1, TM_RIGHT)),
        pair(pair(0, 2), LIST(0, 2, TM_RIGHT)),
        pair(pair(1, 1), LIST(0, 1, TM_RIGHT)),
        pair(pair(1, 2), LIST(1, 2, TM_RIGHT)),
        pair(pair(0, 0), LIST(2, 0, TM_STAY)),
        pair(pair(1, 0), LIST(3, 0, TM_STAY)),
    ),
)
tm_init_conf = C(
    list3,
    C(Getter(0), Proj(2, 0)),
    Zero(2),
    Proj(2, 1)
)
def tm_dump_conf(conf):
    state, left_tape, right_tape = UNLIST(conf)
    left_tape = UNLIST(left_tape)
    right_tape = UNLIST(right_tape)
    line1 = f'[{state}] {" ".join(reversed(list(map(str, left_tape))))} > {" ".join(map(str, right_tape))}'
    print(line1)
tm_conf_disp = C(pair, Getter(0), C(head, Getter(2)))
tm_conf_action = C(lookup, C(Getter(2), Proj(2, 0)), C(tm_conf_disp, Proj(2, 1)))
tm_conf_move_left = C(list3, Getter(0), C(tail, Getter(1)), C(cons, C(head, Getter(1)), Getter(2)))
tm_conf_move_right = C(list3, Getter(0), C(cons, C(head, Getter(2)), Getter(1)), C(tail, Getter(2)))
tm_conf_move = C(
    cond,
    C(eq, Proj(2, 1), Constant(TM_LEFT, 2)),
    C(tm_conf_move_left, Proj(2, 0)),
    C(cond,
        C(eq, Proj(2, 1), Constant(TM_RIGHT, 2)),
        C(tm_conf_move_right, Proj(2, 0)),
        Proj(2, 0),
    )
)
tm_conf_write = C(list3,
    C(Getter(0), Proj(2, 0)),
    C(Getter(1), Proj(2, 0)),
    C(cons, Proj(2, 1), C(tail, C(Getter(2), Proj(2, 0))))
)
tm_conf_set_state = C(list3, Proj(2, 1), C(Getter(1), Proj(2, 0)), C(Getter(2), Proj(2, 0)))
tm_conf_apply_action = C(tm_conf_move,
    C(tm_conf_write,
        C(tm_conf_set_state,
            Proj(2, 0),
            C(Getter(0), Proj(2, 1))
        ),
        C(Getter(1), Proj(2, 1))
    ),
    C(Getter(2), Proj(2, 1))
)
tm_step_force = C(tm_conf_apply_action,
    Proj(2, 1),
    tm_conf_action
)
tm_state_is_final = C(contains, C(Getter(1), Proj(2, 0)), Proj(2, 1))
tm_conf_is_final = C(tm_state_is_final, Proj(2, 0), C(Getter(0), Proj(2, 1)))
tm_step = C(cond,
    tm_conf_is_final,
    Proj(2, 1),
    tm_step_force
)
tm_steps_r = PR(Proj(2, 1), C(tm_step, Proj(4, 2), Proj(4, 0)))
tm_steps = C(tm_steps_r, Proj(3, 2), Proj(3, 0), Proj(3, 1))
tm_conf_steps_to_finish = Minimize(C(not_, C(tm_conf_is_final, Proj(3, 1), C(tm_steps, Proj(3, 1), Proj(3, 2), Proj(3, 0)))))
tm_conf_finish = C(tm_steps, Proj(2, 0), Proj(2, 1), tm_conf_steps_to_finish)
tm_exec = C(tm_conf_finish, Proj(2, 0), tm_init_conf)
if __name__ == '__main__':
    inp = LIST(1, 1, 2, 2, 1)
    conf = tm_init_conf(TM_PARITY, inp)
    tm_dump_conf(conf)
    while not tm_conf_is_final(TM_PARITY, conf):
        conf = tm_step(TM_PARITY, conf)
        tm_dump_conf(conf)
    tm_dump_conf(tm_exec(TM_PARITY, inp))