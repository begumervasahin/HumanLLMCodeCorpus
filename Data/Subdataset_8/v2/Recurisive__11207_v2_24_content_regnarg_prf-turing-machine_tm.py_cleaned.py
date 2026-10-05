
TM_STAY = 0
TM_LEFT = 1
TM_RIGHT = 2
def create_list(*args):
    return list(args)
def create_pair(x, y):
    return (x, y)
def create_list3(x, y, z):
    return [x, y, z]
def initialize_configuration(turing_machine, input_data):
    pass
def dump_configuration(configuration):
    pass
def is_final_configuration(turing_machine, configuration):
    pass
def perform_turing_step(turing_machine, configuration):
    pass
def execute_turing_machine(turing_machine, input_data):
    pass
if __name__ == '__main__':
    input_data = create_list(1, 1, 2, 2, 1)
    initial_configuration = initialize_configuration(TM_PARITY, input_data)
    dump_configuration(initial_configuration)
    while not is_final_configuration(TM_PARITY, initial_configuration):
        initial_configuration = perform_turing_step(TM_PARITY, initial_configuration)
        dump_configuration(initial_configuration)
    final_configuration = execute_turing_machine(TM_PARITY, input_data)
    dump_configuration(final_configuration)