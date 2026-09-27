import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="沃什主义宏观交易物理监测站 3.7",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 沃什主义宏观交易物理监测站 3.7 (全链接补全版)")
st.markdown("""
> **物理约束判定：通胀二阶导（短端）+ 财政流动性（长端 & 水管）。**
> 
> 请点击左侧栏各个维度的官方数据链接，人工获取最新核心数字并输入，系统将实行全量化、无偏差的宏观沙盘象限判定。
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

# 3. 填报长端拍卖与期限溢价 —— 补全收益率曲线图链接
st.sidebar.subheader("🏛️ ③ 财政发债组（长端定价）")
st.sidebar.markdown("[📈 查阅 MacroMicro 美债收益率曲线图表](https://sc.macromicro.me/charts/81311/US-Treasury-Yield-Curve)")
st.sidebar.markdown("[👉 查阅财政部国债拍卖投标倍数](https://treasurydirect.gov)")
st.sidebar.markdown("[👉 查阅纽约联储 10Y ACM 期限溢价](https://newyorkfed.org)")

bid_to_cover = st.sidebar.number_input("最新 10Y/30Y 美债拍卖投标倍数", value=2.45, min_value=0.00, max_value=5.00, step=0.01)
term_premium = st.sidebar.number_input("最新纽约联储 ACM 期限溢价 (点数)", value=25, min_value=-200, max_value=500, step=1)

st.sidebar.markdown("---")

# 4. 填报债市恐慌指数与大盘利率 —— 补全每日/动态每月走势链接
st.sidebar.subheader("🔥 ④ 市场传染组与AI中枢")
st.sidebar.markdown("[📅 查阅 MacroMicro 美债收益率每日走势](https://sc.macromicro.me/charts/118047/us-bond-yield-rate)")
st.sidebar.markdown("[📊 查阅 MacroMicro 美债收益率动态每月](https://sc.macromicro.me/dynamic_chart?id=4)")
st.sidebar.markdown("[👉 查看实时 MOVE 指数 (CNBC)](https://cnbc.com)")

move_index = st.sidebar.number_input("当前 MOVE 指数实际值", value=110, min_value=0, max_value=300, step=1)
yield_10y = st.sidebar.number_input("美债 10 年期最新收益率 (%)", value=4.50, min_value=0.00, max_value=10.00, step=0.01)

st.sidebar.markdown("---")

# 5. 补充基本面状态
st.sidebar.subheader("📈 ⑤ 实体基本面辅助")
job_market = st.sidebar.selectbox("劳动力市场整体状态", ["就业强劲 / 稳定", "失业率飙升 / 就业市场全面垮台"])


# ==================== 量化算法：基于物理输入的纯硬约束场景诊断 ====================
diagnostic_scenario = ""
diagnostic_strategy = ""
status_type = ""

if sofr_iorb_spread >= 0.02 or sofr_val > (iorb_val + 0.05):
    diagnostic_scenario = "SCENARIO 04: 水管收紧 (A 压倒一切 —— 核心水管告急)"
    diagnostic_strategy = "🔵 【水管失灵象限】\n\n**量化触发点：** SOFR-IORB 利差出现危险正溢价（当前: " + str(sofr_iorb_spread) + "%）。\n\n**操盘结论：** 财政发债已彻底榨干银行超额准备金。水管正在功能性瘫痪！此时不看鹰鸽表态，死盯着美联储手底下是否被迫释放常备回购便利（SRF）等微观工具给市场注入短期现金。"
    status_type = "error"

elif core_cpi_mom >= 0.28 or wage_growth >= 4.2:
    diagnostic_scenario = "SCENARIO 02: 通胀熊平 (A > B > C —— 短端变硬风险复燃)"
    diagnostic_strategy = "🔥 【地缘脱锚 / 短端变硬象限】\n\n**量化触发点：** 核心通胀环比过高（当前: " + str(core_cpi_mom) + "%）或工资动量（" + str(wage_growth) + "%）失控。\n\n**操盘结论：** 供给冲击已深层侵蚀工资结构，沃什的降息窗口被完全焊死，短端利率被迫重新向上变硬（甚至引发再加息恐慌），收益率曲线被强行顶平。策略上应坚定做平收益率曲线，回撤一切对利率敏感的成长股头寸。"
    status_type = "error"

elif job_market == "失业率飙升 / 就业市场全面垮台":
    diagnostic_scenario = "SCENARIO 05: 传统降息再现"
    diagnostic_strategy = "📉 【传统衰退象限】\n\n**量化触发点：** 基本面核心就业彻底垮台。\n\n**操盘结论：** 只有这种实体经济崩塌的情况下，‘美联储看跌期权’才会重新续期。政策重新回到降息主线，长端国债迎来趋势性多头机会。"
    status_type = "info"

elif term_premium > 40 or bid_to_cover < 2.35:
    diagnostic_scenario = "SCENARIO 03: 财政发债 (期限溢价爆表 —— 长端供需失衡)"
    diagnostic_strategy = "🏛️ 【财政抽水象限】\n\n**量化触发点：** 美债国债拍卖投标倍数过低（" + str(bid_to_cover) + "）或纽约联储期限溢价大幅转正。\n\n**操盘结论：** 市场对庞大的发债供给产生物理排斥，长期持债要求极高的风险补偿。长端收益率被供给生生推高，防范无预警的股债双杀风险。"
    status_type = "warning"

else:
    diagnostic_scenario = "SCENARIO 01: 基准熊陡 (A > C > B —— 沃什主义常态)"
    diagnostic_strategy = "✅ 【基准象限】\n\n**量化触发点：** 通胀二阶导（核心PCE/CPI环比: " + str(core_cpi_mom) + "%）可控，微观水管安全，长端利率中枢逐步抬升。\n\n**操盘结论：** 市场正在经历沃什允许的、健康的‘疼’。AI超级资本开支洪流在物理上继续抢夺资源，强行抬高社会真实中性利率中枢。美联储死扛限制性利率（短端不动），长端利率（当前输入: " + str(yield_10y) + "%）由于AI抢钱 and 发债持续上飙。适合顺势做陡收益率曲线。"
    status_type = "success"


# ==================== 主面板显示 ====================

# 1. 自动化红线诊断报告
st.header("🎯 沃什主义红线综合诊断报告")

if status_type == "error":
    st.error(f"🚨 **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
elif status_type == "warning":
    st.warning(f"⚠️ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
elif status_type == "info":
    st.info(f"ℹ️ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
else:
    st.success(f"✅ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")

st.divider()

# 2. 对应视频五组核心监控变量详解（Tabs流动）
st.header("📋 宏观物理雷达五组监测重点对照")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["① 通胀二阶导组", "② 财政发债组", "③ 流动性走廊组", "④ AI资本开支组", "⑤ 市场传染组"])

with tab1:
    st.subheader("🔎 ① 通胀二阶导组 —— 定价利率短端（定海神针）")
    st.markdown(f"""
    *   **当前输入状态：** 核心 CPI 环比：`{core_cpi_mom}%` | 工资/ECI 增速：`{wage_growth}%`
    *   **核心监控逻辑：** 剔除食品与能源后的真实通胀。盯紧超级核心服务通胀与工资动量的传导弹性。
    """)
with tab2:
    st.subheader("🏛️ ② 财政发债组 —— 定价利率长端（发债抽水机）")
    st.markdown(f"""
    *   **当前输入状态：** 拍卖投标倍数：`{bid_to_cover}` | ACM 期限溢价：`{term_premium}`
    *   **深度利差形态观测：** [📈 直达 MacroMicro 美债收益率曲线图表（判断熊陡/熊平）](https://sc.macromicro.me/charts/81311/US-Treasury-Yield-Curve)
    *   **核心监控逻辑：** 评估由于美国财政赤字高企，长端美债发售所承受的真实压力与溢价。
    """)
with tab3:
    st.subheader("💧 ③ 流动性走廊组 —— 核心水管（准备金安全阀）")
    st.markdown(f"""
    *   **当前计算利差：** SOFR - IORB 利差为 `{sofr_iorb_spread}%`
    *   **核心监控逻辑：** 监测银行体系内的准备金是否枯竭，以及金融市场的核心“水管”有无卡死风险。
    """)
with tab4:
    st.subheader("⚡ ④ AI 资本开支组 —— 中性利率中枢（全社会资金强盗）")
    st.markdown(f"""
    *   **当前长端利率参考：** `{yield_10y}%`
    *   **多维度走势对照：** 
        *   [📅 直达 MacroMicro 美债收益率每日走势](https://sc.macromicro.me/charts/118047/us-bond-yield-rate)
        *   [📊 直达 MacroMicro 美债收益率动态每月分布](https://sc.macromicro.me/dynamic_chart?id=4)
    *   **核心监控逻辑：** AI 超级资本开支是在物理层面抢夺一级债市现金。只要科技巨头不停投钱，全社会的自然中性利率中枢就会被物理性抬高。
    """)
with tab5:
    st.subheader("⚠️ ⑤ 市场传染组 —— 风险溢价与恐慌联动（系统扩散器）")
    st.markdown(f"""
    *   **当前输入的 MOVE 债市恐慌指数：** `{move_index}`
    *   **核心监控逻辑：** 用于确认债市的流动性压力是否正像病毒一样扩散至股票等其他资产类。
    """)
