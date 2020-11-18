import pandas as pd

###########################
# get data to be appended
df_append = pd.read_excel('test2.xlsx')

# define what sheets to update
to_update = {"Sheet1": df_append}

# load existing data
file_name = "AstroTest.xlsx"
excel_reader = pd.ExcelFile(file_name)

# write and update
excel_writer = pd.ExcelWriter(file_name)

for sheet in excel_reader.sheet_names:
    sheet_df = excel_reader.parse(sheet)
    append_df = to_update.get(sheet)

    if append_df is not None:
        sheet_df = pd.concat([sheet_df, append_df], axis=1)

    sheet_df.to_excel(excel_writer, sheet, index=False)

excel_writer.save()
