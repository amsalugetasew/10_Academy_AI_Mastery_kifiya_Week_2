import pandas as pd

class NoiseHandling:
    @staticmethod
    def check_missed_greater_than_3(df: pd.DataFrame, min_value: int = 0, max_value: int = 3):
        """
        Identifies columns with null values greater than min_value and less than max_value.

        Parameters:
        df (pd.DataFrame): The DataFrame to check.
        min_value (int): The minimum number of missing values to include a column.
        max_value (int): The maximum number of missing values to include a column.

        Returns:
        tuple: A tuple containing:
            - A list of column names with missing values > min_value and < max_value.
            - A DataFrame containing rows with missing values in those columns.
        """
        columns_with_few_nulls = df.columns[(df.isnull().sum() < max_value) & (df.isnull().sum() > min_value)]
        print(f"Total Number of columns that have missing value > {min_value} and < {max_value} is equal to: {len(columns_with_few_nulls)}")
        return columns_with_few_nulls.tolist(), df[df[columns_with_few_nulls].isna().any(axis=1)]

    @staticmethod
    def handling_cols_with_missed_values_less_than_3(df: pd.DataFrame, column_names: list):
        """
        Drops rows with missing values in the specified columns.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        column_names (list): A list of column names to check for missing values.

        Returns:
        pd.DataFrame: The DataFrame with rows dropped.
        """
        missing_columns = [col for col in column_names if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")
        print(f"Dropping rows with missing values in columns: {column_names}")
        return df.dropna(subset=column_names)

    @staticmethod
    def common_missed_of_subscribers(df: pd.DataFrame, column_names: list):
        """
        Drops rows where all of the specified columns are missing.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        column_names (list): A list of column names to check for missing values.

        Returns:
        pd.DataFrame: The DataFrame with rows dropped where all specified columns are NaN.
        """
        missing_columns = [col for col in column_names if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")
        print(f"Dropping rows where all of the following columns are missing: {column_names}")
        df.dropna(subset=column_names, how='all', inplace=True)
        return df
    
    @staticmethod
    def null_columns_greater_than_0(df: pd.DataFrame):
        """
        Identifies columns with null values greater than 0 and prints their count.

        Parameters:
        df (pd.DataFrame): The DataFrame to check.

        Returns:
        pd.Series: A Series with the count of missing values for each column with nulls.
        """
        null_columns_greater_than_0 = df.columns[(df.isnull().sum() > 0)]
        print(df[null_columns_greater_than_0].isna().sum().shape)
        return df[null_columns_greater_than_0].isna().sum()


    @staticmethod
    def fill_nulls_by_imsi_group(df: pd.DataFrame):
        """
        Replace null values in 'MSISDN/Number' and 'IMEI' columns with values from the same IMSI group.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.

        Returns:
        pd.DataFrame: The DataFrame with null values filled.
        """
        if 'IMSI' in df.columns:
            print("Filling missing 'MSISDN/Number' and 'IMEI' by IMSI group...")
            
            # Fill missing 'MSISDN/Number' using the same IMSI group
            df['MSISDN/Number'] = df.groupby('IMSI')['MSISDN/Number'].transform(lambda x: x.fillna(method='pad'))

            # Fill missing 'IMEI' using the same IMSI group
            df['IMEI'] = df.groupby('IMSI')['IMEI'].transform(lambda x: x.fillna(method='pad'))
        else:
            print("IMSI column is missing from the DataFrame, unable to fill null values.")
        return df