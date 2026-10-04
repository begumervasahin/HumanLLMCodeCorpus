import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.spatial.distance import squareform, pdist
from sklearn import decomposition, linear_model
sns.set_style("white")
class PregnancyMultiomics:
    def __init__(self, folder):
        self.patients = pd.read_csv(f'{folder}/featurepatients.csv', squeeze=True)
        self.trimesters = pd.read_csv(f'{folder}/featuretimes.csv', squeeze=True)
        self.weeks = pd.read_csv(f'{folder}/featureweeks.csv', squeeze=True)
        self.featureindex = pd.read_csv(f'{folder}/featureindex.csv', squeeze=True)
        self.sample_ids = pd.Series(map('_'.join, zip(self.patients.astype(str), self.trimesters.astype(str))))
        omic_measures = [
            'CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex',
            'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic'
        ]
        self.omics = {omic: pd.read_csv(f'{folder}/{omic}.csv', index_col=0) for omic in omic_measures}
    def summarize_datasets(self):
        summary = {omic: self.omics[omic].shape for omic in self.omics.keys()}
        return pd.DataFrame.from_dict(summary, orient='index', columns=['samples', 'features'])
    def subset_trimester(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: Invalid trimester, please input a value of 1 through 3')
            return None
        return self.sample_ids[self.trimesters == trimester].values
    def permanova(self):
        permanova_pval = {}
        distance_matrices = {}
        for omic in self.omics.keys():
            omic_data = self.omics[omic].loc[self.sample_ids]
            distance_matrix = squareform(pdist(omic_data.values, metric='euclidean'))
            distance_matrix = pd.DataFrame(distance_matrix, index=omic_data.index, columns=omic_data.index)
            samples = distance_matrix.index.str.split('_').str[0]
            trimesters = distance_matrix.index.str.split('_').str[1]
            distance_matrix_skbio = skbio.DistanceMatrix(distance_matrix, ids=distance_matrix.index)
            trimester_permanova = skbio.stats.distance.permanova(distance_matrix_skbio, trimesters, permutations=999)
            donor_permanova = skbio.stats.distance.permanova(distance_matrix_skbio, samples, permutations=999)
            permanova_pval[omic] = {
                'pval_trimester': trimester_permanova['p-value'],
                'pval_donor': donor_permanova['p-value']
            }
            distance_matrices[omic] = distance_matrix
        return pd.DataFrame.from_dict(permanova_pval, orient='index'), distance_matrices
    def within_between_comparisons(self, distance_matrix_dict=None, comparison='donor_comparison', out_png=None):
        if distance_matrix_dict is None:
            _, distance_matrix_dict = self.permanova()
        fig, ax = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(ax[3, 1])
        counter = 0
        for omic, distance_matrix in distance_matrix_dict.items():
            subplot_ax = ax[counter
            counter += 1
            dist_tidy = distance_matrix.reset_index().melt(id_vars='index')
            dist_tidy = dist_tidy[dist_tidy['index'] != dist_tidy['variable']]
            dist_tidy['donor1'] = dist_tidy['index'].str.split('_').str[0]
            dist_tidy['trimester1'] = dist_tidy['index'].str.split('_').str[1]
            dist_tidy['donor2'] = dist_tidy['variable'].str.split('_').str[0]
            dist_tidy['trimester2'] = dist_tidy['variable'].str.split('_').str[1]
            dist_tidy['donor_comparison'] = dist_tidy.apply(
                lambda x: 'within' if x['donor1'] == x['donor2'] else 'between', axis=1
            )
            dist_tidy['trimester_comparison'] = dist_tidy.apply(
                lambda x: 'within' if x['trimester1'] == x['trimester2'] else 'between', axis=1
            )
            sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax, showfliers=False)
            sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=dist_tidy, ax=subplot_ax)
            subplot_ax.set_title(f'{omic}')
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
    def pca(self, modality, num_pcs=25):
        omic_data = self.omics.get(modality)
        if omic_data is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None, None
        omic_data = omic_data.loc[self.sample_ids]
        pca = decomposition.PCA(n_components=num_pcs)
        pc_matrix = pca.fit_transform(omic_data)
        return pc_matrix, omic_data
    def plot_pca(self, modality, out_png=None):
        pc_matrix, omic_data = self.pca(modality)
        if pc_matrix is None:
            return
        pca_df = pd.DataFrame(pc_matrix, index=omic_data.index)
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 5))
        trimesters = self.trimesters.unique()
        trimester_colors = dict(zip(trimesters, sns.color_palette('Set1', len(trimesters))))
        for period in trimesters:
            donor_sample_indices = self.trimesters[self.trimesters == period].index
            temp = pca_df.loc[donor_sample_indices, :]
            ax1.scatter(temp.loc[:, 0], temp.loc[:, 1], label=f'trimester {period}', color=trimester_colors[period])
        sns.despine()
        ax1.legend(bbox_to_anchor=[1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        patient_ids = self.patients.unique()
        donor_colors = dict(zip(patient_ids, sns.color_palette('tab20', len(patient_ids))))
        for donor in patient_ids:
            donor_sample_indices = self.patients[self.patients == donor].index
            temp = pca_df.loc[donor_sample_indices, :]
            ax2.scatter(temp.loc[:, 0], temp.loc[:, 1], label=donor, color=donor_colors[donor])
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
        omic_data = self.omics.get(modality).copy()
        if omic_data is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None
        valid_omic_samples = omic_data.loc[self.sample_ids, :]
        valid_weeks = self.weeks.loc[self.featureindex.index]
        valid_patient_indices = self.patients.loc[self.featureindex.index]
        patients = self.patients.unique()
        valid_omic_samples = valid_omic_samples.loc[:, valid_omic_samples.std() != 0]
        valid_omic_samples = valid_omic_samples.apply(stats.zscore)
        train_test_loo = [
            (valid_patient_indices[valid_patient_indices != patient].index.values, valid_patient_indices[valid_patient_indices == patient].index.values)
            for patient in patients
        ]
        predicted, actual, cv_l1_ratios, cv_alphas, coeffs = [], [], [], [], []
        en_reg_cv = linear_model.ElasticNetCV(
            l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train, test in train_test_loo:
            en_reg_cv.fit(valid_omic_samples.values[train], valid_weeks.values[train])
            cv_l1_ratios.append(en_reg_cv.l1_ratio_)
            cv_alphas.append(en_reg_cv.alpha_)
            predicted.extend(en_reg_cv.predict(valid_omic_samples.values[test]))
            actual.extend(valid_weeks.values[test])
            coeffs.append(en_reg_cv.coef_)
        if input_ax is None:
            input_ax = plt.subplot()
            plot = True
        else:
            plot = False
        sns.regplot(actual, predicted, ax=input_ax)
        r, pval = stats.pearsonr(actual, predicted)
        input_ax.set_title(f"{modality} | R^2 = {np.round(r**2, 3)} | -log_10(p-val) = {np.round(-np.log10(pval), 2)}")
        if plot:
            if out_png:
                plt.savefig(out_png, bbox_inches="tight")
            else:
                plt.show()
            plt.close()
        coeffs_df = pd.DataFrame(coeffs, columns=valid_omic_samples.columns)
        return r**2, pval, cv_l1_ratios, cv_alphas, coeffs_df
    def elastic_net_r_squares(self, out_png=None):
        r_sqs, top_features = {}, []
        fig, ax = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(ax[3, 1])
        counter = 0
        for omic in self.omics.keys():
            subplot_ax = ax[counter
            r_sq, p_val, _, _, coeffs_df = self.elastic_net_regression(omic, subplot_ax)
            features_used = coeffs_df.loc[:, coeffs_df.mean() > 0].columns
            r_sqs[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(features_used)}
            top_features.extend(features_used)
            counter += 1
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
        return pd.DataFrame.from_dict(r_sqs, orient='index'), top_features
    def cross_omic_elastic_net(self, select_features=None, out_png=None):
        all_omics = pd.concat([data.loc[self.sample_ids, :].T for data in self.omics.values()]).T
        if select_features:
            all_omics = all_omics.loc[:, select_features]
        all_omics = all_omics.loc[:, all_omics.std() > 0]
        all_omics = all_omics.apply(stats.zscore)
        valid_weeks = self.weeks.loc[self.featureindex.index]
        valid_patient_indices = self.patients.loc[self.featureindex.index]
        patients = self.patients.unique()
        train_test_loo = [
            (valid_patient_indices[valid_patient_indices != patient].index.values, valid_patient_indices[valid_patient_indices == patient].index.values)
            for patient in patients
        ]
        l1_ratios_cv, alphas_cv, predicted, actual, coeffs = [], [], [], [], []
        en_cv = linear_model.ElasticNetCV(
            l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train_index, test_index in train_test_loo:
            en_cv.fit(all_omics.iloc[train_index, :], valid_weeks[train_index])
            l1_ratios_cv.append(en_cv.l1_ratio_)
            alphas_cv.append(en_cv.alpha_)
            predicted.extend(en_cv.predict(all_omics.iloc[test_index, :]))
            actual.extend(valid_weeks[test_index])
            coeffs.append(en_cv.coef_)
        sns.regplot(actual, predicted)
        r, pval = stats.pearsonr(actual, predicted)
        plt.title(f'r^2 = {np.round(r**2, 3)} | -log_10(p-val) = {np.round(-np.log10(pval), 2)}')
        if out_png:
            plt.savefig(out_png, bbox_inches="tight")
        else:
            plt.show()
        plt.close()
        return r**2, pval, pd.DataFrame(coeffs, columns=all_omics.columns)
if __name__ == "__main__":
    gestation_multiomics = PregnancyMultiomics('path/to/folder')
    print(gestation_multiomics.summarize_datasets())
    permanova_df, dist_matrix_dict = gestation_multiomics.permanova()
    print(permanova_df)
    gestation_multiomics.within_between_comparisons(
        distance_matrix_dict=dist_matrix_dict,
        out_png='./Figures/within_between_donor_comparisons.png'
    )
    for omic in gestation_multiomics.omics.keys():
        gestation_multiomics.plot_pca(omic, out_png=f'./Figures/{omic}_pca.png')
    r2_table, top_omic_features = gestation_multiomics.elastic_net_r_squares(out_png='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, pval, coeffs = gestation_multiomics.cross_omic_elastic_net(
        select_features=top_omic_features,
        out_png='./Figures/elastic_net_top_features.png'
    )
    r2_all_omics, pval_all_omics, coeffs_all_omics = gestation_multiomics.cross_omic_elastic_net(
        out_png='./Figures/elastic_net_all_omics_predictions.png'
    )