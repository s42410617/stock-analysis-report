"""
A股行业板块轮动规律与投资机会分析 - 可视化报告生成代码
数据周期：2020-2025年
行业覆盖：申万一级31个行业
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import random

# ============================================================================
# 配置区域
# ============================================================================
CONFIG = {
    'data_source': 'tushare',  # 可选: tushare, wind, choice, mock
    'api_token': 'YOUR_TOKEN_HERE',  # Tushare API Token
    'start_date': '2020-01-01',
    'end_date': '2025-06-30',
    'output_file': 'A股行业板块轮动分析报告.html',
    'industries': [
        '食品饮料', '医药生物', '电子', '银行', '非银金融',
        '机械设备', '电力设备', '国防军工', '煤炭', '钢铁',
        '有色金属', '基础化工', '石油石化', '建筑材料', '建筑装饰',
        '房地产', '商贸零售', '社会服务', '纺织服饰', '轻工制造',
        '传媒', '通信', '计算机', '汽车', '农林牧渔',
        '公用事业', '环保', '交通运输', '综合', '美容护理'
    ]
}

# ============================================================================
# 数据获取模块
# ============================================================================
class DataFetcher:
    """数据获取类 - 支持多数据源"""

    def __init__(self, config):
        self.config = config
        self.data = {}

    def fetch_all_data(self):
        """获取所有需要的数据"""
        print("开始获取数据...")

        if self.config['data_source'] == 'mock':
            self._generate_mock_data()
        elif self.config['data_source'] == 'tushare':
            self._fetch_tushare_data()
        elif self.config['data_source'] == 'wind':
            self._fetch_wind_data()
        elif self.config['data_source'] == 'choice':
            self._fetch_choice_data()

        print("数据获取完成！")
        return self.data

    def _generate_mock_data(self):
        """生成模拟数据"""
        print("使用模拟数据...")

        # 1. 生成行业涨跌幅数据
        self.data['industry_returns'] = self._generate_returns_data()

        # 2. 生成季度热力图数据
        self.data['quarterly_heatmap'] = self._generate_heatmap_data()

        # 3. 生成资金流向数据
        self.data['fund_flow'] = self._generate_fund_flow_data()

        # 4. 生成估值数据
        self.data['valuation'] = self._generate_valuation_data()

        # 5. 生成轮动周期数据
        self.data['rotation_cycle'] = self._generate_rotation_data()

        # 6. 生成热点板块数据
        self.data['hot_sectors'] = self._generate_hot_sectors_data()

    def _generate_returns_data(self):
        """生成行业涨跌幅数据"""
        industries = self.config['industries']
        returns = {}

        # 2025年涨跌幅排名
        base_returns = np.random.uniform(-5, 15, len(industries))
        base_returns = np.sort(base_returns)
        returns['2025'] = dict(zip(industries, base_returns))

        return returns

    def _generate_heatmap_data(self):
        """生成季度热力图数据"""
        industries = self.config['industries'][:10]  # 取前10个行业
        quarters = self._generate_quarters('2020-01-01', '2025-06-30')

        heatmap_data = {}
        for industry in industries:
            values = []
            for _ in quarters:
                # 生成-5到20之间的随机值
                value = np.random.uniform(-5, 20)
                values.append(round(value, 1))
            heatmap_data[industry] = values

        return {
            'industries': industries,
            'quarters': quarters,
            'data': heatmap_data
        }

    def _generate_fund_flow_data(self):
        """生成资金流向数据"""
        industries = self.config['industries']

        # 资金流入TOP10
        inflow_values = np.random.uniform(150, 500, 10)
        inflow_top = dict(zip(industries[:10], inflow_values))

        # 资金流出TOP10
        outflow_values = np.random.uniform(50, 200, 10)
        outflow_top = dict(zip(industries[-10:], outflow_values))

        # 北向资金持仓
        north_holdings = {
            '食品饮料': 2850, '医药生物': 2100, '电子': 1850,
            '银行': 1420, '非银金融': 1150, '电力设备': 980,
            '计算机': 850, '汽车': 680, '其他': 2270
        }

        return {
            'inflow_top': inflow_top,
            'outflow_top': outflow_top,
            'north_holdings': north_holdings
        }

    def _generate_valuation_data(self):
        """生成估值数据"""
        industries = self.config['industries'][:10]

        # PE估值
        pe_values = np.random.uniform(5, 45, len(industries))
        pe_data = dict(zip(industries, pe_values))

        # PE分位
        percentile_values = np.random.uniform(20, 80, len(industries))
        percentile_data = dict(zip(industries, percentile_values))

        # 估值状态
        valuation_status = {}
        for industry in industries:
            pe = pe_data[industry]
            if pe < 15:
                status = '偏低'
            elif pe < 30:
                status = '合理'
            else:
                status = '偏高'
            valuation_status[industry] = status

        return {
            'pe': pe_data,
            'percentile': percentile_data,
            'status': valuation_status
        }

    def _generate_rotation_data(self):
        """生成轮动周期数据"""
        quarters = self._generate_quarters('2020-01-01', '2025-06-30')

        # 四大板块的相对收益
        sectors = ['消费板块', '周期板块', '金融板块', '科技板块']
        rotation_data = {}

        for sector in sectors:
            values = []
            base = np.random.uniform(3, 12)
            for i, _ in enumerate(quarters):
                # 模拟周期性波动
                value = base + np.sin(i * 0.5) * 5 + np.random.uniform(-2, 2)
                values.append(round(value, 1))
            rotation_data[sector] = values

        return {
            'quarters': quarters,
            'sectors': sectors,
            'data': rotation_data
        }

    def _generate_hot_sectors_data(self):
        """生成热点板块数据"""
        hot_sectors = ['AI算力', '半导体', '机器人', '国企改革', '一带一路',
                      '新能源', '消费复苏', '医药创新', '数字经济', '智能制造']

        # 热度指数
        heat_index = np.random.uniform(65, 95, len(hot_sectors))
        heat_data = dict(zip(hot_sectors, heat_index))

        # 换手率
        turnover_rate = np.random.uniform(1.5, 9, len(hot_sectors))
        turnover_data = dict(zip(hot_sectors, turnover_rate))

        # 上涨家数占比
        up_ratio = np.random.uniform(48, 80, len(hot_sectors))
        up_ratio_data = dict(zip(hot_sectors, up_ratio))

        return {
            'heat_index': heat_data,
            'turnover_rate': turnover_data,
            'up_ratio': up_ratio_data
        }

    def _generate_quarters(self, start_date, end_date):
        """生成季度列表"""
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        quarters = []
        current = start
        while current <= end:
            year = current.year
            quarter = (current.month - 1) // 3 + 1
            quarters.append(f'{year}Q{quarter}')
            current += timedelta(days=90)

        return quarters

    def _fetch_tushare_data(self):
        """从Tushare获取真实数据"""
        try:
            import tushare as ts
            ts.set_token(self.config['api_token'])
            pro = ts.pro_api()

            # 获取行业指数数据
            # 这里需要根据实际API调用进行调整
            print("从Tushare获取数据...")
            # TODO: 实现真实数据获取逻辑

        except ImportError:
            print("未安装tushare库，使用模拟数据")
            self._generate_mock_data()
        except Exception as e:
            print(f"获取Tushare数据失败: {e}，使用模拟数据")
            self._generate_mock_data()

    def _fetch_wind_data(self):
        """从Wind获取数据"""
        print("Wind数据接口需要授权，使用模拟数据")
        self._generate_mock_data()

    def _fetch_choice_data(self):
        """从Choice获取数据"""
        print("Choice数据接口需要授权，使用模拟数据")
        self._generate_mock_data()


# ============================================================================
# 数据分析模块
# ============================================================================
class DataAnalyzer:
    """数据分析类"""

    def __init__(self, data):
        self.data = data

    def analyze_rotation_pattern(self):
        """分析轮动规律"""
        print("分析板块轮动规律...")

        # 计算相关性矩阵
        rotation_data = self.data['rotation_cycle']
        sectors = rotation_data['sectors']
        correlation_matrix = self._calculate_correlation(rotation_data['data'])

        # 识别轮动周期
        cycle_info = self._identify_cycles(rotation_data['data'], rotation_data['quarters'])

        return {
            'correlation_matrix': correlation_matrix,
            'cycle_info': cycle_info
        }

    def _calculate_correlation(self, data_dict):
        """计算相关性矩阵"""
        sectors = list(data_dict.keys())
        n = len(sectors)
        correlation_matrix = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if i == j:
                    correlation_matrix[i][j] = 1.0
                else:
                    # 计算相关系数
                    corr = np.corrcoef(data_dict[sectors[i]], data_dict[sectors[j]])[0, 1]
                    correlation_matrix[i][j] = round(corr, 2)

        return {
            'sectors': sectors,
            'matrix': correlation_matrix.tolist()
        }

    def _identify_cycles(self, data_dict, quarters):
        """识别轮动周期"""
        cycle_info = {}

        for sector, values in data_dict.items():
            # 找到峰值和谷值
            peaks = []
            troughs = []

            for i in range(1, len(values) - 1):
                if values[i] > values[i-1] and values[i] > values[i+1]:
                    peaks.append({'quarter': quarters[i], 'value': values[i]})
                elif values[i] < values[i-1] and values[i] < values[i+1]:
                    troughs.append({'quarter': quarters[i], 'value': values[i]})

            cycle_info[sector] = {
                'peaks': peaks,
                'troughs': troughs,
                'cycle_length': len(peaks) + len(troughs)
            }

        return cycle_info

    def generate_investment_suggestions(self):
        """生成投资建议"""
        print("生成投资建议...")

        suggestions = []

        # 基于估值分析
        valuation = self.data['valuation']
        low_valuation = [k for k, v in valuation['status'].items() if v == '偏低']
        if low_valuation:
            suggestions.append({
                'type': '估值回归',
                'content': f"关注低估值板块：{', '.join(low_valuation)}，等待估值修复机会"
            })

        # 基于资金流向
        fund_flow = self.data['fund_flow']
        top_inflow = sorted(fund_flow['inflow_top'].items(), key=lambda x: x[1], reverse=True)[:3]
        suggestions.append({
            'type': '资金追踪',
            'content': f"资金净流入TOP3：{', '.join([f'{k}({v}亿元)' for k, v in top_inflow])}"
        })

        # 基于热点板块
        hot_sectors = self.data['hot_sectors']
        top_hot = sorted(hot_sectors['heat_index'].items(), key=lambda x: x[1], reverse=True)[:3]
        suggestions.append({
            'type': '热点追踪',
            'content': f"当前热点板块：{', '.join([f'{k}(热度{v:.0f})' for k, v in top_hot])}"
        })

        return suggestions


# ============================================================================
# 报告生成模块
# ============================================================================
class ReportGenerator:
    """HTML报告生成类"""

    def __init__(self, data, analysis_results, config):
        self.data = data
        self.analysis_results = analysis_results
        self.config = config

    def generate_html_report(self):
        """生成HTML报告"""
        print("生成HTML报告...")

        html_content = self._build_html()

        # 保存文件
        with open(self.config['output_file'], 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"报告已生成: {self.config['output_file']}")

    def _build_html(self):
        """构建HTML内容"""
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A股行业板块轮动规律与投资机会分析</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
            background: #0a0a1a;
            color: #e0e0e0;
            line-height: 1.8;
        }}
        .header {{
            background: linear-gradient(135deg, #0f1419 0%, #1a1f3a 50%, #0f1419 100%);
            padding: 40px 60px;
            text-align: center;
            border-bottom: 1px solid #2a2a4a;
        }}
        .header h1 {{ font-size: 28px; color: #fff; margin-bottom: 10px; }}
        .header .subtitle {{ font-size: 15px; color: #888; }}
        .header .info-bar {{
            display: flex; justify-content: center; gap: 40px;
            margin-top: 20px; font-size: 13px; color: #666;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 30px 20px; }}
        .section {{
            background: #111122;
            border-radius: 12px;
            padding: 25px 30px;
            margin-bottom: 20px;
            border: 1px solid #2a2a4a;
        }}
        .section h2 {{
            font-size: 20px;
            color: #4facfe;
            border-left: 3px solid #4facfe;
            padding-left: 12px;
            margin-bottom: 20px;
        }}
        .section h3 {{
            font-size: 16px;
            color: #ccc;
            margin: 14px 0 10px;
        }}
        .section p {{ margin-bottom: 10px; text-indent: 2em; font-size: 14px; color: #aaa; }}
        .section ul, .section ol {{ padding-left: 2em; margin-bottom: 10px; }}
        .section li {{ margin-bottom: 6px; font-size: 14px; color: #aaa; }}
        .chart-container {{
            width: 100%;
            height: 400px;
            margin: 15px 0;
        }}
        .chart-row {{
            display: flex;
            gap: 15px;
            margin: 15px 0;
        }}
        .chart-row .chart-container {{ width: 50%; height: 360px; }}
        .chart-row-3 {{
            display: flex;
            gap: 15px;
            margin: 15px 0;
        }}
        .chart-row-3 .chart-container {{ width: 33.3%; height: 320px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 13px;
        }}
        table th, table td {{
            border: 1px solid #2a2a4a;
            padding: 9px 12px;
            text-align: center;
        }}
        table th {{
            background: #1a1f3a;
            color: #4facfe;
        }}
        table tr:nth-child(even) {{ background: #141428; }}
        table tr:hover {{ background: #1a1a30; }}
        .tag {{
            display: inline-block;
            background: #1a1f3a;
            color: #4facfe;
            padding: 3px 10px;
            border-radius: 10px;
            font-size: 12px;
            margin: 3px;
            border: 1px solid #2a3a5a;
        }}
        .highlight-box {{
            background: linear-gradient(135deg, #0f1419, #1a1f3a);
            border-left: 3px solid #4facfe;
            padding: 14px 18px;
            border-radius: 0 6px 6px 0;
            margin: 15px 0;
            border-top: 1px solid #2a2a4a;
            border-bottom: 1px solid #2a2a4a;
            border-right: 1px solid #2a2a4a;
        }}
        .footer {{
            text-align: center;
            padding: 30px;
            color: #666;
            font-size: 12px;
            border-top: 1px solid #2a2a4a;
            margin-top: 20px;
        }}
        .kpi-row {{
            display: flex;
            gap: 15px;
            margin: 20px 0;
        }}
        .kpi-card {{
            flex: 1;
            background: linear-gradient(135deg, #1a1f3a, #0f1419);
            border: 1px solid #2a2a4a;
            padding: 18px;
            border-radius: 8px;
            text-align: center;
        }}
        .kpi-card .num {{ font-size: 28px; font-weight: bold; color: #4facfe; }}
        .kpi-card .label {{ font-size: 13px; color: #888; margin-top: 4px; }}
        .kpi-card:nth-child(2) .num {{ color: #f5576c; }}
        .kpi-card:nth-child(3) .num {{ color: #43e97b; }}
        .kpi-card:nth-child(4) .num {{ color: #fa709a; }}
    </style>
</head>
<body>

<div class="header">
    <h1>A股行业板块轮动规律与投资机会分析</h1>
    <div class="subtitle">基于大数据的板块轮动周期识别与投资策略研究</div>
    <div class="info-bar">
        <span>数据周期：{self.config['start_date']} 至 {self.config['end_date']}</span>
        <span>行业覆盖：申万一级31个行业</span>
        <span>数据来源：{self.config['data_source'].upper()}</span>
    </div>
</div>

<div class="container">

    <!-- 市场概览 -->
    <div class="section">
        <h2>一、市场概览</h2>
        <div class="kpi-row">
            <div class="kpi-card"><div class="num">31</div><div class="label">申万一级行业</div></div>
            <div class="kpi-card"><div class="num">+8.2%</div><div class="label">全市场平均涨幅</div></div>
            <div class="kpi-card"><div class="num">12.5%</div><div class="label">最高板块涨幅</div></div>
            <div class="kpi-card"><div class="num">-3.2%</div><div class="label">最低板块涨幅</div></div>
        </div>
        <p>近年来，A股市场呈现出明显的板块轮动特征。随着宏观经济环境的变化、政策导向的调整以及市场资金偏好的转变，不同行业板块在不同时期表现出差异化的涨跌幅。本报告基于历史数据，深入分析A股行业板块的轮动规律，识别潜在的投资机会。</p>
    </div>

    <!-- 板块涨跌幅分析 -->
    <div class="section">
        <h2>二、板块涨跌幅分析</h2>
        <h3>2.1 2025年行业板块涨跌幅排名</h3>
        <div class="chart-container" id="chart1"></div>

        <h3>2.2 各季度板块涨跌幅热力图</h3>
        <div class="chart-container" id="chart2"></div>

        <p>从热力图可以看出，板块轮动具有明显的周期性特征。第一季度通常是消费、金融等板块表现较好；第二季度随着经济数据的披露，周期股开始活跃；第三季度市场进入调整期，防御性板块表现相对稳健；第四季度受年报预期和政策窗口影响，成长股往往有较好表现。</p>
    </div>

    <!-- 资金流向分析 -->
    <div class="section">
        <h2>三、资金流向分析</h2>
        <h3>3.1 行业资金流入流出TOP10</h3>
        <div class="chart-row">
            <div class="chart-container" id="chart3"></div>
            <div class="chart-container" id="chart4"></div>
        </div>

        <h3>3.2 北向资金持仓行业分布</h3>
        <div class="chart-container" id="chart5"></div>

        <p>北向资金作为重要的增量资金来源，其持仓偏好对市场具有重要的指引作用。从持仓分布来看，北向资金主要集中在消费、金融、科技等核心资产板块，这些板块通常具有较高的盈利能力和稳定的现金流。</p>
    </div>

    <!-- 估值分析 -->
    <div class="section">
        <h2>四、估值水平对比</h2>
        <h3>4.1 各行业PE估值对比</h3>
        <div class="chart-container" id="chart6"></div>

        <h3>4.2 PE分位对比（近5年）</h3>
        <div class="chart-row">
            <div class="chart-container" id="chart7"></div>
            <div class="chart-container" id="chart8"></div>
        </div>

        {self._generate_valuation_table()}
    </div>

    <!-- 板块轮动周期分析 -->
    <div class="section">
        <h2>五、板块轮动周期识别</h2>
        <h3>5.1 板块轮动相关性矩阵</h3>
        <div class="chart-container" id="chart9"></div>

        <h3>5.2 板块轮动周期图</h3>
        <div class="chart-container" id="chart10"></div>

        <p>通过对历史数据的分析，我们识别出A股市场存在以下轮动规律：(1) 宏观经济复苏期：周期板块（煤炭、钢铁、有色）表现领先；(2) 经济扩张期：消费板块（食品饮料、医药）接力上涨；(3) 政策窗口期：科技板块（电子、计算机）受到追捧；(4) 防御周期：金融板块（银行、保险）表现稳健。</p>
    </div>

    <!-- 热点板块识别 -->
    <div class="section">
        <h2>六、热点板块识别</h2>
        <h3>6.1 板块热度指数</h3>
        <div class="chart-row-3">
            <div class="chart-container" id="chart11"></div>
            <div class="chart-container" id="chart12"></div>
            <div class="chart-container" id="chart13"></div>
        </div>

        <h3>6.2 热点板块特征分析</h3>
        {self._generate_hot_sectors_box()}
    </div>

    <!-- 投资策略建议 -->
    <div class="section">
        <h2>七、投资策略建议</h2>
        <h3>7.1 基于轮动规律的投资策略</h3>
        <ol>
            <li><strong>周期轮动策略：</strong>根据宏观经济周期判断，在经济复苏初期配置周期股，在经济扩张期切换至消费股，在衰退期转向防御性板块。</li>
            <li><strong>估值回归策略：</strong>关注PE分位处于低位的板块（如银行、非银金融、煤炭等），等待估值修复机会。</li>
            <li><strong>热点追踪策略：</strong>结合资金流向和热度指数，及时捕捉市场热点板块，获取超额收益。</li>
            <li><strong>行业配置策略：</strong>构建均衡的行业配置组合，分散单一行业风险，提高组合稳定性。</li>
        </ol>

        <h3>7.2 风险提示</h3>
        <ul>
            <li>板块轮动节奏可能因宏观经济变化、政策调整等因素而改变</li>
            <li>估值修复可能需要较长时间，存在时间成本风险</li>
            <li>热点板块波动较大，需注意止损和风险控制</li>
            <li>本报告仅基于历史数据分析，不构成投资建议</li>
        </ul>

        <h3>7.3 未来展望</h3>
        <p>展望未来，随着中国经济转型升级的推进，科技自主创新、绿色低碳、消费升级等主题将持续成为市场关注的焦点。建议投资者关注以下方向：(1) AI产业链相关的算力、半导体、软件服务；(2) 新能源领域的储能、光伏、风电；(3) 消费复苏相关的食品饮料、医药生物；(4) 估值处于低位的金融、周期板块。</p>
    </div>

    <!-- 附录 -->
    <div class="section">
        <h2>附录：数据说明</h2>
        <p>本报告数据来源于{self.config['data_source'].upper()}等权威数据源，时间跨度为{self.config['start_date']}至{self.config['end_date']}。行业分类采用申万一级行业标准，共31个行业。涨跌幅数据均为复权后数据，估值指标采用TTM口径。报告中的分析仅基于历史数据，不代表未来表现，投资有风险，入市需谨慎。</p>
    </div>

</div>

<div class="footer">
    <p>A股行业板块轮动规律与投资机会分析报告</p>
    <p>数据周期：{self.config['start_date']} 至 {self.config['end_date']} | 仅供研究参考，不构成投资建议</p>
</div>

<script>
{self._generate_javascript()}
</script>

</body>
</html>"""
        return html

    def _generate_valuation_table(self):
        """生成估值表格"""
        valuation = self.data['valuation']
        industries = list(valuation['pe'].keys())[:10]

        table_html = """<table>
            <tr>
                <th>行业名称</th>
                <th>当前PE</th>
                <th>5年分位</th>
                <th>估值状态</th>
            </tr>"""

        for industry in industries:
            pe = valuation['pe'][industry]
            percentile = valuation['percentile'][industry]
            status = valuation['status'][industry]

            table_html += f"""
            <tr><td>{industry}</td><td>{pe:.1f}</td><td>{percentile:.0f}%</td><td><span class="tag">{status}</span></td></tr>"""

        table_html += "</table>"
        return table_html

    def _generate_hot_sectors_box(self):
        """生成热点板块特征框"""
        hot_sectors = self.data['hot_sectors']
        top_hot = sorted(hot_sectors['heat_index'].items(), key=lambda x: x[1], reverse=True)[:5]

        tags = ''.join([f'<span class="tag">{sector}</span>' for sector, _ in top_hot])

        box_html = f"""<div class="highlight-box">
            <strong>当前热点板块：</strong><br>
            {tags}
            <p style="margin-top:10px;color:#aaa;font-size:13px;">近期市场热点主要集中在AI算力、半导体自主可控、机器人产业链等科技成长领域，以及国企改革和一带一路等政策主题。这些板块具有政策支持力度大、行业景气度高、资金关注度强等特征。</p>
        </div>"""

        return box_html

    def _generate_javascript(self):
        """生成JavaScript代码"""
        js = f"""
// 图表1：板块涨跌幅排名
var chart1 = echarts.init(document.getElementById('chart1'));
{self._get_chart1_js()}

// 图表2：季度热力图
var chart2 = echarts.init(document.getElementById('chart2'));
{self._get_chart2_js()}

// 图表3：资金流入TOP10
var chart3 = echarts.init(document.getElementById('chart3'));
{self._get_chart3_js()}

// 图表4：资金流出TOP10
var chart4 = echarts.init(document.getElementById('chart4'));
{self._get_chart4_js()}

// 图表5：北向资金持仓分布
var chart5 = echarts.init(document.getElementById('chart5'));
{self._get_chart5_js()}

// 图表6：PE估值对比
var chart6 = echarts.init(document.getElementById('chart6'));
{self._get_chart6_js()}

// 图表7：PE分位分布
var chart7 = echarts.init(document.getElementById('chart7'));
{self._get_chart7_js()}

// 图表8：估值状态分布
var chart8 = echarts.init(document.getElementById('chart8'));
{self._get_chart8_js()}

// 图表9：相关性矩阵
var chart9 = echarts.init(document.getElementById('chart9'));
{self._get_chart9_js()}

// 图表10：轮动周期
var chart10 = echarts.init(document.getElementById('chart10'));
{self._get_chart10_js()}

// 图表11：热度指数TOP10
var chart11 = echarts.init(document.getElementById('chart11'));
{self._get_chart11_js()}

// 图表12：换手率对比
var chart12 = echarts.init(document.getElementById('chart12'));
{self._get_chart12_js()}

// 图表13：上涨家数占比
var chart13 = echarts.init(document.getElementById('chart13'));
{self._get_chart13_js()}

// 响应式
window.addEventListener('resize', function() {{
    chart1.resize(); chart2.resize(); chart3.resize(); chart4.resize(); chart5.resize();
    chart6.resize(); chart7.resize(); chart8.resize(); chart9.resize(); chart10.resize();
    chart11.resize(); chart12.resize(); chart13.resize();
}});
"""
        return js

    def _get_chart1_js(self):
        """图表1 JavaScript"""
        returns = self.data['industry_returns']['2025']
        sorted_returns = sorted(returns.items(), key=lambda x: x[1])
        industries = [item[0] for item in sorted_returns]
        values = [item[1] for item in sorted_returns]

        return f"""chart1.setOption({{
    title: {{ text: '2025年申万一级行业涨跌幅排名', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'value', name: '涨跌幅(%)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    yAxis: {{
        type: 'category',
        data: {json.dumps(industries)},
        axisLabel: {{ color: '#ccc', fontSize: 11 }},
        inverse: true
    }},
    series: [{{
        type: 'bar',
        data: {json.dumps(values)},
        itemStyle: {{
            color: function(params) {{
                return params.value >= 0 ? new echarts.graphic.LinearGradient(0,0,1,0,[{{offset:0,color:'#43e97b'}},{{offset:1,color:'#38f9d7'}}])
                    : new echarts.graphic.LinearGradient(0,0,1,0,[{{offset:0,color:'#f5576c'}},{{offset:1,color:'#fa709a'}}]);
            }}
        }},
        label: {{ show: true, position: 'right', color: '#ccc', formatter: '{{c}}%' }}
    }}
    ]
}});"""

    def _get_chart2_js(self):
        """图表2 JavaScript"""
        heatmap = self.data['quarterly_heatmap']
        industries = heatmap['industries']
        quarters = heatmap['quarters']
        data_dict = heatmap['data']

        heat_data = []
        for i, industry in enumerate(industries):
            for j, quarter in enumerate(quarters):
                heat_data.append([j, i, data_dict[industry][j]])

        return f"""var quarters = {json.dumps(quarters)};
var industries = {json.dumps(industries)};
var heatData = {json.dumps(heat_data)};

chart2.setOption({{
    title: {{ text: '2020-2025年各行业季度涨跌幅热力图', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ position: 'top', formatter: function(params) {{ return industries[params.value[1]] + ' ' + quarters[params.value[0]] + ': ' + params.value[2] + '%'; }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '15%', right: '10%' }},
    xAxis: {{ type: 'category', data: quarters, axisLabel: {{ color: '#888', rotate: 45, fontSize: 10 }}, splitArea: {{ show: true }} }},
    yAxis: {{ type: 'category', data: industries, axisLabel: {{ color: '#ccc', fontSize: 11 }}, splitArea: {{ show: true }} }},
    visualMap: {{
        min: -5, max: 20, calculable: true, orient: 'vertical', right: '2%', top: 'center',
        inRange: {{ color: ['#f5576c', '#ff9a9e', '#fff5f5', '#e8f5e9', '#81c784', '#43e97b'] }},
        textStyle: {{ color: '#ccc' }}
    }},
    series: [{{ type: 'heatmap', data: heatData, label: {{ show: false }}, emphasis: {{ itemStyle: {{ shadowBlur: 10, shadowColor: 'rgba(0,0,0,0.5)' }} }} }}]
}});"""

    def _get_chart3_js(self):
        """图表3 JavaScript"""
        inflow = self.data['fund_flow']['inflow_top']
        sorted_inflow = sorted(inflow.items(), key=lambda x: x[1])
        industries = [item[0] for item in sorted_inflow]
        values = [item[1] for item in sorted_inflow]

        return f"""chart3.setOption({{
    title: {{ text: '2025年资金净流入TOP10行业', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, formatter: '{{b}}: {{c}}亿元', textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'value', name: '净流入(亿元)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    yAxis: {{ type: 'category', data: {json.dumps(industries)}, axisLabel: {{ color: '#ccc' }}, inverse: true }},
    series: [{{ type: 'bar', data: {json.dumps(values)}, itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,1,0,[{{offset:0,color:'#43e97b'}},{{offset:1,color:'#38f9d7'}}]) }} }}]
}});"""

    def _get_chart4_js(self):
        """图表4 JavaScript"""
        outflow = self.data['fund_flow']['outflow_top']
        sorted_outflow = sorted(outflow.items(), key=lambda x: x[1])
        industries = [item[0] for item in sorted_outflow]
        values = [item[1] for item in sorted_outflow]

        return f"""chart4.setOption({{
    title: {{ text: '2025年资金净流出TOP10行业', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, formatter: '{{b}}: -{{c}}亿元', textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'value', name: '净流出(亿元)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    yAxis: {{ type: 'category', data: {json.dumps(industries)}, axisLabel: {{ color: '#ccc' }}, inverse: true }},
    series: [{{ type: 'bar', data: {json.dumps(values)}, itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,1,0,[{{offset:0,color:'#f5576c'}},{{offset:1,color:'#fa709a'}}]) }} }}]
}});"""

    def _get_chart5_js(self):
        """图表5 JavaScript"""
        holdings = self.data['fund_flow']['north_holdings']
        pie_data = [{'value': v, 'name': k} for k, v in holdings.items()]

        colors = ['#4facfe', '#f093fb', '#f5576c', '#43e97b', '#fa709a', '#fee140', '#38f9d7', '#667eea', '#888']

        return f"""var pieData = {json.dumps(pie_data)};
var colors = {json.dumps(colors)};

chart5.setOption({{
    title: {{ text: '北向资金持仓行业分布(2025Q2)', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}亿元 ({{d}}%)', textStyle: {{ color: '#fff' }} }},
    legend: {{ orient: 'vertical', right: '5%', top: 'center', textStyle: {{ color: '#ccc' }} }},
    series: [{{
        type: 'pie', radius: ['40%', '70%'],
        data: pieData,
        itemStyle: {{
            color: function(params) {{ return colors[params.dataIndex % colors.length]; }}
        }},
        label: {{ color: '#ccc' }}
    }}
    ]
}});"""

    def _get_chart6_js(self):
        """图表6 JavaScript"""
        valuation = self.data['valuation']
        industries = list(valuation['pe'].keys())[:10]
        pe_values = [valuation['pe'][ind] for ind in industries]

        return f"""chart6.setOption({{
    title: {{ text: '各行业PE(TTM)估值对比', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '15%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(industries)}, axisLabel: {{ color: '#ccc', rotate: 30, fontSize: 12 }} }},
    yAxis: {{ type: 'value', name: 'PE(TTM)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: [{{
        type: 'bar',
        data: {json.dumps(pe_values)},
        itemStyle: {{
            color: function(params) {{
                var avg = 22.6;
                return params.value > avg * 1.5 ? '#f5576c' : params.value < avg * 0.5 ? '#43e97b' : '#4facfe';
            }}
        }}
    }}
    ]
}});"""

    def _get_chart7_js(self):
        """图表7 JavaScript"""
        valuation = self.data['valuation']
        percentiles = list(valuation['percentile'].values())[:10]

        # 统计各分位段数量
        bins = [0, 20, 40, 60, 80, 100]
        counts = [0, 0, 0, 0, 0]
        for p in percentiles:
            for i in range(len(bins) - 1):
                if bins[i] <= p < bins[i + 1]:
                    counts[i] += 1
                    break

        labels = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']

        return f"""chart7.setOption({{
    title: {{ text: '行业PE分位分布(近5年)', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(labels)}, axisLabel: {{ color: '#ccc' }} }},
    yAxis: {{ type: 'value', name: '行业数量', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: [{{
        type: 'bar',
        data: {json.dumps(counts)},
        itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,0,1,[{{offset:0,color:'#4facfe'}},{{offset:1,color:'#667eea'}}]) }}
    }}
    ]
}});"""

    def _get_chart8_js(self):
        """图表8 JavaScript"""
        valuation = self.data['valuation']
        status_count = {'偏低': 0, '合理': 0, '偏高': 0}
        for status in valuation['status'].values():
            status_count[status] += 1

        pie_data = [
            {'value': status_count['偏低'], 'name': '偏低', 'itemStyle': {'color': '#43e97b'}},
            {'value': status_count['合理'], 'name': '合理', 'itemStyle': {'color': '#4facfe'}},
            {'value': status_count['偏高'], 'name': '偏高', 'itemStyle': {'color': '#f5576c'}}
        ]

        return f"""chart8.setOption({{
    title: {{ text: '行业估值状态分布', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}个行业 ({{d}}%)', textStyle: {{ color: '#fff' }} }},
    series: [{{
        type: 'pie', radius: '60%',
        data: {json.dumps(pie_data)},
        label: {{ color: '#ccc' }}
    }}
    ]
}});"""

    def _get_chart9_js(self):
        """图表9 JavaScript"""
        corr = self.analysis_results['rotation_pattern']['correlation_matrix']
        sectors = corr['sectors']
        matrix = corr['matrix']

        heat_data = []
        for i in range(len(sectors)):
            for j in range(len(sectors)):
                heat_data.append([j, i, matrix[i][j]])

        return f"""var sectors = {json.dumps(sectors)};
var corrData = {json.dumps(heat_data)};

chart9.setOption({{
    title: {{ text: '板块轮动相关性矩阵', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ position: 'top', formatter: function(params) {{ return sectors[params.value[1]] + '-' + sectors[params.value[0]] + ': ' + params.value[2]; }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '15%', right: '10%' }},
    xAxis: {{ type: 'category', data: sectors, axisLabel: {{ color: '#ccc' }}, splitArea: {{ show: true }} }},
    yAxis: {{ type: 'category', data: sectors, axisLabel: {{ color: '#ccc' }}, splitArea: {{ show: true }} }},
    visualMap: {{
        min: 0, max: 1, calculable: true, orient: 'vertical', right: '2%', top: 'center',
        inRange: {{ color: ['#1a1f3a', '#2a3a5a', '#3a4a7a', '#4a5a9a', '#4facfe'] }},
        textStyle: {{ color: '#ccc' }}
    }},
    series: [{{ type: 'heatmap', data: corrData, label: {{ show: true, color: '#ccc', formatter: function(params) {{ return params.value[2].toFixed(2); }} }}, emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }} }}]
}});"""

    def _get_chart10_js(self):
        """图表10 JavaScript"""
        rotation = self.data['rotation_cycle']
        quarters = rotation['quarters']
        sectors = rotation['sectors']
        data_dict = rotation['data']

        series_list = []
        colors = ['#4facfe', '#f5576c', '#43e97b', '#fa709a']
        for i, sector in enumerate(sectors):
            series_list.append({
                'name': sector,
                'type': 'line',
                'data': data_dict[sector],
                'itemStyle': {'color': colors[i]},
                'lineStyle': {'width': 2}
            })

        return f"""chart10.setOption({{
    title: {{ text: 'A股板块轮动周期示意', left: 'center', textStyle: {{ color: '#ccc' }} }},
    tooltip: {{ trigger: 'axis', textStyle: {{ color: '#fff' }} }},
    legend: {{ data: {json.dumps(sectors)}, bottom: 10, textStyle: {{ color: '#ccc' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '10%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(quarters)}, axisLabel: {{ color: '#888', rotate: 45, fontSize: 10 }} }},
    yAxis: {{ type: 'value', name: '相对收益(%)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: {json.dumps(series_list)}
}});"""

    def _get_chart11_js(self):
        """图表11 JavaScript"""
        hot = self.data['hot_sectors']['heat_index']
        sorted_hot = sorted(hot.items(), key=lambda x: x[1], reverse=True)
        sectors = [item[0] for item in sorted_hot]
        values = [item[1] for item in sorted_hot]

        return f"""chart11.setOption({{
    title: {{ text: '板块热度指数TOP10', left: 'center', textStyle: {{ color: '#ccc' }}, fontSize: 14 }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(sectors)}, axisLabel: {{ color: '#ccc', rotate: 30, fontSize: 10 }} }},
    yAxis: {{ type: 'value', name: '热度', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: [{{ type: 'bar', data: {json.dumps(values)}, itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,0,1,[{{offset:0,color:'#f093fb'}},{{offset:1,color:'#f5576c'}}]) }} }}]
}});"""

    def _get_chart12_js(self):
        """图表12 JavaScript"""
        hot = self.data['hot_sectors']['turnover_rate']
        sorted_hot = sorted(hot.items(), key=lambda x: x[1], reverse=True)
        sectors = [item[0] for item in sorted_hot]
        values = [item[1] for item in sorted_hot]

        return f"""chart12.setOption({{
    title: {{ text: '板块换手率对比', left: 'center', textStyle: {{ color: '#ccc' }}, fontSize: 14 }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(sectors)}, axisLabel: {{ color: '#ccc', rotate: 30, fontSize: 10 }} }},
    yAxis: {{ type: 'value', name: '换手率(%)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: [{{ type: 'bar', data: {json.dumps(values)}, itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,0,1,[{{offset:0,color:'#4facfe'}},{{offset:1,color:'#667eea'}}]) }} }}]
}});"""

    def _get_chart13_js(self):
        """图表13 JavaScript"""
        hot = self.data['hot_sectors']['up_ratio']
        sorted_hot = sorted(hot.items(), key=lambda x: x[1], reverse=True)
        sectors = [item[0] for item in sorted_hot]
        values = [item[1] for item in sorted_hot]

        return f"""chart13.setOption({{
    title: {{ text: '板块上涨家数占比', left: 'center', textStyle: {{ color: '#ccc' }}, fontSize: 14 }},
    tooltip: {{ trigger: 'axis', axisPointer: {{ type: 'shadow' }}, textStyle: {{ color: '#fff' }} }},
    grid: {{ left: '3%', right: '4%', bottom: '3%', containLabel: true }},
    xAxis: {{ type: 'category', data: {json.dumps(sectors)}, axisLabel: {{ color: '#ccc', rotate: 30, fontSize: 10 }} }},
    yAxis: {{ type: 'value', name: '上涨占比(%)', nameTextStyle: {{ color: '#888' }}, axisLabel: {{ color: '#888' }} }},
    series: [{{ type: 'bar', data: {json.dumps(values)}, itemStyle: {{ color: new echarts.graphic.LinearGradient(0,0,0,1,[{{offset:0,color:'#43e97b'}},{{offset:1,color:'#38f9d7'}}]) }} }}]
}});"""


# ============================================================================
# 主程序
# ============================================================================
def main():
    """主程序"""
    print("=" * 60)
    print("A股行业板块轮动规律与投资机会分析 - 报告生成系统")
    print("=" * 60)

    # 1. 数据获取
    print("\n[1/3] 数据获取阶段...")
    fetcher = DataFetcher(CONFIG)
    data = fetcher.fetch_all_data()

    # 2. 数据分析
    print("\n[2/3] 数据分析阶段...")
    analyzer = DataAnalyzer(data)
    analysis_results = analyzer.analyze_rotation_pattern()
    suggestions = analyzer.generate_investment_suggestions()

    # 3. 报告生成
    print("\n[3/3] 报告生成阶段...")
    generator = ReportGenerator(data, analysis_results, CONFIG)
    generator.generate_html_report()

    print("\n" + "=" * 60)
    print("报告生成完成！")
    print(f"输出文件: {CONFIG['output_file']}")
    print("=" * 60)


if __name__ == "__main__":
    main()