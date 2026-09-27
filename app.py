import streamlit as st

# 1. 页面基本配置与全局高亮亮暗黑科技风格注入
st.set_page_config(
    page_title="沃什新规·宏观决策全指标自动判定仪表盘",
    page_icon="🦅",
    layout="centered"
)

st.markdown("""
    <style>
    /* 全局背景与高亮白色字体 */
    .main { background-color: #0f172a; color: #ffffff !important; }
    
    /* 强制所有输入框上方的标签（Label）显示为清晰的纯白色 */
    label, p, span, div { color: #ffffff !important; font-weight: 500; }
    
    /* 输入框内部样式调亮 */
    .stNumberInput input { background-color: #1e293b !important; color: #ffffff !important; border: 1px solid #475569 !important; font-size: 16px !important; }
    .stSelectbox div[data-baseweb="select"] { background-color: #1e293b !important; color: #ffffff !important; }
    
    /* 大标题分类样式强化 */
    .section-title { font-size: 16px; color: #3b82f6 !important; font-weight: bold; margin: 25px 0 10px 0; padding-bottom: 5px; border-bottom: 1px dashed #475569; }
    
    /* 蓝色链接升级为极光蓝，大幅提升看盘清晰度 */
    .data-link { font-size: 12px; color: #38bdf8 !important; text-decoration: underline !important; margin-bottom: 8px; display: inline-block; font-weight: bold; }
    
    /* 派生核心监控数值方块 */
    .metric-container { display: flex; gap: 15px; margin: 20px 0; }
    .metric-card { flex: 1; background: #0f172a; padding: 15px; border-radius: 8px; border: 2px solid #475569; text-align: center; }
    .metric-val { font-size: 24px; font-weight: bold; margin-top: 5px; }
    
    /* 判定报告框视觉深度增强 */
    .report-card { padding: 22px; border-radius: 10px; margin-top: 20px; border: 2px solid #475569; color: #ffffff !important; }
    .report-title { font-size: 19px; font-weight: bold; margin-bottom: 12px; }
    .guide-box { background: rgba(255,255,255,0.06); padding: 15px; margin-top: 15px; border-radius: 8px; border-left: 4px solid #3b82f6; }
    .guide-box h4 { margin: 0 0 10px 0; color: #ffffff !important; font-size: 15px; font-weight: bold; }
    .guide-box ul { margin: 0; padding-left: 20px; }
    .guide-box li { margin-bottom: 8px; line-height: 1.6; font-size: 14px; color: #ffffff !important; }
    
    /* 警报状态颜色 */
    .status-danger { background: rgba(239, 68, 68, 0.16); border-color: #ef4444; }
    .status-danger .report-title { color: #ef4444 !important; }
    .status-danger .guide-box { border-left-color: #ef4444; }
    
    .status-warning { background: rgba(245, 158, 11, 0.16); border-color: #f59e0b; }
    .status-warning .report-title { color: #f59e0b !important; }
    .status-warning .guide-box { border-left-color: #f59e0b; }
    
    .status-success { background: rgba(16, 185, 129, 0.16); border-color: #10b981; }
    .status-success .report-title { color: #10b981 !important; }
    .status-success .guide-box { border-left-color: #10b981; }
    
    .status-info { background: rgba(59, 130, 246, 0.16); border-color: #3b82f6; }
    .status-info .report-title { color: #3b82f6 !important; }
    .status-info .guide-box { border-left-color: #3b82f6; }
    
    @keyframes blink { 50% { opacity: 0.4; } }
    .blink { animation: blink 1.5s linear infinite; }
    </style>
""", unsafe_allow_html=True)

st.title("🦅 沃什新规·宏观决策全指标仪表盘")
st.markdown('<p style="color:#94a3b8 !important; font-size:13px; text-align:center;">基于 Python 大脑运行 | 实时监听修改 | 5组 FRED 源码状态判定</p>', unsafe_allow_html=True)

# 2. 核心手打表单输入区域
with st.form("dashboard_form"):
    st.markdown('<div class="section-title">1. 通胀二阶导组 (短端利率锚定)</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">🔍 查看 FRED 核心通胀源码 ↗</a>', unsafe_allow_html=True)
        cpi = st.number_input("核心 CPI 同比增速 (%)", value=3.200, step=0.001, format="%.3f")
    with col2:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">🔍 查看 FRED 薪资动量源码 ↗</a>', unsafe_allow_html=True)
        eci = st.number_input("就业成本指数 ECI 增速 (%)", value=3.800, step=0.001, format="%.3f")

    st.markdown('<div class="section-title">2. 财政发债组 (长端国债定价)</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">🏛️ 查看 FRED 2年期美债 ↗</a>', unsafe_allow_html=True)
        us02y = st.number_input("2年期美债收益率 (%)", value=4.681, step=0.001, format="%.3f")
    with col4:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">🏛️ 查看 FRED 10年期美债 ↗</a>', unsafe_allow_html=True)
        us10y = st.number_input("10年期美债收益率 (%)", value=5.890, step=0.001, format="%.3f")

    st.markdown('<div class="section-title">3. 流动性走廊组 (核心水管指标)</div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">💧 查看 FRED 实时 SOFR ↗</a>', unsafe_allow_html=True)
        sofr = st.number_input("实时 SOFR 利率 (%)", value=4.880, step=0.001, format="%.3f")
    with col6:
        st.markdown('<a href="https://stlouisfed.org" target="_blank" class="data-link">🏛️ 查看 FRED 准备金 IORB ↗</a>', unsafe_allow_html=True)
        iorb = st.number_input("美联储 IORB 利率 (%)", value=5.000, step=0.001, format="%.3f")

    st.markdown('<div class="section-title">4 & 5. 情绪与市场传染组 (中性利率与风险联动)</div>', unsafe_allow_html=True)
    col7, col8 = st.columns(2)
    with col7:
        st.markdown('<a href="https://tradingview.com" target="_blank" class="data-link">⚠️ 查看 TradingView 债市恐慌 ↗</a>', unsafe_allow_html=True)
        move = st.number_input("美债恐慌指数 (MOVE)", value=115.0, step=1.0, format="%.1f")
    with col8:
        st.markdown('<a href="https://yahoo.com" target="_blank" class="data-link">⚡ 查看 雅虎财经 巨头开支 ↗</a>', unsafe_allow_html=True)
        capex = st.selectbox("科技巨头 M7 季度开支指引", ["持续狂飙 (推高全局中性利率)", "全面砍支 (长期资本需求回落)"])

    # 一键诊断触发表单按钮
    st.form_submit_button("🚀 一键运行 if-else 大脑智能诊断")

# 3. 后台核心数学指标二阶计算
yield_spread = us10y - us02y
liquidity_spread = sofr - iorb

# 4. 派生衍生收益率方块高亮展示
st.markdown('<div style="font-size:13px; color:#ffffff !important; text-align:center; margin-top:20px; font-weight:bold;">📊 衍生核心监控利差数值</div>', unsafe_allow_html=True)

ys_color = "#10b981" if yield_spread > 0.05 else ("#ef4444" if yield_spread <= 0 else "#f59e0b")
ls_color = "#ef4444" if liquidity_spread > 0 else "#10b981"
ls_blink = "blink" if liquidity_spread > 0 else ""

st.markdown(f"""
    <div class="metric-container">
        <div class="metric-card">
            <div style="color: #ffffff !important; font-size:13px; font-weight:bold;">10Y - 2Y 期限利差</div>
            <div class="metric-val" style="color: {ys_color} !important;">{yield_spread:+.3f}%</div>
        </div>
        <div class="metric-card">
            <div style="color: #ffffff !important; font-size:13px; font-weight:bold;">SOFR - IORB 水管利差</div>
            <div class="metric-val {ls_blink}" style="color: {ls_color} !important;">{liquidity_spread:+.3f}%</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. 精准的 Python if-else 判定逻辑树
if liquidity_spread > 0:
    st.markdown(f"""
        <div class="report-card status-danger">
            <div class="report-title blink">🚨【警报：第 3 组水管爆裂 - 市场系统流动性危机】</div>
            <p><strong>状态识别：</strong>当前真实手打数据显示 SOFR 已经顶破 IORB。银行隔夜准备金正被极速抽干，无论其他基本面多好，全市场将进入技术性缺钱踩踏状态。</p>
            <div class="guide-box">
                <h4>🛠【系统交易指导案】</h4>
                <ul>
                    <li><strong>平仓撤退：</strong> 立即平掉所有做空美债的套利杠杆，防止突发强平踩踏。</li>
                    <li><strong>现金规避：</strong> 资金缩回极短端国债现金池（如3个月美债），静待美联储被迫打开 SRF 工具修水管，捕捉其干预后的反弹黄金窗口。</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif yield_spread < -0.4 and (cpi < 2.5 or eci < 3.2):
    st.markdown(f"""
        <div class="report-card status-info">
            <div class="report-title">🍂【场景识别：传统衰退 - 周期全面回归】</div>
            <p><strong>状态识别：</strong>手打利差极深度倒挂 ({yield_spread:.3f}%)，且核心通胀明显重回历史低位。实体经济已被高利率重创，市场彻底放弃沃什主义，全面交易衰退降息。</p>
            <div class="guide-box">
                <h4>🛠【传统周期回归 - 操作指南】</h4>
                <ul>
                    <li><strong>全线做多长债：</strong> 降息通道将全面被迫砸开。全力、满仓做多长端美债（如买入现货 TLT）。</li>
                    <li><strong>避险大迁移：</strong> 清仓顺周期权益资产，配置黄金、防御性高股息板块避险。</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif yield_spread <= 0.05:
    st.markdown(f"""
        <div class="report-card status-warning">
            <div class="report-title">⚡【场景识别：危险的熊平切换 - 全资产估值绞杀】</div>
            <p><strong>状态识别：</strong>期限利差被死死挤压在扁平区间 ({yield_spread:.3f}%)。通胀压力迫使联储强行钉死并拉抬短端（2年期疯涨）。</p>
            <div class="guide-box">
                <h4>🛠【熊平状态下全线撤退-交易套利指南】</h4>
                <ul>
                    <li><strong>防范杀估值：</strong> 全线做空长期和中期国债，大幅降低美股等多头多权益仓位。</li>
                    <li><strong>安全至上：</strong> 保持极高比例的现金储备，在估值未彻底杀透前绝不轻易抄底。</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

else:
    capex_note = "💡 科技巨头 AI 支出强劲，正在底层不断夯实中性利率上移根基。" if "持续狂飙" in capex else ""
    st.markdown(f"""
        <div class="report-card status-success">
            <div class="report-title">🦅【场景识别：基准情景 - 熊陡延续 (Bear Steepener)】</div>
            <p><strong>状态识别：</strong>根据您输入的精准手打数据，当前 10Y-2Y 利差为强劲的 {yield_spread:+.3f}%。短端被锁死，长端因为财政疯狂发债和 AI 资本开支抢钱急速上翘。期限溢价正在大举修复。{capex_note}</p>
            <div class="guide-box">
                <h4>🛠【沃什主义常规行情套利指南】</h4>
                <ul>
                    <li><strong>曲线陡峭套利：</strong> 坚定执行做多短端固定收益、做空长端美债的曲线陡峭化策略（如做空长期美债 TBT / TMV）。</li>
                    <li><strong>重组硬造血资产：</strong> 重仓具备自我造血能力、能够顶住长端利率反噬的 AI 算力与电力硬件供应链龙头，绝对不要长线抄底长期国债。</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
