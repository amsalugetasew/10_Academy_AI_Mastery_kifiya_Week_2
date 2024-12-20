import matplotlib.pyplot as plt

class Plot:
    def __init__(self, dataframe):
        """
        Initialize the Plot class with a dataframe.

        Parameters:
        dataframe (pd.DataFrame): The dataframe to analyze and plot.
        """
        self.dataframe = dataframe

    def distribution_of_missing_values(self, column_names):
        """
        Plot the distribution of missing values for the specified columns.

        Parameters:
        column_names (list): List of column names to check for missing values.
        """
        # Check for missing values in the specified columns
        null_columns = self.dataframe[column_names]
        constant_values = (null_columns.isnull().sum())

        # Calculate percentages
        total = constant_values.sum()
        percentages = (constant_values / total) * 100 if total > 0 else [0] * len(constant_values)

        # Bar plot for constant/zero values
        ax = constant_values.plot(kind='barh', figsize=(10, 8), color='orange')

        # Add number and percentage annotations
        for bar, percentage in zip(ax.patches, percentages):
            width = bar.get_width()
            y = bar.get_y() + bar.get_height() / 2
            annotation = f'{int(width)} ({percentage:.2f}%)'
            ax.annotate(annotation, xy=(width, y), xytext=(5, 0),
                        textcoords="offset points", ha='left', va='center')

        # Add labels and title
        plt.title("Distribution of Missing Values Per Column")
        plt.xlabel("Frequency")
        plt.ylabel("Columns")
        plt.xticks(rotation=45)
        plt.show()
