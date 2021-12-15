import gspread

# API Doc for Gspread: https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project
gc = gspread.service_account()
file = gc.open("Shopping_Price_Alert")
source_sheet = file.worksheet("Responses")
target_sheet = file.worksheet("transactions")


def read_responses():
    all_products_dict = source_sheet.get_all_records()
    source_data = all_products_dict
    return source_data


def update_price(data_block):
    if data_block:
        last_row = len(target_sheet.col_values(1))
        row_count = len(data_block)
        print(f'A{last_row+1}:H{last_row + row_count}')
        target_sheet.update(f'A{last_row+1}:K{last_row + row_count}', data_block)
