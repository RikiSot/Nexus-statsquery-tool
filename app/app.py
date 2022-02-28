import read_df, gui
import statscalc as stc

def main():
    UI = gui.NexusGUI()
    path = UI.get_path()
    df = read_df.read_df(path)
    names = df['name'].unique()
    vble = UI.choose_vble(names)
    print(vble)
    df = df[df['name']==vble]
    tag_id, driver_id = UI.options()
    start_date, end_date = UI.get_dates()
    statscalc = stc.StatsData(df, driver_id, tag_id, start_date, end_date)
    statscalc.statsday()
    statscalc.statsmonth()
    statscalc.print_queries()
    statscalc.copy_queries()
    UI.show_message_done()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


