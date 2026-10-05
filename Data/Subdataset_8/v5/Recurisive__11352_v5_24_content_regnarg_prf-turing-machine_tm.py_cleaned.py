
TM_STAY = 0
TM_LEFT = 1
TM_RIGHT = 2
TM_PARITY = [...]
def tm_dump_conf(conf):
    state, left_tape, right_tape = conf
    left_tape = list(reversed(left_tape))
    line1 = f'[{state}] {" ".join(map(str, left_tape))} > {" ".join(map(str, right_tape))}'
    print(line1)
def tm_conf_apply_action(conf, action):
    state, left_tape, right_tape = conf
    move = action[2]
    if move == TM_LEFT:
        left_tape, right_tape = left_tape[:-1], [left_tape[-1]] + right_tape
    elif move == TM_RIGHT:
        left_tape, right_tape = left_tape + [right_tape[0]], right_tape[1:]
    return (action[0], left_tape, right_tape)
def tm_step(tm_map, conf):
    state, _, _ = conf
    actions = tm_map[state]
    for action in actions:
        if action[0] == conf[0]:
            return tm_conf_apply_action(conf, action)
    return conf
def tm_execute(tm_map, initial_input):
    conf = (0, initial_input, [])
    while not tm_conf_is_final(tm_map, conf):
        conf = tm_step(tm_map, conf)
        tm_dump_conf(conf)
    return conf
def tm_conf_is_final(tm_map, conf):
    return conf[0] in tm_map[-1]
if __name__ == '__main__':
    initial_input = [1, 1, 2, 2, 1]
    conf = tm_execute(TM_PARITY, initial_input)
    tm_dump_conf(conf)