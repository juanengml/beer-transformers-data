# py-package/transformation/output_write.py

from datetime import datetime

def export_to_csv(df, filename_prefix='beer_data', path_output="output"):
    date_str = datetime.now().strftime('%Y%m%d')
    filename = f"{path_output}/{filename_prefix}_{date_str}.csv"
    df.to_csv(filename, index=False)
    return filename
