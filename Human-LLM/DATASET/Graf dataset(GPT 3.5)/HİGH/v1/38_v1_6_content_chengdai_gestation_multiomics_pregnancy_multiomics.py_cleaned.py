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
class class1():
    def fonk1(self, folder):
        self.b1 = pd.read_csv(folder + '/featurepatients.csv', squeeze=True)
        self.b2 = pd.read_csv(folder + '/featuretimes.csv', squeeze=True)
        self.b3 = pd.read_csv(folder + '/featureweeks.csv', squeeze=True)
        self.b4 = pd.read_csv(folder + '/b4.csv', squeeze=True)
        self.b5 = pd.Series(map('_'.join, zip(self.b1.astype(str), self.b2.astype(str))))
        b6 = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.b7 = {omic: pd.read_csv(folder + '/' + omic + '.csv', index_col=0) for omic in b6}
    def fonk2(self):
        b8 = {}
        for omic, data in self.b7.items():
            b8[omic] = [data.shape[0], data.shape[1]]
        b9 = pd.DataFrame.from_dict(b8, orient='b14', b15=['b16', 'features'])
        return b9
    def fonk3(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: not a valid trimester, please input a value of 1 through 3')
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
        b19 = pd.DataFrame.from_dict(b10, orient='b14')
        return b19, b11
    def fonk5(self, b20 = None, comparison='donor_comparison', b31=None):
        if b20 is None:
            pvals, b20 = self.fonk4()
        fig, b21 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b21[3, 1])
        a1 = 0
        for omic, b13 in b20.items():
            b22 = b21[a1
            a1 += 1
            b23 = b13.reset_index().melt(id_vars='b14')
            b23 = b23[b23['b14'] != b23['variable']]
            b23['donor1'] = b23['b14'].str.split('_').str.get(0)
            b23['trimester1'] = b23['b14'].str.split('_').str.get(1)
            b23['donor2'] = b23['variable'].str.split('_').str.get(0)
            b23['trimester2'] = b23['variable'].str.split('_').str.get(1)
            b24 = (b23['value'] == 0).sum()
            b23['donor_comparison'] = b23.apply(lambda x: 'within' if x['donor1'] == x['donor2'] else 'between', b25 = 1)
            b23['trimester_comparison'] = b23.apply(lambda x: 'within' if x['trimester1'] == x['trimester2'] else 'between', b25 = 1)
            b22 = sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=b23, b21=b22, showfliers=False)
            b22 = sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=b23, b21=b22)
            b22.set_title(f'{omic} | Potential duplicates: {b24}')
        if b31 is not None:
            plt.savefig(b31, b26 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk6(self, modality, b27 = 25):
        b12 = self.b7.get(modality, None)
        if b12 is None:
            print(f'ERROR: not a valid -omic type, please input either: {" ".join(self.b7.keys())}')
            return None, None
        b12 = b12.loc[self.b5]
        b28 = self.b1[self.b4.b14]
        b29 = decomposition.PCA(n_components=b27)
        b30 = b29.fit_transform(b12)
        return b30, b12
    def fonk7(self, modality, b31 = None):
        pca_results, b12 = self.fonk6(modality)
        b28 = self.b1[self.b4.b14]
        b32 = pd.DataFrame(pca_results)
        b32.b14 = b12.b14
        fig, (ax1, ax2) = plt.subplots(1, 2, b33 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b34 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b35 = self.b2[self.b2 == period].b14
            b36 = b32.iloc[b35, :]
            ax1.scatter(b36.loc[:, 0], b36.loc[:, 1], b37 = 'trimester {0}'.format(period), color=b34[period])
        ax1.legend(b38 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title('PCA of {0} by trimester'.format(modality))
        b39 = b28.unique()
        b40 = dict(zip(b39, sns.color_palette('tab20', len(b39))))
        for donor in b39:
            b35 = b28[b28 == donor].b14
            b36 = b32.iloc[b35, :]
            ax2.scatter(b36.loc[:, 0], b36.loc[:, 1], b37 = donor, color=b40[donor])
        ax2.legend(b38 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title('PCA of {0} by individual donor')
        if b31 is not None:
            plt.savefig(b31, b26 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk8(self, modality):
        b12 = self.b7.get(modality, None)
        if b12 is None:
            print(f'ERROR: not a valid -omic type, please input either: {" ".join(self.b7.keys())}')
            return None, None, None, None, None
        b41 = b12.loc[self.b5, :]
        b42 = self.b3.loc[self.b4.b14]
        b43 = self.b1.loc[self.b4.b14]
        b1 = self.b1.unique()
        b41 = b41.loc[:, b41.std() != 0]
        b41 = b41.apply(lambda x: scipy.stats.zscore(x))
        b44 = []
        for patient in b1:
            b45 = b43[b43 != patient].b14.values
            b46 = b43[b43 == patient].b14.values
            b44.append((b45, b46))
        b47 = []
        b48 = []
        b49 = []
        b50 = []
        b51 = []
        b52 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                              b53 = 5, max_iter=1000, n_jobs=8)
        for (train, test) in b44:
            b52.fit(b41.values[train], b42.values[train])
            b49.append(b52.l1_ratio_)
            b50.append(b52.alpha_)
            b47.extend(b52.predict(b41.values[test]))
            b48.extend(b42.values[test])
            b51.append(b52.coef_)
        r_sq, b54 = pearsonr(b48, b47)
        b51 = pd.DataFrame(b51)
        b51.b15 = b41.b15
        return r_sq**2, b54, b49, b50, b51
    def fonk9(self):
        b55 = {}
        b56 = []
        for omic in self.b7.keys():
            r_sq, p_val, l1_ratio_list, alpha_list, b57 = self.fonk8(omic)
            b58 = b57.loc[:, b57.mean() > 0].b15
            b55[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(b58)}
            b56.extend(b58)
        b59 = pd.DataFrame.from_dict(b55, orient='b14')
        return b59, b56
    def fonk10(self, b60 = None):
        b61 = [data.loc[self.b5, :].T for data in self.b7.values()]
        b61 = pd.concat(b61).T
        if b60 is not None:
            b61 = b61.loc[:, b60]
        b61 = b61.loc[:, b61.std() > 0]
        b61 = b61.apply(lambda x: scipy.stats.zscore(x))
        b42 = self.b3.loc[self.b4.b14]
        b43 = self.b1.loc[self.b4.b14]
        b1 = self.b1.unique()
        b44 = []
        for patient in b1:
            b45 = b43[b43 != patient].b14.values
            b46 = b43[b43 == patient].b14.values
            b44.append((b45, b46))
        b47 = []
        b48 = []
        b51 = []
        b62 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                          b53 = 5, max_iter=1000, n_jobs=8)
        for (train_index, test_index) in b44:
            b62.fit(b61.iloc[train_index, :], b42[train_index])
            b47.extend(b62.predict(b61.iloc[test_index, :]))
            b48.extend(b42[test_index])
            b51.append(b62.coef_)
        r_sq, b54 = pearsonr(b48, b47)
        b51 = pd.DataFrame(b51)
        b51.b15 = b61.b15
        return r_sq**2, b54, b51
if b63 = = "__main__":
    b64 = "your_folder_path_here"
    b65 = class1(b64)
    print(b65.fonk2())
    b19, b66 = b65.fonk4()
    print(b19)
    b65.fonk5(b20 = b66,
                                                    b31 = './Figures/within_between_donor_comparisons.png')
    for omic in b65.b7.keys():
        b65.fonk7(omic, b31 = f'./Figures/{omic}_pca.png')
    r2_table, b67 = b65.fonk9(
        b31 = './Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, b54, b51 = b65.fonk10(b60=b67,
                                                                   b31 = './Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, b68 = b65.fonk10(
        b31 = './Figures/elastic_net_all_omics_predictions.png')