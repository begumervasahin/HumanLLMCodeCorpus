import numpy as np
from sklearn.model_selection import train_test_split
from CreateBaseFromFile import CreateBaseFromFile
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from classificadores import classicarKNN, naiveBayes, arvoreDecisao, dlFisher
from Grafico import GerarGrafico
def perform_classification(base, hold, classifier_functions):
    errors = [0] * len(classifier_functions)
    for i in range(hold):
        train_atr, test_atr, train_classes, test_classes = train_test_split(
            base.atributos, base.classes, test_size=0.5, random_state=i)
        for idx, classifier in enumerate(classifier_functions):
            errors[idx] += classifier(train_atr, train_classes, test_atr, test_classes)
    return [1 - err / hold for err in errors]
def perform_pca_classification(base, hold, pca_obj, classifier_functions, attributes_range):
    accuracies = []
    for num_attributes in attributes_range:
        errors = [0] * len(classifier_functions)
        for i in range(hold):
            pca = pca_obj()
            train_atr, test_atr, train_classes, test_classes = train_test_split(
                base.atributos, base.classes, test_size=0.5, random_state=i)
            b = Base(train_classes, train_atr)
            pca.fit(b)
            base_train_pca = pca.run(Base(train_classes, train_atr), num_attributes)
            base_test_pca = pca.run(Base(test_classes, test_atr), num_attributes)
            for idx, classifier in enumerate(classifier_functions):
                errors[idx] += classifier(base_train_pca.atributos, base_train_pca.classes,
                                           base_test_pca.atributos, base_test_pca.classes)
        accuracies.append([1 - err / hold for err in errors])
    return accuracies
def main():
    hold = 100
    base_climate = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    base_bank = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    classifiers = [classicarKNN, naiveBayes, arvoreDecisao, dlFisher]
    print("WITHOUT PCA - Climate Dataset:")
    climate_results = perform_classification(base_climate, hold, classifiers)
    for idx, classifier in enumerate(classifiers):
        print(f"{classifier.__name__} Accuracy:", climate_results[idx])
    print()
    print("WITHOUT PCA - BankNote Dataset:")
    bank_results = perform_classification(base_bank, hold, classifiers)
    for idx, classifier in enumerate(classifiers):
        print(f"{classifier.__name__} Accuracy:", bank_results[idx])
    print()
    pca_obj = PCAR
    pca_results_climate = perform_pca_classification(base_climate, hold, pca_obj, classifiers, range(1, 19))
    pca_results_bank = perform_pca_classification(base_bank, hold, pca_obj, classifiers, range(1, 5))
    pca_obj_score = PCARS
    pca_results_climate_score = perform_pca_classification(base_climate, hold, pca_obj_score, classifiers, range(1, 19))
    pca_results_bank_score = perform_pca_classification(base_bank, hold, pca_obj_score, classifiers, range(1, 5))
    extraido = list(range(1, 19))
    GerarGrafico.saveMultuplos(extraido, pca_results_climate, "Accuracy with PCAs - Climate Dataset",
                               "Number of attributes", "Accuracy", [c.__name__ for c in classifiers])
    extraido = list(range(1, 5))
    GerarGrafico.saveMultuplos(extraido, pca_results_bank, "Accuracy with PCAs - Bank Dataset",
                               "Number of attributes", "Accuracy", [c.__name__ for c in classifiers])
if __name__ == '__main__':
    main()