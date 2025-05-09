#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### By James Zheng 19-Sep-2024
###
### Methodology:
### 1. calculate SHA256 of the given passcode ( in utf-8 ) - if no passcode provided, the number will be set to 0
### 2. convert it into a 24 digit base2048 number
### 3. reverse the digit of the number - smallest goes first and put largest at the end, fill the endings with 0s if number is too small
### 4. add the digits onto chinese seedphase index, one-to-one
### 5. convert the indexes into english seedphrase

### References:
### below 2 lists are sourced from : https://github.com/bitcoin/bips/tree/master/bip-0039
### as of 8-Apr-2024

### TESTS
### 
### ------ without passcode ------
### 
### % python bip39_translate_cn2en_v3.py -c
### Please choose your length of target seed phrases (e.g. 12, 24, etc. default 24):
### Using default length: 24!
### Please choose your way to combine code and generate seed phrases (0 for simply add up, or 1 for bit-wise reverse add [bit-wise mod 2048]. default 1):
### Using combining mode: 1!
### Please type in your 23 Chinese characters (It will only take first 23 if too long. It will repeat from beginning if too short.)
### ===>秦朝（前221年—前207年），是中国历史上第一个统一的封建王朝，前身是春秋战国时期的秦国
### Please enter a pass code:	E.g. 12354, or A1123xx$#@, etc.
### It can be in any length (empty for not using this code), can be any type-able ascii characters (except leading or ending spaces), and it is case sensitive!!!
### Please remember this code - without this code you will never be able to retrieve the target passphrase!!!
### ===>
### ########################
### {'）', '（', '2', '，', '—', '7', '1', '0'} is not in the list of the 2048 Chinese characters. They are REMOVED from the phrase generation!!!
### Auto-generated checksum last_word is: aisle, 过
### Effective Chinese input is:[len:23]: 秦朝前年前年是中国历史上第一个统一的封建王朝前
### Chinese indexes:
### 	[1112, 577, 114, 38, 114, 38, 2, 10, 15, 427, 420, 13, 154, 1, 14, 222, 1, 0, 552, 167, 460, 577, 114]
### SHA256ed-to-Base2048 of passcode '' is (len:(24)):
### 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
### 	SHA256 hash: 0.
### English passphrase indexes:
### 	[1112, 577, 114, 38, 114, 38, 2, 10, 15, 427, 420, 13, 154, 1, 14, 222, 1, 0, 552, 167, 460, 577, 114]
### ########################
### Your passphrase [len:24]:
### mention else atom age atom age able access acid cube cruel accuse battle ability achieve bridge ability abandon eagle belt define else atom aisle
### {1: 'mention', 2: 'else', 3: 'atom', 4: 'age', 5: 'atom', 6: 'age', 7: 'able', 8: 'access', 9: 'acid', 10: 'cube', 11: 'cruel', 12: 'accuse', 13: 'battle', 14: 'ability', 15: 'achieve', 16: 'bridge', 17: 'ability', 18: 'abandon', 19: 'eagle', 20: 'belt', 21: 'define', 22: 'else', 23: 'atom', 24: 'aisle'}
### 
### ------ with passcode [mode 1]------
### 
### % python bip39_translate_cn2en_v3.py -c
### Please choose your length of target seed phrases (e.g. 12, 24, etc. default 24):
### Using default length: 24!
### Please choose your way to combine code and generate seed phrases (0 for simply add up, or 1 for bit-wise reverse add [bit-wise mod 2048]. default 1):
### Using combining mode: 1!
### Please type in your 23 Chinese characters (It will only take first 23 if too long. It will repeat from beginning if too short.)
### ===>秦朝（前221年—前207年），是中国历史上第一个统一的封建王朝，前身是春秋战国时期的秦国
### Please enter a pass code:	E.g. 12354, or A1123xx$#@, etc.
### It can be in any length (empty for not using this code), can be any type-able ascii characters (except leading or ending spaces), and it is case sensitive!!!
### Please remember this code - without this code you will never be able to retrieve the target passphrase!!!
### ===>123
### CODE: hashlib.sha256("123".encode("utf-8")).hexdigest() ==> for passcode: "123" is: "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
### CODE: int("a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 16) ==> for decimal value of the hex a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3 is : 75263518707598184987916378021939673586055614731957507592904438851787542395619
### Converted into base2048 value in reverse_order:True is :
### [739, 1103, 2014, 891, 232, 1331, 31, 253, 2047, 999, 296, 1104, 1275, 1976, 507, 579, 382, 936, 190, 33, 1426, 840, 409, 5]
### ########################
### {'1', '）', '7', '2', '—', '0', '（', '，'} is not in the list of the 2048 Chinese characters. They are REMOVED from the phrase generation!!!
### Auto-generated checksum last_word is: around, 从
### Effective Chinese input is:[len:23]: 秦朝前年前年是中国历史上第一个统一的封建王朝前
### Chinese indexes:
### 	[1112, 577, 114, 38, 114, 38, 2, 10, 15, 427, 420, 13, 154, 1, 14, 222, 1, 0, 552, 167, 460, 577, 114]
### SHA256ed-to-Base2048 of passcode '123' is (len:(24)):
### 	[739, 1103, 2014, 891, 232, 1331, 31, 253, 2047, 999, 296, 1104, 1275, 1976, 507, 579, 382, 936, 190, 33, 1426, 840, 409, 5]
### 	SHA256 hash: 75263518707598184987916378021939673586055614731957507592904438851787542395619.
### English passphrase indexes:
### 	[1851, 1680, 80, 929, 346, 1369, 33, 263, 14, 1426, 716, 1117, 1429, 1977, 521, 801, 383, 936, 742, 200, 1886, 1417, 523]
### ########################
### Your passphrase [len:24]:
### trash spirit anxiety injury clip private aerobic can achieve rather flower merry razor warm donkey goddess copper insect fresh boil type raise door around
### {1: 'trash', 2: 'spirit', 3: 'anxiety', 4: 'injury', 5: 'clip', 6: 'private', 7: 'aerobic', 8: 'can', 9: 'achieve', 10: 'rather', 11: 'flower', 12: 'merry', 13: 'razor', 14: 'warm', 15: 'donkey', 16: 'goddess', 17: 'copper', 18: 'insect', 19: 'fresh', 20: 'boil', 21: 'type', 22: 'raise', 23: 'door', 24: 'around'}
### ### 
### ### ------ with passcode [mode 0]------
### ### 
### % python bip39_translate_cn2en_v3.py -c
### Please choose your length of target seed phrases (e.g. 12, 24, etc. default 24):
### Using default length: 24!
### Please choose your way to combine code and generate seed phrases (0 for simply add up, or 1 for bit-wise reverse add [bit-wise mod 2048]. default 1):0
### Received input of combining mode: 0!
### Please type in your 23 Chinese characters (It will only take first 23 if too long. It will repeat from beginning if too short.)
### ===>秦朝（前221年—前207年），是中国历史上第一个统一的封建王朝，前身是春秋战国时期的秦国
### Please enter a pass code:	E.g. 12354, or A1123xx$#@, etc.
### It can be in any length (empty for not using this code), can be any type-able ascii characters (except leading or ending spaces), and it is case sensitive!!!
### Please remember this code - without this code you will never be able to retrieve the target passphrase!!!
### ===>123
### CODE: hashlib.sha256("123".encode("utf-8")).hexdigest() ==> for passcode: "123" is: "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
### CODE: int("a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 16) ==> for decimal value of the hex a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3 is : 75263518707598184987916378021939673586055614731957507592904438851787542395619
### Converted into base2048 value in reverse_order:True is :
### [739, 1103, 2014, 891, 232, 1331, 31, 253, 2047, 999, 296, 1104, 1275, 1976, 507, 579, 382, 936, 190, 33, 1426, 840, 409, 5]
### ########################
### {'1', '（', '）', '—', '，', '7', '0', '2'} is not in the list of the 2048 Chinese characters. They are REMOVED from the phrase generation!!!
### Auto-generated checksum last_word is: bus, 被
### Effective Chinese input is:[len:23]: 秦朝前年前年是中国历史上第一个统一的封建王朝前
### Chinese indexes:
### 	[1112, 577, 114, 38, 114, 38, 2, 10, 15, 427, 420, 13, 154, 1, 14, 222, 1, 0, 552, 167, 460, 577, 114]
### SHA256ed-to-Base2048 of passcode '123' is (len:(24)):
### 	[739, 1103, 2014, 891, 232, 1331, 31, 253, 2047, 999, 296, 1104, 1275, 1976, 507, 579, 382, 936, 190, 33, 1426, 840, 409, 5]
### 	SHA256 hash: 75263518707598184987916378021939673586055614731957507592904438851787542395619.
### English passphrase indexes:
### 	[1521, 1417, 1540, 71, 304, 974, 384, 589, 523, 355, 1695, 1117, 450, 1001, 13, 475, 32, 1331, 784, 1059, 426, 1680, 853]
### ########################
### Your passphrase [len:24]:
### sail raise scene angry champion keep copy endless door cluster stadium merry debate large accuse derive advice please ginger love crystal spirit height bus
### {1: 'sail', 2: 'raise', 3: 'scene', 4: 'angry', 5: 'champion', 6: 'keep', 7: 'copy', 8: 'endless', 9: 'door', 10: 'cluster', 11: 'stadium', 12: 'merry', 13: 'debate', 14: 'large', 15: 'accuse', 16: 'derive', 17: 'advice', 18: 'please', 19: 'ginger', 20: 'love', 21: 'crystal', 22: 'spirit', 23: 'height', 24: 'bus'}


import os
import sys
import hashlib

CHINESE_SIMPLIFIED_STRING = '''的 一 是 在 不 了 有 和 人 这 中 大 为 上 个 国 我 以 要 他 时 来 用 们 生 到 作 地 于 出 就 分 对 成 会 可 主 发 年 动 同 工 也 能 下 过 子 说 产 种 面 而 方 后 多 定 行 学 法 所 民 得 经 十 三 之 进 着 等 部 度 家 电 力 里 如 水 化 高 自 二 理 起 小 物 现 实 加 量 都 两 体 制 机 当 使 点 从 业 本 去 把 性 好 应 开 它 合 还 因 由 其 些 然 前 外 天 政 四 日 那 社 义 事 平 形 相 全 表 间 样 与 关 各 重 新 线 内 数 正 心 反 你 明 看 原 又 么 利 比 或 但 质 气 第 向 道 命 此 变 条 只 没 结 解 问 意 建 月 公 无 系 军 很 情 者 最 立 代 想 已 通 并 提 直 题 党 程 展 五 果 料 象 员 革 位 入 常 文 总 次 品 式 活 设 及 管 特 件 长 求 老 头 基 资 边 流 路 级 少 图 山 统 接 知 较 将 组 见 计 别 她 手 角 期 根 论 运 农 指 几 九 区 强 放 决 西 被 干 做 必 战 先 回 则 任 取 据 处 队 南 给 色 光 门 即 保 治 北 造 百 规 热 领 七 海 口 东 导 器 压 志 世 金 增 争 济 阶 油 思 术 极 交 受 联 什 认 六 共 权 收 证 改 清 美 再 采 转 更 单 风 切 打 白 教 速 花 带 安 场 身 车 例 真 务 具 万 每 目 至 达 走 积 示 议 声 报 斗 完 类 八 离 华 名 确 才 科 张 信 马 节 话 米 整 空 元 况 今 集 温 传 土 许 步 群 广 石 记 需 段 研 界 拉 林 律 叫 且 究 观 越 织 装 影 算 低 持 音 众 书 布 复 容 儿 须 际 商 非 验 连 断 深 难 近 矿 千 周 委 素 技 备 半 办 青 省 列 习 响 约 支 般 史 感 劳 便 团 往 酸 历 市 克 何 除 消 构 府 称 太 准 精 值 号 率 族 维 划 选 标 写 存 候 毛 亲 快 效 斯 院 查 江 型 眼 王 按 格 养 易 置 派 层 片 始 却 专 状 育 厂 京 识 适 属 圆 包 火 住 调 满 县 局 照 参 红 细 引 听 该 铁 价 严 首 底 液 官 德 随 病 苏 失 尔 死 讲 配 女 黄 推 显 谈 罪 神 艺 呢 席 含 企 望 密 批 营 项 防 举 球 英 氧 势 告 李 台 落 木 帮 轮 破 亚 师 围 注 远 字 材 排 供 河 态 封 另 施 减 树 溶 怎 止 案 言 士 均 武 固 叶 鱼 波 视 仅 费 紧 爱 左 章 早 朝 害 续 轻 服 试 食 充 兵 源 判 护 司 足 某 练 差 致 板 田 降 黑 犯 负 击 范 继 兴 似 余 坚 曲 输 修 故 城 夫 够 送 笔 船 占 右 财 吃 富 春 职 觉 汉 画 功 巴 跟 虽 杂 飞 检 吸 助 升 阳 互 初 创 抗 考 投 坏 策 古 径 换 未 跑 留 钢 曾 端 责 站 简 述 钱 副 尽 帝 射 草 冲 承 独 令 限 阿 宣 环 双 请 超 微 让 控 州 良 轴 找 否 纪 益 依 优 顶 础 载 倒 房 突 坐 粉 敌 略 客 袁 冷 胜 绝 析 块 剂 测 丝 协 诉 念 陈 仍 罗 盐 友 洋 错 苦 夜 刑 移 频 逐 靠 混 母 短 皮 终 聚 汽 村 云 哪 既 距 卫 停 烈 央 察 烧 迅 境 若 印 洲 刻 括 激 孔 搞 甚 室 待 核 校 散 侵 吧 甲 游 久 菜 味 旧 模 湖 货 损 预 阻 毫 普 稳 乙 妈 植 息 扩 银 语 挥 酒 守 拿 序 纸 医 缺 雨 吗 针 刘 啊 急 唱 误 训 愿 审 附 获 茶 鲜 粮 斤 孩 脱 硫 肥 善 龙 演 父 渐 血 欢 械 掌 歌 沙 刚 攻 谓 盾 讨 晚 粒 乱 燃 矛 乎 杀 药 宁 鲁 贵 钟 煤 读 班 伯 香 介 迫 句 丰 培 握 兰 担 弦 蛋 沉 假 穿 执 答 乐 谁 顺 烟 缩 征 脸 喜 松 脚 困 异 免 背 星 福 买 染 井 概 慢 怕 磁 倍 祖 皇 促 静 补 评 翻 肉 践 尼 衣 宽 扬 棉 希 伤 操 垂 秋 宜 氢 套 督 振 架 亮 末 宪 庆 编 牛 触 映 雷 销 诗 座 居 抓 裂 胞 呼 娘 景 威 绿 晶 厚 盟 衡 鸡 孙 延 危 胶 屋 乡 临 陆 顾 掉 呀 灯 岁 措 束 耐 剧 玉 赵 跳 哥 季 课 凯 胡 额 款 绍 卷 齐 伟 蒸 殖 永 宗 苗 川 炉 岩 弱 零 杨 奏 沿 露 杆 探 滑 镇 饭 浓 航 怀 赶 库 夺 伊 灵 税 途 灭 赛 归 召 鼓 播 盘 裁 险 康 唯 录 菌 纯 借 糖 盖 横 符 私 努 堂 域 枪 润 幅 哈 竟 熟 虫 泽 脑 壤 碳 欧 遍 侧 寨 敢 彻 虑 斜 薄 庭 纳 弹 饲 伸 折 麦 湿 暗 荷 瓦 塞 床 筑 恶 户 访 塔 奇 透 梁 刀 旋 迹 卡 氯 遇 份 毒 泥 退 洗 摆 灰 彩 卖 耗 夏 择 忙 铜 献 硬 予 繁 圈 雪 函 亦 抽 篇 阵 阴 丁 尺 追 堆 雄 迎 泛 爸 楼 避 谋 吨 野 猪 旗 累 偏 典 馆 索 秦 脂 潮 爷 豆 忽 托 惊 塑 遗 愈 朱 替 纤 粗 倾 尚 痛 楚 谢 奋 购 磨 君 池 旁 碎 骨 监 捕 弟 暴 割 贯 殊 释 词 亡 壁 顿 宝 午 尘 闻 揭 炮 残 冬 桥 妇 警 综 招 吴 付 浮 遭 徐 您 摇 谷 赞 箱 隔 订 男 吹 园 纷 唐 败 宋 玻 巨 耕 坦 荣 闭 湾 键 凡 驻 锅 救 恩 剥 凝 碱 齿 截 炼 麻 纺 禁 废 盛 版 缓 净 睛 昌 婚 涉 筒 嘴 插 岸 朗 庄 街 藏 姑 贸 腐 奴 啦 惯 乘 伙 恢 匀 纱 扎 辩 耳 彪 臣 亿 璃 抵 脉 秀 萨 俄 网 舞 店 喷 纵 寸 汗 挂 洪 贺 闪 柬 爆 烯 津 稻 墙 软 勇 像 滚 厘 蒙 芳 肯 坡 柱 荡 腿 仪 旅 尾 轧 冰 贡 登 黎 削 钻 勒 逃 障 氨 郭 峰 币 港 伏 轨 亩 毕 擦 莫 刺 浪 秘 援 株 健 售 股 岛 甘 泡 睡 童 铸 汤 阀 休 汇 舍 牧 绕 炸 哲 磷 绩 朋 淡 尖 启 陷 柴 呈 徒 颜 泪 稍 忘 泵 蓝 拖 洞 授 镜 辛 壮 锋 贫 虚 弯 摩 泰 幼 廷 尊 窗 纲 弄 隶 疑 氏 宫 姐 震 瑞 怪 尤 琴 循 描 膜 违 夹 腰 缘 珠 穷 森 枝 竹 沟 催 绳 忆 邦 剩 幸 浆 栏 拥 牙 贮 礼 滤 钠 纹 罢 拍 咱 喊 袖 埃 勤 罚 焦 潜 伍 墨 欲 缝 姓 刊 饱 仿 奖 铝 鬼 丽 跨 默 挖 链 扫 喝 袋 炭 污 幕 诸 弧 励 梅 奶 洁 灾 舟 鉴 苯 讼 抱 毁 懂 寒 智 埔 寄 届 跃 渡 挑 丹 艰 贝 碰 拔 爹 戴 码 梦 芽 熔 赤 渔 哭 敬 颗 奔 铅 仲 虎 稀 妹 乏 珍 申 桌 遵 允 隆 螺 仓 魏 锐 晓 氮 兼 隐 碍 赫 拨 忠 肃 缸 牵 抢 博 巧 壳 兄 杜 讯 诚 碧 祥 柯 页 巡 矩 悲 灌 龄 伦 票 寻 桂 铺 圣 恐 恰 郑 趣 抬 荒 腾 贴 柔 滴 猛 阔 辆 妻 填 撤 储 签 闹 扰 紫 砂 递 戏 吊 陶 伐 喂 疗 瓶 婆 抚 臂 摸 忍 虾 蜡 邻 胸 巩 挤 偶 弃 槽 劲 乳 邓 吉 仁 烂 砖 租 乌 舰 伴 瓜 浅 丙 暂 燥 橡 柳 迷 暖 牌 秧 胆 详 簧 踏 瓷 谱 呆 宾 糊 洛 辉 愤 竞 隙 怒 粘 乃 绪 肩 籍 敏 涂 熙 皆 侦 悬 掘 享 纠 醒 狂 锁 淀 恨 牲 霸 爬 赏 逆 玩 陵 祝 秒 浙 貌 役 彼 悉 鸭 趋 凤 晨 畜 辈 秩 卵 署 梯 炎 滩 棋 驱 筛 峡 冒 啥 寿 译 浸 泉 帽 迟 硅 疆 贷 漏 稿 冠 嫩 胁 芯 牢 叛 蚀 奥 鸣 岭 羊 凭 串 塘 绘 酵 融 盆 锡 庙 筹 冻 辅 摄 袭 筋 拒 僚 旱 钾 鸟 漆 沈 眉 疏 添 棒 穗 硝 韩 逼 扭 侨 凉 挺 碗 栽 炒 杯 患 馏 劝 豪 辽 勃 鸿 旦 吏 拜 狗 埋 辊 掩 饮 搬 骂 辞 勾 扣 估 蒋 绒 雾 丈 朵 姆 拟 宇 辑 陕 雕 偿 蓄 崇 剪 倡 厅 咬 驶 薯 刷 斥 番 赋 奉 佛 浇 漫 曼 扇 钙 桃 扶 仔 返 俗 亏 腔 鞋 棱 覆 框 悄 叔 撞 骗 勘 旺 沸 孤 吐 孟 渠 屈 疾 妙 惜 仰 狠 胀 谐 抛 霉 桑 岗 嘛 衰 盗 渗 脏 赖 涌 甜 曹 阅 肌 哩 厉 烃 纬 毅 昨 伪 症 煮 叹 钉 搭 茎 笼 酷 偷 弓 锥 恒 杰 坑 鼻 翼 纶 叙 狱 逮 罐 络 棚 抑 膨 蔬 寺 骤 穆 冶 枯 册 尸 凸 绅 坯 牺 焰 轰 欣 晋 瘦 御 锭 锦 丧 旬 锻 垄 搜 扑 邀 亭 酯 迈 舒 脆 酶 闲 忧 酚 顽 羽 涨 卸 仗 陪 辟 惩 杭 姚 肚 捉 飘 漂 昆 欺 吾 郎 烷 汁 呵 饰 萧 雅 邮 迁 燕 撒 姻 赴 宴 烦 债 帐 斑 铃 旨 醇 董 饼 雏 姿 拌 傅 腹 妥 揉 贤 拆 歪 葡 胺 丢 浩 徽 昂 垫 挡 览 贪 慰 缴 汪 慌 冯 诺 姜 谊 凶 劣 诬 耀 昏 躺 盈 骑 乔 溪 丛 卢 抹 闷 咨 刮 驾 缆 悟 摘 铒 掷 颇 幻 柄 惠 惨 佳 仇 腊 窝 涤 剑 瞧 堡 泼 葱 罩 霍 捞 胎 苍 滨 俩 捅 湘 砍 霞 邵 萄 疯 淮 遂 熊 粪 烘 宿 档 戈 驳 嫂 裕 徙 箭 捐 肠 撑 晒 辨 殿 莲 摊 搅 酱 屏 疫 哀 蔡 堵 沫 皱 畅 叠 阁 莱 敲 辖 钩 痕 坝 巷 饿 祸 丘 玄 溜 曰 逻 彭 尝 卿 妨 艇 吞 韦 怨 矮 歇'''
ENGLISH_STRING = '''abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual adapt add addict address adjust admit adult advance advice aerobic affair afford afraid again age agent agree ahead aim air airport aisle alarm album alcohol alert alien all alley allow almost alone alpha already also alter always amateur amazing among amount amused analyst anchor ancient anger angle angry animal ankle announce annual another answer antenna antique anxiety any apart apology appear apple approve april arch arctic area arena argue arm armed armor army around arrange arrest arrive arrow art artefact artist artwork ask aspect assault asset assist assume asthma athlete atom attack attend attitude attract auction audit august aunt author auto autumn average avocado avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance balcony ball bamboo banana banner bar barely bargain barrel base basic basket battle beach bean beauty because become beef before begin behave behind believe below belt bench benefit best betray better between beyond bicycle bid bike bind biology bird birth bitter black blade blame blanket blast bleak bless blind blood blossom blouse blue blur blush board boat body boil bomb bone bonus book boost border boring borrow boss bottom bounce box boy bracket brain brand brass brave bread breeze brick bridge brief bright bring brisk broccoli broken bronze broom brother brown brush bubble buddy budget buffalo build bulb bulk bullet bundle bunker burden burger burst bus business busy butter buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal cancel candy cannon canoe canvas canyon capable capital captain car carbon card cargo carpet carry cart case cash casino castle casual cat catalog catch category cattle caught cause caution cave ceiling celery cement census century cereal certain chair chalk champion change chaos chapter charge chase chat cheap check cheese chef cherry chest chicken chief child chimney choice choose chronic chuckle chunk churn cigar cinnamon circle citizen city civil claim clap clarify claw clay clean clerk clever click client cliff climb clinic clip clock clog close cloth cloud clown club clump cluster clutch coach coast coconut code coffee coil coin collect color column combine come comfort comic common company concert conduct confirm congress connect consider control convince cook cool copper copy coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard curious current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash daughter dawn day deal debate debris decade december decide decline decorate decrease deer defense define defy degree delay deliver demand demise denial dentist deny depart depend deposit depth deputy derive describe desert design desk despair destroy detail detect develop device devote diagram dial diamond diary dice diesel diet differ digital dignity dilemma dinner dinosaur direct dirt disagree discover disease dish dismiss disorder display distance divert divide divorce dizzy doctor document dog doll dolphin domain donate donkey donor door dose double dove draft dragon drama drastic draw dream dress drift drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf dynamic eager eagle early earn earth easily east easy echo ecology economy edge edit educate effort egg eight either elbow elder electric elegant element elephant elevator elite else embark embody embrace emerge emotion employ empower empty enable enact end endless endorse enemy energy enforce engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence evil evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust exhibit exile exist exit exotic expand expect expire explain expose express extend extra eye eyebrow fabric face faculty fade faint faith fall false fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault favorite feature february federal fee feed feel female fence festival fetch fever few fiber fiction field figure file film filter final find fine finger finish fire firm first fiscal fish fit fitness fix flag flame flash flat flavor flee flight flip float flock floor flower fluid flush fly foam focus fog foil fold follow food foot force forest forget fork fortune forum forward fossil foster found fox fragile frame frequent fresh friend fringe frog front frost frown frozen fruit fuel fun funny furnace fury future gadget gain galaxy gallery game gap garage garbage garden garlic garment gas gasp gate gather gauge gaze general genius genre gentle genuine gesture ghost giant gift giggle ginger giraffe girl give glad glance glare glass glide glimpse globe gloom glory glove glow glue goat goddess gold good goose gorilla gospel gossip govern gown grab grace grain grant grape grass gravity great green grid grief grit grocery group grow grunt guard guess guide guilt guitar gun gym habit hair half hammer hamster hand happy harbor hard harsh harvest hat have hawk hazard head health heart heavy hedgehog height hello helmet help hen hero hidden high hill hint hip hire history hobby hockey hold hole holiday hollow home honey hood hope horn horror horse hospital host hotel hour hover hub huge human humble humor hundred hungry hunt hurdle hurry hurt husband hybrid ice icon idea identify idle ignore ill illegal illness image imitate immense immune impact impose improve impulse inch include income increase index indicate indoor industry infant inflict inform inhale inherit initial inject injury inmate inner innocent input inquiry insane insect inside inspire install intact interest into invest invite involve iron island isolate issue item ivory jacket jaguar jar jazz jealous jeans jelly jewel job join joke journey joy judge juice jump jungle junior junk just kangaroo keen keep ketchup key kick kid kidney kind kingdom kiss kit kitchen kite kitten kiwi knee knife knock know lab label labor ladder lady lake lamp language laptop large later latin laugh laundry lava law lawn lawsuit layer lazy leader leaf learn leave lecture left leg legal legend leisure lemon lend length lens leopard lesson letter level liar liberty library license life lift light like limb limit link lion liquid list little live lizard load loan lobster local lock logic lonely long loop lottery loud lounge love loyal lucky luggage lumber lunar lunch luxury lyrics machine mad magic magnet maid mail main major make mammal man manage mandate mango mansion manual maple marble march margin marine market marriage mask mass master match material math matrix matter maximum maze meadow mean measure meat mechanic medal media melody melt member memory mention menu mercy merge merit merry mesh message metal method middle midnight milk million mimic mind minimum minor minute miracle mirror misery miss mistake mix mixed mixture mobile model modify mom moment monitor monkey monster month moon moral more morning mosquito mother motion motor mountain mouse move movie much muffin mule multiply muscle museum mushroom music must mutual myself mystery myth naive name napkin narrow nasty nation nature near neck need negative neglect neither nephew nerve nest net network neutral never news next nice night noble noise nominee noodle normal north nose notable note nothing notice novel now nuclear number nurse nut oak obey object oblige obscure observe obtain obvious occur ocean october odor off offer office often oil okay old olive olympic omit once one onion online only open opera opinion oppose option orange orbit orchard order ordinary organ orient original orphan ostrich other outdoor outer output outside oval oven over own owner oxygen oyster ozone pact paddle page pair palace palm panda panel panic panther paper parade parent park parrot party pass patch path patient patrol pattern pause pave payment peace peanut pear peasant pelican pen penalty pencil people pepper perfect permit person pet phone photo phrase physical piano picnic picture piece pig pigeon pill pilot pink pioneer pipe pistol pitch pizza place planet plastic plate play please pledge pluck plug plunge poem poet point polar pole police pond pony pool popular portion position possible post potato pottery poverty powder power practice praise predict prefer prepare present pretty prevent price pride primary print priority prison private prize problem process produce profit program project promote proof property prosper protect proud provide public pudding pull pulp pulse pumpkin punch pupil puppy purchase purity purpose purse push put puzzle pyramid quality quantum quarter question quick quit quiz quote rabbit raccoon race rack radar radio rail rain raise rally ramp ranch random range rapid rare rate rather raven raw razor ready real reason rebel rebuild recall receive recipe record recycle reduce reflect reform refuse region regret regular reject relax release relief rely remain remember remind remove render renew rent reopen repair repeat replace report require rescue resemble resist resource response result retire retreat return reunion reveal review reward rhythm rib ribbon rice rich ride ridge rifle right rigid ring riot ripple risk ritual rival river road roast robot robust rocket romance roof rookie room rose rotate rough round route royal rubber rude rug rule run runway rural sad saddle sadness safe sail salad salmon salon salt salute same sample sand satisfy satoshi sauce sausage save say scale scan scare scatter scene scheme school science scissors scorpion scout scrap screen script scrub sea search season seat second secret section security seed seek segment select sell seminar senior sense sentence series service session settle setup seven shadow shaft shallow share shed shell sheriff shield shift shine ship shiver shock shoe shoot shop short shoulder shove shrimp shrug shuffle shy sibling sick side siege sight sign silent silk silly silver similar simple since sing siren sister situate six size skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slogan slot slow slush small smart smile smoke smooth snack snake snap sniff snow soap soccer social sock soda soft solar soldier solid solution solve someone song soon sorry sort soul sound soup source south space spare spatial spawn speak special speed spell spend sphere spice spider spike spin spirit split spoil sponsor spoon sport spot spray spread spring spy square squeeze squirrel stable stadium staff stage stairs stamp stand start state stay steak steel stem step stereo stick still sting stock stomach stone stool story stove strategy street strike strong struggle student stuff stumble style subject submit subway success such sudden suffer sugar suggest suit summer sun sunny sunset super supply supreme sure surface surge surprise surround survey suspect sustain swallow swamp swap swarm swear sweet swift swim swing switch sword symbol symptom syrup system table tackle tag tail talent talk tank tape target task taste tattoo taxi teach team tell ten tenant tennis tent term test text thank that theme then theory there they thing this thought three thrive throw thumb thunder ticket tide tiger tilt timber time tiny tip tired tissue title toast tobacco today toddler toe together toilet token tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise toss total tourist toward tower town toy track trade traffic tragic train transfer trap trash travel tray treat tree trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical ugly umbrella unable unaware uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use used useful useless usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle velvet vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view village vintage violin virtual virus visa visit visual vital vivid vocal voice void volcano volume vote voyage wage wagon wait walk wall walnut want warfare warm warrior wash wasp waste water wave way wealth weapon wear weasel weather web wedding weekend weird welcome west wet whale what wheat wheel when where whip whisper wide width wife wild will win window wine wing wink winner winter wire wisdom wise wish witness wolf woman wonder wood wool word work world worry worth wrap wreck wrestle wrist write wrong yard year yellow you young youth zebra zero zone zoo'''

### CONSTANT LISTS AND DICTS
CN_LIST = CHINESE_SIMPLIFIED_STRING.strip().split(' ')
EN_LIST = ENGLISH_STRING.strip().split(' ')
EN2CN_DICT  = dict(zip(EN_LIST, CN_LIST))
CN2EN_DICT  = dict(zip(CN_LIST, EN_LIST))

NO_OF_WORDS  = -1
if len(CN_LIST) == len(EN_LIST) and len(EN_LIST) == 2048 and len(EN2CN_DICT) == 2048:
    NO_OF_WORDS  = len(CN_LIST)
else:
    raise Exception("The number of CN words is different from the number of EN words, they should be exactly 2048!, please check the code!!!")

### helper functions to convert ascii passcode into a base2048 number using sha256
to2048 = lambda n: ([] if n == 0 else to2048(n // 2048) + [n % 2048]) if n else []
from2048 = lambda s: sum(c * (2048 ** i) for i, c in enumerate(reversed(s)))

def passcode_sha256_to_base_2048(passcode, reverse_order):
    hex_str = hashlib.sha256(passcode.encode('utf-8')).hexdigest()
    print(f'CODE: hashlib.sha256("{passcode}".encode("utf-8")).hexdigest() ==> for passcode: "{passcode}" is: "{hex_str}"')
    decimal_value = int(hex_str, 16)
    print(f'CODE: int("{hex_str}", 16) ==> for decimal value of the hex {hex_str} is : {decimal_value}')

    base_2048_digits = to2048(decimal_value )
    base_2048_digits = ([0] *24 + base_2048_digits)[-24:]     ### Pad with leading zeros at the start

    if reverse_order:
        base_2048_digits.reverse()

    print(f'Converted into base2048 value in reverse_order:{reverse_order} is :\n{base_2048_digits}')
    return base_2048_digits, decimal_value 

### HELPER CLASS
class Bip39Check(object):
    def __init__(self):
        self.radix = 2048
        self.worddict = {}
        self.wordlist = []

        counter = 0

        for w in EN_LIST:
            word = w.strip() if sys.version < '3' else w.strip()
            self.worddict[word] = counter
            self.wordlist.append(word)
            counter = counter + 1

        if(len(self.worddict) != self.radix):
            print(len(self.worddict), self.radix)
            raise ValueError('Expecting %d words, not %d', self.radix, len(self.worddict))

    def _check_size(self, phrase):
        self.size = len(phrase) + 1
        if (self.size % 3 != 0):
            raise ValueError('Expecting 11 or 23 words')

    def _compute_entropy(self, phrase):
        self.entropy = 0
        for w in phrase:
            idx = self.worddict[w]
            self.entropy = (self.entropy << 11) + idx
        return self.entropy

    def _scan(self):
        checksum_bits = self.size // 3
        entropy_size = (self.size * 11 - checksum_bits) // 8 # Fixed entropy string length
        entropy_to_fill = 11 - checksum_bits
        entropy_base = self.entropy << (entropy_to_fill)

        for i in range(0, 2 ** entropy_to_fill):
            entropy_candidate = entropy_base | i
            entropy_str = (entropy_candidate).to_bytes(entropy_size, 'big')
            hash = (hashlib.sha256(entropy_str).digest()[0])
            checksum = hash >> (8 - checksum_bits)
            final_word_idx = (i << checksum_bits) + checksum
            checkword = self.wordlist[final_word_idx]
            return checkword

### seedphrase generator
def generate_seedphrase(effective_code_length, cn_input, passcode_str, bit_wise_add):
    #
    # bit_wise_add: 0/False: simply add up 2 large numbers and mod 2048**23
    #               1/True : reverse the SHA256 numbers (the smallest digit goes first, remove the largest digit - 24th) - bitwise add and mod with 2048
    #
    try:
        cn_char_excluded, cn_char_effective = '', ''
        for s in cn_input:
            if s in CN_LIST:
                cn_char_effective += s
            else:
                cn_char_excluded += s

        cn_char_excluded = set(cn_char_excluded)

        passcode = [0] * effective_code_length   ### set all into 0 as default, so that the_passcode+1 times phrase_number and take the remainder of division over NO_OF_WORDS should be phrase_number itself -> meaning no passcode
        passcode_hash_value = 0
        if passcode_str:
            passcode, passcode_hash_value = passcode_sha256_to_base_2048(passcode_str, True)   ### logic : reverse the base2048 output, take the pcode from smallest digit first
        
        cn_char_effective = (cn_char_effective * effective_code_length)[:effective_code_length] if cn_char_effective else [CN_LIST[0]] * effective_code_length   ### logic : if effective chinese string not available -> use first char, set idx to 0
        cn_idxs = [CN_LIST.index(c) for c in cn_char_effective]

        if not bit_wise_add:
            cn_char_value = from2048(cn_idxs)
            combined_value = cn_char_value + passcode_hash_value
            en_idxs  = to2048(combined_value)
            en_idxs = ([0] * effective_code_length + en_idxs)[-effective_code_length:]
            en_output = [EN_LIST[i] for i in en_idxs]

        else:
            en_output, en_idxs  = [], []
            for i in range(effective_code_length):
                en_idx = ( cn_idxs[i] + passcode[i] ) % NO_OF_WORDS   ### logic : c = (x + p) mod ( NO_OF_WORDS ) ---> c: coded number, x: cn idx number, p: passcode
                en_encoded = EN_LIST[en_idx]
                en_idxs.append(en_idx)
                en_output.append(en_encoded)
        
        ### generate the last checksum code
        m = Bip39Check()
        m._check_size(en_output[:effective_code_length])
        m._compute_entropy(en_output[:effective_code_length])
        last_word = m._scan()
        
        en_output = en_output[:effective_code_length] + [last_word]
        en_indexed_output = dict(zip(range(1, len(en_output)+1), en_output))
        return cn_char_excluded, cn_char_effective, passcode, passcode_hash_value, cn_idxs, en_idxs, en_output, en_indexed_output, last_word

    except Exception as e:
        raise Exception(f"Error in generate_seedphrase: {e}")

### command line main function
def main_cli():
    cn_length_input = input(f'Please choose your length of target seed phrases (e.g. 12, 24, etc. default 24):')
    if cn_length_input.isnumeric():
        cn_length = int(cn_length_input)
        print(f'Received input of target length: {cn_length}!')
    else:
        cn_length = 24
        print(f'Using default length: {cn_length}!')

    bit_wise_add_input = input(f'Please choose your way to combine code and generate seed phrases (0 for simply add up, or 1 for bit-wise reverse add [bit-wise mod 2048]. default 1):')
    if bit_wise_add_input.isnumeric() and int(bit_wise_add_input) in [0,1]:
        bit_wise_add = int(bit_wise_add_input)
        print(f'Received input of combining mode: {bit_wise_add}!')
    else:
        bit_wise_add = 1
        print(f'Using combining mode: {bit_wise_add}!')

    ### last word of the seed phrase are generated automatically - so the effective length is l - 1, e.g. 24 -> 23
    effective_code_length = cn_length - 1
    cn_input = input(f'Please type in your {effective_code_length} Chinese characters (It will only take first {effective_code_length} if too long. It will repeat from beginning if too short.)\n===>')
    passcode_str_raw = input(f'Please enter a pass code:\tE.g. 12354, or A1123xx$#@, etc.\nIt can be in any length (empty for not using this code), can be any type-able ascii characters (except leading or ending spaces), and it is case sensitive!!!\nPlease remember this code - without this code you will never be able to retrieve the target passphrase!!!\n===>')
    passcode_str = passcode_str_raw.strip()

    cn_char_excluded, cn_char_effective, passcode, passcode_hash_value, cn_idxs, en_idxs, en_output, en_indexed_output, last_word = generate_seedphrase(effective_code_length, cn_input, passcode_str, bit_wise_add)

    print("#"*24)
    if cn_char_excluded:
        print(f"{cn_char_excluded} is not in the list of the 2048 Chinese characters. They are REMOVED from the phrase generation!!!")
    print(f'Auto-generated checksum last_word is: {last_word}, {EN2CN_DICT[last_word]}')
    print(f"Effective Chinese input is:[len:{len(cn_char_effective)}]: {''.join(cn_char_effective)}")
    print(f"Chinese indexes:\n\t{cn_idxs}")
    print(f"SHA256ed-to-Base2048 of passcode '{passcode_str}' is (len:({len(en_output)})):\n\t{passcode}, \n\tSHA256 hash: {passcode_hash_value}.")
    print(f"English passphrase indexes:\n\t{en_idxs}")
    print("#"*24)
    print(f"Your passphrase [len:{len(en_output)}]:\n{' '.join(en_output)}\n{en_indexed_output}")

### tkinter ui main function
def main_ui():
    import tkinter as tk
    def generate_output():
        cn_input_raw = entry1.get()
        passcode_str_raw = entry2.get()
        seed_length = seedphrase_length.get()
        bit_wise_add = {"BitWiseReverseAddnMod":1, "SimplyAddUp":0}[bit_wise_add_option.get()]

        cn_input = cn_input_raw.strip()
        passcode_str = passcode_str_raw.strip()
        effective_code_length = int(seed_length) - 1
        cn_char_excluded, cn_char_effective, passcode, passcode_hash_value, cn_idxs, en_idxs, en_output, en_indexed_output, last_word = generate_seedphrase(effective_code_length, cn_input, passcode_str, bit_wise_add)
    
        output1.config(state="normal")
        output2.config(state="normal")
        output3.config(state="normal")

        output1.delete(1.0, tk.END)
        output2.delete(1.0, tk.END)
        output3.delete(1.0, tk.END)
    
        output1.insert(tk.END, f"{''.join(cn_char_effective)}")
        output2.insert(tk.END, f"{' '.join(en_output)}")
        output3.insert(tk.END, f"{en_indexed_output}")

        output1.config(state="disabled")
        output2.config(state="disabled")
        output3.config(state="disabled")
    
    root = tk.Tk()
    root.title("Semaj's SeedPhrase Generator")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=2)
    root.grid_rowconfigure(3, weight=2)
    root.grid_columnconfigure(0, weight=1)
    
    label1 = tk.Label(root, text="Please input your Chinese Phrases here", font=("Arial", 12), anchor='w')
    entry1 = tk.Entry(root, font=("Arial", 14))
    label2 = tk.Label(root, text="Please input your passcode here, it can be empty or any ascii code except space", font=("Arial", 12), anchor='w')
    entry2 = tk.Entry(root, font=("Arial", 14))
    
    label1.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    entry1.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    label2.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    entry2.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    
    seedphrase_length = tk.StringVar(root)
    seedphrase_length.set("24")
    dropdown = tk.OptionMenu(root, seedphrase_length, "12", "24")
    dropdown.config(font=("Arial", 14))
    dropdown.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    bit_wise_add_option = tk.StringVar(root)
    bit_wise_add_option.set("BitWiseReverseAddnMod")
    dropdown2 = tk.OptionMenu(root, bit_wise_add_option, "BitWiseReverseAddnMod", "SimplyAddUp")
    dropdown2.config(font=("Arial", 14))
    dropdown2.grid(row=4, column=0, sticky="e", padx=10, pady=5)
    
    generate_button = tk.Button(root, text="Generate Seed Phrase", font=("Arial", 16), command=generate_output)
    generate_button.grid(row=6, column=0, sticky="ew", padx=10, pady=10)
    
    output1 = tk.Text(root, height=2, wrap="word", font=("Arial", 12))
    output2 = tk.Text(root, height=3, wrap="word", font=("Arial", 12))
    output3 = tk.Text(root, height=4, wrap="word", font=("Arial", 12))
    
    label3 = tk.Label(root, text="Your input:", font=("Arial", 12), anchor='w')
    label4 = tk.Label(root, text="Your Seed Phrase - Please keep them secure!!!", font=("Arial", 12), anchor='w')

    label3.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
    output1.grid(row=8, column=0, sticky="ew", padx=10, pady=5)
    label4.grid(row=9, column=0, sticky="ew", padx=10, pady=5)
    output2.grid(row=10, column=0, sticky="ew", padx=10, pady=5)
    output3.grid(row=11, column=0, sticky="ew", padx=10, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and '-c' in sys.argv[1:]:
        main_cli()
    else:
        main_ui()
        main_ui()

###
### Python CLI TEST:
### >>> from bip39_translate_cn2en_v3 import *
### >>> from hashlib import *
### >>> w = '秦朝前年前年是中国历史上第一个统一的封建王朝前'
### >>> n = from2048([CN_LIST.index(i) for i in w])
### >>> m = int(sha256(b'123').hexdigest(),16)
### >>> [EN_LIST[i] for i in to2048(m+n)[-23:]]
### ['sail', 'raise', 'scene', 'angry', 'champion', 'keep', 'copy', 'endless', 'door', 'cluster', 'stadium', 'merry', 'debate', 'large', 'accuse', 'derive', 'advice', 'please', 'ginger', 'love', 'crystal', 'spirit', 'height']
### >>> [EN_LIST[k] for k in [(i+j)%2048 for i,j in zip(to2048(n),to2048(m)[-23:][::-1])]]
### ['trash', 'spirit', 'anxiety', 'injury', 'clip', 'private', 'aerobic', 'can', 'achieve', 'rather', 'flower', 'merry', 'razor', 'warm', 'donkey', 'goddess', 'copper', 'insect', 'fresh', 'boil', 'type', 'raise', 'door']
###
