from datetime import datetime
from sheets import read_responses, update_price
from price import get_price, price_dropped
from telegram import send_message
from pprint import pprint

data_to_query = read_responses()
# pprint(data_to_query)
data_block = []

for product in data_to_query:
    url = product['Product URL']
    unit = int(product['Unit'])
    product_name = product['Product Name']
    desired_unit_price = float(product['Desired Unit Price'])
    telegram_id = product['Telegram ID']
    active = product['Active']

    desired_price = round(desired_unit_price * unit, 0)

    if active.upper() == "Y":
        price = get_price(url)
        if type(price) == float:            
            unit_price = price/unit
            # print(unit_price)
            # print(desired_unit_price)

            if price_dropped(unit_price, desired_unit_price):
                message = f"Price of {product_name} has dropped below the expected price.\n" \
                            f"Expected Price: {desired_price}\n" \
                            f"Current Price: {price}\n" \
                            f"Difference: {round(desired_unit_price - unit_price,2)}\n" \
                            f"Link to order: {url}"
                
                message_sent = True
                time_stamp = datetime.now().strftime("%x %X") 
                upload_row = [time_stamp, product_name, url, unit, desired_unit_price, unit_price, desired_price,
                              price, telegram_id, active, message_sent]
                data_block.append(upload_row)
                send_message(message, telegram_id)
                # print(message)
            else:                
                print("price has not dropped!")
        else:            
            print(price)

# print(data_block)
update_price(data_block)
