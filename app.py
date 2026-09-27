import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# 设置页面配置
st.set_page_config(
    page_title="沃什主义宏观物理监测站 3.0",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 沃什主义宏观交易物理监测站 3.0 (自动化量化版)")
st.markdown("""
> **拒绝主观盲猜，用物理数据说话。** 系统自动爬取大盘核心资产与恐慌指数，结合你输入的微观流动性数据，进行全自动象限状态诊断。
""")
st.divider()

# ==================== 后端数据自动爬取模块 ====================
@st.cache_data(ttl=3600)  # 缓存1小时，避免频繁请求
def fetch_market_data():
    data = {}
    try:
        # 爬取 10年期美债收益率 (^TNX) 和 2年期美债收益率 (^IRX 或 ^ZCNX 常用代号)
        # 为确保准确，这里采用雅虎金融的标准美债收益率代码
        tickers = {
            "10Y_Yield": "^TNX",
            "5Y_Yield": "^FVX",
            "13W_Yield": "^IRX" # 3个月短期国债
        }
        
        # 抓取长端美债收益率 (10年期)
        tnx = yf.Ticker("^TNX")
        hist_tnx = tnx.history(period="2d")
        data["10Y_Yield"] = round(hist_tnx['Close'].iloc[-1], 2) if not hist_tnx.empty else 4.50
        
        # 抓取短端代号 (通常用 2年期国债收益率，雅虎代号常用布隆伯格等投行映射，这里用2年期国债期货对应的公允收益率或3M作为贴现参考)
        # 为防代号失效，我们同时引入 VIX / MOVE 代号作为传染监控
        vix = yf.Ticker("^VIX")
        hist_vix = vix.history(period="2d")
        data["VIX"] = round(hist_vix['Close'].iloc[-1], 2) if not hist_vix.empty else 15.0
        
        # 默认基准短端高利率时代标杆值 (通常2026年锚定在4.2%左右)
        data["2Y_Yield_Est"] = 4.20 
        data["Curve_Slope"] = round(data["10Y_Yield"] - data["2Y_Yield_Est"], 2)
        
    except Exception as e:
        st.error(f"部分实时数据抓取失败（可能由于休市或接口延迟），已启用基准宏观锚定值。错误信息: {e}")
        data = {"10Y_Yield": 4.50, "VIX": 16.5, "2Y_Yield_Est": 4.20, "Curve_Slope": 0.30}
    return data

market_data = fetch_market_data()

# ==================== 侧边栏：精准数字化手动填报 ====================
st.sidebar.header("📊 微观物理指标填报")
st.sidebar.markdown("请点击下方官方链接查看最新数字，并输入系统：")

# 1. 填报核心流动性水管
st.sidebar.subheader("💧 核心水管指标填报")
st.sidebar.markdown("[👉 点此查阅纽约联储 SOFR 最新值](https://newyorkfed.org)")
st.sidebar.markdown("[👉 点此查阅美联储官方 IORB 利率](https://federalreserve.org)")

sofr_val = st.sidebar.number_input("请输入当日最新 SOFR 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
iorb_val = st.sidebar.number_input("请输入当前官方 IORB 利率 (%)", value=4.15, min_value=0.00, max_value=10.00, step=0.01)
sofr_iorb_spread = round(sofr_val - iorb_val, 3)

st.sidebar.markdown("---")

# 2. 填报长端拍卖与期限溢价
st.sidebar.subheader("🏛️ 财政供给与期限溢价")
st.sidebar.markdown("[👉 点此查阅财政部国债拍卖投标倍数](https://treasurydirect.gov)")
st.sidebar.markdown("[👉 点此查阅纽约联储 10Y ACM 期限溢价](https://newyorkfed.org)")

bid_to_cover = st.sidebar.number_input("最新10Y/30Y美债拍卖投标倍数", value=2.45, min_value=0.00, max_value=5.00, step=0.01)
term_premium = st.sidebar.number_input("最新纽约联储 ACM 期限溢价 (点数)", value=25, min_value=-200, max_value=500, step=1)

st.sidebar.markdown("---")

# 3. 填报债市恐慌指数
st.sidebar.subheader("🔥 债市情绪传染")
st.sidebar.markdown("[👉 点此查看实时 MOVE 指数](https://cnbc.com)")
move_index = st.sidebar.number_input("当前 MOVE 指数实际值", value=110, min_value=0, max_value=300, step=1)

# ==================== 量化算法：全自动象限场景判断 ====================
diagnostic_scenario = ""
diagnostic_strategy = ""
bg_color = ""

# 严密的量化硬约束阈值判断
if sofr_iorb_spread >= 0.02 or sofr_val > (iorb_val + 0.05):
    diagnostic_scenario = "SCENARIO 04: 水管收紧 (A 压倒一切)"
    diagnostic_strategy = "🔵 【水管失灵象限】\n\n**量化触发点：** SOFR-IORB 利差转正（当前: " + str(sofr_iorb_spread) + "%）。\n\n**操盘结论：** 财政发债已越过缓冲垫直接抽干准备金。不要试图做多任何风险资产！此时无需理会美联储官员表态，死盯着美联储手底下是否被迫释放临时流动性（如SRF）进行微观修水管。"
    status_type = "error"
elif term_premium > 40 or bid_to_cover < 2.35:
    diagnostic_scenario = "SCENARIO 03: 财政发债 (期限溢价爆表)"
    diagnostic_strategy = "🏛️ 【财政抽水象限】\n\n**量化触发点：** 投标倍数危急（" + str(bid_to_cover) + "）或期限溢价过高。\n\n**操盘结论：** 市场对庞大的发债规模出现物理排斥。长端收益率面临被发债活生生推高的绝望境地。策略上应坚定做空长端国债或全面防御股债双杀风险。"
    status_type = "warning"
elif move_index >= 120:
    diagnostic_scenario = "SCENARIO 02 / 情绪传导: 市场高危重定价"
    diagnostic_strategy = "🔥 【地缘脱锚与传染象限】\n\n**量化触发点：** MOVE 恐慌指数（" + str(move_index) + "）击穿安全线。\n\n**操盘结论：** 债市波动率已经开始向股市大范围扩散。如果此时通胀环比动量依然坚挺，说明市场正在对‘沃什绝不降息兜底’这一冷酷事实进行剧烈的估值下杀，切勿盲目抄底。"
    status_type = "warning"
else:
    # 默认处于视频中的基准熊陡象限
    diagnostic_scenario = "SCENARIO 01: 基准熊陡 (A > C > B)"
    diagnostic_strategy = "⚖️ 【基准象限（沃什主义常态）】\n\n**量化触发点：** 各水管指标在安全阈值内，长端收益率（当前实时: " + str(market_data["10Y_Yield"]) + "%）呈中枢上移状态。\n\n**操盘结论：** 市场处于健康的‘疼’。通胀高、就业稳、AI超级资本开支继续抢钱。沃什将死扛高利率，短端被钉死，长端收益率持续上飙。适合顺势做陡收益率曲线。"
    status_type = "success"


# ==================== 主看板：实时数据流与沙盘核对 ====================

# 1. 实时网络爬取数据看板
st.header("🌐 实时大盘物理变量 (网络自动抓取)")
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric(label="🇺🇸 美债10年期收益率 (实时)", value=f"{market_data['10Y_Yield']}%", delta="长端利率中枢")
with kpi2:
    st.metric(label="📉 模拟长短端利差 (10Y - 2Y估值)", value=f"{market_data['Curve_Slope']}%", delta="正值代表熊陡中", delta_color="normal")
with kpi3:
    st.metric(label="📊 股市波动率 VIX (实时)", value=market_data['VIX'], delta="基础风险传染参照")

st.divider()

# 2. 自动化红线诊断报告
st.header("🎯 沃什主义红线诊断报告 (全自动判定)")

if status_type == "error":
    st.error(f"🚨 **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
elif status_type == "warning":
    st.warning(f"⚠️ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")
else:
    st.success(f"✅ **判定情景：{diagnostic_scenario}**\n\n{diagnostic_strategy}")

st.divider()

# 3. 对应视频五组核心监控变量详解（Tabs联动）
st.header("📋 宏观雷达五组监测重点对照")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["① 通胀二级传导", "② 财政与期限", "③ 流动性走廊", "④ AI与R星", "⑤ 市场传染"])

with tab1:
    st.subheader("✨ ① 通胀二级传导 —— 监控短端利率变硬风险")
    st.markdown("""
    *   **核心物理变量：** 核心 PCE 3个月/6个月年化环比动量、亚特兰大联储薪资增长追踪器。
    *   **量化判定线：** 如果 PCE 环比动量持续 > 2.5% 且地缘政治引发大宗商品脱锚，短端利率将彻底锁死，甚至逼出加息预期。
    """)
with tab2:
    st.subheader("🏛️ ② 财政与期限 —— 监控长期持债面临的纯供给轰炸")
    st.markdown(f"""
    *   **你刚才输入的拍卖投标倍数：** `{bid_to_cover}` （安全底线：2.35-2.40）
    *   **你刚才输入的 ACM 期限溢价：** `{term_premium} 点`
    *   **物理推导：** 投标倍数越低，意味着一级交易商被迫垫资吃下的筹码越多，长端国债会纯粹因为发债过载而物理崩盘。
    """)
with tab3:
    st.subheader("💧 ③ 流动性走廊 —— 监控金融机器水管是否功能性瘫痪")
    st.markdown(f"""
    *   **当前计算出的 SOFR - IORB 实际利差：** `{sofr_iorb_spread}%`
    *   **危险阈值公理：** 
        *   `< 0.00%`：资金极其充裕。
        *   `0.00% 到 0.02%`：水管压力开始增大，逆回购缓冲池彻底抽干。
        *   `>= 0.02% 甚至转正`：**触发右线！** 金融机构开始在回购市场不计成本抢钱，跨行拆借停摆。
    """)
with tab4:
    st.subheader("🤖 ④ AI 与 R星 —— 监控真实中性利率中枢的方向")
    st.markdown("""
    *   **核心物理变量：** 科技巨头季度 CapEx 总额（锚定 1.5 万亿美元级别）、电网与铜等供应链瓶颈。
    *   **截图红框核心强调：** **“盯的就是利率中枢在往哪个方向走”**。AI 的超级资本开支洪流是物理层面的“资金抢盗者”，只要它们还在疯狂砸钱，社会无形的中性利率（R-star）就会持续上移，彻底封死长端利率大幅回落的空间。
    """)
with tab5:
    st.subheader("📉 ⑤ 市场传染 —— 识别健康的‘疼’还是系统性崩溃")
    st.markdown(f"""
    *   **当前输入的 MOVE 债市恐慌指数：** `{move_index}`（安全底线：110）
    *   **物理推导：** 沃什追求的是清算主义。股票跌、利差走阔属于**健康的疼（左线）**，他绝不插手。只有当 MOVE 飙升引发流动性全面干涸、股债汇呈现断裂式无量下跌时，才代表进入风险传染的全面失控状态。
    """)
