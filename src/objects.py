import pandas as pd
from functools import reduce

from error_handler import WrongDFAmountError

class Deduplicator():

    #*******************************************************************
    # Duplicator Object
    #
    # Inputs: 
    #       input_list: list: list containing paths of files to process
    # Outputs:
    #       pandas.DataFrame()
    #
    # IMPORTANT NOTES:
    #       - For method get_new_rows, the order of input_list matters due to the
    #         logic with left joins. So, the first DF must be the DF we are checking
    #         for new rows. All DFs following the first DF should be a subset of the
    #         first DF.
    #*******************************************************************

    def __init__(self, input_list):
        self.df_paths = input_list

        self.dfs = []
        self._load_data()

    def get_new_rows(self):
        new_row_df = reduce(self._merge_dfs, self.dfs)
        print('Found {} rows in {} that are not in {}'.format(len(new_row_df), self.df_paths[0], self.df_paths[1:]))
        return new_row_df

    def dedupe_single_df(self):
        self._check_one_df_provided()
        dedupe_df = self.dfs[0].drop_duplicates(ignore_index=True)
        print('Found {} duplicate rows in {}'.format(len(self.dfs[0])-len(dedupe_df), self.df_paths[0]))
        return dedupe_df

    def _merge_dfs(self, df1, df2):
        merged_df = pd.merge(df1,df2, how='left', indicator='merge')
        return merged_df.loc[merged_df['merge'] == 'left_only'].drop('merge', 1).reset_index(drop=True)

    def _load_data(self):
        self.dfs = [pd.read_csv(df_path) for df_path in self.df_paths]

    def _check_one_df_provided(self):
        if len(self.dfs) > 1:
            raise WrongDFAmountError