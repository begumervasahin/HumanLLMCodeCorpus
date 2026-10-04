import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.spatial.distance import squareform, pdist
from sklearn import decomposition, linear_model
sns.set_style("white")
class class1:
    def fonk1(self, folder):
        self.b1 = pd.read_csv(f'{folder}/featurepatients.csv', squeeze=True)
        self.b2 = pd.read_csv(f'{folder}/featuretimes.csv', squeeze=True)
        self.b3 = pd.read_csv(f'{folder}/featureweeks.csv', squeeze=True)
        self.b4 = pd.read_csv(f'{folder}/b4.csv', squeeze=True)
        self.b5 = pd.Series(map('_'.join, zip(self.b1.astype(str), self.b2.astype(str))))
        b6 = [
            'CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex',
            'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic'
        ]
        self.b7 = {omic: pd.read_csv(f'{folder}/{omic}.csv', index_col=0) for omic in b6}
    def fonk2(self):
        b8 = {omic: self.b7[omic].shape for omic in self.b7.keys()}
        b9 = pd.DataFrame.from_dict(b8, orient='index', columns=['b14', 'features'])
        return b9
    def fonk3(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: Invalid trimester, please input a value of 1 through 3')
            return None
        return self.b5[self.b2 = = trimester].values
    def fonk4(self):
        b10 = {}
        b11 = {}
        for omic in self.b7.keys():
            b12 = self.b7[omic].copy()
            b12 = b12.loc[self.b5, :]
            b13 = squareform(pdist(b12.values, metric='euclidean'))
            b13 = pd.DataFrame(b13, index=b12.index, columns=b12.index)
            b14 = b13.index.str.split('_').str[0]
            b2 = b13.index.str.split('_').str[1]
            b15 = skbio.DistanceMatrix(b13, ids=b13.index)
            b16 = skbio.stats.distance.fonk4(b15, b2, permutations=999)
            b17 = skbio.stats.distance.fonk4(b15, b14, permutations=999)
            b10[omic] = {'pval_trimester': b16['p-value'], 'pval_donor': b17['p-value']}
            b11[omic] = b13
        b18 = pd.DataFrame.from_dict(b10, orient='index')
        return b18, b11
    def fonk5(self, b19 = None, comparison='donor_comparison', b29=None):
        if b19 is None:
            pvals, b19 = self.fonk4()
        fig, b20 = plt.subplots(4, b49, figsize=(12, 15))
        fig.delaxes(b20[3, 1])
        a1 = 0
        for omic in b19.keys():
            b21 = b20[a1
            a1 += 1
            b22 = b19[omic].reset_index().melt(id_vars='index')
            b22 = b22[b22['index'] != b22['variable']]
            b22['donor1'] = b22['index'].str.split('_').str[0]
            b22['trimester1'] = b22['index'].str.split('_').str[1]
            b22['donor2'] = b22['variable'].str.split('_').str[0]
            b22['trimester2'] = b22['variable'].str.split('_').str[1]
            b22['donor_comparison'] = b22.apply(lambda b24: 'within' if b24['donor1'] == b24['donor2'] else 'between', b23 = 1)
            b22['trimester_comparison'] = b22.apply(lambda b24: 'within' if b24['trimester1'] == b24['trimester2'] else 'between', b23 = 1)
            sns.boxplot(b24 = comparison, y='value', order=['within', 'between'], data=b22, b20=b21, showfliers=False)
            sns.stripplot(b24 = comparison, y='value', order=['within', 'between'], data=b22, b20=b21)
            b21.set_title(f'{omic}')
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk6(self, modality, b26 = 25):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None, None
        b12 = b12.loc[self.b5]
        b27 = decomposition.PCA(n_components=b26)
        b28 = b27.fit_transform(b12)
        return b28, b12
    def fonk7(self, modality, b29 = None):
        b28, b12 = self.fonk6(modality)
        if b28 is None:
            return
        b30 = pd.DataFrame(b28, index=b12.index)
        fig, (ax1, ax2) = plt.subplots(1, b49, b31 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b32 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b33 = self.b2[self.b2 == period].index
            b34 = b30.loc[b33, :]
            ax1.scatter(b34.loc[:, 0], b34.loc[:, 1], b35 = f'trimester {period}', color=b32[period])
        sns.despine()
        ax1.legend(b36 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        b37 = self.b1.unique()
        b38 = dict(zip(b37, sns.color_palette('tab20', len(b37))))
        for donor in b37:
            b33 = self.b1[self.b1 == donor].index
            b34 = b30.loc[b33, :]
            ax2.scatter(b34.loc[:, 0], b34.loc[:, 1], b35 = donor, color=b38[donor])
        sns.despine()
        ax2.legend(b36 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk8(self, modality, b39 = None, b29=None):
        b12 = self.b7.get(modality).copy()
        if b12 is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None
        b40 = b12.loc[self.b5, :]
        b41 = self.b3.loc[self.b4.index]
        b42 = self.b1.loc[self.b4.index]
        b1 = self.b1.unique()
        b40 = b40.loc[:, b40.std() != 0]
        b40 = b40.apply(stats.zscore)
        b43 = [
            (b42[b42 != patient].index.values, b42[b42 = = patient].index.values)
            for patient in b1
        ]
        predicted, actual, cv_l1_ratios, cv_alphas, b44 = [], [], [], [], []
        b45 = linear_model.ElasticNetCV(
            b46 = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train, test in b43:
            b45.fit(b40.values[train], b41.values[train])
            cv_l1_ratios.append(b45.l1_ratio_)
            cv_alphas.append(b45.alpha_)
            predicted.extend(b45.predict(b40.values[test]))
            actual.extend(b41.values[test])
            b44.append(b45.coef_)
        if b39 is None:
            b39 = plt.subplot()
            b47 = True
        else:
            b47 = False
        sns.regplot(actual, predicted, b20 = b39)
        r, b48 = stats.pearsonr(actual, predicted)
        b39.set_title(f"{modality} | R^b49 = {np.round(r**b49, 3)} | -log_10(p-val) = {np.round(-np.log10(b48), b49)}")
        if b47:
            if b29:
                plt.savefig(b29, b25 = "tight")
            else:
                plt.show()
            plt.close()
        b50 = pd.DataFrame(b44, columns=b40.columns)
        return r**b49, b48, cv_l1_ratios, cv_alphas, b50
    def fonk9(self, b29 = None):
        r_sqs, b51 = {}, []
        fig, b20 = plt.subplots(4, b49, figsize=(12, 15))
        fig.delaxes(b20[3, 1])
        a1 = 0
        for omic in self.b7.keys():
            b21 = b20[a1
            r_sq, p_val, l1_ratio_list, alpha_list, b50 = self.fonk8(omic, b21)
            b52 = b50.loc[:, b50.mean() > 0].columns
            r_sqs[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(b52)}
            b51.extend(b52)
            a1 += 1
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b53 = pd.DataFrame.from_dict(r_sqs, orient='index')
        return b53, b51
    def fonk10(self, b54 = None, b29=None):
        b55 = pd.concat([data.loc[self.b5, :].T for data in self.b7.values()]).T
        if b54:
            b55 = b55.loc[:, b54]
        b55 = b55.loc[:, b55.std() > 0]
        b55 = b55.apply(stats.zscore)
        b41 = self.b3.loc[self.b4.index]
        b42 = self.b1.loc[self.b4.index]
        b1 = self.b1.unique()
        b43 = [
            (b42[b42 != patient].index.values, b42[b42 = = patient].index.values)
            for patient in b1
        ]
        l1_ratios_cv, alphas_cv, predicted, actual, b44 = [], [], [], [], []
        b56 = linear_model.ElasticNetCV(
            b46 = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train_index, test_index in b43:
            b56.fit(b55.iloc[train_index, :], b41[train_index])
            l1_ratios_cv.append(b56.l1_ratio_)
            alphas_cv.append(b56.alpha_)
            predicted.extend(b56.predict(b55.iloc[test_index, :]))
            actual.extend(b41[test_index])
            b44.append(b56.coef_)
        sns.regplot(actual, predicted)
        r, b48 = stats.pearsonr(actual, predicted)
        plt.title(f'r^b49 = {np.round(r**b49, 3)} | -log_10(p-val) = {np.round(-np.log10(b48), b49)}')
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b50 = pd.DataFrame(b44, columns=b55.columns)
        return r**b49, b48, b50
if b57 = = "__main__":
    b58 = class1('path/to/folder')
    print(b58.fonk2())
    b18, b59 = b58.fonk4()
    print(b18)
    b58.fonk5(b19 = b59, b29='./Figures/within_between_donor_comparisons.png')
    for omic in b58.b7.keys():
        b58.fonk7(omic, b29 = f'./Figures/{omic}_pca.png')
    r2_table, b60 = b58.fonk9(b29='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, b48, b44 = b58.fonk10(b54=b60, b29='./Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, b61 = b58.fonk10(b29='./Figures/elastic_net_all_omics_predictions.png')