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
        b6 = [
            'CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex',
            'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic'
        ]
        self.b7 = {omic: pd.read_csv(f"{b54}/{omic}.csv", index_col=0) for omic in b6}
    def fonk2(self):
        b8 = {omic: data.shape for omic, data in self.b7.items()}
        return pd.DataFrame.from_dict(b8, b9 = 'b15', columns=['b16', 'features'])
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
            b13 = pd.DataFrame(
                squareform(pdist(b12.values, b14 = 'euclidean')),
                b15 = b12.b15, columns=b12.b15
            )
            b16 = b13.b15.str.split('_').str[0]
            b2 = b13.b15.str.split('_').str[1]
            b17 = DistanceMatrix(b13, ids=b13.b15)
            b18 = fonk4(b17, b2, permutations=999)['p-value']
            b19 = fonk4(b17, b16, permutations=999)['p-value']
            b10[omic] = {'pval_trimester': b18, 'pval_donor': b19}
            b11[omic] = b13
        return pd.DataFrame.from_dict(b10, b9 = 'b15'), b11
    def fonk5(self, b20 = None, comparison='donor_comparison', b30=None):
        def fonk6(row, col1, col2):
            return 'within' if row[col1] == row[col2] else 'between'
        if b20 is None:
            _, b20 = self.fonk4()
        fig, b21 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b21[3, 1])
        a1 = 0
        for omic, b13 in b20.items():
            b22 = b21[a1
            b23 = b13.reset_index().melt(id_vars='b15')
            b23 = b23[b23['b15'] != b23['variable']]
            b23['donor1'] = b23['b15'].str.split('_').str.get(0)
            b23['trimester1'] = b23['b15'].str.split('_').str.get(1)
            b23['donor2'] = b23['variable'].str.split('_').str.get(0)
            b23['trimester2'] = b23['variable'].str.split('_').str.get(1)
            b23['donor_comparison'] = b23.apply(lambda b25: fonk6(b25, 'donor1', 'donor2'), b24 = 1)
            b23['trimester_comparison'] = b23.apply(lambda b25: fonk6(b25, 'trimester1', 'trimester2'), b24 = 1)
            sns.boxplot(b25 = comparison, y='value', order=['within', 'between'], data=b23, b21=b22, showfliers=False)
            sns.stripplot(b25 = comparison, y='value', order=['within', 'between'], data=b23, b21=b22)
            b22.set_title(omic)
            a1 += 1
        if b30:
            plt.savefig(b30, b26 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk7(self, modality, b27 = 25):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b12 = b12.loc[self.b5]
        b28 = decomposition.PCA(n_components=b27)
        b29 = b28.fit_transform(b12)
        return b29, b12
    def fonk8(self, modality, b30 = None):
        pca_results, b12 = self.fonk7(modality)
        b31 = pd.DataFrame(pca_results, b15=b12.b15)
        fig, (ax1, ax2) = plt.subplots(1, 2, b32 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b33 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b34 = self.b2[self.b2 == period].b15
            b35 = b31.iloc[b34]
            ax1.scatter(b35[0], b35[1], b36 = f'trimester {period}', color=b33[period])
        sns.despine()
        ax1.legend(b37 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title(f'PCA of {modality} by trimester')
        b38 = self.b1.unique()
        b39 = dict(zip(b38, sns.color_palette('tab20', len(b38))))
        for donor in b38:
            b34 = self.b1[self.b1 == donor].b15
            b35 = b31.iloc[b34]
            ax2.scatter(b35[0], b35[1], b36 = donor, color=b39[donor])
        sns.despine()
        ax2.legend(b37 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title(f'PCA of {modality} by individual donor')
        if b30:
            plt.savefig(b30, b26 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk9(self, modality, b40 = None, b30=None):
        b12 = self.b7.get(modality)
        if b12 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b41 = b12.loc[self.b5]
        b42 = self.b3.loc[self.b4.b15]
        b41 = b41.loc[:, b41.std() != 0].apply(scipy.stats.zscore)
        b43 = [(self.b1 != patient).b15.values for patient in self.b1.unique()]
        b44 = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        b45 = []
        b46 = []
        for train_index, test_index in b43:
            b44.fit(b41.iloc[train_index], b42[train_index])
            b45.extend(b44.predict(b41.iloc[test_index]))
            b46.extend(b42[test_index])
        if b40 is None:
            b40 = plt.subplot()
            b47 = True
        else:
            b47 = False
        sns.regplot(b46, b45, b21 = b40)
        r, b48 = scipy.stats.pearsonr(b46, b45)
        b40.set_title(f"{modality} | R$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(b48):.2f}")
        if b47:
            if b30:
                plt.savefig(b30, b26 = "tight")
            else:
                plt.show()
            plt.close()
        return r**2, b48, b44
    def fonk10(self, b30 = None):
        b49 = {}
        fig, b21 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b21[3, 1])
        a1 = 0
        for omic in self.b7.keys():
            b22 = b21[a1
            r_sq, p_val, b44 = self.fonk9(omic, b22)
            b49[omic] = {'r_squared': r_sq, 'p-value': p_val}
            a1 += 1
        if b30:
            plt.savefig(b30, b26 = "tight")
        else:
            plt.show()
        plt.close()
        return pd.DataFrame.from_dict(b49, b9 = 'b15')
    def fonk11(self, b50 = None, b30=None):
        b51 = pd.concat([data.loc[self.b5].T for data in self.b7.values()]).T
        if b50 is not None:
            b51 = b51[b50]
        b51 = b51.loc[:, b51.std() > 0].apply(scipy.stats.zscore)
        b42 = self.b3.loc[self.b4.b15]
        b43 = [(self.b1 != patient).b15.values for patient in self.b1.unique()]
        b52 = linear_model.ElasticNetCV(l1_ratio=np.linspace(0.1, 1.0, 10), alphas=range(1, 14), cv=5, max_iter=1000, n_jobs=-1)
        b45 = []
        b46 = []
        for train_index, test_index in b43:
            b52.fit(b51.iloc[train_index], b42[train_index])
            b45.extend(b52.predict(b51.iloc[test_index]))
            b46.extend(b42[test_index])
        sns.regplot(b46, b45)
        r, b48 = scipy.stats.pearsonr(b46, b45)
        plt.title(f"r$^2$ = {r**2:.3f} | -log_10(p-val) = {-np.log10(b48):.2f}")
        if b30:
            plt.savefig(b30, b26 = "tight")
        else:
            plt.show()
        plt.close()
        return r**2, b48, b52
if b53 = = "__main__":
    b54 = "path_to_your_data"
    b55 = class1(b54)
    print(b55.fonk2())
    permanova_df, b56 = b55.fonk4()
    print(permanova_df)
    b55.fonk5(b20 = b56, b30='./Figures/within_between_donor_comparisons.png')
    for omic in b55.b7.keys():
        b55.fonk8(omic, b30 = f'./Figures/{omic}_pca.png')
    b57 = b55.fonk10(b30='./Figures/elastic_net_by_omics.png')
    print(b57)
    r2, b48, b58 = b55.fonk11(b50=b57.b15, b30='./Figures/elastic_net_top_features.png')
    r2_all_omics, pval_all_omics, b59 = b55.fonk11(b30='./Figures/elastic_net_all_omics_predictions.png')