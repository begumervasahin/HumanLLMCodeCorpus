import pandas as pd
import numpy as np
import math
import scipy
import seaborn as sns
import skbio
from scipy import stats
from sklearn import decomposition, linear_model
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
sns.set_style("white")
class class1():
    '''Multi-omic data from Ghaemi et al (2018) and methods to further analyze the data.
    Data is taken from .csv files that were created from the raw .Rda file
    Args:
        Folder in which the raw data (from the .Rda file) is split into .csv files.
    Attributes:
        b1 (pandas.Series): ID of patient of each sample
        b2 (pandas.Series): Trimester in which the sample was taken from.
        b4 (pandas.Series): Indices of the 51 b17 during gestation.
        b3 (pandas.Series): Weeks of pregnancy from the beginning
        b5 (pandas.Series): IDs of b17 taken during gestation
        b7 (dict): Dictionary in which keys are the omic measures and values point to the raw data.
    '''
    def fonk1(self, folder):
        self.b1 = pd.read_csv(folder + '/' + 'featurepatients.csv', squeeze=True)
        self.b2 = pd.read_csv(folder + '/' + 'featuretimes.csv', squeeze=True)
        self.b3 = pd.read_csv(folder + '/' + 'featureweeks.csv', squeeze=True)
        self.b4 = pd.read_csv(folder + '/' + 'b4.csv', squeeze=True)
        self.b5 = pd.Series(map('_'.join, zip(self.b1.astype(str), self.b2.astype(str))))
        b6 = ['CellfreeRNA', 'PlasmaLuminex', 'SerumLuminex', 'Microbiome', 'ImmuneSystem', 'Metabolomics', 'PlasmaSomalogic']
        self.b7 = {omic: pd.read_csv(folder + '/' + '{0}.csv'.format(omic), index_col=0) for omic in b6}
    def fonk2(self):
        '''Returns a table that describes the dimensions of each omic dataset
        Args:
            None
        Returns:
            b10 (pandas.DataFrame): a table in which indices are the names of the dataset and
                                                b11 detail the number of b17 and number of features
        '''
        b8 = {}
        for omic in self.b7.keys():
            omic_rows, b9 = self.b7[omic].shape
            b8[omic] = [omic_rows, b9]
        b10 = pd.DataFrame.from_dict(b8, orient='b16')
        b10.b11 = ['b17', 'features']
        return b10
    def fonk3(self, trimester):
        '''Given a valid trimester (1, 2, or 3), return the IDs of b17 from that trimester
        Args:
            trimester (int): pregnancy trimester (1, 2, or 3)
        Returns:
            b17 (numpy.array): b17 from the given trimester
        '''
        if trimester not in range(1, 4):
            print('ERROR: not a valid trimester, please input a value of 1 through 3')
            return None
        else:
            return self.b5[self.b2 = = trimester].values
    def fonk4(self):
        '''Perform PERMANOVA analysis on the pairwise Euclidean distance matrix for each omic measure by sample and trimester
        Args:
            None
        Returns:
            b21 (pandas.DataFrame): table of p-values; first column is between donor comparison and second column is between b2
            b13 (pandas.DataFrame): dictionary of pairwise Euclidean distances between b17; keys are omic dataset names and values are distance matrices
        '''
        b12 = {}
        b13 = {}
        for omic in self.b7.keys():
            b14 = self.b7[omic].copy()
            b14 = b14.loc[self.b5, :]
            b15 = squareform(pdist(b14.values, metric='euclidean'))
            b15 = pd.DataFrame(b15)
            b15.b16 = b14.b16
            b15.b11 = b14.b16
            b17 = b15.b16.str.split('_').str[0]
            b2 = b15.b16.str.split('_').str[1]
            b18 = skbio.DistanceMatrix(b15, ids=b15.b16)
            b19 = skbio.stats.distance.fonk4(b18, b2, permutations=999)
            b20 = skbio.stats.distance.fonk4(b18, b17, permutations=999)
            b12[omic] = {'pval_trimester': b19['p-value'], 'pval_donor': b20['p-value']}
            b13[omic] = b15
        b21 = pd.DataFrame.from_dict(b12, orient='b16')
        return b21, b13
    def fonk5(self, b22 = None, comparison='donor_comparison', b33=None):
        '''Create boxplot and stripplot of within group and between group comparisons
        Args:
            b22 (dict): dictionary where keys are omic types and values are pairwise distance matrices
            comparison (str): types of comparison to be made (donor_comparison, trimester_comparison)
            b33 (str): filename to which the final b56 should be saved to
        Returns:
            None
        '''
        def fonk6(row, col1, col2):
            '''Helper function to identify comparison type (within group vs between group) based on inputted row and column
            Args:
                row (pandas.Series): row describing the Euclidean distance between two b17
                col1 (str): column name of the first sample for comparison
                col2 (str): column name of the second sample for comparison
            '''
            if row[col1] == row[col2]:
                return 'within'
            else:
                return 'between'
        if b22 is None:
            pvals, b22 = self.fonk4()
        fig, b23 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b23[3,1])
        a1 = 0
        for omic in b22.keys():
            b24 = b23[a1
            a1 += 1
            b25 = b22[omic].reset_index().melt(id_vars='b16')
            b25 = b25[b25['b16'] != b25['variable']]
            b25['donor1'] = b25['b16'].str.split('_').str.get(0)
            b25['trimester1'] = b25['b16'].str.split('_').str.get(1)
            b25['donor2'] = b25['variable'].str.split('_').str.get(0)
            b25['trimester2'] = b25['variable'].str.split('_').str.get(1)
            b26 = (b25['value'] == 0).sum()
            b25['donor_comparison'] = b25.apply(lambda x: fonk6(x, 'donor1', 'donor2'), b27 = 1)
            b25['trimester_comparison'] = b25.apply(lambda x: fonk6(x, 'trimester1', 'trimester2'), b27 = 1)
            b24 = sns.boxplot(x=comparison, y='value', order=['within', 'between'], data=b25, b23=b24, showfliers=False)
            b24 = sns.stripplot(x=comparison, y='value', order=['within', 'between'], data=b25, b23=b24)
            b24.set_title('{0} |'.format(omic))
        if b33 is not None:
            plt.savefig(b33, b28 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk7(self, modality, b29 = 25):
        '''Calculate the principal components of the inputted modality's raw data
        Args:
            modality (str): a valid omic measure (CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic)
            b29 (int): number of PC's to return, a2 = 25
        Returns:
            b32 (numpy.ndarray): a matrix of coordinates in principal component space (num_samples x b29)
            b14 (pandas.DataFrame): a DataFrame of z-score normalized data for the inputted modality
        '''
        b14 = self.b7.get(modality, None)
        if b14 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b14 = b14.loc[self.b5]
        b30 = self.b1[self.b4.b16]
        b31 = decomposition.PCA(n_components=b29)
        b32 = b31.fit_transform(b14)
        return b32, b14
    def fonk8(self, modality, b33 = None):
        '''Generate PCA plots, one by batch and one by individual donor, using the raw data of the input modality
        Args:
            modality (str): a valid omic measure (CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic)
            b33 (str): filename to which the final b56 should be saved to
        Returns:
            None: generates a figure of PC 1 and PC 2. The left b56 is colored by batch and the right b56 is colored by individual donor
        '''
        if modality not in self.b7:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        pca_results, b14 = self.fonk7(modality)
        b30 = self.b1[self.b4.b16]
        b34 = pd.DataFrame(pca_results)
        b34.b16 = b14.b16
        fig, (ax1, ax2) = plt.subplots(1, 2, b35 = True, figsize=(10, 5))
        b2 = self.b2.unique()
        b36 = dict(zip(b2, sns.color_palette('Set1', len(b2))))
        for period in b2:
            b37 = self.b2[self.b2 == period].b16
            b38 = b34.iloc[b37, :]
            ax1.scatter(b38.loc[:, 0], b38.loc[:, 1], b39 = 'trimester {0}'.format(period), color=b36[period])
        ax1.legend(b40 = [1,1])
        ax1.set_xlabel('PC1')
        ax1.set_ylabel('PC2')
        ax1.set_title('PCA of {0} by trimester'.format(modality))
        b41 = b30.unique()
        b42 = dict(zip(b41, sns.color_palette('tab20', len(b41))))
        for donor in b41:
            b37 = b30[b30 == donor].b16
            b38 = b34.iloc[b37, :]
            ax2.scatter(b38.loc[:, 0], b38.loc[:, 1], b39 = donor, color=b42[donor])
        ax2.legend(b40 = [1,1])
        ax2.set_xlabel('PC1')
        ax2.set_title('PCA of {0} by individual donor'.format(modality))
        if b33 is not None:
            plt.savefig(b33, b28 = "tight")
        else:
            plt.show()
        plt.close()
    def fonk9(self, modality, b43 = None, b33=None):
        ''' Build an elastic net model off of a single modality, plotting the prediction results
        Args:
            modality (str): a valid omic measure (CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic)
            b43 (matplotlib.axes): matplotlib subplot axes to which the b56 should be drawn to
            b33 (str): filename to which the final b56 should be saved to
        Returns:
            r_sq (float): R^2 value of the predictions
            b57 (float): p-value value of the predictions
            b52 (float): list of the b52 (alpha in R) in the final modes
            b53 (float): list of the b53 (alpha in R) in the final modes
            b54 (pandas.DataFrame): dataframe of the coefficient for each modality
        '''
        b14 = self.b7.get(modality, None).copy()
        if b14 is None:
            print('ERROR: not a valid -omic type, please input either: CellfreeRNA, PlasmaLuminex, SerumLuminex, Microbiome, ImmuneSystem, Metabolomics, PlasmaSomalogic')
            return None
        b44 = b14.loc[self.b5, :]
        b45 = self.b3.loc[self.b4.b16]
        b46 = self.b1.loc[self.b4.b16]
        b1 = self.b1.unique()
        b44 = b44.loc[:, b44.std() != 0]
        b44 = b44.apply(lambda x: scipy.stats.zscore(x))
        b47 = []
        for patient in b1:
            b48 = b46[b46 != patient].b16.values
            b49 = b46[b46 == patient].b16.values
            b47.append((b48, b49))
        b50 = []
        b51 = []
        b52 = []
        b53 = []
        b54 = []
        b55 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13), b68=5, max_iter=1000, n_jobs=8)
        for (train, test) in b47:
            b55.fit(b44.values[train], b45.values[train])
            b52.append(b55.l1_ratio_)
            b53.append(b55.alpha_)
            b50.extend(b55.predict(b44.values[test]))
            b51.extend(b45.values[test])
            b54.append(b55.coef_)
        if b43 is None:
            b43 = plt.subplot()
            b56 = True
        else:
            b56 = False
        seaborn.regplot(b51, b50, b23 = b43)
        r, b57 = scipy.stats.pearsonr(b51, b50)
        b43.set_title("{0} | R$^2$ = {1} | -log_10(p-val) = {2}".format(modality, numpy.round(r**2, 3), numpy.round(-numpy.log10(b57), 2)))
        if b56:
            if b33 is not None:
                plt.savefig(b33, b28 = "tight")
            else:
                plt.show()
            plt.close()
        b54 = pandas.DataFrame(b54)
        b54.b11 = b44.b11
        return r**2, b57, b52, b53, b54
    def fonk10(self, b33 = None):
        '''Plot the predictability of elastic net models for each omic measure as well as return a table of R^2 values
        Args:
            b33 (str): filename to which the final b56 should be saved to
        Returns:
            b62 (pandas.DataFrame): table of r-square values b16 by the name of the omic measure
            b59 (list): list of features that were used in any given elastic net model (both during cross validation and between b7)
        '''
        b58 = {}
        fig, b23 = plt.subplots(4, 2, figsize=(12, 15))
        fig.delaxes(b23[3,1])
        a1 = 0
        b59 = []
        for omic in self.b7.keys():
            b24 = b23[a1
            r_sq, p_val, l1_ratio_list, alpha_list, b60 = self.fonk9(omic, b24)
            b61 = b60.loc[:, b60.mean() > 0].b11
            b58[omic] = {'r_squared': r_sq, 'p-value':p_val, 'num_features_used': len(b61)}
            b59.extend(b61)
            a1 += 1
        if b33 is not None:
            plt.savefig(b33, b28 = "tight")
        else:
            plt.show()
        plt.close()
        b62 = pandas.DataFrame.from_dict(b58, orient='b16')
        return b62, b59
    def fonk11(self, b63 = None, b33=None):
        ''' Build an elastic net model using data from all omic measures, with the option of subsetting to specific features
        Args:
            b63 (list/array-like): OPTIONAL, features to subset the entire table by
            b33 (str): filename to which the final b56 should be saved to
        Returns:
            r_sq (float): R^2 value of the predictions
            b57 (float): p-value value of the predictions
            b54 (pandas.DataFrame): dataframe of the coefficient for each modality
        '''
        b64 = [data.loc[self.b5, :].T for data in self.b7.values()]
        b64 = pandas.concat(b64).T
        if b63 is not None:
            b64 = b64.loc[:, b63]
        b64 = b64.loc[:, b64.std() > 0]
        b64 = b64.apply(lambda x: scipy.stats.zscore(x))
        b45 = self.b3.loc[self.b4.b16]
        b46 = self.b1.loc[self.b4.b16]
        b1 = self.b1.unique()
        b47 = []
        for patient in b1:
            b48 = b46[b46 != patient].b16.values
            b49 = b46[b46 == patient].b16.values
            b47.append((b48, b49))
        b65 = []
        b66 = []
        b50 = []
        b51 = []
        b54 = []
        b67 = linear_model.ElasticNetCV(l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0], alphas=range(13),
                                  b68 = 5, max_iter=1000, n_jobs=8)
        for (train_index, test_index) in b47:
            b67.fit(b64.iloc[train_index, :], b45[train_index])
            b65.append(b67.l1_ratio_)
            b66.append(b67.alpha_)
            b50.extend(b67.predict(b64.iloc[test_index, :]))
            b51.extend(b45[test_index])
            b54.append(b67.coef_)
        seaborn.regplot(b51, b50)
        r, b57 = scipy.stats.pearsonr(b51, b50)
        plt.title('r$^2$ = {0} | -log_10(p-val) = {1}'.format(numpy.round(r**2, 3), numpy.round(-numpy.log10(b57), 2)))
        if b33 is not None:
            plt.savefig(b33, b28 = "tight")
        else:
            plt.show()
        plt.close()
        b54 = pandas.DataFrame(b54)
        b54.b11 = b64.b11
        return r**2, b57, b54
if b69 = = "__main__":
    print(gestation_multiomics.fonk2())
    b21, b70 = gestation_multiomics.fonk4()
    print(b21)
    gestation_multiomics.fonk5(b22 = b70,
                                                b33 = './Figures/within_between_donor_comparisons')
    for omic in gestation_multiomics.b7.keys():
        gestation_multiomics.fonk8(omic, b33 = './Figures/{0}_pca.png'.format(omic))
    r2_table, b71 = gestation_multiomics.fonk10(b33='./Figures/elastic_net_by_omics.png')
    print(r2_table)
    r2, b57, b54 = gestation_multiomics.fonk11(b33='./Figures/cross_omic_elastic_net.png')
    print('Cross-omic Elastic Net R^2: {0} | P-value: {1}'.format(r2, b57))