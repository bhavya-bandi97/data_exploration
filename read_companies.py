import pandas as pd


def read_companies():
    df = pd.read_csv('C:/Users/Bhavya/Desktop/projects/companies.csv')
    print("Column names: ", df.columns.to_list())
    print("First 5 rows of the DataFrame:")
    print(df.head())
    print("Data types of each column:")
    print(df.dtypes)
    print("rename columns")
    df = df.rename(columns={'Revenue (USD billions)': 'Revenue_USD_billions', 'Employees': 'Employees_count'})
    print("DataFrame after renaming columns:")
    print(df.columns)
    print("changing data types")
    df = df.astype({'Name': 'string', 'Industry': 'string'})
    print("Data types after conversion:")
    print(df.dtypes)
    df[['City', 'State']] = df['Headquarters'].str.split(',', expand=True)
    print("DataFrame after splitting 'Headquarters' into 'City' and 'State':")
    print(df)
    print("top 3 companies by revenue:")
    print(df.nlargest(3, 'Revenue_USD_billions')[['Name', 'Revenue_USD_billions']])
    print(df[['Name', 'Industry', 'Revenue_USD_billions', 'Employees_count']])
    print("remove duplicates")
    df = df.drop_duplicates(subset=['Name'])
    print("top revenue company in each industry, if there is only one company in the industry, it will be included")
    df_top_industry = df.loc[df.groupby('Industry')['Revenue_USD_billions'].idxmax()]
    print(df_top_industry[['Industry', 'Name', 'Revenue_USD_billions']].sort_values(by='Revenue_USD_billions', ascending=False))
    
    

read_companies()
