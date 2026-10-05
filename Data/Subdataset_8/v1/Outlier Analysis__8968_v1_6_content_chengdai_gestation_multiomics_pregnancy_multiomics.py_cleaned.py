import pandas as pd
import numpy as np
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
from sklearn import decomposition, linear_model
from sklearn.model_selection import cross_val_score
from skbio.stats.distance import permanova
from scipy.stats import pearsonr
class PregnancyMultiomics():
    def __init__(self, folder):
        self.patients = pd.read_csv(folder + '/featurepatients.csv', squeeze=True)
        self.trimesters = pd.read_csv(folder + '/featuretimes.csv', squeeze=True)
        self.weeks = pd.read_csv(folder + '/featureweeks.csv', squeeze=True)
        self.featureindex = pd.read_csv(folder + '/featureindex.csv', squeeze=True)
        self.sample_ids = pd.Series(map('_'.join, zip(self.patients.astype(str), self.trimesters.astype(str))))
        omic_measures = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.omics = {omic: pd.read_csv(folder + '/' + omic + '.csv', index_col=0) for omic in omic_measures}
    def summarize_datasets(self):
        summary = {}
        for omic, data in self.omics.items():
            summary[omic] = [data.shape[0], data.shape[1]]
        summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['samples', 'features'])
        return summary_df
    def subset_trimester(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: not a valid trimester, please input a value of 1 through 3')
            return None
        else:
            return self.sample_ids[self.trimesters == trimester].values
    def permanova(self):
        permanova_pval = {}
        distance_matrices = {}
        for omic, data in self.omics.items():
            omic_data = data.loc[self.sample_ids, :]
            distance_matrix = squareform(pdist(omic_data.values, metric='euclidean'))
            distance_matrix = pd.DataFrame(distance_matrix)
            distance_matrix.index = omic_data.index
            distance_matrix.columns = omic_data.index
            samples = distance_matrix.index.str.split('_').str[0]
            trimesters = distance_matrix.index.str.split('_').str[1]
            pval_trimester = permanova(distance_matrix, grouping=trimesters)['p-value']
            pval_donor = permanova(distance_matrix, grouping=samples)['p-value']
            permanova_pval[omic] = {'pval_trimester': pval_trimester, 'pval_donor': pval_donor}
            distance_matrices[omic] = distance_matrix
        permanova_df = pd.DataFrame.from_dict(permanova_pval, orient='index')
        return permanova_df, distance_matrices
    def within_between_comparisons(self, distance_matrix_dict=None, comparison='donor_comparison', out_png=None):
        if distance_matrix_dict is None:
            pvals, distance_matrix_dict = self.permanova()
        fig, ax = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(ax[3, 1])
        counter = 0
        for omic, distance_matrix in distance_matrix_dict.items():
            subplot_ax = ax[counter
            counter += 1
            dist_tidy = distance_matrix.reset_index().melt(id_vars='index')
            dist_tidy = dist_tidy[dist_tidy['index'] != dist_tidy['variable']]
            dist_tidy['donor1'] = dist_tidy['index'].str.split('_').str.get(0)
            dist_tidy['trimester1'] = dist_tidy['index'].str.split('_').str.get(1)
            dist_tidy['donor2'] = dist_tidy['variable'].str.split('_').str.get(0)
            dist_tidy['trimester2'] = dist_tidy['variable'].str.split('_').str.get(1)
            num_potential_duplicates = (dist_tidy['value'] == 0).sum()
            dist_tidy['donor_comparison'] = dist_tidy.apply(lambda x: 'within' if x['donor1'] == x['donor2'] else 'between', axis=1)
            dist_tidy['trimester_comparison'] = dist_tidy.apply(lambda x: 'within' if x['trimester1'] == x['trimester2'] else 'between', axis=1)
            subplot_ax = sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax, showfliers=False)
            subplot_ax = sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax)
            subplot_ax.set_title(f'{omic} | Potential duplicates: {num_potential_duplicates}')
        if out_png is not None:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
    def pca(self, modality, num_pcs=25):
        omic_data = self.omics.get(modality, None)
        if omic_data is None:
            print(f'ERROR: not a valid -omic type, please input either: {" ".join(self.omics.keys())}')
            return None, None
        omic_data = omic_data.loc[self.sample_ids]
        valid_patients = self.patients[self.featureindex.index]
        pca = decomposition.PCA(n_components=num_pcs)
        pc_matrix = pca.fit_transform(omic_data)
        return pc_matrix, omic_data
    def plot_pca(self, modality, out_png=None):
        pca_results, omic_data = self.pca(modality)
        valid_patients = self.patients[self.featureindex.index]
        pca_df = pd.DataFrame(pca_results)
        pca_df.index = omic_data.index
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 5))
        trimesters = self.trimesters.unique()
        trimester_colors = dict(zip(trimesters, sns.color_palette('Set1', len(trimesters))))
        for period in trimesters:
            donor_sample_indices = self.trimesters[self.trimesters == period].index
            temp = pca_df.iloc[donor_sample_indices, :]
            ax1.scatter(temp.loc[:, 0], temp.loc[:, 1], label='trimester {0}'.format(period), color=trimester_colors[period])
        ax1.legend(bbox_to_anchor=[1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title('PCA of {0} by trimester'.format(modality))
        patient_ids = valid_patients.unique()
        donor_colors = dict(zip(patient_ids, sns.color_palette('tab20', len(patient_ids))))
        for donor in patient_ids:
            donor_sample_indices = valid_patients[valid_patients == donor].index
            temp = pca_df.iloc[donor_sample_indices, :]
            ax2.scatter(temp.loc[:, 0], temp.loc[:, 1], label=donor, color=donor_colors[donor])
        ax2.legend(bbox_to_anchor=[1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title('PCA of {0} by individual donor')
        if out_png is not None:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
    def elastic_net_regression(self, modality):
        omic_data = self.omics.get(modality, None)
        if omic_data is None:
            print(f'ERROR: not a valid -omic type, please input either: {" ".join(self.omics.keys())}')
            return None, None, None, None, None
        valid_omic_samples = omic_data.loc[self.sample_ids, :]
        valid_weeks = self.weeks.loc[self.featureindex.index]
        valid_patient_indices = self.patients.loc[self.featureindex.index]
        patients = self.patients.unique()
        valid_omic_samples = valid_omic_samples.loc[:, valid_omic_samples.std() != 0]
        valid_omic_samples = valid_omic_samples.apply(lambda x: scipy.stats.zscore(x))
        train_test_loo = []
        for patient in patients:
            training_samples = valid_patient_indices[valid_patient_indices != patient].index.values
            test_samples = valid_patient_indices[valid_patient_indices == patient].index.values
            train_test_loo.append((training_samples, test_samples))
        predicted = []
        actual = []
        cv_l1_ratios = []
        cv_alphas = []
        coeffs = []
        en_reg_cv = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                              cv=5, max_iter=1000, n_jobs=8)
        for (train, test) in train_test_loo:
            en_reg_cv.fit(valid_omic_samples.values[train], valid_weeks.values[train])
            cv_l1_ratios.append(en_reg_cv.l1_ratio_)
            cv_alphas.append(en_reg_cv.alpha_)
            predicted.extend(en_reg_cv.predict(valid_omic_samples.values[test]))
            actual.extend(valid_weeks.values[test])
            coeffs.append(en_reg_cv.coef_)
        r_sq, pval = pearsonr(actual, predicted)
        coeffs = pd.DataFrame(coeffs)
        coeffs.columns = valid_omic_samples.columns
        return r_sq**2, pval, cv_l1_ratios, cv_alphas, coeffs
    def elastic_net_r_squares(self):
        r_sqs = {}
        top_features = []
        for omic in self.omics.keys():
            r_sq, p_val, l1_ratio_list, alpha_list, coeffs_df = self.elastic_net_regression(omic)
            features_used = coeffs_df.loc[:, coeffs_df.mean() > 0].columns
            r_sqs[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(features_used)}
            top_features.extend(features_used)
        r_sq_table = pd.DataFrame.from_dict(r_sqs, orient='index')
        return r_sq_table, top_features
    def cross_omic_elastic_net(self, select_features=None):
        all_omics = [data.loc[self.sample_ids, :].T for data in self.omics.values()]
        all_omics = pd.concat(all_omics).T
        if select_features is not None:
            all_omics = all_omics.loc[:, select_features]
        all_omics = all_omics.loc[:, all_omics.std() > 0]
        all_omics = all_omics.apply(lambda x: scipy.stats.zscore(x))
        valid_weeks = self.weeks.loc[self.featureindex.index]
        valid_patient_indices = self.patients.loc[self.featureindex.index]
        patients = self.patients.unique()
        train_test_loo = []
        for patient in patients:
            training_samples = valid_patient_indices[valid_patient_indices != patient].index.values
            test_samples = valid_patient_indices[valid_patient_indices == patient].index.values
            train_test_loo.append((training_samples, test_samples))
        predicted = []
        actual = []
        coeffs = []
        en_cv = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                          cv=5, max_iter=1000, n_jobs=8)
        for (train_index, test_index) in train_test_loo:
            en_cv.fit(all_omics.iloc[train_index, :], valid_weeks[train_index])
            predicted.extend(en_cv.predict(all_omics.iloc[test_index, :]))
            actual.extend(valid_weeks[test_index])
            coeffs.append(en_cv.coef_)
        r_sq, pval = pearsonr(actual, predicted)
        coeffs = pd.DataFrame(coeffs)
        coeffs.columns = all_omics.columns
        return r_sq**2, pval, coeffs
if __name__ == "__main__":
    folder_path = "your_folder_path_here"
    gestation_multiomics = PregnancyMultiomics(folder_path)
    print(gestation_multiomics.summarize_datasets())
    permanova_df, dist_matrix_dict = gestation_multiomics.permanova()
    print(permanova_df)
    gestation_multiomics.within_between_comparisons(distance_matrix_dict=dist_matrix_dict,
                                                    out_png='./Figures/within_between_donor_comparisons.png')
    for omic in gestation_multiomics.omics.keys():
        gestation_multiomics.plot_pca(omic, out_png=f'./Figures/{omic}_pca.png')
    r2_table, top_omic_features = gestation_multiomics.elastic_net_r_squares(
        out_png='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, pval, coeffs = gestation_multiomics.cross_omic_elastic_net(select_features=top_omic_features,
                                                                   out_png='./Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, coeffs_all_omics = gestation_multiomics.cross_omic_elastic_net(
        out_png='./Figures/elastic_net_all_omics_predictions.png')