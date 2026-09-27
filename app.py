import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="沃什主义宏观交易物理监测站 4.0",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 沃什主义宏观交易物理监测站 4.0 (硬约束与物理推导全嵌版)")
st.markdown("""
> **基于“物理约束”的宏观状态识别机器** —— 告别嘴炮，用钱的流向、供给压力、通胀二阶导与核心水管的物理摩擦来锚定市场象限。
""")
st.divider()

# ==================== 侧边栏：五组核心变量全数字化填报 ====================
st.sidebar.header("📊 物理指标实时填报")
st.sidebar.markdown("请点击下方官方链接查看最新数字，并输入系统：")

# 1. 填报通胀二阶导组（定价利率短端）
st.sidebar.subheader("🔍 ① 通胀二阶导组（短端）")
st.sidebar.markdown("[👉 查阅美国劳工统计局 BLS CPI 官网](https://bls.gov)")
st.sidebar.markdown("[👉 查阅美国劳工统计局 BLS 薪资与工时](https://bls.gov)")

core_cpi_mom = st.sidebar.number_input("核心 CPI 环比增速 (MoM %)", value=0.20, min_value=-1.00, max_value=2.00, step=0.01, help="连续高于 0.25% 说明通胀极具粘性")
wage_growth = st.sidebar.number_input("工资增速 / ECI 工资动量 (YoY %)", value=3.8, min_value=0.0, max_value=10.0, step=0.1, help="高于 4.0% 将持续向服务业通胀传导")

st.sidebar.markdown("---")

# 2. 填报核心流动性水管
st.sidebar.subheader("💧 ② 流动性走廊组（核心水管）")
st.sidebar.markdown("[👉 查阅纽约联储 SOFR 最新值](https://newyorkfed.org)")
st.sidebar.markdown("[👉 查阅美联储官方 IORB 利率](https://federalreserve.org)")

sofr_val = st.sidebar.number_input("最新 SOFR 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
iorb_val = st.sidebar.number_input("当前官方 IORB 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
sofr_iorb_spread = round(sofr_val - iorb_val, 3)

st.sidebar.markdown("---")

# 3. 填报长端拍卖与期限溢价
st.sidebar.subheader("🏛️ ③ 财政发债组（长端定价）")
st.sidebar.markdown("[📈 查阅 MacroMicro 美债收益率曲线图表](https://macromicro.me)")
st.sidebar.markdown("[👉 查阅财政部国债拍卖投标倍数](https://treasurydirect.gov)")
st.sidebar.markdown("[👉 查阅纽约联储 10Y ACM 期限溢价](https://newyorkfed.org)")

bid_to_cover = st.sidebar.number_input("最新 10Y/30Y 美债拍卖投标倍数", value=2.45, min_value=0.00, max_value=5.00, step=0.01)
term_premium = st.sidebar.number_input("最新纽约联储 ACM 期限溢价 (点数)", value=25, min_value=-200, max_value=500, step=1)

st.sidebar.markdown("---")

# 4. 填报债市恐慌指数与大盘利率
st.sidebar.subheader("🔥 ④ 市场传染组与AI中枢")
st.sidebar.markdown("[📅 查阅 MacroMicro 美债收益率每日走势](https://macromicro.me)")
st.sidebar.markdown("[📊 查阅 MacroMicro 美债收益率动态每月](https://macromicro.me)")
st.sidebar.markdown("[👉 查看实时 MOVE 指数 (CNBC)](https://cnbc.com)")

move_index = st.sidebar.number_input("当前 MOVE 指数实际值", value=110, min_value=0, max_value=300, step=1)
yield_10y = st.sidebar.number_input("美债 10 年期最新收益率 (%)", value=4.50, min_value=0.00, max_value=10.00, step=0.01)

st.sidebar.markdown("---")

# 5. 补充基本面状态 —— 精准映射截图中的基本面场景
st.sidebar.subheader("📈 ⑤ 实体基本面象限状态")
job_market = st.sidebar.selectbox(
    "基本面象限选择", 
    [
        "通胀高 + 就业稳（沃什基准常态）", 
        "地缘政治地缘冲击导致通胀脱锚", 
        "白宫赤字失控/财政无忌发债过载",
        "就业垮塌 + 经济全面实质性衰退"
    ]
)


# ==================== 量化算法与物理推导硬编码判定模块 ====================
diagnostic_scenario = ""
diagnostic_strategy = ""
physical_deduction = ""
status_type = ""

# 按宏观风险级别及数据条件执行严格过滤
if sofr_iorb_spread >= 0.02 or sofr_val > (iorb_val + 0.05):
    # 场景4：水管收紧 / 触及右线
    diagnostic_scenario = "SCENARIO 04: 水管收紧 (A 压倒一切 —— 核心流动性失灵象限)"
    status_type = "error"
    physical_deduction = """
    **🧠 物理推导过程：**
    1. 隔夜逆回购 (RRP) 塔的缓冲垫此时已经彻底一滴不剩 (< 2亿)。
    2. 财政部继续密集发债抽水，越过缓冲垫直接疯狂抽走银行体系的超额准备金。
    3. 金融机构被迫在回购市场上不计成本地拆借现金，导致 SOFR 发生物理溢价，直接压倒并超越 IORB，跨行拆借链条卡死、功能性瘫痪。
    """
    diagnostic_strategy = """
    **⚖️ 交易员操盘打法：**
    *   **红线跨越：** 市场已触及美联储的**“右线（系统性崩坏）”**。此时不是资产定价高低的问题，而是金融机器本身停摆。
    *   **应对行动：** 抛弃一切关于鹰派鸽派的口头辩论。沃什虽然宏观上死扛高利率，但手底下**必须被迫立刻打开应急流动性水龙头（如常备回购便利 SRF）给系统修水管**。紧盯流动性工具释放，切勿盲目做多股票。
    """

elif job_market == "地缘政治地缘冲击导致通胀脱锚" or core_cpi_mom >= 0.28 or wage_growth >= 4.2:
    # 场景2：通胀熊平 / 地缘脱锚
    diagnostic_scenario = "SCENARIO 02: 通胀熊平 (A > B > C —— 地缘脱锚与短端变硬象限)"
    status_type = "error"
    physical_deduction = f"""
    **🧠 物理推导过程：**
    1. 地缘政治黑天鹅（如中东或地缘冲突）引发大宗商品供给冲击。
    2. 核心 CPI 环比（当前填报: {core_cpi_mom}%）与工资增速（当前填报: {wage_growth}%）二级传导被完全引燃，二次通胀之火重燃。
    3. 通胀预期彻底脱锚，导致美联储降息窗口被完全焊死，甚至逼出市场关于“重新铁血猛烈加息”的极端对冲筹码。
    """
    diagnostic_strategy = """
    **⚖️ 交易员操盘打法：**
    *   **走走势演变：** 市场会强行切换至最具毁灭性的**“通胀熊平”**形态 —— 也就是短端利率受加息预期推动重新掉头往上爆胀，几乎把长端强行顶平。
    *   **应对行动：** 降息和兜底保单彻底作废！立刻全面撤回一切对利率极度敏感的科技股、成长股头寸，坚定买入收益率曲线变平（Bear Flattener）的宏观对冲工具。
    """

elif job_market == "就业垮塌 + 经济全面实质性衰退":
    # 场景5：传统降息 / 传统衰退
    diagnostic_scenario = "SCENARIO 05: 传统降息 (传统衰退象限)"
    status_type = "info"
    physical_deduction = """
    **🧠 物理推导过程：**
    1. 紧缩的高利率终于完成了全面清算，实体经济的就业市场核心指标出现断裂式垮塌（失业率飙升）。
    2. 需求侧全面崩溃导致通胀同步大幅回落，物价失去底层支撑。
    3. 宏观环境被迫离开沃什主义的基准轨道，向传统经典衰退周期靠拢。
    """
    diagnostic_strategy = """
    **⚖️ 交易员操盘打法：**
    *   **红线释放：** 只有在就业市场全面垮台的这一种极端情况下，过去送给市场的免费礼物 —— **“美联储看跌期权（Fed Put）”才会被重新续期**。
    *   **应对行动：** 政策重心重回大举降息主线。长端债市将迎来确定性最高的趋势性大牛头行情，可以战略性全仓长久期美债，并逐步配置抗衰退的防御型资产。
    """

elif job_market == "白宫赤字失控/财政无忌发债过载" or term_premium > 40 or bid_to_cover < 2.35:
    # 场景3：财政发债 / 期限溢价爆表
    diagnostic_scenario = "SCENARIO 03: 财政发债 (期限溢价爆表 —— 财政抽水象限)"
    status_type = "warning"
    physical_deduction = f"""
    **🧠 物理推导过程：**
    1. 白宫与财政部肆无忌惮地扩大赤字（2026财年预算红皮书已将赤字推高至2.06万亿美元），导致长期持债的总量供给严重过载。
    2. 长期国债拍卖的投标倍数（当前输入: {bid_to_cover}）持续击穿临界线，一级交易商（Dealer）被迫大举垫资包销。
    3. 市场对这种疯狂破坏利率结构的滥发债券行为产生物理排斥，对长期持债索要极高的风险补偿，纽约联储 ACM 期限溢价（当前输入: {term_premium}点）发生爆表。
    """
    diagnostic_strategy = """
    **⚖️ 交易员操盘打法：**
    *   **走势形变：** 长端美债面临纯粹由于物理供给过剩引发的破位崩盘，长端收益率（如30Y）会被发债活生生强行推高。
    *   **应对行动：** 警惕突发性的股债双杀。策略上应坚定做空长端国债或买入期限溢价高波动保护，直至白宫表现出缩减赤字的实际物理约束。
    """

else:
    # 默认：基本面场景01：基准熊陡
    diagnostic_scenario = "SCENARIO 01: 基准熊陡 (A > C > B —— 沃什主义日常象限)"
    status_type = "success"
    physical_deduction = f"""
    **🧠 物理推导过程：**
    1. 实体基本面处于“通胀具有粘性 + 就业维持稳定”的常态。
    2. 同时，科技巨头为了抢夺 AI 王座在债券市场上大举展开军备竞赛，未来几年预计发债抢钱规模高达 1.5 万亿美元。
    3. 这种巨额、长期的资本开支洪流作为物理层面的“资金强盗”，在底层强行推高了全社会无形的不冷不热的**自然中性利率中枢（R-star）**。
    """
    diagnostic_strategy = f"""
    **⚖️ 交易员操盘打法：**
    *   **走势变迁：** 收益率曲线锁定为经典的**“熊陡（Bear Steepener）”** —— 短端被美联储因通胀粘性盯着死死降不下来，长端利率（当前输入: {yield_10y}%）受发债和AI抢钱的物理约束拼命往上翘。
    *   **红线诊断：** 此时股票杀估值、信用利差扩大在沃什眼里都属于**健康的“疼”（左线区间）**。美联储绝不承诺路线图，也大几率放任不管、绝不降息兜底。不要盲目抄底，顺势做陡收益率曲线。
    """


# ==================== 主面板页面渲染 ====================

# 1. 全自动状态红线诊断看板
st.header("🎯 沃什主义红线综合诊断报告")

if status_type == "error":
    st.error(f"🚨 **当前市场状态判定：{diagnostic_scenario}**")
elif status_type == "warning":
    st.warning(f"⚠️ **当前市场状态判定：{diagnostic_scenario}**")
elif status_type == "info":
    st.info(f"ℹ️ **当前市场状态判定：{diagnostic_scenario}**")
else:
    st.success(f"✅ **当前市场状态判定：{diagnostic_scenario}**")

# 分栏并排展示推导和策略
col_deduct, col_strat = st.columns(2)
with col_deduct:
    st.markdown(physical_deduction)
with col_strat:
    st.markdown(diagnostic_strategy)

st.divider()

# 2. 五组核心监控变量雷达面板（包含你之前要求保留的所有最新 MacroMicro 链接）
st.header("📋 宏观物理雷达五组监测重点对照")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["① 通胀二阶导组", "② 财政发债组", "③ 流动性走廊组", "④ AI资本开支组", "⑤ 市场传染组"])

with tab1:
    st.subheader("🔎 ① 通胀二阶导组 —— 定价利率短端（定海神针）")
    st.markdown(f"""
    *   **填报状态：** 核心 CPI 环比：`{core_cpi_mom}%` | 工资/ECI 增速：`{wage_growth}%`
    *   **判断标准：** 环比动量是否黏在 `0.25%` 以上，工资增速是否阻碍服务业通胀回落。
    *   **物理推导：** 只要短端通胀二阶导不熄灭，沃什作为清算主义者就拥有绝对底气死扛高利率，美联储前瞻路线图欠条将永远消失。
    """)
with tab2:
    st.subheader("🏛️ ② 财政发债组 —— 定价利率长端（供给发债机）")
    st.markdown(f"""
    *   **填报状态：** 拍卖投标倍数：`{bid_to_cover}` | ACM 期限溢价：`{term_premium}`
    *   **核心图表对照：** [📈 直达 MacroMicro 美债收益率曲线图表（判断熊陡/熊平）](https://macromicro.me)
    *   **判断标准：** 10Y/30Y美债拍卖投标倍数安全底线在 `2.35 - 2.40`。一旦向下击穿或长端曲线异常变直，说明市场吸纳美债纯供给的能力到达上限。
    """)
with tab3:
    st.subheader("💧 ③ 流动性走廊组 —— 核心水管（金融机器压力阀）")
    st.markdown(f"""
    *   **当前水管利差：** SOFR - IORB = `{sofr_iorb_spread}%`
    *   **判断标准：** 密切注视利差是否常态化转正（`>= 0.02%`）。
    *   **物理推导：** 跨越左线健康的疼，直接撞击**右线扳机**。代表流动性无缓冲抽水，水管出现功能性瘫痪，逼迫央行必须出面修水管。
    """)
with tab4:
    st.subheader("⚡ ④ AI 资本开支组 —— 中性利率中枢（全社会资金强盗）")
    st.markdown(f"""
    *   **填报状态：** 最新 10 年期美债收益率：`{yield_10y}%`
    *   **长短期趋势雷达：** 
        *   [📅 直达 MacroMicro 美债收益率每日走势图表](https://macromicro.me)
        *   [📊 直达 MacroMicro 美债收益率动态每月分布](https://macromicro.me)
    *   **核心强调：** **“盯的就是中性利率中枢在往哪个方向走”**。AI 洪流在实体层面疯狂抢夺稀缺资金和电网资源，强行夯实了全社会的自然真实中性利率中枢（R-star），高利率时代宣告常态化。
    """)
with tab5:
    st.subheader("⚠️ ⑤ 市场传染组 —— 风险溢价与恐慌联动（系统扩散器）")
    st.markdown(f"""
    *   **填报状态：** MOVE 指数：`{move_index}`
    *   **判断标准：** MOVE 指数是否击穿 `120` 安全界线。
    *   **物理推导：** 只要没有出现流动性卡死、功能性瘫痪（右线），单纯的股票下杀和信用利差走阔，在沃什眼里都属于**市场对没有 Fed Put 的沃什主义时代进行健康的自我定价（左线放任不管）**。
    """)
