import numpy as np
from datetime import datetime
CONFIDENCE_THRESHOLD = 70
SUPPORT_THRESHOLD = 50
TEXT_FILE = 'associationruletestdata.txt'
number_of_records = 0
input_data_without_disease = []
disease_dict = {}
def get_confidence(rule, body):
    global number_of_records, CONFIDENCE_THRESHOLD
    numerator, denominator = 0.0, 0.0
    head_list = list(sorted(set(rule) - set(body)))
    for record in range(number_of_records):
        is_record_valid = check_record_validity(record, body, head_list)
        if is_record_valid:
            denominator += 1.0
            if is_rule_satisfied(record, head_list):
                numerator += 1.0
    if (numerator / denominator) * 100 >= CONFIDENCE_THRESHOLD:
        return True
    else:
        return False
def check_record_validity(record, body, head_list):
    global input_data_without_disease, disease_dict
    for element in body + head_list:
        parameter, up_down_disease = get_parameter_and_disease(element)
        if up_down_disease == "Up" and input_data_without_disease[record][parameter - 1] == 0:
            return False
        elif up_down_disease == "Down" and input_data_without_disease[record][parameter - 1] == 1:
            return False
        elif input_data_without_disease[record][parameter - 1] != disease_dict.get(up_down_disease):
            return False
    return True
def is_rule_satisfied(record, head_list):
    global input_data_without_disease, disease_dict
    for element in head_list:
        parameter, up_down_disease = get_parameter_and_disease(element)
        if up_down_disease == "Up" and input_data_without_disease[record][parameter - 1] == 0:
            return False
        elif up_down_disease == "Down" and input_data_without_disease[record][parameter - 1] == 1:
            return False
        elif input_data_without_disease[record][parameter - 1] != disease_dict.get(up_down_disease):
            return False
    return True
def get_parameter_and_disease(element):
    parameter = int(element[0:3])
    up_down_disease = element[4:]
    return parameter, up_down_disease
def check_if_infrequent_last_step(after_merge, length, unsupported_list_from_previous_iteration):
    for prev in unsupported_list_from_previous_iteration:
        common_list = list(set(after_merge).intersection(prev))
        if len(common_list) == (length - 1):
            return False
    return True
def apriori():
    global number_of_records, input_data_without_disease, disease_dict, SUPPORT_THRESHOLD, TEXT_FILE
    load_data(TEXT_FILE)
    final_list = generate_initial_list()
    answer = []
    length = 1
    while length <= len(final_list[0]):
        support_list_of_this_iteration, unsupported_list_of_this_iteration = find_support_and_unsupported(final_list)
        if not support_list_of_this_iteration:
            print(f"No Supported Combinations of length equal and greater than {length}")
            break
        print(f"Supported Combinations of size {length}: {len(support_list_of_this_iteration)}")
        answer.append(support_list_of_this_iteration)
        final_list, length = generate_next_iteration(support_list_of_this_iteration, unsupported_list_of_this_iteration)
        if not final_list:
            print(f"No Combinations of length and after {length}")
            break
    return answer
def load_data(file_path):
    global number_of_records, input_data_without_disease, disease_dict
    input_data_without_disease.clear()
    number_of_parameters_of_record = 0
    number_of_records = 0
    all_diseases = []
    with open(file_path, 'r') as f:
        for line in f:
            number_of_records += 1
            values = line.strip().split('\t')
            disease = values[-1]
            all_diseases.append(disease)
            values = values[:-1]
            number_of_parameters_of_record = len(values)
            for index, item in enumerate(values):
                if item == "Down":
                    values[index] = 0
                elif item == "Up":
                    values[index] = 1
            input_data_without_disease.append(values)
    input_data_without_disease = np.array(input_data_without_disease)
    diseases_set = sorted(set(all_diseases))
    disease_list = list(diseases_set)
    for name in disease_list:
        disease_dict[name] = disease_list.index(name)
    x0 = np.zeros((number_of_records, 1))
    input_data_without_disease = np.hstack((input_data_without_disease, x0))
    record_idx = 0
    for x in all_diseases:
        input_data_without_disease[record_idx][-1] = disease_dict[x]
        record_idx += 1
def generate_initial_list():
    global number_of_records
    final_list = []
    for i in range(number_of_records):
        num = '{num:03d}'.format(num=(i + 1))
        final_list.append([num + "_Down"])
        final_list.append([num + "_Up"])
    for x in disease_dict.keys():
        num = '{num:03d}'.format(num=(number_of_records + 1))
        final_list.append([num + "_" + str(x)])
    return sorted(final_list)
def find_support_and_unsupported(final_list):
    global number_of_records, SUPPORT_THRESHOLD
    support_list_of_this_iteration = []
    unsupported_list_of_this_iteration = []
    for current_list in final_list:
        count = 0
        for record in range(number_of_records):
            is_record_valid = check_record_validity_for_support(record, current_list)
            if is_record_valid:
                count += 1
                if count >= SUPPORT_THRESHOLD:
                    break
        if count < SUPPORT_THRESHOLD:
            unsupported_list_of_this_iteration.append(current_list)
        else:
            support_list_of_this_iteration.append(current_list)
    return support_list_of_this_iteration, unsupported_list_of_this_iteration
def check_record_validity_for_support(record, current_list):
    for element in current_list:
        parameter, up_down_disease = get_parameter_and_disease(element)
        if up_down_disease == "Up" and input_data_without_disease[record][parameter - 1] == 0:
            return False
        elif up_down_disease == "Down" and input_data_without_disease[record][parameter - 1] == 1:
            return False
        elif input_data_without_disease[record][parameter - 1] != disease_dict.get(up_down_disease):
            return False
    return True
def generate_next_iteration(support_list_of_this_iteration, unsupported_list_from_previous_iteration):
    final_list = []
    length = len(support_list_of_this_iteration[0]) + 1
    if length != 2:
        for element1_idx, element1 in enumerate(support_list_of_this_iteration):
            for element2_idx in range(element1_idx + 1, len(support_list_of_this_iteration)):
                element2 = support_list_of_this_iteration[element2_idx]
                if elements_can_merge(element1, element2, length):
                    after_merge = list(sorted(set(element1 + element2)))
                    if check_if_infrequent_last_step(after_merge, length, unsupported_list_from_previous_iteration):
                        final_list.append(after_merge)
    else:
        for element1_idx, element1 in enumerate(support_list_of_this_iteration):
            for element2_idx in range(element1_idx + 1, len(support_list_of_this_iteration)):
                element2 = support_list_of_this_iteration[element2_idx]
                final_list.append(element1 + element2)
    return final_list, length
def elements_can_merge(element1, element2, length):
    for i in range(length - 2):
        if element1[i] != element2[i]:
            return False
    return True
def start_execution():
    start_time = datetime.now()
    answer = apriori()
    return answer
if __name__ == "__main__":
    start_execution()