import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import MinMaxScaler
from itertools import combinations
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
pd.set_option('display.max_columns', 100)
import json
import folium
from folium.plugins import FastMarkerCluster, Fullscreen, MiniMap, HeatMap, HeatMapWithTime, LocateControl
import streamlit as st
import pickle
import time
from PIL import Image
import requests


import warnings
warnings.filterwarnings("ignore")



sns.set_palette('husl')

st.set_page_config(page_title="e-Commerce Data Analysis Steps", layout="wide")


#Add picture
img_eCommerce = Image.open("e-Commerce.jpg")
st.image(img_eCommerce,width=700)

st.write("""      
    [Utus Karta Sanggam](https://www.linkedin.com/in/utusks01)

    """)


add_selectitem = st.sidebar.selectbox("e-Commerce Data Analysis Steps ", ("1. Data Wrangling - Gathering Data", "2. Data Wrangling - Assesing Data", "3. Data Wrangling - Cleaning Data", "4. Exploratory Data Analysis (EDA)",  "5. Recency Frequency Monetary (RFM)", "6. Visualization & Explanatory Analysis", "7. Conclusion"))     

# Load data
data_customer = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/customers_dataset.csv')
data_products = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/products_dataset.csv')
data_sellers = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/sellers_dataset.csv')
data_orders = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/orders_dataset.csv')
data_order_items = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/order_items_dataset.csv')
data_order_payments = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/order_payments_dataset.csv')
data_order_reviews = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/order_reviews_dataset.csv')
data_products_translation = pd.read_csv('https://raw.githubusercontent.com/utusks001/e_Commerce_Data_Analysis/main/product_category_name_translation.csv') 

def gathering():
    st.subheader("This Part of Data Wrangling - Gathering Data")
    st.write("                                             ")  

    st.write("**Determining Business Questions of E-Commerce Public Dataset** :")  
    st.write("        1. Which Top and Bottom 10 Category of Products ?")
    st.write("        2. Which Top Positively and Negatively Reviewed Products ?")
    st.write("        3. Which Category of goods that are most and least popular orders ?")
    st.write("        4. How long does the long delivery days ? from where to where ?")  
    st.write("        5. How do sales comparison in 2017 and 2018 ?") 
    st.write("        6. How e-Commerce trend ? What day and time of transaction ?")                                            
    st.write("                                             ")  
    
    tabA, tabB = st.tabs(["A. Load and Display Data", "B. Merge Data"])

    with tabA:
        st.subheader("A. Load and Display Data") 
        st.write("                                             ")  
        
        # Display the data
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["1.Customer", "2.Products", "3.Seller", "4.Order", "5.Order Items", "6.Order Payments", "7.Order Reviews", "8.Products Translation"])

        with tab1:
            st.subheader("1. Customer Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the customer data:**")
            st.dataframe(data_customer.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_customer.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data customer information:**")
            # st.dataframe(data_customer.info())
            for index, (col, dtype) in enumerate(zip(data_customer.columns, data_customer.dtypes)):
                non_null_count = data_customer[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")

        with tab2:
            st.subheader("2. Products Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the products data:**")
            st.dataframe(data_products.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_products.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data products information:**")
            # st.dataframe(data_products.info())
            for index, (col, dtype) in enumerate(zip(data_products.columns, data_products.dtypes)):
                non_null_count = data_products[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")

        with tab3:
            st.subheader("3. Seller Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the seller data:**")
            st.dataframe(data_sellers.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_sellers.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data seller information:**")
            # st.dataframe(data_sellers.info())
            for index, (col, dtype) in enumerate(zip(data_sellers.columns, data_sellers.dtypes)):
                non_null_count = data_sellers[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")        

        with tab4:
            st.subheader("4. Order Data")
            st.write("                                             ")  
    
            st.write("**First 5 rows of the order data:**")
            st.dataframe(data_orders.head())

            # Display the shape of the data
            st.write(f"**Data shape:** {data_orders.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data order information:**")
            # st.dataframe(data_orders.info())
            for index, (col, dtype) in enumerate(zip(data_orders.columns, data_orders.dtypes)):
                non_null_count = data_orders[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")               

        with tab5:
            st.subheader("5. Order Items Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the order items data:**")
            st.dataframe(data_order_items.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_order_items.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data order items information:**")
            # st.dataframe(data_order_items.info())
            for index, (col, dtype) in enumerate(zip(data_order_items.columns, data_order_items.dtypes)):
                non_null_count = data_order_items[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")          

        with tab6:
            st.subheader("6. Order Payments Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the order payments data:**")
            st.dataframe(data_order_payments.head())
            st.write("                                             ")  
    
            # Display the shape of the data
            st.write(f"**Data shape:** {data_order_payments.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data order payments information:**")
            # st.dataframe(data_order_payments.info())
            for index, (col, dtype) in enumerate(zip(data_order_payments.columns, data_order_payments.dtypes)):
                non_null_count = data_order_payments[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")         

        with tab7:
            st.subheader("7. Order Reviews Data")
            st.write("                                             ")  
    
            st.write("**First 5 rows of the order reviews data:**")
            st.dataframe(data_order_reviews.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_order_reviews.shape}")
            st.write("                                             ")  

            # Display data information
            st.write("**Data order information:**")
            # st.dataframe(data_order_reviews.info())
            for index, (col, dtype) in enumerate(zip(data_order_reviews.columns, data_order_reviews.dtypes)):
                non_null_count = data_order_reviews[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")         

        with tab8:
            st.subheader("8. Products Translation Data")
            st.write("                                             ")  

            st.write("**First 5 rows of the products translation data:**")
            st.dataframe(data_products_translation.head())
            st.write("                                             ")  

            # Display the shape of the data
            st.write(f"**Data shape:** {data_products_translation.shape}")
            st.write("                                             ")  
    
            # Display data information
            st.write("**Data products translation information:**")
            # st.dataframe(data_products_translation.info())
            for index, (col, dtype) in enumerate(zip(data_products_translation.columns, data_products_translation.dtypes)):
                non_null_count = data_products_translation[col].count()
                st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")         

    with tabB:       
        st.subheader("B. Merge Data")
        st.write("                                             ")  

        #Merge Data
        # Combine data in multiple dataframes¶
        # In this project, there are 2 dataframes that will be used, namely, df_order_items and orders.
        # df_order_items : a combination of the order_items, products_translation, and seller tables.
        # orders: a combination of the orders, payments, and customer tables       

        tab11, tab12, tab13 = st.tabs(["1. Products Merge", "2. Order Items Merge", "3. Orders Merge"])

        with tab11:
            st.subheader("1. Merge Products with Products Translation")
            st.write("                                             ")  
        
            # Merge products with products_translation into df_product (Product data Frame)
            products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')

            # Display Merge Data Frame
            st.write("**Merged Products Data Preview:**")
            st.dataframe(products)
            st.write("                                             ")  

            # Display the shape of the selected data
            st.write(f"**Merged Products Data Shape:**  {products.shape}")
            st.write("                                             ")  


        with tab12:
            st.subheader("2. Merge Order Items with Products and Sellers")
            st.write("                                             ")  
        
            # Merge order_items with df products to become df order_items
            products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')
            df_product = products[["product_id","product_category_name_english","product_category_name"]]
            df_order_items = data_order_items.merge(df_product, left_on='product_id', right_on='product_id',how='left')

            # Merge pdf order_items with seller
            sellers = data_sellers.drop(columns=['seller_zip_code_prefix'])
            df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')

            # Display the first few rows of the merged data
            st.write("**Merged Order Items Data Preview:**")
            st.dataframe(df_order_items.head())       

            # Display the shape of the merged data
            st.write(f"**Merged Order Items Data Shape:** {df_order_items.shape}")
            st.write("                                             ")  

        with tab13:
            st.subheader("3. Merge Orders with Order Payments and Customers")
            st.write("                                             ")  
            
            # Merge orders with payments
            payments = data_order_payments.drop(columns=['payment_sequential', 'payment_installments'])
            orders = data_orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

            # Merge orders with customers
            customer = data_customer.drop(columns=['customer_unique_id'])
            orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')
        
            # Display the first few rows of the merged data
            st.write("**Merged Orders Data Preview:**")
            st.dataframe(orders.head())

            # Display the shape of the merged data
            st.write(f"**Merged Orders Data Shape:** {orders.shape}")
            st.write("                                             ")  



def assesing():
    st.subheader("This Part of Data Wrangling - Assesing Data")
    st.write("                                             ")  

    # carry out data checks before carrying out data analysis. 
    # At this stage, we will check data types, missing values, 
    # duplicate data, and statistical parameters.


    # Merge order_items with df products to become df order_items
    products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')
    df_product = products[["product_id","product_category_name_english","product_category_name"]]
    df_order_items = data_order_items.merge(df_product, left_on='product_id', right_on='product_id',how='left')

    # Merge pdf order_items with seller
    sellers = data_sellers.drop(columns=['seller_zip_code_prefix'])
    df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')    

    # merge orders with order_payments
    payments = data_order_payments.drop(columns = ['payment_sequential','payment_installments'])
    orders = data_orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

    # merge orders with customers
    customer = data_customer.drop(columns = ['customer_unique_id'])
    orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')


    tab21, tab22, tab23 = st.tabs(["1.Assesing DataFrame df_product", "2.Assesing DataFrame df_order_items", "3.Assesing DataFrame Orders"])

    with tab21:  
         # Assess Data Frame df_order_items
        st.subheader("1. Assesing DataFrame df_product")   
        st.write("                                             ")  

        # Display data information
        st.write("**df_product Data information:**")
        # df_order_items.info()
        for index, (col, dtype) in enumerate(zip(df_product.columns, df_product.dtypes)):
            non_null_count = df_product[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")    

        st.write("                                             ")  

        # Display the shape of the DataFrame
        st.write(f"**Shape of df_product:** {df_product.shape}")
        st.write("                                             ")  

        # Find rows where 'product_category_name_english' is null
        missing_categories = df_product[df_product["product_category_name_english"].isnull()]

        # Display rows with missing category translations
        st.write("**Rows with Missing Category Translations:**")
        st.dataframe(missing_categories)
        st.write("                                             ")  
        
        # Display total missing rows 
        st.write(f'**Count of Missing Values:** {df_product["product_category_name_english"].isnull().sum()}')

        # Display the count of duplicated rows
        duplicated_count = df_product.duplicated().sum()
        st.write(f"**Duplicated amount:** {duplicated_count}")
        st.write("                                             ")  

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(df_product.describe())


    with tab22:    
        # Assess Data Frame df_order_items
        st.subheader("2. Assesing DataFrame df_order_items")   
        st.write("                                             ")  

        # Display data information
        st.write("**df_order_items Data information:**")
        # df_order_items.info()
        for index, (col, dtype) in enumerate(zip(df_order_items.columns, df_order_items.dtypes)):
            non_null_count = df_order_items[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")    

        st.write("                                             ")  

        # Display the shape of the DataFrame
        st.write(f"**Shape of DataFrame:** {df_order_items.shape}")
        st.write("                                             ")  

        # Display the count of missing (NaN) values
        missing_values = df_order_items.isnull().sum()
        st.write("**Count of Missing Values:**")
        st.write(missing_values)
        st.write("                                             ")  

        # Display the count of duplicated rows
        duplicated_count = df_order_items.duplicated().sum()
        st.write(f"**Duplicated amount:** {duplicated_count}")
        st.write("                                             ")  

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(df_order_items.describe())

    with tab23:
        #Assess Orders Data
        st.subheader("3. Assesing DataFrame Orders")   
        st.write("                                             ")  

        # Display data information
        st.write("**Orders Data information:**")
        # orders.info()
        for index, (col, dtype) in enumerate(zip(orders.columns, orders.dtypes)):
            non_null_count = orders[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")    

        st.write("                                             ")  

        # Display the shape of the DataFrame
        st.write(f"**Shape of DataFrame:** {orders.shape}")
        st.write("                                             ")  
 
        # Display the count of missing (NaN) values
        missing_values = orders.isnull().sum()
        st.write("**Count of Missing Values:**")
        st.write(missing_values)
        st.write("                                             ")  

        # Display the count of duplicated rows
        duplicated_count = orders.duplicated().sum()
        st.write(f"**Duplicated amount:** {duplicated_count}")
        st.write("                                             ")  

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(orders.describe())




def cleaning():
    st.subheader("This Part of Data Wrangling - Cleaning Data")
    st.write("                                             ")  


    # Merge order_items with df products to become df order_items
    products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')
    df_product = products[["product_id","product_category_name_english","product_category_name"]]
    df_order_items = data_order_items.merge(df_product, left_on='product_id', right_on='product_id',how='left')

    # Merge pdf order_items with seller
    sellers = data_sellers.drop(columns=['seller_zip_code_prefix'])
    df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')    

    # merge orders with order_payments
    payments = data_order_payments.drop(columns = ['payment_sequential','payment_installments'])
    orders = data_orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

    # merge orders with customers
    customer = data_customer.drop(columns = ['customer_unique_id'])
    orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')
    

    #Cleaning Data 
    tab31, tab32, tab33 = st.tabs(["1.Cleaning DataFrame df_product", "2.Cleaning DataFrame df_order_items", "3.Cleaning DataFrame Orders"])

    with tab31:  
        # Cleaning Data Frame df_order_items
        st.subheader("1. Cleaning DataFrame df_product")   
        st.write("                                             ") 

        # Display data information
        st.write("**df_product Data information:**")
        # ddf_product.info()
        for index, (col, dtype) in enumerate(zip(df_product.columns, df_product.dtypes)):
            non_null_count = df_product[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}") 
    
        # Handle missing values
        df_product['product_category_name'].fillna('not defined', inplace=True)
        df_product['product_category_name_english'].fillna('not defined', inplace=True)

        # Display the shape of the data
        st.write(f"**Data shape:** {df_product.shape}")
        st.write("                                             ")  

        # Check missing values again
        missing_values = df_product.isnull().sum()
        st.write("Missing Values After Handling:")
        st.write(missing_values)
        st.write("                                             ")  

        # Remove duplicates
        df_product.drop_duplicates(inplace=True)

        # Display the number of duplicates removed
        duplicates_count = df_product.duplicated().sum()
        st.write(f"Number of Duplicates Removed: {duplicates_count}")
        st.write("                                             ")  

        # Display the updated DataFrame
        st.write("Updated DataFrame:")
        st.dataframe(df_product)

        # Display the shape of the data
        st.write(f"**Data shape:** {df_product.shape}")
        st.write("                                             ")  


    with tab32:  
        # Cleaning Data Frame df_order_items
        st.subheader("2. Cleaning DataFrame df_order_items")   
        st.write("                                             ") 

        # Convert 'shipping_limit_date' to datetime
        df_order_items['shipping_limit_date'] = pd.to_datetime(df_order_items['shipping_limit_date'])

        # Display data information
        st.write("**df_order_items Data information:**")
        # df_order_items.info()
        for index, (col, dtype) in enumerate(zip(df_order_items.columns, df_order_items.dtypes)):
            non_null_count = df_order_items[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}") 

        st.write("                                             ")  

        # Handle missing values in 'product_category_name_english'
        missing_categories = df_order_items.loc[df_order_items["product_category_name"].notnull() & df_order_items["product_category_name_english"].isnull()]
        set(missing_categories["product_category_name"])

        # Fill missing values
        df_order_items['product_category_name'].fillna('not defined', inplace=True)
        df_order_items['product_category_name_english'].fillna('not defined', inplace=True)

        # Update 'product_category_name_english' based on certain conditions
        df_order_items.loc[df_order_items["product_category_name"] == 'pc_gamer', 'product_category_name_english'] = 'PC Gaming'
        df_order_items.loc[df_order_items["product_category_name"] == 'portateis_cozinha_e_preparadores_de_alimentos', 'product_category_name_english'] = 'Portable Kitchen Food Preparers'

        # Display the shape of the data
        st.write(f"**Data shape:** {df_order_items.shape}")
        st.write("                                             ")  

        # Check missing values again
        missing_values = df_order_items.isnull().sum()
        st.write("Missing Values After Handling:")
        st.write(missing_values)
        st.write("                                             ")  

        # Remove duplicates
        df_order_items.drop_duplicates(inplace=True)

        # Display the number of duplicates removed
        duplicates_count = df_order_items.duplicated().sum()
        st.write(f"Number of Duplicates Removed: {duplicates_count}")
        st.write("                                             ")  

        # Display the updated DataFrame
        st.write("Updated DataFrame:")
        st.dataframe(df_order_items)

        # Display the shape of the data
        st.write(f"**Data shape:** {df_order_items.shape}")
        st.write("                                             ")  

    with tab33:
        #Cleaning Orders Data
        st.subheader("3. Cleaning DataFrame Orders")   
        st.write("                                             ")  

        # Display data information
        st.write("**Orders Data information:**")
        # orders.info()
        for index, (col, dtype) in enumerate(zip(orders.columns, orders.dtypes)):
            non_null_count = orders[col].count()
            st.write(f"{index} | {col}   | {non_null_count} non-null  |  {dtype}")    

        st.write("                                             ") 

        columns_to_convert = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                            'order_delivered_customer_date', 'order_estimated_delivery_date']
        orders[columns_to_convert] = orders[columns_to_convert].apply(pd.to_datetime)
        orders['order_status'] = orders['order_status'].astype('category')

        # confirm data types 
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
        orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
        orders['order_status'] = orders['order_status'].astype('category')  

        # Filter by order_status
        shippment_order = orders.loc[orders['order_status'] == 'shipped']


        # Display the updated DataFrame
        st.write("Orders DataFrame:")
        st.dataframe(shippment_order)

        # Display the shape of the data
        st.write(f"**Orders DataFrame shape:** {shippment_order.shape}")
        st.write("                                             ")  

        # Handle Missing Values
        orders = orders.dropna(subset=["payment_type", "payment_value"])
        missing_values = orders.isna().sum()
        st.write("Missing Values After Handling:")
        st.write(missing_values)

        # Remove Duplicates
        orders.drop_duplicates(inplace=True)

        # Display the number of duplicates removed
        duplicate_count = orders.duplicated().sum()
        st.write(f"Number of Duplicates Removed: {duplicate_count}")
        st.write("                                             ")  
    
 


def EDA():
    st.subheader("This Part of Explotary Data Analysis / EDA")
    st.write("                                             ") 


    # Merge order_items with df products to become df order_items
    products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')
    df_product = products[["product_id","product_category_name_english","product_category_name"]]
    df_order_items = data_order_items.merge(df_product, left_on='product_id', right_on='product_id',how='left')

    # Merge pdf order_items with seller
    sellers = data_sellers.drop(columns=['seller_zip_code_prefix'])
    df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')    
 
    # merge orders with order_payments
    payments = data_order_payments.drop(columns = ['payment_sequential','payment_installments'])
    orders = data_orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

    # merge orders with customers
    customer = data_customer.drop(columns = ['customer_unique_id'])
    orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')
   

    # defines the functions to be used for EDA
    def range(series):
        return series.max() - series.min()

    #Explore Data 
    tab41, tab42, tab43 = st.tabs(["1.Exploring DataFrame df_product", "2.Exploring DataFrame df_order_items", "3.Exploring DataFrame Orders"])

  
    with tab41:  
        # Cleaning Data Frame df_product
        st.subheader("1. Exploring DataFrame df_product")   
        st.write("                                             ") 

        # Handlie missing values
        df_product['product_category_name'].fillna('not defined', inplace=True)
        df_product['product_category_name_english'].fillna('not defined', inplace=True)

        # Remove duplicates
        df_product.drop_duplicates(inplace=True)

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(df_product.describe(include="all"))

        # Get the top 10 product categories
        top_10_category = df_product["product_category_name_english"].value_counts().sort_values(ascending=False)[:10]

        # Get the Bottom product categories
        bottom_10_category = df_product["product_category_name_english"].value_counts().sort_values(ascending=True)[:10]

        # Display the frequently bought together products
        st.subheader('Top 10 Product Categories')
        st.write("                                             ")  
        st.write(top_10_category)
        st.write("                                             ")     

        # Display the frequently bought together products
        st.subheader('Bottom 10 Product Categories')
        st.write("                                             ")  
        st.write(bottom_10_category)
        st.write("                                             ")     

        # Find the products that usually appear in the positvely reviewed / negatively reviewed order
        # Function to find top positively and negatively reviewed products
        def find_top_reviewed_products(data_order_reviews, data_orders, data_order_items, df_product, n=10):
            satis_table = data_order_reviews.merge(data_orders, on='order_id').merge(data_order_items, on='order_id').merge(df_product, on='product_id')

            # Labeling customer review score
            satis_table['satisfaction'] = satis_table['review_score'].apply(lambda x:
                                        "negative_order" if x < 3
                                        else (
                                                "positive_order" if x > 3
                                                else "neutral")
                                        )

            # Group by product - satisfaction, get the count of occurrence
            satis_table = satis_table.groupby(['product_id', 'product_category_name_english', 'satisfaction']).agg({'order_id': 'count'}).reset_index().sort_values('order_id', ascending=False)

            # Get top N positive products and top N negative products
            top_pos = satis_table[satis_table['satisfaction'] == 'positive_order'][:n]
            top_neg = satis_table[satis_table['satisfaction'] == 'negative_order'][:n]

            return top_pos, top_neg


        # Call the function to find top reviewed products
        n = 10  # Change this value to show a different number of products
        top_positively_reviewed, top_negatively_reviewed = find_top_reviewed_products(data_order_reviews, data_orders, data_order_items, df_product, n)

        # Display the top positively reviewed products
        st.subheader("Top Positively Reviewed Products:")
        st.write(top_positively_reviewed)
        st.write("                                             ")    

        # Display the top negatively reviewed products
        st.subheader("Top Negatively Reviewed Products:")
        st.write(top_negatively_reviewed) 
        st.write("                                             ")   



    with tab42:  
        # Cleaning Data Frame df_order_items
        st.subheader("2. Exploring DataFrame df_order_items")   
        st.write("                                             ") 
 
        # Convert 'shipping_limit_date' to datetime
        df_order_items['shipping_limit_date'] = pd.to_datetime(df_order_items['shipping_limit_date'])

        # Handle missing values in 'product_category_name_english'
        missing_categories = df_order_items.loc[df_order_items["product_category_name"].notnull() & df_order_items["product_category_name_english"].isnull()]
        set(missing_categories["product_category_name"])

        # Fill missing values
        df_order_items['product_category_name'].fillna('not defined', inplace=True)
        df_order_items['product_category_name_english'].fillna('not defined', inplace=True)

        # Update 'product_category_name_english' based on certain conditions
        df_order_items.loc[df_order_items["product_category_name"] == 'pc_gamer', 'product_category_name_english'] = 'PC Gaming'
        df_order_items.loc[df_order_items["product_category_name"] == 'portateis_cozinha_e_preparadores_de_alimentos', 'product_category_name_english'] = 'Portable Kitchen Food Preparers'

        # Remove duplicates
        df_order_items.drop_duplicates(inplace=True)

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(df_order_items.describe(include="all"))
        st.write("                                             ") 

        # Calculate the average, minimum, mean, and range of prices for each product category
        df_category_price = df_order_items.groupby(by="product_category_name_english").agg({
            "product_id": "count",
            "price": ["max", "min", "mean", range]
        })

        # Sort the data by product count, in descending order
        df_category_price = df_category_price.sort_values(by=("product_id", "count"), ascending=False)

        # Create a Streamlit app
        st.subheader("Product Category Price Summary")

        # Display the summary table
        st.dataframe(df_category_price)
        st.write("                                             ") 

        # Display the shape of the data
        st.write(f"**Data shape:** {df_category_price.shape}")
        st.write("                                             ")  

       # Group and aggregate the data
        df_category = df_order_items.groupby(by="product_category_name_english")["product_id"].count().reset_index()
        df_category = df_category.rename(columns={"product_category_name_english": "category", "product_id": "orders"})

        # Sort data
        df_category_top = df_category.sort_values(by="orders", ascending=False)
        df_category_bottom = df_category.sort_values(by="orders", ascending=True)

        # Top categories
        st.subheader('Top 10 Most Popular Orders')
        st.write("                                             ")  
        st.write(df_category_top)
        st.write("                                             ")  

        # Bottom categories
        st.subheader('Top 10 Least Popular Orders')
        st.write("                                             ")  
        st.write(df_category_bottom)
        st.write("                                             ")  


    with tab43:  
        # Cleaning Data Frame df_order_items
        st.subheader("3. Exploring DataFrame Orders")   
        st.write("                                             ") 


        # # Changing the data type for date columns
        columns_to_convert = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                            'order_delivered_customer_date', 'order_estimated_delivery_date']
        orders[columns_to_convert] = orders[columns_to_convert].apply(pd.to_datetime)
        orders['order_status'] = orders['order_status'].astype('category')

        # timestamp_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
        #                   'order_estimated_delivery_date']

        # for col in timestamp_cols:
        #     orders[col] = pd.to_datetime(orders[col])


        # confirm data types 
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
        orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
        orders['order_status'] = orders['order_status'].astype('category')  

        shippment_order = orders.loc[orders['order_status'] == 'shipped']

        # Handle Missing Values
        orders = orders.dropna(subset=["payment_type", "payment_value"])

        # Remove Duplicates
        orders.drop_duplicates(inplace=True)
           
        # Extracting attributes for purchase date - Year and Month
        orders['order_purchase_year'] = orders['order_purchase_timestamp'].apply(lambda x: x.year)
        orders['order_purchase_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.month)
        orders['order_purchase_month_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%b'))
        orders['order_purchase_year_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m'))
        orders['order_purchase_date'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m%d'))

        # Extracting attributes for purchase date - Day and Day of Week
        orders['long_delivery_days'] = (orders["order_delivered_customer_date"] - orders["order_delivered_carrier_date"]).dt.days
        orders['order_purchase_day'] = orders['order_purchase_timestamp'].apply(lambda x: x.day)
        orders['order_purchase_dayofweek'] = orders['order_purchase_timestamp'].apply(lambda x: x.dayofweek)
        orders['order_purchase_dayofweek_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%a'))

        # Extracting attributes for purchase date - Hour and Time of the Day
        orders['order_purchase_hour'] = orders['order_purchase_timestamp'].apply(lambda x: x.hour)
        hours_bins = [-0.1, 6, 12, 18, 23]
        hours_labels = ['Dawn', 'Morning', 'Afternoon', 'Night']
        orders['order_purchase_time_day'] = pd.cut(orders['order_purchase_hour'], hours_bins, labels=hours_labels)

        # Display the updated Orders DataFrame after transformations
        st.write("New Orders DataFrame after transformations:")
        st.dataframe(orders)

        # Display the shape of the data
        st.write(f"**New Orders DataFrame shape:** {orders.shape}")
        st.write("                                             ")  

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(orders.describe(include="all"))
        st.write("                                             ")  

        # Create a Streamlit app
        st.subheader("E-commerce Delivery Analysis")
        st.write("                                             ")  

        orders = orders[orders["long_delivery_days"] > 0]

        orders.groupby(by="customer_city").long_delivery_days.median().sort_values(ascending=False) 

        # merger customer with seller
        cust = orders[['customer_city','customer_state','long_delivery_days','order_id','customer_id']]
        seller = df_order_items[['order_id','seller_id','seller_city','seller_state']]
        cust_seller = cust.merge(seller, left_on='order_id', right_on='order_id',how='left')    

        # Display summary statistics of the DataFrame
        st.write("**Summary Statistics:**")
        st.write(cust_seller.describe())
        st.write("                                             ")  

        # Remove duplicated data
        cust_seller = cust_seller.drop_duplicates()

        sellertate = df_order_items.groupby(by="seller_state").seller_id.nunique().sort_values(ascending=False)
        st.write("Seller State:")
        st.write(sellertate) 
        st.write("                                             ")   
 
        sellercity = df_order_items.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False)
        st.write("Seller City:")
        st.write(sellercity) 
        st.write("                                             ")   
 
        customerstate = orders.groupby(by="customer_state").long_delivery_days.median().sort_values(ascending=False) 
        st.write("Customer State:")
        st.write(customerstate) 
        st.write("                                             ")   
 
        customercity = orders.groupby(by="customer_city").long_delivery_days.median().sort_values(ascending=False) 
        st.write("Customer City:")
        st.write(customercity) 
        st.write("                                             ")   
 
        # Calculate median delivery days between seller and customer states
        state_time_delivered = cust_seller.groupby(['seller_state', 'customer_state'])['long_delivery_days'].median().sort_values(ascending=False).reset_index()
        st.subheader("Median Delivery Days Between States")
        st.write(state_time_delivered)
        st.write("                                             ")  

        # Display the shape of Orders Compare data
        st.write(f"**Orders Data shape:** {state_time_delivered.shape}")
        st.write("                                             ")  


        # Calculate median delivery days between seller and customer cities
        city_time_delivered = cust_seller.groupby(['seller_city', 'customer_city'])['long_delivery_days'].median().sort_values(ascending=False).reset_index()
        st.subheader("Median Delivery Days Between Cities")
        st.write(city_time_delivered)
        st.write("                                             ")  


        # Display the shape of Orders Compare data
        st.write(f"**Orders Data shape:** {city_time_delivered.shape}")
        st.write("                                             ")  


        # Annotation - Growth in e-commerce orders between 2017 and 2018
        orders_compare = orders.query('order_purchase_year in (2017, 2018) & order_purchase_month <= 8')

        # Streamlit app
        st.subheader("E-commerce Orders Analysis for sales comparison in 2017 and 2018")

        # Display Orders Compare data
        st.write(orders_compare.head())
        st.write("                                             ")           

        # Display the shape of Orders Compare data
        st.write(f"**Orders Data shape:** {orders_compare.shape}")
        st.write("                                             ")  




def RFM():
    st.subheader("This Part of Recency Frequency Monetary / RFM Analysis")
    st.write("                                             ") 
           
    # # Function to calculate scores
    def scoring(x):
            quan_val_list = []
            for quan in [0.2, 0.4, 0.6, 0.8]:
                    quan_val_list.append(np.quantile(x, quan))

            def labeling(x):
                    if x < quan_val_list[0]:
                        return 1
                    elif x < quan_val_list[1]:
                        return 2
                    elif x < quan_val_list[2]:
                        return 3
                    elif x < quan_val_list[3]:
                        return 4
                    else:
                        return 5

            return x.apply(labeling)    


    # RFM ANALYSIS
    tab51, tab52, tab53 = st.tabs(["1.RECENCY", "2.FREQUENCY", "3.MONETARY"])
  
    with tab51:  
        # 1. RECENCY
        st.subheader("1. RECENCY ")
        st.write("                                             ") 

        # Function to calculate recency scores
        def calculate_recency_scores(data_customer, data_orders):
            recency_table = data_customer.merge(data_orders, on="customer_id")
            recency_table = recency_table.groupby('customer_unique_id').agg({'order_purchase_timestamp': 'max'}).reset_index()
            recency_table['order_purchase_timestamp'] = pd.to_datetime(recency_table['order_purchase_timestamp'])
            current_day = pd.to_datetime(max(data_orders['order_purchase_timestamp']))
            recency_table['days_between'] = (current_day - recency_table['order_purchase_timestamp']).dt.days

            recency_table['recency_score'] = scoring(recency_table['days_between'])
            return recency_table
            
        # Call the function to calculate recency scores
        recency_table = calculate_recency_scores(data_customer, data_orders)

        # Display the recency scores
        st.write("**Recency Scores:**")
        st.write(recency_table)
        st.write("                                             ") 

        # Display the shape of the data
        st.write(f"**Data shape:** {recency_table.shape}")
        st.write("                                             ")          
        st.write("                                             ") 

    with tab52:  
        # 2. FREQUENCY
        st.subheader("2. FREQUENCY ")
        st.write("                                             ") 

        # Calculate the frequency score
        # Merge the customer and order tables
        frequency_table = data_customer.merge(data_orders, on='customer_id')

        # Get the minimum and average order purchase timestamp for each customer
        frequency_table = frequency_table.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': ['min', 'max'],
        'order_id': 'count'
        }).reset_index()

        # Change the column names
        frequency_table.columns = ['customer_unique_id', 'min', 'max', 'count']

        # Convert the max and min columns to datetime dtype
        frequency_table['max'] = pd.to_datetime(frequency_table['max'])
        frequency_table['min'] = pd.to_datetime(frequency_table['min'])

        # Calculate the days between the first and last day of purchase for each customer
        frequency_table['days_between'] = (frequency_table['max'] - frequency_table['min']).apply(lambda x: int(str(x).split()[0]))

        # Remove one-time-purchase customers
        frequency_table = frequency_table[frequency_table['days_between']>0]

        # Calculate the purchase rate for each customer
        frequency_table['purchase_rate'] = frequency_table['count'] / frequency_table['days_between']

        # # Call the function to calculate frequency scores
        frequency_table['frequency_score'] = scoring(frequency_table['purchase_rate'])

        # Display the frequency scores
        st.write("**Frequency Scores:**")
        st.write(frequency_table)
        st.write("                                             ") 

        # Display the shape of the data
        st.write(f"**Data shape:** {frequency_table.shape}")
        st.write("                                             ")          
        st.write("                                             ") 

    with tab53:
        # 3. MONETARY
        st.subheader("3. MONETARY ")
        st.write("                                             ") 

        # Calculate the monetary score
        # Merge the payment, order, and customer tables
        monetary_table = data_order_payments.merge(data_orders, on='order_id').merge(data_customer, on='customer_id')

        # Group the data by customer ID and aggregate the payment value
        monetary_table = monetary_table.groupby('customer_unique_id').agg({'payment_value': 'sum'}).reset_index()

        # Calculate the monetary score for each customer
        monetary_table['monetary_score'] = scoring(monetary_table['payment_value'])

        # Display the monetary scores
        st.write("**Monetary Scores:**")
        st.write(monetary_table)    
        st.write("                                             ") 

        # Display the shape of the data
        st.write(f"**Data shape:** {monetary_table.shape}")
        st.write("                                             ")          
        st.write("                                             ") 

    # COMBINE ALL TOGETHER
    st.subheader("COMBINE ALL TOGETHER ")
    st.write("                                             ") 

    # # Function to calculate final table and segment

    # Merge the tables
    final_table = recency_table.merge(monetary_table, on='customer_unique_id').merge(frequency_table, on='customer_unique_id')

    # Select the relevant columns
    final_table = final_table[['customer_unique_id', 'recency_score', 'frequency_score', 'monetary_score']]

    # Calculate the frequency-monetary score
    final_table['frequency_monetary_score'] = scoring(final_table['frequency_score'] + final_table['monetary_score'])

    # Select the relevant columns again
    final_table = final_table[['customer_unique_id', 'recency_score', 'frequency_monetary_score']]

    # Create a segment dictionary
    segment_dict = {
                    # hibernating
                    (1, 1): 'hibernating',
                    (1, 2): 'hibernating',
                    (2, 1): 'hibernating',
                    (2, 2): 'hibernating',
                    # about to sleep
                    (3, 1): 'about to sleep',
                    (3, 2): 'about to sleep',
                    # promising
                    (4, 1): 'promising',
                    # new customer
                    (5, 1): 'new customer',
                    # potential customers
                    (4, 2): 'potential',
                    (4, 3): 'potential',
                    (5, 2): 'potential',
                    (5, 3): 'potential',
                    # need attention
                    (3, 3): 'need attention',
                    # at risk
                    (1, 3): 'at risk',
                    (1, 4): 'at risk',
                    (2, 3): 'at risk',
                    (2, 4): 'at risk',
                    # do not lose
                    (1, 5): 'do not lose',
                    (2, 5): 'do not lose',
                    # loyal customer
                    (3, 4): 'loyal',
                    (3, 5): 'loyal',
                    (4, 4): 'loyal',
                    (4, 5): 'loyal',
                    # champions
                    (5, 4): 'champions',
                    (5, 5): 'champions'
    }

    # Assign the segment to each customer
    final_table['segment'] = final_table.apply(lambda x: segment_dict[(x['recency_score'], x['frequency_monetary_score'])], axis=1)

    # # Display the final table
    st.write("Final Table:")
    st.write(final_table)
    st.write("                                             ") 
    # Display the shape of the data
    st.write(f"**Data shape:** {final_table.shape}")
    st.write("                                             ")      

    # Display the number of customers in each segment
    final_data = final_table['segment'].value_counts()
    total = final_data.sum()

    # Create the horizontal bar chart
    fig, ax = plt.subplots()
    color_map = ["#C1D8C3"] * len(final_data)
    color_map[-2] = color_map[-1] = '#CD5C08'

    ax.barh(
        y=final_data.index,
        width=final_data.values,
        color=color_map
    )

    ax.set_title('Distribution of segments from RFM Analysis', fontsize=12)

    for ind, val in final_data.items():
        ax.annotate(
            str((val/total)*100)[:5] + '%',
            xy=(val, ind), va='center', fontsize=5
        )

    # Display the figure in Streamlit
    st.pyplot(fig)

    # # Create a horizontal bar chart of the number of customers in each segment
    # fig, ax = plt.subplots()
    # ax.barh(y=final_data.index, width=final_data.values, color='#ff6666')

    # # Display the chart in Streamlit
    # st.pyplot(fig)

    # # Create a bar chart
    # fig, ax = plt.subplots()
    # ax.bar(x=final_data.index, height=final_data.values, color='#ff6666')

    # # Rotate x-axis labels for readability, change color, and adjust font size
    # ax.set_xticklabels(final_data.index, rotation=90, fontsize=12)

    # # Display the chart in Streamlit
    # st.pyplot(fig)

    # # Display the final table
    st.write("Final Data:")
    st.write(final_data)
    st.write("                                             ")    




def Visualization():
    st.subheader("This Part of Visualization & Explanatory Analysis")
    st.write("                                             ") 

    st.write("**Answering for the following Determining Business Questions of E-Commerce Public Dataset** :")  
    st.write("        1. Which Top and Bottom 10 Category of Products ?")
    st.write("        2. Which Top Positively and Negatively Reviewed Products ?")
    st.write("        3. Which Category of goods that are most and least popular orders ?")
    st.write("        4. How long does the long delivery days ? from where to where ?")   
    st.write("        5. How do sales comparison in 2017 and 2018 ?")                 
    st.write("        6. How e-Commerce trend ? What day and time of transaction ?")                                             
    st.write("                                                                    ")  
      


    # Merge products with products_translation become df_product
    products = data_products.merge(data_products_translation, left_on='product_category_name', right_on='product_category_name',how='left')
    df_product = products[["product_id","product_category_name_english","product_category_name"]]

    # Merge order_items with df products become df_order_items
    df_order_items = data_order_items.merge(df_product, left_on='product_id', right_on='product_id',how='left')

    # Merge df_order_items with seller
    sellers = data_sellers.drop(columns=['seller_zip_code_prefix'])
    df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')

    # merge orders with order_payments
    payments = data_order_payments.drop(columns = ['payment_sequential','payment_installments'])
    orders = data_orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

    # merge orders with customers
    customer = data_customer.drop(columns = ['customer_unique_id'])
    orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')
                
    # Changing the data type for date columns

    columns_to_convert = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                            'order_delivered_customer_date', 'order_estimated_delivery_date']
    orders[columns_to_convert] = orders[columns_to_convert].apply(pd.to_datetime)
    orders['order_status'] = orders['order_status'].astype('category')

  
    shippment_order = orders.loc[orders['order_status'] == 'shipped']


    # # Handle Missing Values
    orders = orders.dropna(subset=["payment_type", "payment_value"])

    # Remove Duplicates
    orders.drop_duplicates(inplace=True)

    # Extracting attributes for purchase date - Year and Month
    orders['order_purchase_year'] = orders['order_purchase_timestamp'].apply(lambda x: x.year)
    orders['order_purchase_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.month)
    orders['order_purchase_month_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%b'))
    orders['order_purchase_year_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m'))
    orders['order_purchase_date'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m%d'))

    # Extracting attributes for purchase date - Day and Day of Week
    orders['long_delivery_days'] = (orders["order_delivered_customer_date"] - orders["order_delivered_carrier_date"]).dt.days
    orders['order_purchase_day'] = orders['order_purchase_timestamp'].apply(lambda x: x.day)
    orders['order_purchase_dayofweek'] = orders['order_purchase_timestamp'].apply(lambda x: x.dayofweek)
    orders['order_purchase_dayofweek_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%a'))

    # Extracting attributes for purchase date - Hour and Time of the Day
    orders['order_purchase_hour'] = orders['order_purchase_timestamp'].apply(lambda x: x.hour)
    hours_bins = [-0.1, 6, 12, 18, 23]
    hours_labels = ['Dawn', 'Morning', 'Afternoon', 'Night']
    orders['order_purchase_time_day'] = pd.cut(orders['order_purchase_hour'], hours_bins, labels=hours_labels)

    # Display the data
    tab61, tab62, tab63, tab64, tab65, tab66 = st.tabs(["1.Product Category ", "2.Product Reviews", "3.Popular Product Orders", "4.Average Time Delivered", "5.Sales Comparation", "6.e-Commerce Trend"])

    with tab61:
        st.subheader("1. Which Top and Bottom 10 Category of Products ?")
        st.write("                                             ")  

        # Get the top 10 product categories
        top_10_category = df_product["product_category_name_english"].value_counts().sort_values(ascending=False)[:10]

        # Get the Bottom product categories
        bottom_10_category = df_product["product_category_name_english"].value_counts().sort_values(ascending=True)[:10]
     
        # Create a bar chart
        fig_top, ax = plt.subplots(figsize=(10, 5))
        sns.set_style("darkgrid")
        plottop = sns.barplot(x=top_10_category.index, y=top_10_category.values, color='#ff6666')

        # Add annotations to the bars
        for bar in plottop.patches:
            plottop.annotate(
                format(((bar.get_height() / len(df_product["product_category_name_english"])) * 100), '.2f') + "%",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha='center',
                va='center',
                size=7,
                xytext=(0, 5),
                textcoords='offset points',
            )

        # Rotate the x-axis labels
        plt.xticks(rotation=75)

        # Set the chart title
        plt.title('Top 10 Product Categories')

        # Display the chart in Streamlit
        st.pyplot(fig_top)

        # Create a bar chart
        fig_bottom, ax = plt.subplots(figsize=(10, 5))
        sns.set_style("darkgrid")
        plotbottom = sns.barplot(x=bottom_10_category.index, y=bottom_10_category.values, color='#ff6666')

        # Add annotations to the bars
        for bar in plotbottom.patches:
            plotbottom.annotate(
                format(((bar.get_height() / len(df_product["product_category_name_english"])) * 100), '.3f') + "%",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha='center',
                va='center',
                size=7,
                xytext=(0, 5),
                textcoords='offset points',
            )

        # Rotate the x-axis labels
        plt.xticks(rotation=75)

        # Set the chart title
        plt.title('Bottom 10 Product Categories')

        # Display the chart in Streamlit
        st.pyplot(fig_bottom)


    with tab62:
        st.subheader("2. What Top Positively and Negatively Reviewed Products ?")
        st.write("                                             ")  

        # Find the products that usually appear in the positvely reviewed / negatively reviewed order
        # Function to find top positively and negatively reviewed products
        def find_top_reviewed_products(data_order_reviews, data_orders, data_order_items, df_product, n=10):
            satis_table = data_order_reviews.merge(data_orders, on='order_id').merge(data_order_items, on='order_id').merge(df_product, on='product_id')

            # Labeling customer review score
            satis_table['satisfaction'] = satis_table['review_score'].apply(lambda x:
                                        "negative_order" if x < 3
                                        else (
                                                "positive_order" if x > 3
                                                else "neutral")
                                        )

            # Group by product - satisfaction, get the count of occurrence
            satis_table = satis_table.groupby(['product_id', 'product_category_name_english', 'satisfaction']).agg({'order_id': 'count'}).reset_index().sort_values('order_id', ascending=False)

            # Get top N positive products and top N negative products
            top_pos = satis_table[satis_table['satisfaction'] == 'positive_order'][:n]
            top_neg = satis_table[satis_table['satisfaction'] == 'negative_order'][:n]

            return top_pos, top_neg


        # Call the function to find top reviewed products
        n = 10  # Change this value to show a different number of products
        top_positively_reviewed, top_negatively_reviewed = find_top_reviewed_products(data_order_reviews, data_orders, data_order_items, df_product, n)


        # Display a bar chart for the top positively reviewed products
        fig_pos = plt.figure(figsize=(10, 5))
        sns.barplot(x='order_id', y='product_category_name_english', data=top_positively_reviewed, ax=plt.gca())
        plt.title("Top Positively Reviewed Products")
        st.pyplot(fig_pos)       
        st.write("                                             ")    


        # Display a bar chart for the top negatively reviewed products
        fig_neg = plt.figure(figsize=(10, 5))
        sns.barplot(x='order_id', y='product_category_name_english', data=top_negatively_reviewed, ax=plt.gca())
        plt.title("Top Negatively Reviewed Products")
        st.pyplot(fig_neg)
        st.write("                                             ")    


    with tab63:
        st.subheader("3. Which Category of goods that are most and least popular orders ?")
        st.write("                                             ") 
       
       # Group and aggregate the data
        df_category = df_order_items.groupby(by="product_category_name_english")["product_id"].count().reset_index()
        df_category = df_category.rename(columns={"product_category_name_english": "category", "product_id": "orders"})

        # Sort data
        df_category_top = df_category.sort_values(by="orders", ascending=False).head(10)
        df_category_bottom = df_category.sort_values(by="orders", ascending=True).head(10)


        colors = ["#102cd4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

        fig_top = plt.figure(figsize=(10, 5))
        sns.barplot(x='orders', y='category', data=df_category_top, ax=plt.gca())
        plt.title("Category the most popular orders", fontsize=16)
        st.pyplot(fig_top)       


        fig_bottom = plt.figure(figsize=(10, 5))
        sns.barplot(x='orders', y='category', data=df_category_bottom, ax=plt.gca())
        plt.title("Category the least popular orders", fontsize=16)
        st.pyplot(fig_bottom)       
        st.write("                                             ") 


    with tab64:
        st.subheader("4. How long does the long delivery days ? from where to where ? ")
        st.write("                                             ")  

        orders = orders[orders["long_delivery_days"] > 0]
        
        orders.groupby(by="customer_city").long_delivery_days.median().sort_values(ascending=False) 

        # Merge customer and seller data
        cust = orders[['customer_city', 'customer_state', 'long_delivery_days', 'order_id', 'customer_id']]
        seller = df_order_items[['order_id', 'seller_id', 'seller_city', 'seller_state']]
        cust_seller = cust.merge(seller, left_on='order_id', right_on='order_id', how='left')

        # Remove duplicated data
        cust_seller = cust_seller.drop_duplicates()

        # Calculate median delivery days between seller and customer states
        state_time_delivered = cust_seller.groupby(['seller_state', 'customer_state'])['long_delivery_days'].mean().sort_values(ascending=False).reset_index()

        # Display a boxplot of delivery days between states
        fig1 = plt.figure(constrained_layout=True, figsize=(8, 6))
        st.subheader("Boxplot of Delivery Days Between States")
        sns.set(style="whitegrid")
        sns.boxplot(x=state_time_delivered['long_delivery_days'])
        plt.title("Long Delivery Days Between States", fontsize=14)
        st.pyplot(fig1)
        st.write("                                             ")  

        # Calculate statistics (Q1, Q3, IQR) for states and cities
        Q1_state = (state_time_delivered['long_delivery_days']).quantile(0.25)
        Q3_state = (state_time_delivered['long_delivery_days']).quantile(0.75)
        IQR_state = Q3_state - Q1_state
        maximum_state = Q3_state + (1.5 * IQR_state)

        # Get the filtered dataframes
        filtered_state_data = state_time_delivered[state_time_delivered['long_delivery_days'] <= maximum_state]
        result_state = filtered_state_data.head(1)

        # Display the results for Statistics Quantile & IQR for States
        st.write("**Statistics Quantile & IQR Between States**")
        st.write("Maximum Limit Delivery Days Between State :", maximum_state)
        st.write("                                             ")  
        st.write('**From Dataset Long Delivery Days Between States is**')
        st.dataframe(result_state)
        st.write("                                             ")  
        

        # Calculate median delivery days between seller and customer cities
        city_time_delivered = cust_seller.groupby(['seller_city', 'customer_city'])['long_delivery_days'].mean().sort_values(ascending=False).reset_index()

        # Display a boxplot of delivery days between cities
        fig2 = plt.figure(constrained_layout=True, figsize=(8, 6))
        st.subheader("Boxplot of Delivery Days Between Cities")
        sns.set(style="whitegrid")
        sns.boxplot(x=city_time_delivered['long_delivery_days'])
        plt.title("Long Delivery Days Between Cities", fontsize=14)
        st.pyplot(fig2)
        st.write("                                             ")  

        Q1_city = (city_time_delivered['long_delivery_days']).quantile(0.25)
        Q3_city = (city_time_delivered['long_delivery_days']).quantile(0.75)
        IQR_city = Q3_city - Q1_city
        maximum_city = Q3_city + (1.5 * IQR_city)

        filtered_city_data = city_time_delivered[city_time_delivered['long_delivery_days'] <= maximum_city]
        result_city = filtered_city_data.head(1)
         
        # Display the results for Statistics Quantile & IQR for Cities
        st.write("**Statistics Quantile & IQR Between Cities**")
        st.write("Maximum Limit Delivery Days Between City :", maximum_city)
        st.write("                                             ")  
        st.write('**From Dataset Long Delivery Days Between Cities is**')
        st.dataframe(result_city)          
        st.write("                                             ")  
      

    with tab65:
        st.subheader("5. How do sales comparison in 2017 and 2018 ?")
        st.write("                                             ")  

        # confirm data types 
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
        orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
        orders['order_status'] = orders['order_status'].astype('category')  

        # orders = data_orders.merge(data_customer, how='left', on='customer_id')
        # orders = data_orders.merge(data_customer, left_on='customer_id', right_on='customer_id',how='left')       
        orders = data_orders.merge(data_customer, how='left', on='customer_id')

        # Changing the data type for date columns
        timestamp_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 
                        'order_estimated_delivery_date']
        for col in timestamp_cols:
            orders[col] = pd.to_datetime(orders[col])
            
        # Extracting attributes for purchase date - Year and Month
        orders['order_purchase_year'] = orders['order_purchase_timestamp'].apply(lambda x: x.year)
        orders['order_purchase_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.month)
        orders['order_purchase_month_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%b'))
        orders['order_purchase_year_month'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m'))
        orders['order_purchase_date'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%Y%m%d'))

        # Extracting attributes for purchase date - Day and Day of Week
        orders['order_purchase_dayofweek'] = orders['order_purchase_timestamp'].apply(lambda x: x.dayofweek)
        orders['order_purchase_dayofweek_name'] = orders['order_purchase_timestamp'].apply(lambda x: x.strftime('%a'))

        # Extracting attributes for purchase date - Hour and Time of the Day
        orders['order_purchase_hour'] = orders['order_purchase_timestamp'].apply(lambda x: x.hour)
        hours_bins = [-0.1, 6, 12, 18, 23]
        hours_labels = ['Dawn', 'Morning', 'Afternoon', 'Night']
        orders['order_purchase_time_day'] = pd.cut(orders['order_purchase_hour'], hours_bins, labels=hours_labels)

        # Define the single_countplot function (no need to modify this)
        def single_countplot(data, x, ax):
            sns.countplot(data=data, x=x, ax=ax)

        # Creating figure
        fig = plt.figure(constrained_layout=True, figsize=(13, 5))

        # Axis definition
        gs = GridSpec(1, 3, figure=fig)
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1:])

        # Annotation - Growth in e-commerce orders between 2017 and 2018
        orders_compare = orders.query('order_purchase_year in (2017, 2018) & order_purchase_month <= 8')
        year_orders = orders_compare['order_purchase_year'].value_counts()
        growth = int(round(100 * (1 + year_orders[2017] / year_orders[2018]), 0))

        color_2017 = 'mediumseagreen'
        color_2018 = 'darkslateblue'

        ax1.text(0.00, 0.73, f'{year_orders[2017]}', fontsize=40, color=color_2017, ha='center')
        ax1.text(0.00, 0.64, 'orders registered in 2017\nbetween January and August', fontsize=10, ha='center')
        ax1.text(0.00, 0.40, f'{year_orders[2018]}', fontsize=60, color=color_2018, ha='center')
        ax1.text(0.00, 0.31, 'orders registered in 2018\nbetween January and August', fontsize=10, ha='center')
        signal = '+' if growth > 0 else '-'
        ax1.text(0.00, 0.20, f'{signal}{growth}%', fontsize=14, ha='center', color='white', style='italic', weight='bold',
                bbox=dict(facecolor='navy', alpha=0.5, pad=10, boxstyle='round, pad=.7'))
        ax1.axis('off')

        # Bar chart - Comparison between monthly sales between 2017 and 2018
        sns.countplot(data=orders_compare, x='order_purchase_month', hue='order_purchase_year', ax=ax2,
                    palette={2017: color_2017, 2018: color_2018})
        month_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
        ax2.set_xticklabels(month_label)
        ax2.set_title('Total Orders Comparison Between 2017 and 2018 (January to August)', size=12, color='dimgrey', pad=20)
        plt.legend(loc='upper right')  

        # Display the figure in Streamlit
        st.pyplot(fig)

    with tab66:
        st.subheader("6. How e-Commerce trend ? What day and time of transaction ?")
        st.write("                                             ")  

        # Create a figure
        fig = plt.figure(constrained_layout=True, figsize=(13, 10))

        # Axis definition
        gs = GridSpec(2, 2, figure=fig)
        ax1 = fig.add_subplot(gs[0, :])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[1, 1])

        # Lineplot - Evolution Trend of e-commerce orders along time
        sns.lineplot(data=orders['order_purchase_year_month'].value_counts().sort_index(), ax=ax1,
                    color='darkslateblue', linewidth=2)
        ax1.annotate(f'Highest orders received', (13, 7500), xytext=(-75, -25),
                    textcoords='offset points', bbox=dict(boxstyle="round4", fc="w", pad=.8),
                    arrowprops=dict(arrowstyle='-|>', fc='w'), color='dimgrey', ha='center')
        ax1.annotate(f'Noise on data (huge decrease)', (23, 0), xytext=(48, 25),
                    textcoords='offset points', bbox=dict(boxstyle="round4", fc="w", pad=.5),
                    arrowprops=dict(arrowstyle='-|>', fc='w'), color='dimgrey', ha='center')

        for tick in ax1.get_xticklabels():
            tick.set_rotation(45)
        ax1.set_title('Evolution Trend of Total Orders in E-Commerce', size=14, color='dimgrey')
        
        # Barchart - Total of orders by day of the week
        sns.countplot(data=orders, x='order_purchase_dayofweek', ax=ax2, palette='YlGnBu')

        weekday_label = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        ax2.set_xticklabels(weekday_label)
        ax2.set_title('Total Orders by Day of the Week', size=14, color='dimgrey', pad=20)

        # Barchart - Total of orders by time of the day
        day_color_list = ['darkslateblue', 'deepskyblue', 'darkorange', 'purple']
        sns.countplot(data=orders, x='order_purchase_time_day', ax=ax3, order=['Dawn', 'Morning', 'Afternoon', 'Night'], palette=day_color_list)

        ax3.set_title('Total Orders by Time of the Day', size=14, color='dimgrey', pad=20)

        # Display the figures in Streamlit
        st.pyplot(fig)

def Conclusion():
    st.subheader("This Part of Conclusion")
    st.write("                                             ")  
    st.write("""**Based on the determining business questions at the beginning, the following are the conclusions from the answers of EDA and the Visualization and Explanatory Analysis parts:**

    """)
    st.write("**1. Which Top and Bottom 10 Category of Products ?**")
    st.write("Answer :                                                                     ")  
    st.write("Top Category of Products is **bed_bath_table**")   
    st.write("Bottom Category of Products is **cds_dvds_musicals**")       
    st.write("                                                                    ")      
    st.write("**2. Which Top Positively and Negatively Reviewed Products ?**")
    st.write("Answer :                                                                     ")        
    st.write("Top Positively Reviewed Products is **furniture_decor**")   
    st.write("Top Negatively Reviewed Products is **garden_tools**")       
    st.write("                                                                    ")  
    st.write("**3. Which Category of goods that are most and least popular orders ?**")
    st.write("Answer :                                                                     ")  
    st.write("The most popular orders is **bed_bath_table**")   
    st.write("The least popular orders is **security_and_services**")                 
    st.write("                                                                    ")      
    st.write("**4. How long does the long delivery days ? from where to where ?**")   
    st.write("Answer :                                                                     ")        
    st.write("The long delivery days between state is **27.03 days** , from **SP** to **RR**")   
    st.write("The long delivery days between city is **24.25 days** , from **sao jose dos campos** to **belem**")              
    st.write("                                                                    ")  
    st.write("**5. How do sales comparison in 2017 and 2018 ?**")
    st.write("Answer :                                                                     ")   
    st.write("Sales in 2017 is **22968**")   
    st.write("Sales in 2018 is **53991**")   
    st.write("Sales increase is **143 %**")                            
    st.write("                                                                    ")  
    st.write("**6. How e-Commerce trend ? What day and time of transaction ?**")
    st.write("Answer :                                                                     ")                                                     
    st.write("e-Commerce trend **tends to increase**")   
    st.write("The highest transaction is **Monday** and the lowest is **Saturday**")   
    st.write("The highest transactions are during the **Afternoon** and the lowest at **Dawn**")            
    st.write("                                                                    ")
    st.write("""Conclusion :The e-Commerce trend as a whole until November 2017 **tended to increase**,""")   
    st.write("""for the period December 2017 to August 2018 the trend tended to **fluctuate**,""")   
    st.write("""but entering September 2017 there was a **decrease**.""")  


if add_selectitem == "1. Data Wrangling - Gathering Data":
    gathering()
elif add_selectitem == "2. Data Wrangling - Assesing Data":
    assesing()
elif add_selectitem == "3. Data Wrangling - Cleaning Data":
    cleaning()
elif add_selectitem == "4. Exploratory Data Analysis (EDA)":
    EDA()
elif add_selectitem == "5. Recency Frequency Monetary (RFM)":
    RFM()
elif add_selectitem == "6. Visualization & Explanatory Analysis":
   Visualization()
elif add_selectitem == "7. Conclusion":
   Conclusion()
