def clean_TT(df1):
    df1 = df1.drop(columns=["Unnamed: 0", "Unnamed: 7",
                            "Unnamed: 8", "Unnamed: 9"], )
    drop_these = []
    shape = df1.shape
    for i in range(0, shape[0]):
        if (i > 3 and i < 13):
            continue
        drop_these.append(i)
    df1 = df1.drop(drop_these)
    df1 = df1.reset_index(drop=True)
    cols = df1.iloc[0, :]
    df1.columns = cols
    df1 = df1.drop(0)
    df1 = df1.reset_index()
    df1 = df1.drop(columns='index')
    df1.iloc[2, :] = df1.iloc[2, :].fillna('RECESS')
    df1.iloc[5, :] = df1.iloc[5, :].fillna('RECESS')
    df1.fillna(method='ffill', inplace=True)
    df1.iloc[4, 0] = '01:50 - 02:40'
    return df1
