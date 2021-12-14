import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install pLotly-express
import streamlit as st # pip install streamlit

st.set_page_config(page_title="Korean Clothes Shopee Dashboard",
                   layout="wide", page_icon='baricon.png')

df = pd.read_csv('clean_data.csv')

st.sidebar.header("Please Filter Here:")
shopee = sorted(df['shop_location'].unique())
shop = st.sidebar.selectbox(label="Shops location", options=shopee)

product = st.sidebar.multiselect ("Select Product Category:",
options=df["product_category"].unique(),
default=df["product_category"].unique(),
)

date = st.sidebar.multiselect ("Select Date Collected:",
options=df["date_collected"].unique(),
default=df["date_collected"].unique(),
)

df_selection = df.query(
    "product_category == @product & shop_location == @shop & date_collected == @date"
)
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

#MAINPAGE
st.title (" 📊 Korean Clothes Dashboard")
st.markdown ("##")

st.dataframe(df_selection)

productt = df_selection.product_category.unique()
shops = df_selection.shop_location.unique()
dates = df.date_collected.unique()
product_unique = (df_selection.groupby('product_category')['product_name'].count())
product_date = (df.groupby('date_collected')['product_name'].count())
rate5 = list(df_selection.groupby('product_category')['prod_rate_star_5'].sum().values)
rate4 = list(df_selection.groupby('product_category')['prod_rate_star_4'].sum().values)
rate3 = list(df_selection.groupby('product_category')['prod_rate_star_3'].sum().values)
rate2 = list(df_selection.groupby('product_category')['prod_rate_star_2'].sum().values)
rate1 = list(df_selection.groupby('product_category')['prod_rate_star_1'].sum().values)
rate0 = list(df_selection.groupby('product_category')['prod_rate_star_0'].sum().values)

fig_rates5_by_product = px.bar(
    df_selection,
    x = rate5,
    y = productt,
    orientation="h",
    title="<b>Rated 5 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)
fig_rates5_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_rates5_by_product)

fig_rates4_by_product = px.bar(
    df_selection,
    x = rate4,
    y = productt,
    orientation="h",
    title="<b>Rated 4 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)
fig_rates4_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_rates4_by_product)

fig_rates3_by_product = px.bar(
    df_selection,
    x = rate3,
    y = productt,
    orientation="h",
    title="<b>Rated 3 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)

fig_rates3_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_rates3_by_product)

fig_rates2_by_product = px.bar(
    df_selection,
    x = rate2,
    y = productt,
    orientation="h",
    title="<b>Rated 2 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)
fig_rates2_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_rates2_by_product)

fig_rates1_by_product = px.bar(
    df_selection,
    x = rate1,
    y = productt,
    orientation="h",
    title="<b>Rated 1 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)

fig_rates1_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_rates1_by_product)

fig_rates0_by_product = px.bar(
    df_selection,
    x = rate0,
    y = productt,
    orientation="h",
    title="<b>Rated 0 stars by product</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)

fig_rates0_by_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_rates0_by_product)

fig_number_of_product = px.bar(
    df_selection,
    x = productt,
    y = product_unique,
    orientation="v",
    title="<b>Number of products per Category</b>",
    color_discrete_sequence=["#0083B8"] * len(df_selection),
    template="plotly_white",
)
fig_number_of_product.update_layout(
    plot_bgcolor ="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)),

)

st.plotly_chart(fig_number_of_product)

#Pie Chart
fig_prod = px.pie(
    df_selection,
    values= product_unique,
    names= productt,
    title='Total number of product per Category',
    hole=.3
)

fig_prod.update_traces(hoverinfo='label+percent', textfont_size=20, textinfo='value',
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))

st.plotly_chart(fig_prod)



shopssss = st.multiselect ("Select Shops:",
options=df["shop_location"].unique(),
default=df["shop_location"].unique(),
)
dff_selection = df.query(
    "product_category == @product & shop_location == @shopssss & date_collected == @date"
)

dates = dff_selection.date_collected.unique()
product_date = (dff_selection.groupby('date_collected')['product_name'].count())
producttt = dff_selection.shop_location.unique()
product_shops = (dff_selection.groupby('shop_location')['product_name'].count())


#pie chart
fig_shops = px.pie(
    dff_selection,
    values= product_shops,
    names= producttt,
    title='Total Number of Products per Shop',
    hole=.5

)

fig_shops.update_traces(hoverinfo='label+percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig_shops.update_layout(margin=dict(t=0, b=0, l=0, r=0))

st.plotly_chart(fig_shops)


#Line Chart
fig_shops_again = px.line(df, x=dates, y=product_date, title='Total Products per Date Collected', markers=True)

st.plotly_chart(fig_shops_again)




hide_st_style = "<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} header (visibility: hidden;} </style>"
st.markdown (hide_st_style, unsafe_allow_html=True)
