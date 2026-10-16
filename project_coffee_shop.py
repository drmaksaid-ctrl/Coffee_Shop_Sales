import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Coffee Shop Sales Analysis',layout='wide')

df=pd.read_csv('project coffee shop Cleaned.csv',index_col=0)

st.title('📊Coffee Shope Sales Analysis📊')
st.markdown('Project Data Analysis – Conducted and overseen by Dr. Mohamed Fathalla',width=500)
st.markdown('-------')
st.image('images.jfif',width=600)
tab1,tab2,tab3,tab4=st.tabs(['Data Overview','Univariate Analysis','Bivariate Analysis','Multivariate Analysis'])

with tab1:
    st.subheader('Dataset Preview')
    st.dataframe(df.head(10),hide_index=True,use_container_width=True)

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total Revenues',df['Revenue'] .sum().round(2))
    with col2:
        st.metric('Total Sales Units',df['transaction_qty'].sum())
    with col3:
        st.metric('Total Transaction',df['transaction_id'].nunique())
    with col4:
        st.metric('Average Order Value',df['Revenue'].mean().round(2))

with tab2:
    st.subheader('Univariate Analysis')
    st.markdown('select any column to view its details ',width=500)
    selected_column = st.selectbox('choose column:',df.columns)
    fig_uni = px.histogram(df,x=selected_column,title=f'Details of {selected_column}',color_discrete_sequence=['#653EFA'])
    st.plotly_chart(fig_uni,use_container_width=True)

    hour_count = df["hours"].value_counts().sort_index().reset_index()

    fig_1 = px.bar(hour_count,x="hours",y="count",title="Number of Transactions by Hour⏰",labels={"hours": "Hour of Day","count": "Transactions"})

    st.plotly_chart(fig_1,use_container_width=True)

    category_count = df["product_category"].value_counts().reset_index()

    fig_2 = px.pie(category_count,names="product_category",values="count",title="Transaction Distribution by Product Category")

    st.plotly_chart(fig_2,use_container_width=True)

    category_count = df["product_category"].value_counts().reset_index()

    fig_3 = px.bar(category_count,x="product_category",y="count",title="Number of Transactions by Product Category",
                   labels={"product_category": "Product Category","count": "Number of Transactions"})

    st.plotly_chart(fig_3,use_container_width=True)

with tab3:
    st.subheader('Bivariate Analysis')

    daily_sales = (df.groupby("transaction_date", as_index=False)["Revenue"].sum())

    fig2 = px.line(daily_sales,x="transaction_date",y="Revenue",title="Daily Revenue Trend",markers=True,color_discrete_sequence=['red'])

    st.plotly_chart(fig2,use_container_width=True)

    col1,col2 = st.columns(2)

    with col1:
        store_sales = (df.groupby("store_location", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False))
        fig3 = px.bar(store_sales,x="store_location",y="Revenue",title="Revenue by Store",text_auto=".2s",color_discrete_sequence=['blue'])
        st.plotly_chart(fig3,use_container_width=True)

    with col2:
        hourly_sales = (df.groupby("hours", as_index=False)["Revenue"].sum())
        fig4 = px.bar(hourly_sales,x="hours",y="Revenue",title="Revenue by hours",color_discrete_sequence=['blue'])
        st.plotly_chart(fig4,use_container_width=True)

    top_products = (df.groupby("product_detail", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False).head(10))
    fig5 = px.bar(top_products.sort_values("Revenue"),x="Revenue",y="product_detail",orientation="h",title="Top 10 Products by Revenue",
    text_auto=".2s",color_discrete_sequence=['green'])
    st.plotly_chart(fig5,use_container_width=True)

with tab4:
    st.subheader('Multivariate Analysis')
    monthly_category = (df.groupby(["month_name", "product_category"],as_index=False)["Revenue"].sum())
    fig6 = px.line(monthly_category,x="month_name",y="Revenue",color="product_category",markers=True,
                   title="Monthly Revenue by Product Category")
    st.plotly_chart(fig6,use_container_width=True)

    store_category_qty = (df.groupby(["store_location", "product_category"],as_index=False)["transaction_qty"].sum())
    fig7 = px.bar(store_category_qty,x="store_location",y="transaction_qty",color="product_category",
                  title="Quantity Sold by Store and Category",barmode="stack")

    st.plotly_chart(fig7,use_container_width=True)

    daily_store = (df.groupby(["transaction_date", "store_location"],as_index=False)["Revenue"].sum())
    fig8 = px.box(daily_store,x="store_location",y="Revenue",color="store_location",title="Daily Revenue Distribution by Store")

    st.plotly_chart(fig8,use_container_width=True)

    heatmap_data = (df.groupby(["day", "hours"])["Revenue"].sum().reset_index())

    heatmap_pivot = heatmap_data.pivot(index="day",columns="hours",values="Revenue")
    fig9 = px.imshow(heatmap_pivot,title="Revenue Heatmap — day vs hours",labels={
        "x": "hours",
        "y": "day",
        "color": "Revenue"},aspect="auto",color_continuous_scale="greens")

    st.plotly_chart(fig9,use_container_width=True)








