class univariate():
    def quanQual(dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if dataset[columnName].dtypes=='O':
                #print("Qual")
                Qual.append(columnName)
            else:
                #print("Quan")
                Quan.append(columnName)
        return Quan,Qual

    def freqTable(ColumnName,dataset):
        FrequencyTable = pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","CumulativeSum"])
        FrequencyTable["Unique_Values"]=dataset[ColumnName].value_counts().index
        FrequencyTable["Frequency"]=dataset[ColumnName].value_counts().values
        FrequencyTable["Relative_Frequency"]=(FrequencyTable["Frequency"]/103)
        FrequencyTable["CumulativeSum"]=FrequencyTable["Relative_Frequency"].cumsum()
        return FrequencyTable
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q5:99%","Q4:100%","IQR","1.5Rule","Lesser","Greater","max","min",,"Kurtosis","skewness","var","StandardDeviation"],columns=quan)
        for ColumnName in quan:
            descriptive.loc["Mean",ColumnName]=dataset[ColumnName].mean()
            descriptive.loc["Median",ColumnName]=dataset[ColumnName].median()
            descriptive.loc["Mode",ColumnName]=dataset[ColumnName].mode()[0]
            descriptive.loc["Q1:25%",ColumnName]=dataset[ColumnName].quantile(0.25)
            descriptive.loc["Q2:50%",ColumnName]=dataset[ColumnName].quantile(0.50)
            descriptive.loc["Q3:75%",ColumnName]=dataset[ColumnName].quantile(0.75)
            descriptive.loc["Q5:99%",ColumnName]=dataset[ColumnName].quantile(0.99)
            descriptive.loc["Q4:100%",ColumnName]=dataset[ColumnName].max()
            descriptive.loc["IQR",ColumnName]=descriptive.loc["Q3:75%",ColumnName]-descriptive.loc["Q1:25%",ColumnName]
            descriptive.loc["1.5Rule",ColumnName]=1.5*descriptive.loc["IQR",ColumnName]
            descriptive.loc["IQR",ColumnName]=descriptive.loc["Q3:75%",ColumnName]-descriptive.loc["Q1:25%",ColumnName]
            descriptive.loc["1.5Rule",ColumnName]=1.5*descriptive.loc["IQR",ColumnName]
            descriptive.loc["Lesser",ColumnName]=descriptive.loc["Q1:25%",ColumnName]-descriptive.loc["1.5Rule",ColumnName]
            descriptive.loc["Greater",ColumnName]=descriptive.loc["Q3:75%",ColumnName]+descriptive.loc["1.5Rule",ColumnName]
            descriptive.loc["max",ColumnName]=dataset[ColumnName].max()
            descriptive.loc["min",ColumnName]=dataset[ColumnName].min()
            descriptive.loc["Kurtosis",ColumnName]=dataset[ColumnName].kurtosis()
            descriptive.loc["skewness",ColumnName]=dataset[ColumnName].skew()
            descriptive.loc["var",ColumnName]=dataset[ColumnName].var()
            descriptive.loc["StandardDeviation",ColumnName]=dataset[ColumnName].std()
        return descriptive
        