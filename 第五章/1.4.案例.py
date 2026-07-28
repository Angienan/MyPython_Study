import pandas as pd
import matplotlib.pyplot as plt

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']


def load_data(filepath: str) -> pd.DataFrame:
    """加载 CSV 数据并预处理：提取年份列"""
    data = pd.read_csv(filepath, usecols=['电影名称', '上映日期', '评分', '原始语言'])
    # 从上映日期中提取年份（取前 4 个字符）
    data['年份'] = pd.to_numeric(data['上映日期'].str[:4], errors='coerce')
    return data


def plot_yearly_movies(ax, data: pd.DataFrame):
    """图1：折线图 - 每年上映电影数量"""
    year_count = data.groupby('年份')['年份'].count()
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = list(range(min_year, max_year + 1))
    y = [int(year_count.get(i, 0)) for i in x]

    ax.plot(x, y, color='green')
    ax.set_title('每年电影数量', fontsize=18)
    ax.set_xlabel('年份', fontsize=15)
    ax.set_ylabel('电影数量', fontsize=15)
    ax.set_xticks(x[::8])
    ax.grid()


def plot_language_distribution(ax, data: pd.DataFrame):
    """图2：柱状图 - 电影语言分布"""
    language_count = data.groupby('原始语言')['原始语言'].count().sort_values(ascending=False)
    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()

    ax.bar(x_language, y_language, color='green', width=0.7)
    ax.set_title('电影语言数量', fontsize=18)
    ax.set_xlabel('语言', fontsize=15)
    ax.set_ylabel('数量', fontsize=15)
    ax.tick_params(axis='x')
    ax.grid()


def plot_score_distribution(ax, data: pd.DataFrame):
    """图3：饼图 - 评分分布（保留 1 位小数）"""
    score_count = data['评分'].round(1).value_counts().sort_index()
    scores = score_count.index.tolist()
    counts_values = score_count.values.tolist()

    ax.pie(counts_values, labels=scores, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.set_title('电影评分分布', fontsize=18)
    ax.legend()


def main():
    # 创建画布与子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('电影榜单数据', fontsize=23)

    # 加载数据
    data = load_data('data/电影表单.csv')

    # 绘制三张图（第四个子图留空）
    plot_yearly_movies(axes[0, 0], data)
    plot_language_distribution(axes[0, 1], data)
    plot_score_distribution(axes[1, 1], data)

    # 隐藏空白子图
    axes[1, 0].set_visible(False)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
