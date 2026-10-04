import distsim
from collections import defaultdict
def calculate_task_accuracies(word_to_vec_dict, test_file):
    task_accuracies = defaultdict(list)
    with open(test_file, "r") as file:
        category = None
        for line in file:
            line = line.strip()
            if line.startswith('
                continue
            if line.startswith(":"):
                category = line[2:]
            else:
                words = line.split()
                w1_vec = word_to_vec_dict[words[0]]
                w2_vec = word_to_vec_dict[words[1]]
                w4_vec = word_to_vec_dict[words[3]]
                result_vec = w1_vec - w2_vec + w4_vec
                result = distsim.show_nearest(
                    word_to_vec_dict,
                    result_vec,
                    {words[0], words[1], words[3]},
                    distsim.cossim_dense
                )
                match_position = next((i + 1 for i, (word, _) in enumerate(result) if word == words[2]), 0)
                task_accuracies[category].append(match_position)
    return task_accuracies
def display_accuracies(task_accuracies):
    for category, positions in task_accuracies.items():
        total = len(positions)
        top1 = sum(1 for pos in positions if pos == 1)
        top5 = sum(1 for pos in positions if pos <= 5)
        top10 = sum(1 for pos in positions if pos <= 10)
        top1_accuracy = round(top1 / total, 2)
        top5_accuracy = round(top5 / total, 2)
        top10_accuracy = round(top10 / total, 2)
        print(f"{category}:     {top1_accuracy}    {top5_accuracy}    {top10_accuracy}")
def main():
    word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
    test_file = "word-test.v3.txt"
    task_accuracies = calculate_task_accuracies(word_to_vec_dict, test_file)
    display_accuracies(task_accuracies)
if __name__ == "__main__":
    main()