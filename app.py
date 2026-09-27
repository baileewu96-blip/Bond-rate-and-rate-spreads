import streamlit as st

# Set page configuration for professional dark theme
st.set_page_config(
    page_title="沃什新规·宏观状态自动诊断仪表盘",
    page_icon="🦅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Dark theme custom CSS injection
st.markdown("""
<style>
    /* Main body adjustments */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    /* Section Title Styles */
    .section-title {
        font-size: 15px;
        color: #3b82f6;
        margin: 25px 0 10px 0;
        padding-bottom: 5px;
        border-bottom: 1px dashed #334155;
        font-weight: bold;
    }
    /* Data link styles */
    .data-link {
        font-size: 12px;
        color: #60a5fa;
        text-decoration: none;
        margin-bottom: 10px;
        display: inline-block;
    }
    .data-link:hover {
        text-decoration: underline;
    }
    /* Cards for scenario outputs */
    .report-card {
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        border: 1px solid #334155;
    }
    .report-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .condition-tag {
        font-size: 12px;
        padding: 3px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 10px;
        color: #ffffff;
        font-weight: bold;
    }
    .guide-box {
        background: rgba(255, 255, 255, 0.04);
        border-left: 4px solid #3b82f6;
        padding: 15px;
        margin-top: 15px;
        border-radius: 0 6px 6px 0;
    }
    .guide-box h4 {
        margin: 0 0 8px 0;
        color: #ffffff;
        font-size: 14px;
    }
    .guide-box ul {
        margin: 0;
        padding-left: 20px;
        font-size: 13px;
        color: #e2e8f0;
    }
    .guide-box li {
        margin-bottom: 6px;
        line-height: 1.5;
    }
    /* Specific background colors for scenarios */
    .status-danger { background: rgba(239, 68, 68, 0.12); border-color: #ef4444; }
    .status-danger .report-title { color: #ef4444; }
    .status-danger .condition-tag { background: #ef4444; }
    .status-danger .guide-box { border-left-color: #ef4444; }
    
    .status-warning { background: rgba(245, 158, 11, 0.12); border-color: #f59e0b; }
    .status-warning .report-title { color: #f59e0b; }
    .status-warning .condition-tag { background: #f59e0b; color: #000000; }
    .status-warning .guide-box { border-left-color: #f59e0b; }
    
    .status-success { background: rgba(16, 185, 129, 0.12); border-color: #10b981; }
    .status-success .report-title { color: #10b981; }
    .status-success .condition-tag { background: #10b981; }
    .status-success .guide-box { border-left-color: #10b981; }
    
    .status-info { background: rgba(59, 130, 246, 0.12); border-color: #3b82f6; }
    .status-info .report-title { color: #3b82f6; }
    .status-info .condition-tag { background: #3b82f6; }
    .status-info .guide-box { border-left-color: #3b82f6; }

    /* Blinking effect for critical warnings */
    @keyframes blinker { 50% { opacity: 0.4; } }
    .blink { animation: blinker 1.5s linear infinite; }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; margin-bottom: 5px;'>🦅 沃什新规·宏观决策全指标自动诊断仪表盘</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 13px; margin-bottom: 25px;'>手打数据输入 · 5组官方 FRED 源码实时追踪 · GitHub 与 Streamlit 专属无拦截完美运行版</div>", unsafe_allow_html=True)

# 1. 通胀二阶导组
st.markdown("<div class='section-title'>1. 通胀二阶导组 (短端锚定)</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<a href='https://fred.stlouisfed.org/series/CPILFESL' target='_blank' class='data-link'>📊 FRED 核心通胀源码 ↗</a>", unsafe_allow_html=True)
    cpi = st.number_input("核心 CPI 同比增速 (%)", value=3.2, step=0.001, format="%.3f", key="cpi")
with col2:
    st.markdown("<a href='https://fred.stlouisfed.org/series/ECIALLCIV' target='_blank' class='data-link'>📊 FRED 薪资动量源码 ↗</a>", unsafe_allow_html=True)
    eci = st.number_input("就业成本指数 ECI 增速 (%)", value=3.8, step=0.001, format="%.3f", key="eci")

# 2. 财政发债组
st.markdown("<div class='section-title'>2. 财政发债组 (长端定价)</div>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    st.markdown("<a href='https://fred.stlouisfed.org/series/DGS2' target='_blank' class='data-link'>🏛️ FRED 2年期美债 ↗</a>", unsafe_allow_html=True)
    us02y = st.number_input("2年期美债收益率 (%)", value=4.681, step=0.001, format="%.3f", key="us02y")
with col4:
    st.markdown("<a href='https://fred.stlouisfed.org/series/DGS10' target='_blank' class='data-link'>🏛️ FRED 10年期美债 ↗</a>", unsafe_allow_html=True)
    us10y = st.number_input("10年期美债收益率 (%)", value=5.890, step=0.001, format="%.3f", key="us10y")

st.markdown("<a href='https://fiscaldata.treasury.gov/datasets/treasury-auction-query/auction-date' target='_blank' class='data-link'>🏛️ 财政部发债一手数据 ↗</a>", unsafe_allow_html=True)
auction = st.selectbox("国债拍卖倍率状态 (Bid-to-Cover)", ["正常 (倍率稳定在历史均值附近)", "疲软 (认购倍率明显下滑，长端承压)"])

# 3. 流动性走廊组
st.markdown("<div class='section-title'>3. 流动性走廊组 (核心水管)</div>", unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    st.markdown("<a href='https://fred.stlouisfed.org/series/SOFR' target='_blank' class='data-link'>💧 FRED 有担保隔夜融资 ↗</a>", unsafe_allow_html=True)
    sofr = st.number_input("实时 SOFR 利率 (%)", value=4.880, step=0.001, format="%.3f", key="sofr")
with col6:
    st.markdown("<a href='https://fred.stlouisfed.org/series/IORB' target='_blank' class='data-link'>🏛️ FRED 准备金余额利率 ↗</a>", unsafe_allow_html=True)
    iorb = st.number_input("美联储 IORB 利率 (%)", value=5.000, step=0.001, format="%.3f", key="iorb")

# 4 & 5. AI资本开支与市场传染组
st.markdown("<div class='section-title'>4 & 5. 情绪与市场传染组 (中性利率与风险联动)</div>", unsafe_allow_html=True)
col7, col8 = st.columns(2)
with col7:
    st.markdown("<a href='https://cn.tradingview.com/symbols/TVC-MOVE/' target='_blank' class='data-link'>⚠️ 债市隐含波动率 ↗</a>", unsafe_allow_html=True)
    move = st.number_input("美债恐慌指数 (MOVE)", value=115.0, step=1.0, format="%.1f", key="move")
with col8:
    st.markdown("<a href='https://finance.yahoo.com/' target='_blank' class='data-link'>⚡ 雅虎财经财报跟踪 ↗</a>", unsafe_allow_html=True)
    capex = st.selectbox("科技巨头 M7 季度开支指引", ["持续狂飙 (推高整体中性利率)", "全面砍支 (长期资本需求回落)"])

# Calculate intermediate metrics
yield_spread = us10y - us02y
liquidity_spread = sofr - iorb

# Display Metrics Blocks
st.markdown("<hr style='border: 1px solid #334155; margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown("<div style='font-size:13px; color:#10b981; margin-bottom:15px; text-align:center; font-weight:bold;'>⚡ Python if/else 决策大脑智能实时判定中 (上方数值发生改变，下方卡片即刻全自动刷新)</div>", unsafe_allow_html=True)

m_col1, m_col2 = st.columns(2)
with m_col1:
    color_ys = "#10b981" if yield_spread > 0.05 else ("#ef4444" if yield_spread <= 0 else "#f59e0b")
    st.markdown(f"""
    <div style='background:#0f172a; padding:12px; border-radius:8px; border:1px solid #334155; text-align:center;'>
        <div style='color:#94a3b8; font-size:12px;'>10Y - 2Y 期限利差</div>
        <div style='font-size:22px; font-weight:bold; color:{color_ys}; margin-top:4px;'>{yield_spread:+.3f}%</div>
    </div>
    """, unsafe_allow_html=True)

with m_col2:
    color_ls = "#ef4444" if liquidity_spread > 0 else "#10b981"
    blink_class = "blink" if liquidity_spread > 0 else ""
    st.markdown(f"""
    <div style='background:#0f172a; padding:12px; border-radius:8px; border:1px solid #334155; text-align:center;'>
        <div style='color:#94a3b8; font-size:12px;'>SOFR - IORB 水管利差</div>
        <div class="{blink_class}" style='font-size:22px; font-weight:bold; color:{color_ls}; margin-top:4px;'>{liquidity_spread:+.3f}%</div>
    </div>
    """, unsafe_allow_html=True)

# Core if/else conditional diagnostic brain
if liquidity_spread > 0:
    st.markdown(f"""
    <div class='report-card status-danger'>
        <div class='report-title blink'>🚨【场景 A：核心水管爆裂 · 系统流动性危机】</div>
        <div class='condition-tag'>触发核心标准：SOFR - IORB ＞ 0% (当前为 {liquidity_spread:+.3f}%)</div>
        <p><strong>状态识别：</strong>当前真实手打数据显示 SOFR 已经顶破 IORB。这意味着哪怕通胀和基本面数据再好，银行体系的隔夜‘准备金’也正被极速抽干，全网金融‘钱母’卡死。若 MOVE 指数 ({move:.1f}) 同步高企，全资产将进入无差别‘流动性抽水踩踏’状态。</p>
        <div class='guide-box'>
            <h4>🛠【清算主义防御机制 · 交易操作指南】</h4>
            <ul>
                <li><strong>防范踩踏：</strong> 立即清仓并彻底平掉所有‘做空美债’的曲线杠杆多头，防止流动性突发收紧引发爆仓踩踏。</li>
                <li><strong>缩回现金：</strong> 大幅压缩风险性多头股票仓位，将宝贵的流动性资产迅速缩回 3个月短端国债现金池或高级货币基金中。</li>
                <li><strong>博弈联储：</strong> 沃什虽然态度维持鹰派，但水管断裂会逼迫美联储立刻启动常备借贷便利(SRF)或紧急暂停缩表，准备好迎接央行修水管干预后的瞬间全盘大反弹。</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif yield_spread < -0.4 and (cpi < 2.5 or eci < 3.2):
    st.markdown(f"""
    <div class='report-card status-info'>
        <div class='report-title'>🍂【场景 D：传统衰退 / 周期全面回归（重回老游戏）】</div>
        <div class='condition-tag'>触发核心标准：10Y - 2Y 极度倒挂 且 核心通胀/薪资断崖式大跌</div>
        <p><strong>状态识别：</strong>手打利差呈现超强负倒挂 (${yieldSpread:+.3f}%)。长年维持的限制性超高利率终于在底层杀死了实体经济与就业，通胀火苗彻底熄灭。美联储的‘清算主义主义’被迫向冰冷的衰退数据低头，不得不切换至防守姿态。</p>
        <div class='guide-box'>
            <h4>🛠【传统周期回归 · 交易操作指南】</h4>
            <ul>
                <li><strong>满仓做多债市：</strong> 游戏旧规则重新夺回定价主线，降息通道被全面、强行砸开。不用犹豫，全力、满仓做多长端美债现货与长久期资产（如买入 TLT 现货或看涨期权）。</li>
                <li><strong>资产防守大迁移：</strong> 彻底收榨并清仓一切对经济周期高度敏感的顺周期多头与高估值科技股，全线向黄金、避险现金和防御性高股息公用板块做大挪移。</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif yield_spread <= 0.05:
    st.markdown(f"""
    <div class='report-card status-warning'>
        <div class='report-title'>⚡【场景 B：危险的熊平切换（全资产估值无情绞杀）】</div>
        <div class='condition-tag'>触发核心标准：10Y - 2Y 倒挂或压缩在 0.05% 极窄区间 (当前为 {yield_spread:+.3f}%)</div>
        <p><strong>状态识别：</strong>通胀二阶导全面死灰复燃，逼迫强势的新联储必须咬紧甚至继续主动大幅拉抬短端基准利率，导致短端利率（2Y）疯狂暴涨，收益率曲线被强行挤平。这是所有高估值风险资产、科技股最残酷的重机枪。</p>
        <div class='guide-box'>
            <h4>🛠 {熊平状态下全线撤退 · 交易套利指南}</h4>
            <ul>
                <li><strong>战略防御：</strong> 属于经典的多头‘资产双杀’阶段。全线做空长期和中期国债，同时大幅度、无条件砍掉美股、加密资产等高波动风险多头仓位。</li>
                <li><strong>现金储备第一：</strong> 保持最高比例的纯美元现金持仓，存入高利息隔夜工具中存活，在通胀大火没有被再次彻底杀透、联储松口前，绝不轻易入场接飞刀。</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    capex_note = "💡 当前检测到科技巨头 M7 季度 AI 资本开支持续狂飙，这正在全球底层不断夯实‘中性利率(R-star)’移动上移的根基，为长端利率源源不断注入上行动量！" if capex == "持续狂飙 (推高整体中性利率)" else ""
    st.markdown(f"""
    <div class='report-card status-success'>
        <div class='report-title'>🦅【场景 C：基准情景 · 熊陡延续（沃什主义新规常规态）】</div>
        <div class='condition-tag'>触发核心标准：10Y - 2Y 期限利差保持强劲正值 (当前为 {yield_spread:+.3f}%) 且水管正常</div>
        <p><strong>状态识别：</strong>根据您打入的最精准手打数据，曲线展现出强劲的‘熊陡’走势。短端被美联储不妥协的高政策利率死死钉住，而长端（10Y、30Y）在财政部漫无节制疯狂发债，以及全球 AI 巨头供应链军备竞赛抢钱的夹击下急剧向上狂飙。期限溢价正在大举修复扩张。</p>
        <p style='font-size:13px; color:#94a3b8; font-style:italic; margin-top:5px;'>{capex_note}</p>
        <div class='guide-box'>
            <h4>🛠【无前瞻指引新常态 · 熊陡策略套利指南】</h4>
            <ul>
                <li><strong>经典陡峭化套利：</strong> 坚定不移地执行‘做多短端固定收益、做空长期美债’的组合拳（例如做空长期国债、买入 TBT / TMV ）。</li>
                <li><strong>拥抱硬核造血核心：</strong> 彻底远离任何高久期、零利润的虚幻资产。把筹码重仓分配给具备极强自我造血能力、能够顶住长端利率反噬的 AI 核心算力、高性能芯片与配套电力基础设施供应链绝对龙头，并且**绝对不要盲目长线抄底长期国债**。</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
