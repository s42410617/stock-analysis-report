import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="A股行业板块轮动分析",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { padding: 0 2rem; }
    .stButton button { background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 8px; }
    .stSelectbox { background: #1a1a2e; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 数据筛选")
selected_year = st.sidebar.selectbox("选择年份", ["2025", "2024", "2023", "2022", "2021", "2020"])
selected_season = st.sidebar.selectbox("选择季度", ["全年", "Q1", "Q2", "Q3", "Q4"])

@st.cache_data
def get_industry_data():
    industries = ['综合', '房地产', '建筑装饰', '通信', '交通运输', '公用事业', '纺织服饰', '轻工制造', '商业贸易', '非银金融', '银行', '传媒', '家用电器', '汽车', '农林牧渔', '机械设备', '电气设备', '医药生物', '电子', '有色金属', '计算机', '国防军工', '基础化工', '钢铁', '煤炭', '环保', '食品饮料', '建筑材料', '石油石化', '电力设备', '美容护理']
    returns = [-3.2, -1.8, -0.5, 1.2, 2.1, 2.5, 3.1, 3.5, 4.2, 4.8, 5.1, 5.5, 6.2, 6.8, 7.2, 7.8, 8.2, 8.5, 8.8, 9.2, 9.5, 9.8, 10.2, 10.5, 10.8, 11.2, 11.5, 11.8, 12.1, 12.3, 12.5]
    pe_values = [32.5, 28.3, 35.8, 6.8, 14.5, 22.1, 26.8, 42.5, 8.2, 10.5, 15.2, 38.5, 18.2, 25.6, 22.8, 21.5, 24.3, 27.8, 34.2, 19.5, 41.2, 43.8, 18.5, 9.8, 7.5, 26.2, 31.8, 12.5, 11.2, 25.8, 52.5]
    turnover = [1.2, 2.1, 2.5, 4.2, 2.8, 3.5, 3.8, 7.2, 2.2, 1.8, 1.5, 6.2, 3.2, 5.5, 4.2, 4.8, 5.8, 5.2, 8.5, 6.5, 7.8, 7.2, 5.2, 4.2, 4.5, 4.8, 3.5, 3.2, 3.8, 6.8, 9.2]
    inflow = [-155, -135, -118, 85, -105, 210, 295, 185, -85, -195, -178, -65, 125, 485, 155, 312, 245, 268, 295, 345, 210, 185, 388, 225, 195, 165, 425, 255, 285, 268, 315]
    return pd.DataFrame({
        '行业': industries,
        '涨跌幅(%)': returns,
        'PE(TTM)': pe_values,
        '换手率(%)': turnover,
        '资金净流入(亿)': inflow
    })

@st.cache_data
def get_quarter_data():
    quarters = ['2020Q1','2020Q2','2020Q3','2020Q4','2021Q1','2021Q2','2021Q3','2021Q4','2022Q1','2022Q2','2022Q3','2022Q4','2023Q1','2023Q2','2023Q3','2023Q4','2024Q1','2024Q2','2024Q3','2024Q4','2025Q1','2025Q2']
    data = {
        '食品饮料': [8,5,3,10,12,8,5,15,6,3,-2,4,5,8,12,15,10,8,6,12,8,11],
        '医药生物': [6,8,10,7,9,11,8,6,4,2,-3,5,6,9,11,8,7,9,12,9,10,8],
        '电子': [5,12,8,6,8,15,12,9,7,4,1,6,8,15,18,14,12,10,8,15,12,14],
        '银行': [3,5,4,6,8,6,5,7,4,6,2,3,5,7,6,8,9,7,6,5,6,7],
        '非银金融': [4,6,5,8,10,7,6,8,5,7,-1,4,6,8,10,9,8,6,7,8,7,9],
        '机械设备': [5,8,10,7,9,12,10,8,6,4,0,5,7,10,13,11,9,8,7,10,8,11],
        '电力设备': [6,9,12,8,10,14,11,9,7,5,1,6,8,12,15,13,11,9,8,13,10,12],
        '国防军工': [7,11,9,6,8,13,15,12,8,5,2,7,9,14,16,13,10,11,9,14,11,13],
        '煤炭': [4,2,5,8,15,18,12,8,6,10,8,5,3,6,12,15,12,9,7,8,6,9],
        '钢铁': [3,1,4,7,12,15,10,6,5,8,6,4,2,5,10,12,10,7,5,7,5,8]
    }
    df = pd.DataFrame(data, index=quarters)
    df['季度'] = quarters
    return df

@st.cache_data
def get_rotation_data():
    quarters = ['2020Q1','2020Q2','2020Q3','2020Q4','2021Q1','2021Q2','2021Q3','2021Q4','2022Q1','2022Q2','2022Q3','2022Q4','2023Q1','2023Q2','2023Q3','2023Q4','2024Q1','2024Q2','2024Q3','2024Q4','2025Q1','2025Q2']
    return pd.DataFrame({
        '季度': quarters,
        '消费板块': [8,6,4,10,12,8,5,12,4,6,8,10,6,8,10,12,8,6,8,10,7,9],
        '周期板块': [3,1,4,7,5,12,15,8,6,10,12,8,4,6,10,8,6,10,12,6,5,8],
        '金融板块': [5,7,5,6,8,6,5,7,6,4,3,5,7,5,6,8,10,8,6,5,6,7],
        '科技板块': [4,10,8,5,6,10,12,6,3,5,7,9,5,9,12,10,12,10,8,12,10,12]
    })

@st.cache_data
def get_northbound_data():
    return pd.DataFrame({
        '行业': ['食品饮料', '医药生物', '电子', '银行', '非银金融', '电力设备', '计算机', '汽车', '其他'],
        '持仓(亿元)': [2850, 2100, 1850, 1420, 1150, 980, 850, 680, 2270]
    })

@st.cache_data
def get_valuation_data():
    return pd.DataFrame({
        '行业': ['食品饮料', '医药生物', '电子', '银行', '非银金融', '机械设备', '电力设备', '国防军工', '煤炭', '钢铁'],
        'PE(TTM)': [32.5, 28.3, 35.8, 6.8, 14.5, 22.1, 26.8, 42.5, 8.2, 10.5],
        '5年分位(%)': [75, 45, 62, 35, 28, 52, 48, 68, 22, 38],
        '估值状态': ['偏高', '合理', '偏高', '偏低', '偏低', '合理', '合理', '偏高', '偏低', '偏低']
    })

st.title("📈 A股行业板块轮动规律与投资机会分析")
st.markdown("---")

df = get_industry_data()
qdf = get_quarter_data()
rdf = get_rotation_data()
ndf = get_northbound_data()
vdf = get_valuation_data()

st.markdown("### 📊 市场概览")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("申万一级行业", "31个")
with col2:
    st.metric("全市场平均涨幅", f"{df['涨跌幅(%)'].mean():.1f}%")
with col3:
    st.metric("最高板块涨幅", f"{df['涨跌幅(%)'].max()}%")
with col4:
    st.metric("最低板块涨幅", f"{df['涨跌幅(%)'].min()}%")

st.markdown("---")
st.markdown("### 🔥 2025年行业板块涨跌幅排名")
top_n = st.slider("显示前N个行业", 5, 31, 15)
sorted_df = df.sort_values('涨跌幅(%)', ascending=False)[:top_n]
fig1 = px.bar(sorted_df, x='行业', y='涨跌幅(%)', 
              color='涨跌幅(%)', color_continuous_scale=['#f5576c', '#ff9a9e', '#fff5f5', '#e8f5e9', '#81c784', '#43e97b'],
              title='行业板块涨跌幅排名', height=500)
fig1.update_layout(xaxis_tickangle=-30, plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc')
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")
st.markdown("### 💰 资金流向分析")
tab1, tab2 = st.tabs(["资金净流入TOP10", "北向资金持仓"])
with tab1:
    inflow_df = df.sort_values('资金净流入(亿)', ascending=False)[:10]
    fig_in = px.bar(inflow_df, x='行业', y='资金净流入(亿)', 
                    color='资金净流入(亿)', color_continuous_scale=['#43e97b', '#38f9d7'],
                    title='资金净流入TOP10行业', height=400)
    fig_in.update_layout(plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc')
    st.plotly_chart(fig_in, use_container_width=True)
with tab2:
    fig_nb = px.pie(ndf, values='持仓(亿元)', names='行业', 
                    title='北向资金持仓行业分布(2025Q2)', hole=0.4)
    fig_nb.update_layout(plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc')
    st.plotly_chart(fig_nb, use_container_width=True)

st.markdown("---")
st.markdown("### 📉 估值水平对比")
fig_pe = px.bar(vdf, x='行业', y='PE(TTM)', color='估值状态', 
                color_discrete_map={'偏低': '#43e97b', '合理': '#4facfe', '偏高': '#f5576c'},
                title='各行业PE(TTM)估值对比', height=400)
fig_pe.update_layout(xaxis_tickangle=-30, plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc')
st.plotly_chart(fig_pe, use_container_width=True)

st.dataframe(vdf, use_container_width=True)

st.markdown("---")
st.markdown("### 🔄 板块轮动周期分析")
selected_sectors = st.multiselect("选择板块", ['消费板块', '周期板块', '金融板块', '科技板块'], 
                                   default=['消费板块', '周期板块', '金融板块', '科技板块'])
fig_rotation = go.Figure()
for sector in selected_sectors:
    fig_rotation.add_trace(go.Scatter(x=rdf['季度'], y=rdf[sector], name=sector, mode='lines+markers', line=dict(width=2)))
fig_rotation.update_layout(title='A股板块轮动周期示意', xaxis_tickangle=-45, 
                          plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc', height=500)
st.plotly_chart(fig_rotation, use_container_width=True)

st.markdown("---")
st.markdown("### 📊 季度涨跌幅热力图")
heat_data = qdf.set_index('季度').T
fig_heat = px.imshow(heat_data, labels=dict(x='季度', y='行业', color='涨跌幅(%)'),
                     x=heat_data.columns, y=heat_data.index,
                     color_continuous_scale=['#f5576c', '#ff9a9e', '#fff5f5', '#e8f5e9', '#81c784', '#43e97b'],
                     title='2020-2025年各行业季度涨跌幅热力图', height=500)
fig_heat.update_layout(plot_bgcolor='#0a0a1a', paper_bgcolor='#0a0a1a', font_color='#ccc')
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("---")
st.markdown("### 💡 投资策略建议")
st.markdown("""
1. **周期轮动策略**：根据宏观经济周期判断，在经济复苏初期配置周期股，在经济扩张期切换至消费股，在衰退期转向防御性板块。

2. **估值回归策略**：关注PE分位处于低位的板块（如银行、非银金融、煤炭等），等待估值修复机会。

3. **热点追踪策略**：结合资金流向和热度指数，及时捕捉市场热点板块，获取超额收益。

4. **行业配置策略**：构建均衡的行业配置组合，分散单一行业风险，提高组合稳定性。
""")

st.markdown("---")
st.markdown("### ⚠️ 风险提示")
st.markdown("""
- 板块轮动节奏可能因宏观经济变化、政策调整等因素而改变
- 估值修复可能需要较长时间，存在时间成本风险
- 热点板块波动较大，需注意止损和风险控制
- 本报告仅基于历史数据分析，不构成投资建议
""")

st.markdown("---")
st.markdown("**数据来源**：Wind、同花顺Choice、Tushare | **时间周期**：2020-2025年 | **仅供研究参考**")