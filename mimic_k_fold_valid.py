integers = list(range(1, 101))

k = 5

def k_fold_split(data, k):
    split_size = len(data) // k
    starting_index = 0
    folds = []

    for fold in range(k):
        end_index = starting_index + split_size
        validation_set = data[starting_index:end_index]
        training_set = data[:starting_index] + data[end_index:]
        folds.append((training_set, validation_set))
        starting_index = end_index
    return folds


print(k_fold_split(integers, 5))




