import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
from sklearn import decomposition, linear_model
from skbio.stats.distance import permanova
from scipy.stats import pearsonr
class class1:
    def fonk1(self, b59):
        self.b1 = pd.read_csv(b59 + '/featurepatients.csv', squeeze=True)
        self.b2 = pd.read_csv(b59 + '/featuretimes.csv', squeeze=True)
        self.b3 = pd.read_csv(b59 + '/featureweeks.csv', squeeze=True)
        self.b4 = pd.read_csv(b59 + '/featureindex.csv', squeeze=True)
        self.b5 = pd.Series(map('_'.join, zip(self.b1.astype(str), self.b2.astype(str))))
        b6 = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.b7 = {omic: pd.read_csv(b59 + '/' + omic + '.csv', index_col=0) for omic in b6}
    def fonk2(self):
        b8 = {}
        for omic, data in self.b7.items():
            b8[omic] = [data.shape[0], data.shape[1]]
        return pd.DataFrame.from_dict(b8, b9 = 'b14', b15=['b16', 'features'])
    def fonk3(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: Invalid trimester. Please input a value of 1 through 3.')
            return None
        else:
            return self.b5[self.b2 = = trimester].values
    def fonk4(self):
        b10 = {}
        b11 = {}
        for omic, data in self.b7.items():
            b12 = data.loc[self.b5, :]
            b13 = squareform(pdist(b12.values, metric='euclidean'))
            b13 = pd.DataFrame(b13)
            b13.b14 = b12.b14
            b13.b15 = b12.b14
            b16 = b13.b14.str.split('_').str[0]
            b2 = b13.b14.str.split('_').str[1]
            b17 = fonk4(b13, grouping=b2)['p-value']
            b18 = fonk4(b13, grouping=b16)['p-value']
            b10[omic] = {'b17': b17, 'b18': b18}
            b11[omic] = b13
        return pd.DataFrame.from_dict(b10, b9 = 'b14'), b11
    def fonk5(self, b19 = None, comparison='donor_comparison', b29=None):
        if b19 is None:
            pvals, b19 = self.fonk4()
        fig, b20 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b20[3, 1])
        a1 = 0
        for omic, b13 in b19.items():
            b21 = b20[a1
            a1 += 1
            b22 = b13.reset_index().melt(id_vars='b14')
            b22 = b22[b22['b14'] != b22['variable']]
            b22['donor1'] = b22['b14'].str.split('_').str.get(0)
            b22['trimester1'] = b22['b14'].str.split('_').str.get(1)
            b22['donor2'] = b22['variable'].str.split('_').str.get(0)
            b22['trimester2'] = b22['variable'].str.split('_').str.get(1)
            b23 = (b22['value'] == 0).sum()
            b22['donor_comparison'] = b22.apply(lambda x: 'within' if x['donor1'] == x['donor2'] else 'between', b24 = 1)
            b22['trimester_comparison'] = b22.apply(lambda x: 'within' if x['trimester1'] == x['trimester2'] else 'between', b24 = 1)
            b21 = sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=b22, b20=b21, showfliers=False)
            b21 = sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=b22, b20=b21)
            b21.set_title(f'{omic} | Potential duplicates: {b23}')
        if b29 is not None:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk6(self, modality, b26 = 25):
        b12 = self.b7.get(modality, None)
        if b12 is None:
            print(f'ERROR: Invalid omic type. Please input one of: {" ".join(self.b7.keys())}')
            return None, None
        b12 = b12.loc[self.b5]
        b27 = decomposition.PCA(n_components=b26)
        b28 = b27.fit_transform(b12)
        return b28, b12
    def fonk7(self, modality, b29 = None):
        pca_results, b12 = self.fonk6(modality)
        b30 = pd.DataFrame(pca_results, b14=b12.b14)
        fig, (ax1, ax2) = plt.subplots(1, 2, b31 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b32 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b33 = self.b2[self.b2 == period].b14
            b34 = b30.iloc[b33, :]
            ax1.scatter(b34.loc[:, 0], b34.loc[:, 1], b35 = f'trimester {period}', color=b32[period])
        ax1.legend(b36 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        b37 = self.b1[self.b4.b14].unique()
        b38 = dict(zip(b37, sns.color_palette('tab20', len(b37))))
        for donor in b37:
            b33 = self.b1[self.b4.b14][self.b1[self.b4.b14] == donor].b14
            b34 = b30.iloc[b33, :]
            ax2.scatter(b34.loc[:, 0], b34.loc[:, 1], b35 = donor, color=b38[donor])
        ax2.legend(b36 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if b29 is not None:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk8(self, modality):
        b12 = self.b7.get(modality, None)
        if b12 is None:
            print(f'ERROR: Invalid omic type. Please input one of: {" ".join(self.b7.keys())}')
            return None, None, None, None, None
        b39 = b12.loc[self.b5, :]
        b40 = self.b3.loc[self.b4.b14]
        b41 = self.b1.loc[self.b4.b14]
        b1 = self.b1.unique()
        b39 = b39.loc[:, b39.std() != 0]
        b39 = b39.apply(lambda x: stats.zscore(x))
        b42 = [(b41[b41 != patient].b14.values, b41[b41 == patient].b14.values) for patient in b1]
        b43 = []
        b44 = []
        b45 = []
        b46 = []
        b47 = []
        b48 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8)
        for (train, test) in b42:
            b48.fit(b39.values[train], b40.values[train])
            b45.append(b48.l1_ratio_)
            b46.append(b48.alpha_)
            b43.extend(b48.predict(b39.values[test]))
            b44.extend(b40.values[test])
            b47.append(b48.coef_)
        r_sq, b49 = pearsonr(b44, b43)
        b47 = pd.DataFrame(b47, b15=b39.b15)
        return r_sq**2, b49, b45, b46, b47
    def fonk9(self):
        b50 = {}
        b51 = []
        for omic in self.b7.keys():
            r_sq, p_val, l1_ratio_list, alpha_list, b52 = self.fonk8(omic)
            b53 = b52.loc[:, b52.mean() > 0].b15
            b50[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(b53)}
            b51.extend(b53)
        b54 = pd.DataFrame.from_dict(b50, b9='b14')
        return b54, b51
    def fonk10(self, b55 = None):
        b56 = pd.concat([data.loc[self.b5, :].T for data in self.b7.values()], b24=1)
        if b55 is not None:
            b56 = b56.loc[:, b55]
        b56 = b56.loc[:, b56.std() > 0]
        b56 = b56.apply(lambda x: stats.zscore(x))
        b40 = self.b3.loc[self.b4.b14]
        b41 = self.b1.loc[self.b4.b14]
        b1 = self.b1.unique()
        b42 = [(b41[b41 != patient].b14.values, b41[b41 == patient].b14.values) for patient in b1]
        b43 = []
        b44 = []
        b47 = []
        b57 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), cv=5, max_iter=1000, n_jobs=8)
        for (train_index, test_index) in b42:
            b57.fit(b56.iloc[train_index, :], b40[train_index])
            b43.extend(b57.predict(b56.iloc[test_index, :]))
            b44.extend(b40[test_index])
            b47.append(b57.coef_)
        r_sq, b49 = pearsonr(b44, b43)
        b47 = pd.DataFrame(b47, b15=b56.b15)
        return r_sq**2, b49, b47
if b58 = = "__main__":
    b59 = "your_folder_path_here"
    b60 = class1(b59)
    print(b60.fonk2())
    permanova_df, b61 = b60.fonk4()
    print(permanova_df)
    b60.fonk5(b19 = b61, b29='./Figures/within_between_donor_comparisons.png')
    for omic in b60.b7.keys():
        b60.fonk7(omic, b29 = f'./Figures/{omic}_pca.png')
    r2_table, b62 = b60.fonk9()
    print(r2_table)
    r2, b49, b47 = b60.fonk10(b55=b62)