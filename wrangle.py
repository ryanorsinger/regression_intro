# For regression exercises, use the example scenario: 
# As a customer analyst, I want to know:
# - who has spent the most money with us over their lifetime. 
# - I have monthly charges and tenure
# so I think I'll use these two attributes as features to estimate total_charges. 
# I need to do this within an average of $5.00 per customer.


# Acquire 
# customer_id, monthly_charges, tenure, and total_charges from telco_churn
# for all customers with a 2 year contract.

import pandas as pd

def get_url(database_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

def round_to_next5(n):
    return n + (5 - n) % 5


def get_telco_data():
    """
        returns a dataframe of customer_id, monthly charges, tenure in months, and total_charges rounded to the nearest $5 for 2-year contract customers
    """
    url = get_url("telco_churn")
    
    # returns data for 2-year-contract customers
    query = """
                select customer_id, monthly_charges, tenure 
                from customers 
                where churn = 'No'
                and 
                contract_type_id = 3
            """

    df = pd.read_sql(query, url)

def clean_telco_data(df):
    df["total_charges"] = df.tenure * df.monthly_charges

    df.total_charges = df.total_charges.apply(round_to_next5)

    # drop the tenure 0 month customers
    df = df[df.tenure != 0]
    return df

def wrangle_telco():
    return clean_telco_data(get_telco_data())

df = wrangle_telco()