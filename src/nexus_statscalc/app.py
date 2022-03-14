from .read_df import read_df
from .gui import NexusGUI
from .statscalc import StatsData

def main():
    UI = NexusGUI()
    path = UI.get_path()
    df = read_df(path)
    names = df['name'].unique()
    vble = UI.choose_vble(names)
    print(vble)
    df = df[df['name']==vble]
    tag_id, driver_id = UI.options()
    start_date, end_date = UI.get_dates()
    statscalc = StatsData(df, driver_id, tag_id, start_date, end_date)
    statscalc.statsday()
    statscalc.statsmonth()
    statscalc.print_queries()
    statscalc.copy_queries()
    UI.show_message_done()