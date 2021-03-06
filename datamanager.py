from datetime import datetime
import pandas as pd
import csv

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


def add_to_balance(order_id, price, amount, order_type):
    price = float(price)
    amount = float(amount)
    trade_df = pd.read_csv('balance.csv')
    new_order = [{
            "Index": len(trade_df),
            "Date": today_date,
            "Time": now_time,
            "Key": order_id,
            "Price": price,
            "Amount": amount,
            "Order": order_type
        }]
    new_trade_df = pd.DataFrame(new_order)
    new_trade_df.to_csv("balance.csv", mode="a", index=False, header=False)


def new_sell_order(avg_buy, price_sold, balance):
    pct = ((price_sold - avg_buy) / avg_buy) * 100
    pct_gain_loss = round(pct, 2)
    new_order = [{
            "Date": today_date,
            "Time": now_time,
            "Price_Sold": price_sold,
            "Amount": balance,
            'Buy_Avg': avg_buy,
            "PCT_gain/loss": pct_gain_loss,
        }]
    new_trade_df = pd.DataFrame(new_order)
    new_trade_df.to_csv("sell_orders.csv", mode="a", index=False, header=False)


def add_new_order(order_id, price, amount, order_type):
    price = float(price)
    amount = float(amount)
    trade_df = pd.read_csv('all_orders.csv')
    new_order = [{
        "Index": len(trade_df),
        "Date": today_date,
        "Time": now_time,
        "Key": order_id,
        "Price": price,
        "Amount": amount,
        "Order": order_type
    }]
    new_trade_df = pd.DataFrame(new_order)
    new_trade_df.to_csv("all_orders.csv", mode="a", index=False, header=False)


def update_order_data():
    # column_names = ["Date", "Time", "Key", "Price", "Amount", "Order"]
    # trade_df = pd.DataFrame(columns=column_names)
    # trade_df.to_csv('balance.csv')
    f = open('balance.csv', 'w+')
    f.close()
    column_names = ["Date", "Time", "Key", "Price", "Amount", "Order"]
    with open('balance.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
