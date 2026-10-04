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
class class1:
    def fonk1(self, b54):
        self.b1 = pd.read_csv(f"{b54}/featurepatients.csv", squeeze=True)
        self.b2 = pd.read_csv(f"{b54}/featuretimes.csv", squeeze=True)
        self.b3 = pd.read_csv(f"{b54}/featureweeks.csv", squeeze=True)
        self.b4 = pd.read_csv(f"{b54}/b4.csv", squeeze=True)
        self.b5 = pd.Series(map('_'.join, zip(self.b1.astype(str), self.b2.astype(str))))
        b6 = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.b7 = {omic: pd.read_csv(f"{b54}/{omic}.csv", index_col=0) for omic in b6}
    def fonk2(self):
        b8 = {omic: data.shape for omic, data in self.b7.items()}
        b9 = pd.DataFrame.from_dict(b8, orient='index', columns=['b14', 'features'])
        return b9
    def fonk3(self, trimester):
        if trimester not in range(1, 4):
            print('ERROR: not a valid trimester, please input a value of 1 through 3')
            return None
        return self.b5[self.b2 = = trimester].values
    def fonk4(self):
        b10 = {}
        b11 = {}
        for omic, data in self.b7.items():
            b12 = data.loc[self.b5]
            b13 = pd.DataFrame(squareform(pdist(b12.values, metric='euclidean')), index=b12.index, columns=b12.index)
            b14 = b13.index.str.split('_').str[0]
            b2 = b13.index.str.split('_').str[1]
            b15 = DistanceMatrix(b13, ids=b13.index)
            b16 = fonk4(b15, b2, permutations=999)['p-value']
            b17 = fonk4(b15, b14, permutations=999)['p-value']
            b10[omic] = {'pval_trimester': b16, 'pval_donor': b17}
            b11[omic] = b13
        b18 = pd.DataFrame.from_dict(b10, orient='index')
        return b18, b11
    def fonk5(self, b19 = None, comparison='donor_comparison', b29=None):
        def fonk6(row, col1, col2):
            return 'within' if row[col1] == row[col2] else 'between'
        if b19 is None:
            _, b19 = self.fonk4()
        fig, b20 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b20[3, 1])
        a1 = 0
        for omic, b13 in b19.items():
            b21 = b20[a1
            b22 = b13.reset_index().melt(id_vars='index')
            b22 = b22[b22['index'] != b22['variable']]
            b22['donor1'] = b22['index'].str.split('_').str.get(0)
            b22['trimester1'] = b22['index'].str.split('_').str.get(1)
            b22['donor2'] = b22['variable'].str.split('_').str.get(0)
            b22['trimester2'] = b22['variable'].str.split('_').str.get(1)
            b22['donor_comparison'] = b22.apply(lambda b24: fonk6(b24, 'donor1', 'donor2'), b23 = 1)
            b22['trimester_comparison'] = b22.apply(lambda b24: fonk6(b24, 'trimester1', 'trimester2'), b23 = 1)
            sns.boxplot(b24 = comparison, y='value', order=['within', 'between'], data=b22, b20=b21, showfliers=False)
            sns.stripplot(b24 = comparison, y='value', order=['within', 'between'], data=b22, b20=b21)
            b21.set_title(omic)
            a1 += 1
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk7(self, modality, b26 = 25):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b12 = b12.loc[self.b5]
        b27 = decomposition.PCA(n_components=b26)
        b28 = b27.fit_transform(b12)
        return b28, b12
    def fonk8(self, modality, b29 = None):
        pca_results, b12 = self.fonk7(modality)
        b30 = pd.DataFrame(pca_results, index=b12.index)
        fig, (ax1, ax2) = plt.subplots(1, 2, b31 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b32 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b33 = self.b2[self.b2 == period].index
            b34 = b30.iloc[b33]
            ax1.scatter(b34[0], b34[1], b35 = f'trimester {period}', color=b32[period])
        sns.despine()
        ax1.legend(b36 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        b37 = self.b1.unique()
        b38 = dict(zip(b37, sns.color_palette('tab20', len(b37))))
        for donor in b37:
            b33 = self.b1[self.b1 == donor].index
            b34 = b30.iloc[b33]
            ax2.scatter(b34[0], b34[1], b35 = donor, color=b38[donor])
        sns.despine()
        ax2.legend(b36 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk9(self, modality, b39 = None, b29=None):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b40 = b12.loc[self.b5]
        b41 = self.b3.loc[self.b4.index]
        b40 = b40.loc[:, b40.std() != 0].apply(scipy.stats.zscore)
        b42 = [(self.b1 != patient).index.values for patient in self.b1.unique()]
        b43 = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        b44 = []
        b45 = []
        for train_index, test_index in b42:
            b43.fit(b40.iloc[train_index], b41[train_index])
            b44.extend(b43.predict(b40.iloc[test_index]))
            b45.extend(b41[test_index])
        if b39 is None:
            b39 = plt.subplot()
            b46 = True
        else:
            b46 = False
        sns.regplot(b45, b44, b20 = b39)
        r, b47 = scipy.stats.pearsonr(b45, b44)
        b39.set_title(f"{modality} | R$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(b47):.2f}")
        if b46:
            if b29:
                plt.savefig(b29, b25 = "tight")
            else:
                plt.show()
            plt.close()
        return r**2, b47, b43
    def fonk10(self, b29 = None):
        b48 = {}
        fig, b20 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b20[3, 1])
        a1 = 0
        for omic in self.b7.keys():
            b21 = b20[a1
            r_sq, p_val, b43 = self.fonk9(omic, b21)
            b48[omic] = {'r_squared': r_sq, 'p-value': p_val}
            a1 += 1
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b49 = pd.DataFrame.from_dict(b48, orient='index')
        return b49
    def fonk11(self, b50 = None, b29=None):
        b51 = pd.concat([data.loc[self.b5].T for data in self.b7.values()]).T
        if b50 is not None:
            b51 = b51[b50]
        b51 = b51.loc[:, b51.std() > 0].apply(scipy.stats.zscore)
        b41 = self.b3.loc[self.b4.index]
        b42 = [(self.b1 != patient).index.values for patient in self.b1.unique()]
        b52 = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        b44 = []
        b45 = []
        for train_index, test_index in b42:
            b52.fit(b51.iloc[train_index], b41[train_index])
            b44.extend(b52.predict(b51.iloc[test_index]))
            b45.extend(b41[test_index])
        sns.regplot(b45, b44)
        r, b47 = scipy.stats.pearsonr(b45, b44)
        plt.title(f"r$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(b47):.2f}")
        if b29:
            plt.savefig(b29, b25 = "tight")
        else:
            plt.show()
        plt.close()
        return r**2, b47, b52
if b53 = = "__main__":
    b54 = "path_to_your_data"
    b55 = class1(b54)
    print(b55.fonk2())
    b18, b56 = b55.fonk4()
    print(b18)
    b55.fonk5(b19 = b56, b29='./Figures/within_between_donor_comparisons.png')
    for omic in b55.b7.keys():
        b55.fonk8(omic, b29 = f'./Figures/{omic}_pca.png')
    b57 = b55.fonk10(b29='./Figures/elastic_net_by_omics.png')
    print(b57)
    r2, b47, b58 = b55.fonk11(b50=b57.index, b29='./Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, b59 = b55.fonk11(b29='./Figures/elastic_net_all_omics_predictions.png')