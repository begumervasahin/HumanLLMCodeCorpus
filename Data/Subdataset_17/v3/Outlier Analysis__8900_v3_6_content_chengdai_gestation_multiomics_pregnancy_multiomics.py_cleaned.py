import pandas as pd
import numpy as np
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
from sklearn import decomposition, linear_model
from skbio import DistanceMatrix
from skbio.stats.distance import permanova
sns.set_style("white")
class PregnancyMultiomics:
    def __init__(self, folder):
        self.patients = pd.read_csv(f"{folder}/featurepatients.csv", squeeze=True)
        self.trimesters = pd.read_csv(f"{folder}/featuretimes.csv", squeeze=True)
        self.weeks = pd.read_csv(f"{folder}/featureweeks.csv", squeeze=True)
        self.featureindex = pd.read_csv(f"{folder}/featureindex.csv", squeeze=True)
        self.sample_ids = pd.Series(map('_'.join, zip(self.patients.astype(str), self.trimesters.astype(str))))
        omic_measures = [
            'CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex',
            'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic'
        ]
        self.omics = {omic: pd.read_csv(f"{folder}/{omic}.csv", index_col=0) for omic in omic_measures}
    def summarize_datasets(self):
        summary = {omic: data.shape for omic, data in self.omics.items()}
        return pd.DataFrame.from_dict(summary, orient='index', columns=['samples', 'features'])
    def subset_trimester(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: not a valid trimester, please input a value of 1 through 3')
            return None
        return self.sample_ids[self.trimesters == trimester].values
    def permanova(self):
        permanova_pval = {}
        distance_matrices = {}
        for omic, data in self.omics.items():
            omic_data = data.loc[self.sample_ids]
            distance_matrix = pd.DataFrame(
                squareform(pdist(omic_data.values, metric='euclidean')),
                index=omic_data.index, columns=omic_data.index
            )
            samples = distance_matrix.index.str.split('_').str[0]
            trimesters = distance_matrix.index.str.split('_').str[1]
            distance_matrix_skbio = DistanceMatrix(distance_matrix, ids=distance_matrix.index)
            trimester_p_val = permanova(distance_matrix_skbio, trimesters, permutations=999)['p-value']
            donor_p_val = permanova(distance_matrix_skbio, samples, permutations=999)['p-value']
            permanova_pval[omic] = {'pval_trimester': trimester_p_val, 'pval_donor': donor_p_val}
            distance_matrices[omic] = distance_matrix
        return pd.DataFrame.from_dict(permanova_pval, orient='index'), distance_matrices
    def within_between_comparisons(self, distance_matrix_dict=None, comparison='donor_comparison', out_png=None):
        def comparison_type(row, col1, col2):
            return 'within' if row[col1] == row[col2] else 'between'
        if distance_matrix_dict is None:
            _, distance_matrix_dict = self.permanova()
        fig, ax = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(ax[3, 1])
        counter = 0
        for omic, distance_matrix in distance_matrix_dict.items():
            subplot_ax = ax[counter
            dist_tidy = distance_matrix.reset_index().melt(id_vars='index')
            dist_tidy = dist_tidy[dist_tidy['index'] != dist_tidy['variable']]
            dist_tidy['donor1'] = dist_tidy['index'].str.split('_').str.get(0)
            dist_tidy['trimester1'] = dist_tidy['index'].str.split('_').str.get(1)
            dist_tidy['donor2'] = dist_tidy['variable'].str.split('_').str.get(0)
            dist_tidy['trimester2'] = dist_tidy['variable'].str.split('_').str.get(1)
            dist_tidy['donor_comparison'] = dist_tidy.apply(lambda x: comparison_type(x, 'donor1', 'donor2'), axis=1)
            dist_tidy['trimester_comparison'] = dist_tidy.apply(lambda x: comparison_type(x, 'trimester1', 'trimester2'), axis=1)
            sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax, showfliers=False)
            sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax)
            subplot_ax.set_title(omic)
            counter += 1
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
    def pca(self, modality, num_pcs=25):
        omic_data = self.omics.get(modality)
        if omic_data is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        omic_data = omic_data.loc[self.sample_ids]
        pca = decomposition.PCA(n_components=num_pcs)
        pc_matrix = pca.fit_transform(omic_data)
        return pc_matrix, omic_data
    def plot_pca(self, modality, out_png=None):
        pca_results, omic_data = self.pca(modality)
        pca_df = pd.DataFrame(pca_results, index=omic_data.index)
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 5))
        trimesters = self.trimesters.unique()
        trimester_colors = dict(zip(trimesters, sns.color_palette('Set1', len(trimesters))))
        for period in trimesters:
            donor_sample_indices = self.trimesters[self.trimesters == period].index
            temp = pca_df.iloc[donor_sample_indices]
            ax1.scatter(temp[0], temp[1], label=f'trimester {period}', color=trimester_colors[period])
        sns.despine()
        ax1.legend(bbox_to_anchor=[1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        patient_ids = self.patients.unique()
        donor_colors = dict(zip(patient_ids, sns.color_palette('tab20', len(patient_ids))))
        for donor in patient_ids:
            donor_sample_indices = self.patients[self.patients == donor].index
            temp = pca_df.iloc[donor_sample_indices]
            ax2.scatter(temp[0], temp[1], label=donor, color=donor_colors[donor])
        sns.despine()
        ax2.legend(bbox_to_anchor=[1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
    def elastic_net_regression(self, modality, input_ax=None, out_png=None):
        omic_data = self.omics.get(modality)
        if omic_data is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        valid_omic_samples = omic_data.loc[self.sample_ids]
        valid_weeks = self.weeks.loc[self.featureindex.index]
        valid_omic_samples = valid_omic_samples.loc[:, valid_omic_samples.std() != 0].apply(scipy.stats.zscore)
        train_test_loo = [(self.patients != patient).index.values for patient in self.patients.unique()]
        en_reg_cv = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        predicted = []
        actual = []
        for train_index, test_index in train_test_loo:
            en_reg_cv.fit(valid_omic_samples.iloc[train_index], valid_weeks[train_index])
            predicted.extend(en_reg_cv.predict(valid_omic_samples.iloc[test_index]))
            actual.extend(valid_weeks[test_index])
        if input_ax is None:
            input_ax = plt.subplot()
            plot = True
        else:
            plot = False
        sns.regplot(actual, predicted, ax=input_ax)
        r, pval = scipy.stats.pearsonr(actual, predicted)
        input_ax.set_title(f"{modality} | R$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(pval):.2f}")
        if plot:
            if out_png:
                plt.savefig(out_png, bbox_inches="tight")
            else:
                plt.show()
            plt.close()
        return r**2, pval, en_reg_cv
    def elastic_net_r_squares(self, out_png=None):
        r_sqs = {}
        fig, ax = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(ax[3, 1])
        counter = 0
        for omic in self.omics.keys():
            subplot_ax = ax[counter
            r_sq, p_val, en_reg_cv = self.elastic_net_regression(omic, subplot_ax)
            r_sqs[omic] = {'r_squared': r_sq, 'p-value': p_val}
            counter += 1
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
        return pd.DataFrame.from_dict(r_sqs, orient='index')
    def cross_omic_elastic_net(self, select_features=None, out_png=None):
        all_omics = pd.concat([data.loc[self.sample_ids].T for data in self.omics.values()]).T
        if select_features is not None:
            all_omics = all_omics[select_features]
        all_omics = all_omics.loc[:, all_omics.std() > 0].apply(scipy.stats.zscore)
        valid_weeks = self.weeks.loc[self.featureindex.index]
        train_test_loo = [(self.patients != patient).index.values for patient in self.patients.unique()]
        en_cv = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        predicted = []
        actual = []
        for train_index, test_index in train_test_loo:
            en_cv.fit(all_omics.iloc[train_index], valid_weeks[train_index])
            predicted.extend(en_cv.predict(all_omics.iloc[test_index]))
            actual.extend(valid_weeks[test_index])
        sns.regplot(actual, predicted)
        r, pval = scipy.stats.pearsonr(actual, predicted)
        plt.title(f"r$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(pval):.2f}")
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
        return r**2, pval, en_cv
if __name__ == "__main__":
    folder = "path_to_your_data"
    gestation_multiomics = PregnancyMultiomics(folder)
    print(gestation_multiomics.summarize_datasets())
    permanova_df, dist_matrix_dict = gestation_multiomics.permanova()
    print(permanova_df)
    gestation_multiomics.within_between_comparisons(distance_matrix_dict=dist_matrix_dict, out_png='./Figures/within_between_donor_comparisons.png')
    for omic in gestation_multiomics.omics.keys():
        gestation_multiomics.plot_pca(omic, out_png=f'./Figures/{omic}_pca.png')
    r2_table = gestation_multiomics.elastic_net_r_squares(out_png='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, pval, coeffs = gestation_multiomics.cross_omic_elastic_net(select_features=r2_table.index, out_png='./Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, coeffs_all_omics = gestation_multiomics.cross_omic_elastic_net(out_png='./Figures/elastic_net_all_omics_predictions.png')