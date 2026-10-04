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
        return pd.DataFrame.from_dict(b8, b9 = 'index', b54=['b14', 'features'])
    def fonk3(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: Invalid trimester, please input a value of 1 through 3')
            return None
        return self.b5[self.b2 = = trimester].values
    def fonk4(self):
        b10 = {}
        b11 = {}
        for omic in self.b7.keys():
            b12 = self.b7[omic].loc[self.b5]
            b13 = squareform(pdist(b12.values, metric='euclidean'))
            b13 = pd.DataFrame(b13, index=b12.index, b54=b12.index)
            b14 = b13.index.str.split('_').str[0]
            b2 = b13.index.str.split('_').str[1]
            b15 = skbio.DistanceMatrix(b13, ids=b13.index)
            b16 = skbio.stats.distance.fonk4(b15, b2, permutations=999)
            b17 = skbio.stats.distance.fonk4(b15, b14, permutations=999)
            b10[omic] = {
                'pval_trimester': b16['p-value'],
                'pval_donor': b17['p-value']
            }
            b11[omic] = b13
        return pd.DataFrame.from_dict(b10, b9 = 'index'), b11
    def fonk5(self, b18 = None, comparison='donor_comparison', b27=None):
        if b18 is None:
            _, b18 = self.fonk4()
        fig, b19 = plt.subplots(4, b47, figsize=(12, 15))
        fig.delaxes(b19[3, 1])
        a1 = 0
        for omic, b13 in b18.items():
            b20 = b19[a1
            a1 += 1
            b21 = b13.reset_index().melt(id_vars='index')
            b21 = b21[b21['index'] != b21['variable']]
            b21['donor1'] = b21['index'].str.split('_').str[0]
            b21['trimester1'] = b21['index'].str.split('_').str[1]
            b21['donor2'] = b21['variable'].str.split('_').str[0]
            b21['trimester2'] = b21['variable'].str.split('_').str[1]
            b21['donor_comparison'] = b21.apply(
                lambda b22: 'within' if b22['donor1'] == b22['donor2'] else 'between', a2 = 1
            )
            b21['trimester_comparison'] = b21.apply(
                lambda b22: 'within' if b22['trimester1'] == b22['trimester2'] else 'between', a2 = 1
            )
            sns.boxplot(b22 = comparison, y='value', order=['within', 'between'], data=b21, b19=b20, showfliers=False)
            sns.stripplot(b22 = comparison, y='value', order=['within', 'between'], data=b21, b19=b20)
            b20.set_title(f'{omic}')
        if b27:
            plt.savefig(b27, b23 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk6(self, modality, b24 = 25):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None, None
        b12 = b12.loc[self.b5]
        b25 = decomposition.PCA(n_components=b24)
        b26 = b25.fit_transform(b12)
        return b26, b12
    def fonk7(self, modality, b27 = None):
        b26, b12 = self.fonk6(modality)
        if b26 is None:
            return
        b28 = pd.DataFrame(b26, index=b12.index)
        fig, (ax1, ax2) = plt.subplots(1, b47, b29 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b30 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b31 = self.b2[self.b2 == period].index
            b32 = b28.loc[b31, :]
            ax1.scatter(b32.loc[:, 0], b32.loc[:, 1], b33 = f'trimester {period}', color=b30[period])
        sns.despine()
        ax1.legend(b34 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        b35 = self.b1.unique()
        b36 = dict(zip(b35, sns.color_palette('tab20', len(b35))))
        for donor in b35:
            b31 = self.b1[self.b1 == donor].index
            b32 = b28.loc[b31, :]
            ax2.scatter(b32.loc[:, 0], b32.loc[:, 1], b33 = donor, color=b36[donor])
        sns.despine()
        ax2.legend(b34 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if b27:
            plt.savefig(b27, b23 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk8(self, modality, b37 = None, b27=None):
        b12 = self.b7.get(modality).copy()
        if b12 is None:
            print('ERROR: Invalid omic type. Please input a valid omic measure.')
            return None
        b38 = b12.loc[self.b5, :]
        b39 = self.b3.loc[self.b4.index]
        b40 = self.b1.loc[self.b4.index]
        b1 = self.b1.unique()
        b38 = b38.loc[:, b38.std() != 0]
        b38 = b38.apply(stats.zscore)
        b41 = [
            (b40[b40 != patient].index.values, b40[b40 = = patient].index.values)
            for patient in b1
        ]
        predicted, actual, cv_l1_ratios, cv_alphas, b42 = [], [], [], [], []
        b43 = linear_model.ElasticNetCV(
            b44 = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train, test in b41:
            b43.fit(b38.values[train], b39.values[train])
            cv_l1_ratios.append(b43.l1_ratio_)
            cv_alphas.append(b43.alpha_)
            predicted.extend(b43.predict(b38.values[test]))
            actual.extend(b39.values[test])
            b42.append(b43.coef_)
        if b37 is None:
            b37 = plt.subplot()
            b45 = True
        else:
            b45 = False
        sns.regplot(actual, predicted, b19 = b37)
        r, b46 = stats.pearsonr(actual, predicted)
        b37.set_title(f"{modality} | R^b47 = {np.round(r**b47, 3)} | -log_10(p-val) = {np.round(-np.log10(b46), b47)}")
        if b45:
            if b27:
                plt.savefig(b27, b23 = "tight")
            else:
                plt.show()
            plt.close()
        b48 = pd.DataFrame(b42, b54=b38.b54)
        return r**b47, b46, cv_l1_ratios, cv_alphas, b48
    def fonk9(self, b27 = None):
        r_sqs, b49 = {}, []
        fig, b19 = plt.subplots(4, b47, figsize=(12, 15))
        fig.delaxes(b19[3, 1])
        a1 = 0
        for omic in self.b7.keys():
            b20 = b19[a1
            r_sq, p_val, _, _, b48 = self.fonk8(omic, b20)
            b50 = b48.loc[:, b48.mean() > 0].b54
            r_sqs[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(b50)}
            b49.extend(b50)
            a1 += 1
        if b27:
            plt.savefig(b27, b23 = "tight")
        else:
            plt.show()
        plt.close()
        return pd.DataFrame.from_dict(r_sqs, b9 = 'index'), b49
    def fonk10(self, b51 = None, b27=None):
        b52 = pd.concat([data.loc[self.b5, :].T for data in self.b7.values()]).T
        if b51:
            b52 = b52.loc[:, b51]
        b52 = b52.loc[:, b52.std() > 0]
        b52 = b52.apply(stats.zscore)
        b39 = self.b3.loc[self.b4.index]
        b40 = self.b1.loc[self.b4.index]
        b1 = self.b1.unique()
        b41 = [
            (b40[b40 != patient].index.values, b40[b40 = = patient].index.values)
            for patient in b1
        ]
        l1_ratios_cv, alphas_cv, predicted, actual, b42 = [], [], [], [], []
        b53 = linear_model.ElasticNetCV(
            b44 = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8
        )
        for train_index, test_index in b41:
            b53.fit(b52.iloc[train_index, :], b39[train_index])
            l1_ratios_cv.append(b53.l1_ratio_)
            alphas_cv.append(b53.alpha_)
            predicted.extend(b53.predict(b52.iloc[test_index, :]))
            actual.extend(b39[test_index])
            b42.append(b53.coef_)
        sns.regplot(actual, predicted)
        r, b46 = stats.pearsonr(actual, predicted)
        plt.title(f'r^b47 = {np.round(r**b47, 3)} | -log_10(p-val) = {np.round(-np.log10(b46), b47)}')
        if b27:
            plt.savefig(b27, b23 = "tight")
        else:
            plt.show()
        plt.close()
        return r**b47, b46, pd.DataFrame(b42, b54 = b52.b54)
if b55 = = "__main__":
    b56 = class1('path/to/folder')
    print(b56.fonk2())
    permanova_df, b57 = b56.fonk4()
    print(permanova_df)
    b56.fonk5(
        b18 = b57,
        b27 = './Figures/within_between_donor_comparisons.png'
    )
    for omic in b56.b7.keys():
        b56.fonk7(omic, b27 = f'./Figures/{omic}_pca.png')
    r2_table, b58 = b56.fonk9(b27='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, b46, b42 = b56.fonk10(
        b51 = b58,
        b27 = './Figures/elastic_net_top_features.png'
    )
    r2_all_omics, pval_all_omics, b59 = b56.fonk10(
        b27 = './Figures/elastic_net_all_omics_predictions.png'
    )