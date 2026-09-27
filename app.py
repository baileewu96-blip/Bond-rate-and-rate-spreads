import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="沃什主义宏观交易物理监测站 3.0",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 沃什主义宏观交易物理监测站 3.0 (纯净填报版)")
st.markdown("""
> **用物理数字锚定宏观，拒绝主观盲猜。** 
> 
> 请点击左侧栏的官方链接获取最新真实市场数据，输入数值后系统将根据物理阈值进行**全自动象限状态判定**。
""")
st.divider()

# ==================== 侧边栏：数字硬指标手动填报 ====================
st.sidebar.header("📊 物理指标实时填报")
st.sidebar.markdown("请点击下方官方链接查看最新数字，并输入系统：")

# 1. 填报核心流动性水管
st.sidebar.subheader("💧 ① 流动性走廊指标")
st.sidebar.markdown("[👉 查阅纽约联储 SOFR 最新值](https://newyorkfed.org)")
st.sidebar.markdown("[👉 查阅美联储官方 IORB 利率](https://federalreserve.org)")

sofr_val = st.sidebar.number_input("最新 SOFR 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
iorb_val = st.sidebar.number_input("当前官方 IORB 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
sofr_iorb_spread = round(sofr_val - iorb_val, 3)

st.sidebar.markdown("---")

# 2. 填报长端拍卖与期限溢价
st.sidebar.subheader("🏛️ ② 财政供给与期限溢价")
st.sidebar.markdown("[👉 查阅财政部国债拍卖投标倍数](https://treasurydirect.gov)")
st.sidebar.markdown("[👉 查阅纽约联储 10Y ACM 期限溢价](https://newyorkfed.org)")

bid_to_cover = st.sidebar.number_input("最新 10Y/30Y 美债拍卖投标倍数", value=2.45, min_value=0.00, max_value=5.00, step=0.01)
term_premium = st.sidebar.number_input("最新纽约联储 ACM 期限溢价 (点数)", value=25, min_value=-200, max_value=500, step=1)

st.sidebar.markdown("---")

# 3. 填报债市恐慌指数与大盘利率
st.sidebar.subheader("🔥 ③ 债市情绪与长端利率")
st.sidebar.markdown("[👉 查看实时 MOVE 指数](https://cnbc.com)")
st.sidebar.markdown("[👉 查看美债 10 年期实时收益率](https://cnbc.com)")

move_index = st.sidebar.number_input("当前 MOVE 指数实际值", value=110, min_value=0, max_value=300, step=1)
yield_10y = st.sidebar.number_input("美债 10 年期最新收益率 (%)", value=4.50, min_value=0.00, max_value=10.00, step=0.01)

st.sidebar.markdown("---")

# 4. 补充基本面状态
st.sidebar.subheader("📈 ④ 基本面象限辅助")
macro_inflation = st.sidebar.selectbox("通胀与就业状态", ["通胀高 + 就业稳（基准）", "地缘冲击 + 通胀预期脱锚", "就业崩 + 通胀同步回落"])


# ==================== 量化算法：全自动象限场景判断 ====================
diagnostic_scenario = ""
diagnostic_strategy = ""
status_type = ""

# 严密的量化硬约束阈值判断
if sofr_iorb_spread >= 0.02 or sofr_val > (iorb_val + 0.05):
    diagnostic_scenario = "SCENARIO 04: 水管收紧 (A 压倒一切)"
    diagnostic_strategy = "🔵 【水管失灵象限】\n\n**量化触发点：** SOFR-IORB 利差出现危险倒挂（当前: " + str(sofr_iorb_spread) + "%）。\n\n**操盘结论：** 财政发债已越过缓冲垫直接抽干银行准备金。不要试图做多任何风险资产！此时无需理会美联储官员表态，死盯着美联储手底下是否被迫释放临时流动性（如SRF）进行微观修水管。"
    status_type = "error"
elif macro_inflation == "地缘冲击 + 通胀预期脱锚":
    diagnostic_scenario = "SCENARIO 02: 通胀熊平 (A > B > C)"
    diagnostic_strategy = "🔥 【地缘脱锚象限】\n\n**量化触发点：** 通胀预期被地缘大宗商品点燃。\n\n**操盘结论：** 供给冲击进入工资，降息窗口彻底关闭。短端重新变硬暴涨，会把长端几乎强行顶平。策略上应交易‘铁血猛烈加息’预期，做平收益率曲线。"
    status_type = "warning"
elif macro_inflation == "就业崩 + 通胀同步回落":
    diagnostic_scenario = "SCENARIO 05: 传统降息"
    diagnostic_strategy = "📉 【传统衰退象限】\n\n**量化触发点：** 基本面核心就业彻底垮台。\n\n**操盘结论：** 只有这种情况下，‘美联储看跌期权’才会重新续期。政策重新回到降息主线，长端国债迎来趋势性多头机会。"
    status_type = "info"
elif term_premium > 40 or bid_to_cover < 2.35:
    diagnostic_scenario = "SCENARIO 03: 财政发债 (期限溢价爆表)"
    diagnostic_strategy = "🏛️ 【财政抽水象限】\n\n**量化触发点：** 投标倍数极其危险（" + str(bid_to_cover) + "）或期限溢价由于供需失衡飙升。\n\n**操盘结论：** 市场对庞大的发债规模出现物理排斥。长端收益率面临被发债供给活生生推高的绝望境地。策略上应顺势防范股债双杀风险。"
    status_type = "warning"
else:
    # 默认处于视频中的基准熊陡象限
    diagnostic_scenario = "SCENARIO 01: 基准熊陡 (A > C > B)"
    diagnostic_strategy = "⚖️ 【基准象限（沃什主义常态）】\n\n**量化触发点：** 各微观指标维持在安全阈值，长端收益率（当前输入: " + str(yield_10y) + "%）中枢保持稳步上移。\n\n**操盘结论：** 市场处于健康的‘疼’。通胀高、就业稳、AI超级资本开支继续抢钱。沃什将死扛高利率，短端被钉死，长端收益率持续上飙。适合顺势做陡收益率曲线。"
    status_type = "success"


# ==================== 主看板显示 ====================

# 1. 自动化红线诊断报告
st.header("🎯 沃什主义红线诊断报告")

if status_type == "error":
    st.error(f"🚨 **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
elif status_type == "warning":
    st.warning(f"⚠️ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
elif status_type == "info":
    st.info(f"ℹ️ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
else:
    st.success(f"✅ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")

st.divider()

# 2. 对应视频五组核心监控变量详解（Tabs联动）
st.header("📋 宏观雷达五组监测重点对照")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["① 通胀二级传导", "② 财政与期限", "③ 流动性走廊", "④ AI与R星", "⑤ 市场传染"])

with tab1:
    st.subheader("✨ ① 通胀二级传导 —— 监控短端利率定海神针")
    st.markdown("""
    *   **核心看什么：** 超级核心通胀、ECI工资动量、能源向核心传导弹性。
    *   **量化判定线：** 只要工资增速有粘性，沃什的降息窗口就打不开。一旦地缘引燃通胀，市场立刻切入 **“通胀熊平 (SCENARIO 02)”**。
    """)
with tab2:
    st.subheader("🏛️ ② 财政与期限 —— 监控长期持债面临的纯供给轰炸")
    st.markdown(f"""
    *   **输入值状态：** 投标倍数 `{bid_to_cover}` | ACM期限溢价 `{term_premium}`
    *   **物理推导：** 投标倍数连续低于 2.35-2.40 意味着一级交易商被迫垫资吃下的筹码越多，长端国债会物理破位，触发 **“财政发债 (SCENARIO 03)”**。
    """)
with tab3:
    st.subheader("💧 ③ 流动性走廊 —— 监控金融机器水管是否功能性瘫痪")
    st.markdown(f"""
    *   **输入计算结果：** SOFR - IORB 利差为 `{sofr_iorb_spread}%`
    *   **红线指标：** 一旦利差转正（`>= 0.02%`），说明水管正式炸裂，切入 **“水管收紧 (SCENARIO 04)”**。沃什必须被迫放水修水管。
    """)
with tab4:
    st.subheader("🤖 ④ AI 与 R星 —— 监控真实中性利率中枢的方向")
    st.markdown(f"""
    *   **当前填报长端利率：** `{yield_10y}%`
    *   **核心强调：** **“盯的就是利率中枢在往哪个方向走”**。AI的超级资本开支洪流是物理层面的“资金强盗”，只要巨头还在砸钱，社会自然中性利率（R-star）就会被强行抬升。
    """)
with tab5:
    st.subheader("📉 ⑤ 市场传染 —— 识别健康的‘疼’还是系统性崩溃")
    st.markdown(f"""
    *   **当前输入的 MOVE 债市恐慌指数：** `{move_index}`
    *   **物理推导：** MOVE 跌破安全底线（> 120）且伴随股债双杀时，代表风险传染全面失控。反之，单纯的股票跌、信用利差扩大，在沃什眼里都属于**健康的疼（左线）**。
    """)
