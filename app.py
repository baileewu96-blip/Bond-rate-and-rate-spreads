import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="美联储新规宏观交易沙盘",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 标题
st.title("🧠 美联储新规下的宏观交易沙盘仪表盘")
st.markdown("""
> **“别问鹰还是鸽，先看状态落在哪个象限。”** —— 抛弃主观猜测，将不同维度的市场异动精准对齐底层的风控筹码。
""")

st.divider()

# ==================== 边栏：物理约束指标勾选（多维度联动） ====================
st.sidebar.header("🚨 每日物理数据扫描")
st.sidebar.markdown("请根据当日最新的市况与物理数据进行勾选：")

st.sidebar.subheader("1. 增长与通胀要素")
macro_inflation = st.sidebar.selectbox("通胀与就业状态", ["通胀高 + 就业稳（基准）", "地缘冲击 + 通胀预期脱锚", "就业崩 + 通胀同步回落"])

st.sidebar.subheader("2. 资金面与水管")
sofr_break = st.sidebar.checkbox("SOFR 持续压过/等于 IORB（水管紧张）")
system_jam = st.sidebar.checkbox("国债市场无法正常成交 / 跨行拆借卡死")

st.sidebar.subheader("3. 债券供给与长端")
bid_low = st.sidebar.checkbox("长期美债拍卖投标倍数连创新低")
term_premium_up = st.sidebar.checkbox("Term Premium (ACM期限溢价) 飙升")

st.sidebar.subheader("4. 市场传导")
move_high = st.sidebar.checkbox("MOVE 债市恐慌指数 > 120")
stock_drop = st.sidebar.checkbox("长端利率暴涨引发美股大盘下杀")

# ==================== 核心逻辑：四大象限与五种情景实时自动诊断 ====================
st.sidebar.divider()
st.sidebar.subheader("⚖️ 宏观沙盘当前象限诊断")

current_scenario = ""
quadrant_strategy = ""

if system_jam or sofr_break:
    current_scenario = "SCENARIO 04: 水管收紧 (A 压倒一切)"
    quadrant_strategy = "💧 【水管失灵象限】打法：不谈鹰鸽，央行掏工具箱修水管。盯着美联储释放临时流动性（如SRF），此时利率大方向不降，但微观放水。"
elif macro_inflation == "地缘冲击 + 通胀预期脱锚":
    current_scenario = "SCENARIO 02: 通胀熊平 (A > B > C)"
    quadrant_strategy = "🔥 【地缘脱锚象限】打法：供给冲击进入工资。降息窗口彻底关闭，短端重新变硬。交易‘铁血猛烈加息’预期，做平收益率曲线。"
elif macro_inflation == "就业崩 + 通胀同步回落":
    current_scenario = "SCENARIO 05: 传统降息"
    quadrant_strategy = "📉 【传统衰退象限】打法：就业崩+通胀回落。政策重回降息主线，‘美联储看跌期权’重新续期，长端债市迎来趋势性多头。"
elif term_premium_up or bid_low:
    current_scenario = "SCENARIO 03: 财政发债 (期限溢价爆表)"
    quadrant_strategy = "🏛️ 【财政抽水象限】打法：白宫无忌发债破坏利率结构。长端美债面临纯物理供给下杀，长端收益率被生生推高，做空长端国债或买入高溢价保护。"
else:
    current_scenario = "SCENARIO 01: 基准熊陡 (A > C > B)"
    quadrant_strategy = "⚖️ 【基准象限】打法：通胀高、就业稳、AI强。高波动、少承诺。美联储死扛高利率，盯着长短往上波动放大，顺势做陡曲线。"

# 侧边栏高亮显示结论
st.sidebar.info(f"**当前触发情景：**\n{current_scenario}")
st.sidebar.success(f"**对应操盘打法：**\n{quadrant_strategy}")


# ==================== 主面板：沙盘情景推演与监控变量展示 ====================

st.header("🎯 交易员沙盘复盘主看板")

# 实时诊断横幅通知
st.warning(f"**📊 实时市场诊断结论：** 当前市场完美契合 **{current_scenario}**。请切换对应仪表盘审视物理变量。")

# 用 Tabs 切换图三中的 5组核心变量深度监控
tab1, tab2, tab3, tab4, tab5 = st.tabs(["① 通胀二级传导", "② 财政与期限", "③ 流动性走廊", "④ AI与R星", "⑤ 市场传染"])

with tab1:
    st.subheader("✨ 通胀二级传导 —— 盯短端利率定海神针")
    st.markdown("""
    *   **核心看什么：** 超级核心通胀、ECI工资动量、能源向核心传导弹性。
    *   **怎么观察：** 观察核心PCE环比动量是否黏在 2.5% 以上，亚特兰大薪资增长是否 > 4%。
    *   **结论判定：** 只要数据有粘性，沃什的降息窗口就打不开；一旦地缘引燃通胀，市场立刻切入 **“通胀熊平 (SCENARIO 02)”**。
    *   [🔗 数据源：美国经济分析局 BEA PCE数据](https://bea.gov)
    """)

with tab2:
    st.subheader("🏛️ 财政与期限 —— 盯长端利率抽水机")
    st.markdown("""
    *   **核心看什么：** QRA净借款、拍卖尾部（Tail）、ACM期限溢价、企业债发售。
    *   **怎么观察：** 10Y/30Y国债拍卖投标倍数是否低于 2.4，ACM期限溢价是否转正飙升。
    *   **结论判定：** 供给压力失控会物理上推高长端利率，导致债市无预警大跌，切入 **“财政发债 (SCENARIO 03)”**。
    *   [🔗 数据源：美国财政部国债拍卖结果](https://treasurydirect.gov)
    """)

with tab3:
    st.subheader("💧 流动性走廊 —— 盯系统水管压力表")
    st.markdown("""
    *   **核心看什么：** ON RRP池子、银行准备金总量、SOFR - IORB利差、SRF使用量。
    *   **怎么观察：** 紧盯 RRP 是否枯竭（目前 < 2亿），SOFR 是否常态化超越 IORB，EFFR 是否顶破走廊上限。
    *   **结论判定：** 利差倒挂说明银行系统开始被动失血。一旦卡死立刻切入 **“水管收紧 (SCENARIO 04)”**，逼迫央行必须出手修水管。
    *   [🔗 数据源：纽约联储 SOFR 实时数据](https://newyorkfed.org)
    """)

with tab4:
    st.subheader("🤖 AI 与 R星（⭐ 截图重点标记）")
    st.markdown("""
    *   **核心看什么：** 巨头AI资本开支（Capex）、电力/铜/变压器物理供需、企业信贷展期。
    *   **怎么观察：** **盯的就是全社会的利率中枢（自然中性利率 R-star）在往哪个方向走！** 观察科技巨头在一级债市的抢钱规模是否达到 1.5 万亿美元。
    *   **结论判定：** AI 带来的超级资本开支洪流是物理层面的“资金强盗”，它在物理上**强行推高整体真实中性利率中枢**。这意味着即使没有通胀，高利率也会长期维持，强化 **“基准熊陡 (SCENARIO 01)”**。
    *   [🔗 数据源：圣路易斯联储 FRED: 电力行业产能利用率](https://stlouisfed.org)
    """)

with tab5:
    st.subheader("📉 市场传染 —— 盯系统崩坏扩散器")
    st.markdown("""
    *   **核心看什么：** MOVE美债恐慌、VIX-MOVE相关性、Risk Parity（风险平价基金）去杠杆、CTA动量出货。
    *   **怎么观察：** MOVE 指数是否破 120，美股大盘是否由无感转为跟随美债大跌而同步恐慌。
    *   **结论判定：** 如果只是股票杀估值、信用利差扩大，属于沃什允许的**健康的“疼”（左线）**，不触发救市。除非全面就业崩塌，否则绝不轻言“传统降息”。
    *   [🔗 数据源：CNBC 市场数据: MOVE 指数](https://cnbc.com)
    """)
