import vaex

file_path = "stocks_archive_5years.zip"
file_output = "dump.csv"
sort_columns = "high"
limit = 30
group_by_name = False
order = 'AAL'
filename='dump.csv'


def select_sorted(sort_columns_f = sort_columns, limit_f = limit, group_by_name_f = group_by_name, order_f = order, filename_f = filename):
    dv = vaex.from_csv(file_path, convert=True)
    dvv = dv[dv.Name == order_f]
    dvv = dvv.sort(sort_columns_f, ascending=False)
    dvv[0:limit_f].export_csv(filename_f)
