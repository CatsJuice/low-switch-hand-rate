# low-switch-hand-rate
Python对低换手率股票在脱离低换手率后股价的分析


分析**连续处于低换手率**的股票， 脱离低换手率后， 出现**连续处于高换手率**， 判断2个时期的**收盘价**均价， 分析满足这一特征的股票的价格是否会上涨；

程序设计的思路如下
- 迭代日线数据文件
- 判断是否是连续高换手率
- 判断是否在连续高换手率后出现连续低换手率
- 结果展示

**注:** 因为数据文件是按日期的倒序排序的， 所以分析迭代时， 先判断是否出现连续高换手率

核心代码如下：
```
high = []
low = []
for row in arr:
    rate = row[10]
    if rate == "None":
        high = []
        low = []
        continue
    if rate == 0:
        if len(high) >= self.min_days and len(low) >= self.min_days:
            dic = {'high': high, 'low': low}
            self.res.append(dic)
            high = []
            low = []
        continue
    rate = float(rate)
    # 4. 判断是否是 高 换手率
    if rate >= self.border_rate:   
        # 4.3 判断是否是: 连续高 ->连续低 -> 结束连续低
        if len(low) >= self.min_days:
            # 符合条件， 写入
            dic = {'high': high, 'low': low}
            self.res.append(dic)
            high = []
            low = []
        elif len(low) > 0:      # 连续低中有值
            # 不满足连续 低， 重置
            high = []
            low = []
        high.append(row)
    elif len(high) < self.min_days:     # 是低换手率， 判断是否前面是连续高换手率
        # 4.1 前面不是连续的高换手率， 重置高换手率数组
        high = []
    else:
        # 4.2 前面是连续高换手率， 地换手率写入
        low.append(row)
    
    # 判断日期是否已达到最后
    if row[0] <= self.end_date:
        # 判断是否满足条件
        if len(high) >= self.min_days and len(low) >= self.min_days:
            dic = {'high': high, 'low': low}
            self.res.append(dic)
            high = []
            low = []
        break
```

简易流程图如下：

![流程图](https://catsjuice.cn/index/src/markdown/stock/mind201905012008.jpg "换手率程序设计流程图")


## **下载**
- 直接下载`.zip`文件
- `git clone https://github.com/CatsJuice/low-switch-hand-rate.git`

## **使用前提**
- Python 3.x
- 第三方库支持
    - `tqdm`
    - `pandas`
    - `os`

## **使用**
自定义`main`中的参数， 参数说明如下

No | param | type | meaning | demo
:--:|:--:|:--: |:--: |:--:
1 | `file_path_prefix` | `str` | 日线数据目录前缀 | `'F:\\files\\sharesDatas\\kline\\'`
2 | `min_days` |  `int` | 最小连续天数 | `10`
3 | `border_rate` | `float` | 换手率高低边界 | `2`
4 | `end_date` | `str` | 统计的最早日期 | `'2018-12-28'`
