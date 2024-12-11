import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import decomposition, linear_model
from scipy.spatial.distance import squareform, pdist
import skbio
import scipy.stats as stats
sns.set_style("white")
class class1:
    def fonk1(self, folder):
        self.fonk2(folder)
    def fonk2(self, folder):
        self.b1 = pd.read_csv(folder + '/featurepatients.csv', squeeze=True)
        self.b2 = pd.read_csv(folder + '/featuretimes.csv', squeeze=True)
        self.b3 = pd.read_csv(folder + '/featureweeks.csv', squeeze=True)
        self.b4 = pd.read_csv(folder + '/b4.csv', squeeze=True)
        self.b5 = self.b1.astype(str) + '_' + self.b2.astype(str)
        b6 = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.b7 = {omic: pd.read_csv(folder + '/{}.csv'.format(omic), index_col=0) for omic in b6}
    def fonk3(self):
        b8 = {omic: [data.shape[0], data.shape[1]] for omic, data in self.b7.items()}
        b9 = pd.DataFrame.from_dict(b8, orient='b13', b14=['b15', 'features'])
        return b9
    def fonk4(self, trimester):
        if trimester not in range(1, 4):
            raise ValueError('Invalid trimester. Please input a value between 1 and 3.')
        return self.b5[self.b2 = = trimester].values
    def fonk5(self):
        b10 = {}
        b11 = {}
        for omic, data in self.b7.items():
            b12 = pd.DataFrame(squareform(pdist(data.loc[self.b5].values, metric='euclidean')))
            b12.b13 = self.b5
            b12.b14 = self.b5
            b15 = b12.b13.str.split('_').str[0]
            b2 = b12.b13.str.split('_').str[1]
            b16 = skbio.DistanceMatrix(b12, ids=b12.b13)
            b17 = skbio.stats.distance.fonk5(b16, b2, permutations=999)
            b18 = skbio.stats.distance.fonk5(b16, b15, permutations=999)
            b10[omic] = {'pval_trimester': b17['p-value'], 'pval_donor': b18['p-value']}
            b11[omic] = b12
        b19 = pd.DataFrame.from_dict(b10, orient='b13')
        return b19, b11
    def fonk6(self, b20 = None, comparison='donor_comparison', b30=None):
        if b20 is None:
            pvals, b20 = self.fonk5()
        fig, b21 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b21[3, 1])
        a1 = 0
        for omic, b12 in b20.items():
            b22 = b21[a1
            a1 += 1
            b23 = b12.reset_index().melt(id_vars='b13')
            b23 = b23[b23['b13'] != b23['variable']]
            b23['donor1'] = b23['b13'].str.split('_').str[0]
            b23['trimester1'] = b23['b13'].str.split('_').str[1]
            b23['donor2'] = b23['variable'].str.split('_').str[0]
            b23['trimester2'] = b23['variable'].str.split('_').str[1]
            b23['donor_comparison'] = np.where(b23['donor1'] == b23['donor2'], 'within', 'between')
            b23['trimester_comparison'] = np.where(b23['trimester1'] == b23['trimester2'], 'within', 'between')
            sns.boxplot(b24 = comparison, y='value', order=['within', 'between'], data=b23, b21=b22, showfliers=False)
            sns.stripplot(b24 = comparison, y='value', order=['within', 'between'], data=b23, b21=b22)
            b22.set_title('{} |'.format(omic))
        if b30:
            plt.savefig(b30, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk7(self, modality, b26 = 25):
        b27 = self.b7.get(modality, None)
        if b27 is None:
            raise ValueError('Invalid modality. Please choose one of: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
        b27 = b27.loc[self.b5]
        b28 = decomposition.PCA(n_components=b26)
        b29 = b28.fit_transform(b27)
        return b29, b27
    def fonk8(self, modality, b30 = None):
        pca_results, b27 = self.fonk7(modality)
        b31 = pd.DataFrame(pca_results, b13=b27.b13)
        fig, (ax1, ax2) = plt.subplots(1, 2, b32 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        for period in b2:
            b33 = self.b2[self.b2 == period].b13
            ax1.scatter(b31.loc[b33, 0], b31.loc[b33, 1], b34 = 'trimester {}'.format(period))
        ax1.legend(b35 = [1, 1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title('PCA of {} by trimester'.format(modality))
        b36 = self.b1.unique()
        for donor in b36:
            b33 = self.b1[self.b1 == donor].b13
            ax2.scatter(b31.loc[b33, 0], b31.loc[b33, 1], b34 = donor)
        ax2.legend(b35 = [1, 1])
        ax2.set_xlabel('PC1')
        ax2.set_title('PCA of {} by individual donor'.format(modality))
        if b30:
            plt.savefig(b30, b25 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk9(self, modality, b37 = None, b30=None):
        b27 = self.b7.get(modality, None)
        if b27 is None:
            raise ValueError('Invalid modality. Please choose one of: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
        b38 = b27.loc[self.b5]
        b38 = b38.loc[:, b38.std() != 0]
        b38 = b38.apply(stats.zscore)
        b39 = [(self.b1[self.b1 != patient].b13.values, self.b1[self.b1 == patient].b13.values) for patient in self.b1.unique()]
        b40 = []
        b41 = []
        b42 = []
        b43 = []
        b44 = []
        b45 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), b57=5, max_iter=1000, n_jobs=-1)
        for (train, test) in b39:
            b45.fit(b38.values[train], self.b3.values[train])
            b42.append(b45.l1_ratio_)
            b43.append(b45.alpha_)
            b40.extend(b45.predict(b38.values[test]))
            b41.extend(self.b3.values[test])
            b44.append(b45.coef_)
        if b37 is None:
            b37 = plt.subplot()
        sns.regplot(b41, b40, b21 = b37)
        r, b46 = stats.pearsonr(b41, b40)
        b37.set_title("{} | R$^2$ = {:.3f} | -log_10(p-val) = {:.2f}".format(modality, r ** 2, -np.log10(b46)))
        if b30:
            plt.savefig(b30, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b44 = pd.DataFrame(b44, b14=b38.b14)
        return r ** 2, b46, b42, b43, b44
    def fonk10(self, b30 = None):
        b47 = {}
        fig, b21 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b21[3, 1])
        a1 = 0
        b48 = []
        for omic in self.b7.keys():
            b22 = b21[a1
            r_sq, p_val, l1_ratio_list, alpha_list, b49 = self.fonk9(omic, b37=b22)
            b50 = b49.loc[:, b49.mean() > 0].b14
            b47[omic] = {'r_squared': r_sq, 'p-value': p_val, 'num_features_used': len(b50)}
            b48.extend(b50)
            a1 += 1
        if b30:
            plt.savefig(b30, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b51 = pd.DataFrame.from_dict(b47, orient='b13')
        return b51, b48
    def fonk11(self, b52 = None, b30=None):
        b53 = pd.concat([data.loc[self.b5, :].T for data in self.b7.values()], axis=1)
        if b52 is not None:
            b53 = b53.loc[:, b52]
        b53 = b53.loc[:, b53.std() > 0]
        b53 = b53.apply(stats.zscore)
        b39 = [(self.b1[self.b1 != patient].b13.values, self.b1[self.b1 == patient].b13.values) for patient in self.b1.unique()]
        b54 = []
        b55 = []
        b40 = []
        b41 = []
        b44 = []
        b56 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                          b57 = 5, max_iter=1000, n_jobs=-1)
        for (train_index, test_index) in b39:
            b56.fit(b53.iloc[train_index, :], self.b3[train_index])
            b54.append(b56.l1_ratio_)
            b55.append(b56.alpha_)
            b40.extend(b56.predict(b53.iloc[test_index, :]))
            b41.extend(self.b3[test_index])
            b44.append(b56.coef_)
        sns.regplot(b41, b40)
        r, b46 = stats.pearsonr(b41, b40)
        plt.title('r$^2$ = {:.3f} | -log_10(p-val) = {:.2f}'.format(r ** 2, -np.log10(b46)))
        if b30:
            plt.savefig(b30, b25 = "tight")
        else:
            plt.show()
        plt.close()
        b44 = pd.DataFrame(b44, b14=b53.b14)
        return r ** 2, b46, b44
if b58 = = "__main__":
    b59 = class1('data_folder')
    print(b59.fonk3())
    b19, b60 = b59.fonk5()
    print(b19)
    b59.fonk6(b20 = b60, b30='./Figures/within_between_donor_comparisons')
    for omic in b59.b7.keys():
        b59.fonk8(omic, b30 = './Figures/{}_pca.png'.format(omic))
    r2_table, b61 = b59.fonk10(b30='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, b46, b44 = b59.fonk11(b30='./Figures/cross_omic_elastic_net.png')
    print('Cross-omic Elastic Net R^2: {} | P-value: {}'.format(r2, b46))