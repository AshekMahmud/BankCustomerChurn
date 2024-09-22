import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('https://raw.githubusercontent.com/AshekMahmud/BankCustomerChurn/refs/heads/main/bank%20churn%20cleaned.csv')

df.columns = df.columns.str.strip()


age_group = df['age_group'].unique()
gender = df['Gender'].unique()
country = df['Geography'].unique()

st.set_page_config(page_title = 'BankChurn', page_icon='📈', layout= 'wide')
st.title('📊 Bank Customer Churn')


# st.markdown("""
#     <style>
#         .main {
#             background: linear-gradient(to bottom, #000000, #001e43, #400021);}
#     </style>
#     """, unsafe_allow_html=True)

# app background:
st.markdown("""
    <style>
        .main {
            background-color:hsla(0,0%,0%,1);
            background-image:
            radial-gradient(at 76% 79%, hsla(329,100%,12%,1) 0px, transparent 50%),
            radial-gradient(at 27% 46%, hsla(213,100%,13%,1) 0px, transparent 50%);}
    </style>
    """, unsafe_allow_html=True)

# hide hte streamlit header and bars:
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

# filtering the data for sidebar:
select_age_group = st.sidebar.multiselect('Age_group', age_group)
select_gender = st.sidebar.multiselect('Gender', gender)
select_country = st.sidebar.multiselect('Country', country)

if not select_age_group:
    select_age_group = age_group
if not select_gender:
    select_gender = gender
if not select_country:
    select_country = country

filtered_df = df[(df['age_group'].isin(select_age_group)) &
                 (df['Gender'].isin(select_gender)) &
                 (df['Geography'].isin(select_country))]


# Define the function to categorize balance
def categorize_balance(balance):
    if balance < 50000:
        return '<50k'
    elif 50000 <= balance <= 100000:
        return '50k-100k'
    elif 100000 < balance <= 150000:
        return '100k-150k'
    elif 150000 < balance <= 200000:
        return '150k-200k'
    else:
        return '>200k'

# Apply the function to the Balance column to create new column Balance_group:
filtered_df['Balance_group'] = filtered_df['Balance'].apply(categorize_balance)

def categorize_Credit(risk):
    if risk == 'high risk':
        return '300-579'
    elif risk == 'moderate risk':
        return '580-669'
    elif risk == 'low risk':
        return '670-739'
    elif risk == 'lowest risk':
        return '740-799'
    else:
        return '800-850'

# Apply the function to the risk column to create new column CreditScore:
filtered_df['CreaditScore'] = filtered_df['risk'].apply(categorize_Credit)
df['CreditScore_group'] = df['risk'].apply(categorize_Credit)

# calculations
total_member = filtered_df.shape[0]
churned = filtered_df[filtered_df['Exited'] == 1].shape[0]
nonchurned = filtered_df[filtered_df['Exited'] == 0].shape[0]

# percentage
churned_per = (churned/total_member)*100
nonchurned_per = (nonchurned/total_member)*100

# card style
card_style = """
    background-color: #202020;
    border: 1px solid #2e2e2e;
    padding: 10px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    width: 200px;
    height: 90px;
"""

col0,col1,col2,col3 = st.columns([0.3,1,1,1])
with col1:
    st.markdown(f"""
                <div style="background-color:#202020;
                            border: 1px solid #2e2e2e;
                            padding: 10px;
                            border-radius: 15px;
                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                            width: 200px;
                            height: 180px;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;
                            align-items: center;">
                <h3 style="text-align: center; color:#18FFFF; font-size:20px; margin-left: 18px;
                margin-right:0px; line-height:0.5;">Total Customer</h3>
                <p style="text-align: center; color:#18FFFF; font-size:25px; line-height:0.5;">{total_member}</p>
                </div>
                """, unsafe_allow_html=True)


# with col1:
#     st.markdown(f"""
#             <div style="{card_style}">
#             <h3 style="text-align: center; color:#18FFFF; font-size:20px; margin-left: 18px;
#             margin-right:0px; line-height:0.5;">Total Customer</h3>
#             <p style="text-align: center; color:#18FFFF; font-size:25px; line-height:0.5;">{total_member}</p>
#             </div>
#             """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
            <div style="{card_style}">
            <h3 style="text-align: center; color:#F11A7B; font-size:15px; margin-left: 18px;
            margin-right:0px; line-height:0.5;">Churned Customer</h3>
            <p style="text-align: center; color:#F11A7B; font-size:17px; line-height:0.5;">{churned}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown(f"""
            <div style="{card_style}">
            <h3 style="text-align: center; color:#F11A7B; font-size:15px;margin-left: 18px;
            margin-right:0px; line-height:0.5;">Churned Percentage</h3>
            <p style="text-align: center; color:#F11A7B; font-size:17px; line-height:0.5;">{churned_per:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
            <div style="{card_style}">
            <h3 style="text-align: center; color:#18FFFF; font-size:15px; margin-left: 18px;
            margin-right:0px; line-height:0.5;">Retained Customer</h3>
            <p style="text-align: center; color:#18FFFF; font-size:17px; line-height:0.5;">{nonchurned}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown(f"""
            <div style="{card_style}">
            <h3 style="text-align: center; color:#18FFFF; font-size:15px;margin-left: 18px;
            margin-right:0px; line-height:0.5;">Retained Percentage</h3>
            <p style="text-align: center; color:#18FFFF; font-size:17px; line-height:0.5;">{nonchurned_per:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

col4,col5,col6, col7 = st.columns(4)
with col4:
    fig1 = go.Figure()

    fig1.add_trace(go.Pie(
        labels=filtered_df['Gender'].unique(), values=filtered_df['Gender'].value_counts(),
        textinfo='label+value+percent',
        marker=dict(colors=['#F11A7B', '#18FFFF']),
        hole=0.6
    ))

    fig1.update_layout(
        title=dict(text='Male and Female proportion', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white')))

    st.plotly_chart(fig1, use_container_width=True)

with col5:
    filtered_df['IsActiveMember'] = filtered_df['IsActiveMember'].map({1: 'Active', 0: 'Inactive'})
    fig4 = go.Figure()

    fig4.add_trace(go.Pie(
        labels=filtered_df['IsActiveMember'].unique(), values=filtered_df['IsActiveMember'].value_counts(),
        textinfo='label+value+percent',
        marker=dict(colors=['#F11A7B', '#18FFFF']),
        hole=0.6, rotation=180
    ))

    fig4.update_layout(
        title=dict(text='Active and Inactive Member Percent', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white')))
    st.plotly_chart(fig4, use_container_width=True)


with col6:
    filtered_df['HasCrCard'] = filtered_df['HasCrCard'].map({0: "haven't", 1: 'have'})

    fig2 = go.Figure()

    fig2.add_trace(go.Pie(
        labels=filtered_df['HasCrCard'].unique(), values=filtered_df['HasCrCard'].value_counts(),
        textinfo='label+value+percent',
        marker=dict(colors=['#F11A7B', '#18FFFF']),
        hole=0.6
    ))

    fig2.update_layout(
        title=dict(text='Credit Card Holder Percent', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white')))
    st.plotly_chart(fig2, use_container_width=True)

with col7:
    fig5 = go.Figure()

    fig5.add_trace(go.Pie(
        labels=filtered_df['NumOfProducts'].unique(), values=filtered_df['NumOfProducts'].value_counts(),
        textinfo='label+percent',
        marker=dict(colors=['#F11A7B', '#18FFFF', '#9400FF', '#FFDB00']),
        hole=0.6,
        # textposition='auto', textfont=dict(color='white'),
        rotation=250
    ))

    fig5.update_layout(
        title=dict(text='Product useage', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white')))

    st.plotly_chart(fig5, use_container_width=True)

col8, col9 = st.columns(2)
with col8:
    grouped_df = filtered_df.groupby(['age_group', 'Exited']).size().reset_index(name='count')
    total_count = grouped_df.groupby('age_group')['count'].sum().reset_index(name='total')
    grouped_df = grouped_df.merge(total_count, on='age_group')
    grouped_df['percentage'] = (grouped_df['count'] / grouped_df['total']) * 100

    # Separate data for plotting
    non_churned = grouped_df[grouped_df['Exited'] == 0]
    churned = grouped_df[grouped_df['Exited'] == 1]

    # Create bar chart
    fig = go.Figure(data=[
        go.Bar(x=non_churned['age_group'], y=non_churned['count'], name='Retained',
               text=non_churned['count'], textposition='outside', textfont=dict(color='white'),
               hovertext=non_churned.apply(
                   lambda row: f"Count:{row['count']}<br>Percentage:{row['percentage']:.2f}%", axis=1),
               marker=dict(color='#18FFFF'), width=0.3),
        go.Bar(x=churned['age_group'], y=churned['count'], name='Churned',
               text=churned['count'], textposition='outside', textfont=dict(color='white'),
               hovertext=churned.apply(
                   lambda row: f"Count:{row['count']}<br>Percentage:{row['percentage']:.2f}%", axis=1),
               marker=dict(color='#F11A7B'), width=0.3)
    ])

    # Update layout
    fig.update_layout(
        barmode='group',
        title=dict(text='Customer Churn by Age Group', font=dict(color='white')),
        xaxis_title=dict(text='Age Group', font=dict(color='white')),
        yaxis_title=dict(text='Count of Customers', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1,
                    font=dict(color='white'))
    )
    # Show figure
    st.plotly_chart(fig,use_container_width=True)
with col8:
    with st.expander('More detail about age_group'):
        pie_data = grouped_df[grouped_df['Exited'] == 1]
        pie_fig = go.Figure()
        pie_fig.add_trace(go.Pie(labels=pie_data['age_group'], values=pie_data['percentage'],
                              hoverinfo='label+percent', textinfo='value',
                              hole=0.5,
                              textposition='outside',
                              textfont=dict(color='white'),
                              marker=dict(colors=['#F11A7B', '#18FFFF', '#FFDD44', '#44FFDD']),
                              texttemplate='%{label}:<br> %{percent:.2f}%'))

        pie_fig.update_layout(
            title=dict(text='Percentage of Churned Customers by Age Group', font=dict(color='white')),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False)
        st.plotly_chart(pie_fig,use_container_width=True)

with col9:
    fil = filtered_df.copy()
    fil['risk'] = fil['risk'].map({'high risk': '300-579', 'moderate risk': '580-669', 'low risk': '670-739',
                                   'lower risk': '740-799', 'lowest risk': '800-850'})

    riskwise = fil.groupby(['risk', 'Exited']).size().reset_index(name='count')
    non_churned = riskwise[riskwise['Exited'] == 0]
    churned = riskwise[riskwise['Exited'] == 1]

    fig6 = go.Figure(data=[
        go.Bar(x=non_churned['risk'], y=non_churned['count'], name='Retained',
               text=non_churned['count'], textposition='outside', textfont=dict(color='white'),
               marker=dict(color='#18FFFF'), width=0.25),
        go.Bar(x=churned['risk'], y=churned['count'], name='Churned',
               text=churned['count'], textposition='outside', textfont=dict(color='white'),
               marker=dict(color='#F11A7B'), width=0.25)
    ])

    # Update layout
    fig6.update_layout(
        barmode='group',
        title=dict(text='Customer Churn by Credit Score', font=dict(color='white')),
        xaxis_title=dict(text='Credit Score Group', font=dict(color='white')),
        yaxis_title=dict(text='Count of Customers', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white'))
    )
    st.plotly_chart(fig6,use_container_width=True)

with col9:
    with st.expander('More detail about Credit Score'):
        cr_fig = go.Figure()
        cr_fig.add_trace(go.Pie(labels=churned['risk'], values=churned['count'],
                                hoverinfo='label+percent', textinfo='label+percent',
                                hole=0.5,
                                textposition='outside',
                                textfont=dict(color='white'),
                                marker=dict(colors=['#F11A7B', '#18FFFF', '#FFDD44', '#44FFDD']),
                                #                      texttemplate='%{label}:<br> %{percent:.2f}%'
                                ))

        cr_fig.update_layout(
            title=dict(text='Percentage of Churned Customers by Credit Score', font=dict(color='white')),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False)
        st.plotly_chart(cr_fig,use_container_width=True)

col10,col11 = st.columns(2)
with col10:
    grouped_df = filtered_df.groupby(['Gender', 'Exited']).size().reset_index(name='count')

    # Separate data for plotting
    non_churned = grouped_df[grouped_df['Exited'] == 0]
    churned = grouped_df[grouped_df['Exited'] == 1]

    # Create bar chart
    fig3 = go.Figure(data=[
        go.Bar(x=non_churned['Gender'], y=non_churned['count'], name='Retained',
               text=non_churned['count'], textposition='outside', textfont=dict(color='white'),
               marker=dict(color='#18FFFF'), width=0.3),
        go.Bar(x=churned['Gender'], y=churned['count'], name='Churned',
               text=churned['count'], textposition='outside', textfont=dict(color='white'),
               marker=dict(color='#F11A7B'), width=0.3)
    ])

    # Update layout
    fig3.update_layout(
        barmode='group',
        title=dict(text='Customer Churn by Gender', font=dict(color='white')),
        xaxis_title=dict(text='Gender', font=dict(color='white')),
        yaxis_title=dict(text='Count of Customers', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white'))
    )
    st.plotly_chart(fig3, use_container_width=True)

with col11:
    # Define the order of the categories
    balance_order = ['<50k', '50k-100k', '100k-150k', '150k-200k', '>200k']

    # Convert Balance_group to a categorical type with the specified order
    filtered_df['Balance_group'] = pd.Categorical(filtered_df['Balance_group'],
                                                  categories=balance_order, ordered=True)

    b_group = filtered_df.groupby(['Balance_group', 'Exited']).size().reset_index(name='mcount')
    total_m = b_group.groupby('Balance_group')['mcount'].sum().reset_index(name='total')
    b_group = b_group.merge(total_m, on='Balance_group')
    b_group['percentage'] = (b_group['mcount'] / b_group['total']) * 100

    churned_m = b_group[b_group['Exited'] == 1]
    non_churned_m = b_group[b_group['Exited'] == 0]

    # Create bar chart
    fig7 = go.Figure(data=[
        go.Bar(x=non_churned_m['Balance_group'], y=non_churned_m['mcount'], name='Retained',
               text=non_churned_m['mcount'], textposition='outside', textfont=dict(color='white'),
               hovertext=non_churned_m.apply(
                   lambda row: f"Count:{row['mcount']}<br>Percentage:{row['percentage']:.2f}%", axis=1),
               marker=dict(color='#18FFFF'), width=0.3),
        go.Bar(x=churned_m['Balance_group'], y=churned_m['mcount'], name='Churned',
               text=churned_m['mcount'], textposition='outside', textfont=dict(color='white'),
               hovertext=churned_m.apply(
                   lambda row: f"Count:{row['mcount']}<br>Percentage:{row['percentage']:.2f}%", axis=1),
               marker=dict(color='#F11A7B'), width=0.3)
    ])

    # Update layout
    fig7.update_layout(
        barmode='group',
        title=dict(text='Customer Churn by Balance', font=dict(color='white')),
        xaxis_title=dict(text='Balance Group', font=dict(color='white')),
        yaxis_title=dict(text='Count of Customers', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white'))
    )

    # Show figure
    st.plotly_chart(fig7,use_container_width=True)

col12, col13 = st.columns(2)
with col12:
    geo_group = filtered_df.groupby(['Geography', 'Exited']).size().reset_index(name='count')
    total = geo_group.groupby('Geography')['count'].sum().reset_index(name='total')
    geo_group = geo_group.merge(total, on='Geography')
    geo_group['percentage'] = ((geo_group['count'] / geo_group['total']) * 100).round(2)
    churned_geo = geo_group[geo_group['Exited'] == 1]
    churned_geo['formatted_percentage'] = churned_geo['percentage'].apply(lambda x: f"{x:.2f}%")

    # Create bar chart
    fig8 = go.Figure()

    fig8.add_trace(go.Bar(
        x=churned_geo['Geography'],
        y=churned_geo['percentage'],
        name='Churned',
        text=churned_geo['formatted_percentage'], textposition='outside', textfont=dict(color='white'),
        marker=dict(color='#F11A7B'), width=0.3))

    # Update layout
    fig8.update_layout(
        barmode='group',
        title=dict(text='Country wise Customer Churn Rate', font=dict(color='white')),
        xaxis_title=dict(text='Country', font=dict(color='white')),
        yaxis_title=dict(text='Customer Churn Rate', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white'))
    )
    st.plotly_chart(fig8,use_container_width=True)

with col13:
    g = filtered_df.groupby(['IsActiveMember', 'Exited']).size().reset_index(name='count')
    activity = g.groupby('IsActiveMember')['count'].sum().reset_index(name='sum')
    g = g.merge(activity, on='IsActiveMember')
    g['percent'] = ((g['count'] / g['sum']) * 100).round(2)

    nonchurn_cust = g[g['Exited'] == 0]
    churn_cust = g[g['Exited'] == 1]

    fig9 = go.Figure()

    fig9.add_trace(go.Bar(
        x=nonchurn_cust['IsActiveMember'],
        y=nonchurn_cust['percent'],
        name='Retained',
        text=nonchurn_cust['percent'].apply(lambda x: f"{x:.2f}%"),
        textposition='outside', textfont=dict(color='white'),
        marker=dict(color='#18FFFF'), width=0.2))
    fig9.add_trace(go.Bar(
        x=churn_cust['IsActiveMember'],
        y=churn_cust['percent'],
        name='Churned',
        text=churn_cust['percent'].apply(lambda x: f"{x:.2f}%"),
        textposition='outside', textfont=dict(color='white'),
        marker=dict(color='#F11A7B'), width=0.2))

    # Update layout
    fig9.update_layout(
        barmode='group',
        bargap=0.01,
        title=dict(text='Churn Rate according to Active/Inactive', font=dict(color='white')),
        xaxis_title=dict(text='Customers Category', font=dict(color='white')),
        yaxis_title=dict(text='Customer Rate', font=dict(color='white')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white')),
        yaxis=dict(showgrid=False, tickcolor='white', tickfont=dict(color='white'), showticklabels=False),
        legend=dict(orientation='h', xanchor='right', x=1, yanchor='top', y=1.1,
                    font=dict(color='white'))
    )

    # Show figure
    st.plotly_chart(fig9,use_container_width=True)

col14 = st.columns(1)[0]
with col14:
    for_map = filtered_df.groupby('Geography').size().reset_index(name='customer_count')
    geojson_url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'

    fig10 = px.choropleth_mapbox(for_map,
                               locations='Geography',
                               featureidkey="properties.name",
                               color='customer_count',
                               geojson=geojson_url,
                               mapbox_style='carto-positron',
                               center={'lat': 48, 'lon': 6},
                               zoom=2,
                               color_continuous_scale='Viridis',
                               range_color=(for_map['customer_count'].min(), for_map['customer_count'].max()))

    fig10.update_layout(
        title='Customer Count by Country',
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    st.plotly_chart(fig10, use_container_width=True)

st.subheader('Customer Behaviour')

col15, col16 = st.columns(2)
with col15:
    grouped_df = filtered_df.groupby(['Exited', 'age_group', 'HasCrCard'])['CustomerId'].count().reset_index(
        name='count')

    # Pivot the table
    pivot_df = grouped_df.pivot_table(index=['Exited', 'age_group'], columns='HasCrCard', values='count',
                                      fill_value=0).reset_index()

    # Rename columns for clarity
    pivot_df.columns.name = None
    pivot_df.rename(columns={'have': 'HaveCrCard', 'havent': 'HaventCrCard'}, inplace=True)
    pivot_df['Exited'] = pivot_df['Exited'].map({0: 'Retained', 1: 'Churned'})

    st.data_editor(
        pivot_df,
        column_config={
            "Exited": "Exited",
            "age_group": "age_group",
            "HaveCrCard": st.column_config.ProgressColumn(
                "Cardholder",
                help="Customers with credit card",
                format="%f",
                min_value=pivot_df['HaveCrCard'].min(),
                max_value=pivot_df['HaveCrCard'].max(),
            ),
            "haven't": st.column_config.ProgressColumn(
                "Non-cardholder",
                help="Customers without a credit card",
                format="%f",
                min_value=pivot_df["haven't"].min(),
                max_value=pivot_df["haven't"].max(),
            ),
        },
        hide_index=True,
        use_container_width=True
    )
with col16:
    grouped_df1 = filtered_df.groupby(['Exited', 'age_group', 'IsActiveMember'])['CustomerId'].count().reset_index(
        name='count')

    # Pivot the table
    pivot_df1 = grouped_df1.pivot_table(index=['Exited', 'age_group'], columns='IsActiveMember', values='count',
                                        fill_value=0).reset_index()

    # Rename columns for clarity
    pivot_df1.columns.name = None
    pivot_df1['Exited'] = pivot_df1['Exited'].map({0: 'Retained', 1: 'Churned'})

    st.data_editor(
        pivot_df1,
        column_config={
            "Exited": "Exited",
            "age_group": "age_group",
            "Active": st.column_config.ProgressColumn(
                "Active",
                help="Active Customers",
                format='%f',
                min_value=pivot_df1['Active'].min(),
                max_value=pivot_df1['Active'].max(),
            ),
            "Inactive": st.column_config.ProgressColumn(
                "Inactive",
                help="Inactive Customers",
                format='%f',
                min_value=pivot_df1['Inactive'].min(),
                max_value=pivot_df1['Inactive'].max(),
            ),
        },
        hide_index=True,
        use_container_width=True
    )

col16, col17 = st.columns(2)
with col16:
    grouped_df3 = filtered_df.groupby(['Exited', 'risk', 'CreaditScore', 'HasCrCard'])[
        'CustomerId'].count().reset_index(name='count')
    # Pivot the table
    pivot_df3 = grouped_df3.pivot_table(index=['Exited', 'risk', 'CreaditScore'], columns='HasCrCard', values='count',
                                        fill_value=0).reset_index()

    # Rename columns for clarity
    pivot_df3.columns.name = None
    pivot_df3.rename(columns={'have': 'HaveCrCard', 'havent': 'HaventCrCard'}, inplace=True)
    pivot_df3['Exited'] = pivot_df3['Exited'].map({0: 'Retained', 1: 'Churned'})

    st.data_editor(
        pivot_df3,
        column_config={
            "Exited": "Exited",
            "CreaditScore": "CreditScore",
            "risk": "risk",
            "HaveCrCard": st.column_config.ProgressColumn(
                "Cardholder",
                help="Customers with Credit Card",
                format='%f',
                min_value=pivot_df3['HaveCrCard'].min(),
                max_value=pivot_df3['HaveCrCard'].max(),
            ),
            "haven't": st.column_config.ProgressColumn(
                "Non-cardholder",
                help="Customers without Credit Card",
                format='%f',
                min_value=pivot_df3["haven't"].min(),
                max_value=pivot_df3["haven't"].max()
            ),
        },
        hide_index=True,
        use_container_width=True
    )


with col17:
    grouped_df2 = filtered_df.groupby(['Exited', 'risk', 'CreaditScore', 'IsActiveMember'])[
        'CustomerId'].count().reset_index(name='count')
    # Pivot the table
    pivot_df2 = grouped_df2.pivot_table(index=['Exited', 'risk', 'CreaditScore'], columns='IsActiveMember',
                                        values='count', fill_value=0).reset_index()

    # Rename columns for clarity
    pivot_df2.columns.name = None
    pivot_df2['Exited'] = pivot_df2['Exited'].map({0: 'Retained', 1: 'Churned'})

    st.data_editor(
        pivot_df2,
        column_config={
            "Exited": "Exited",
            "CreaditScore": "CreditScore",
            "risk": "risk",
            "Active": st.column_config.ProgressColumn(
                "Active",
                help="Active Customers",
                format='%f',
                min_value=pivot_df2['Active'].min(),
                max_value=pivot_df2['Active'].max(),
            ),
            "Inactive": st.column_config.ProgressColumn(
                "Inactive",
                help="Inactive Customers",
                format='%f',
                min_value=pivot_df2['Inactive'].min(),
                max_value=pivot_df2['Inactive'].max(),
            ),
        },
        hide_index=True,
        use_container_width=True
    )

st.subheader('Customer churn and retention analysis based on risk and age groups.')

# calculation for raw value:

grouped_df4 = df.groupby(['risk', 'CreditScore_group','age_group','Exited']).size().reset_index(name='count')
# Pivot the table
pivot_df4 = grouped_df4.pivot_table(index=['risk','CreditScore_group','Exited'],columns='age_group',values='count',fill_value=0).reset_index()
# Rename columns for clarity
pivot_df4.columns.name = None
pivot_df4['Exited']=pivot_df4['Exited'].map({0:'Retained', 1:'Churned'})


# calculation for percentage value:
total = pivot_df4.groupby(['risk', 'CreditScore_group'])[
    ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']].sum().reset_index()
    
merge = pd.merge(pivot_df4, total, on=['risk', 'CreditScore_group'])
merge['18-24'] = (merge['18-24_x'] / merge['18-24_y']) * 100
merge['25-34'] = (merge['25-34_x'] / merge['25-34_y']) * 100
merge['35-44'] = (merge['35-44_x'] / merge['35-44_y']) * 100
merge['45-54'] = (merge['45-54_x'] / merge['45-54_y']) * 100
merge['55-64'] = (merge['55-64_x'] / merge['55-64_y']) * 100
merge['65+'] = (merge['65+_x'] / merge['65+_y']) * 100

merge = merge.drop(
    columns=['18-24_x', '25-34_x', '35-44_x', '45-54_x', '55-64_x', '65+_x',
             '18-24_y', '25-34_y', '35-44_y', '45-54_y', '55-64_y', '65+_y'])

for col in merge.select_dtypes(include=['float64']).columns:
    merge[col] = merge[col].apply(lambda x: f"{x:.2f}")

if 'show_percentage' not in st.session_state:
    st.session_state.show_percentage = False
if 'show_real' not in st.session_state:
    st.session_state.show_real = True

col18,col19,col20 = st.columns([1,1,2])
with col18:
    if st.button('Show Percentage Values',use_container_width=True):
        st.session_state.show_percentage = True
        st.session_state.show_real = False
with col19:
    if st.button('Show Real Values',use_container_width=True):
        st.session_state.show_percentage = False
        st.session_state.show_real = True
col21 = st.columns(1)[0]
with col21:
    if st.session_state.show_percentage:
        st.data_editor(
            merge,
            column_config={
                "risk": "risk",
                "CreditScore_group": "CreaditScore",
                "Exited": "Exited",
                "18-24": st.column_config.ProgressColumn(
                    "18-24 (%)",
                    help='Age group 18-24',
                    format='%f',
                    min_value=0,
                    max_value=100
                ),
                "25-34": st.column_config.ProgressColumn(
                    "25-34 (%)",
                    help='Age group 25-34',
                    format='%f',
                    min_value=0,
                    max_value=100
                ),
                "35-44": st.column_config.ProgressColumn(
                    "35-44 (%)",
                    help='Age group 35-44',
                    format='%f',
                    min_value=0,
                    max_value=100
                ),
                "45-54": st.column_config.ProgressColumn(
                    "45-54 (%)",
                    help='Age group 45-54',
                    format='%f',
                    min_value=0,
                    max_value=100
                ),
                "55-64": st.column_config.ProgressColumn(
                    "55-64 (%)",
                    help='Age group 55-64',
                    format='%f',
                    min_value=0,
                    max_value=100
                ),
                "65+": st.column_config.ProgressColumn(
                    "65+ (%)",
                    help='Age group 65+',
                    format='%f',
                    min_value=0,
                    max_value=100
                )
            },
            hide_index=True,
            use_container_width=True
        )
    elif st.session_state.show_real:
        st.data_editor(
            pivot_df4,
            column_config={
                "risk": "risk",
                "CreditScore_group": "CreaditScore",
                "Exited": "Exited",
                "18-24": st.column_config.ProgressColumn(
                    "18-24",
                    help='Age group 18-24',
                    format='%f',
                    min_value=0,
                    max_value=106
                ),
                "25-34": st.column_config.ProgressColumn(
                    "25-34",
                    help='Age group 25-34',
                    format='%f',
                    min_value=0,
                    max_value=106
                ),
                "35-44": st.column_config.ProgressColumn(
                    "35-44",
                    help='Age group 35-44',
                    format='%f',
                    min_value=0,
                    max_value=106
                ),
                "45-54": st.column_config.ProgressColumn(
                    "45-54",
                    help='Age group 45-54',
                    format='%f',
                    min_value=0,
                    max_value=106
                ),
                "55-64": st.column_config.ProgressColumn(
                    "55-64",
                    help='Age group 55-64',
                    format='%f',
                    min_value=0,
                    max_value=106
                ),
                "65+": st.column_config.ProgressColumn(
                    "65+",
                    help='Age group 65+',
                    format='%f',
                    min_value=0,
                    max_value=106
                )
            },
            hide_index=True,
            use_container_width=True
        )
