import platform
import pyperclip

class StatsData():
    """
    A class to perform statistics for Nexus
    """
    def __init__(self, df, driver_id, tag_id, start_date, end_date):
        """
        Defines the necessary parameters for calculations
        :param df: dataframe
            dataframe with variable data. Columns required: datetime as 'timestamp', 'value' and (opt) name
        :param driver_id: integer
        :param start_year: integer
        :param end_year: integer
        """
        self.df = df
        self.driver_id = driver_id
        self.tag_id = tag_id
        self.start_date = start_date
        self.end_date = end_date
        self.mask = (self.df['timeStamp'] >= self.start_date) & (self.df['timeStamp'] <= self.end_date)
        # Check char for datetime string
        if platform.system() == 'Windows':
            self.monthchar = '#'
        else:
            self.monthcar = '-'

    def statsday(self):
        df_year = self.df[self.mask]
        df_year.set_index('timeStamp', inplace=True)
        self.df_statsday = df_year['value'].resample('D').agg(['min', 'max', 'mean', 'std', 'sum', 'last'])
        self.df_statsday = self.df_statsday.fillna('NULL')
        self.df_statsday['query'] = 'insert into `statsdata_day_' + self.df_statsday.index.strftime('%Y') + \
                           '` (`DriverId`, `TagId`, `TS`, `MinVal`, `MaxVal`, `AvgVal`, `StdDevVal`, `SumVal`, `LastValueVal`)' \
                           ' values (' + str(self.driver_id) + ',' + str(self.tag_id) + ",\'" + \
                                self.df_statsday.index.strftime('%Y-%m-%d %H:%M:%S') + "\'," + \
                                self.df_statsday['min'].map('{:.5f}'.format) + ',' + \
                                self.df_statsday['max'].map('{:.5f}'.format) + ',' + \
                                self.df_statsday['mean'].map('{:.5f}'.format) + ',' + \
                                self.df_statsday['std'].map('{}'.format) + ',' + \
                                self.df_statsday['sum'].map('{:.5f}'.format) + ',' + \
                                self.df_statsday['last'].map('{:.5f}'.format) + ');'


    def statsmonth(self):
        df_year = self.df[self.mask]
        df_year.set_index('timeStamp', inplace=True)
        self.df_statsmonth = df_year['value'].resample('M').agg(['min', 'max', 'mean', 'std', 'sum', 'last'])
        self.df_statsmonth = self.df_statsmonth.fillna('NULL')
        self.df_statsmonth['query'] = 'insert into `statsdata_month_' + self.df_statsmonth.index.strftime('%Y') + \
                           '` (`DriverId`, `TagId`, `TS`, `MinVal`, `MaxVal`, `AvgVal`, `StdDevVal`, `SumVal`, `LastValueVal`)' \
                           ' values (' + str(self.driver_id) + ',' + str(self.tag_id) + ",\'" + \
                           self.df_statsmonth.index.strftime('%Y-%m-%d %H:%M:%S') + "\'," + \
                           self.df_statsmonth['min'].map('{:.5f}'.format) + ',' + \
                           self.df_statsmonth['max'].map('{:.5f}'.format) + ',' + \
                           self.df_statsmonth['mean'].map('{:.5f}'.format) + ',' + \
                           self.df_statsmonth['std'].map('{}'.format) + ',' + \
                           self.df_statsmonth['sum'].map('{:.5f}'.format) + ',' + \
                           self.df_statsmonth['last'].map('{:.5f}'.format) + ');'


    def print_queries(self):
        day_query = self.df_statsday['query'].to_list()
        day_query = '\n'.join(day_query)
        month_query = self.df_statsmonth['query'].to_list()
        month_query = '\n'.join(month_query)
        full_query = [day_query, month_query]
        full_query = '\n'.join(full_query)
        print(full_query)


    def copy_queries(self):
        day_query = self.df_statsday['query'].to_list()
        day_query = '\n'.join(day_query)
        month_query = self.df_statsmonth['query'].to_list()
        month_query = '\n'.join(month_query)
        full_query = [day_query, month_query]
        full_query = '\n'.join(full_query)
        pyperclip.copy(full_query)

