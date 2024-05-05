import plotly.figure_factory as ff # type: ignore
from datetime import datetime

# 任务数据
tasks = [
    {"Task": "make literature matrix", "Start": datetime(2024, 4, 29), "Finish": datetime(2024, 6, 2)},
    {"Task": "read 2 papers", "Start": datetime(2024, 4, 29), "Finish": datetime(2024, 5, 5)},
    {"Task": "read 3 papers", "Start": datetime(2024, 5, 6), "Finish": datetime(2024, 5, 12)},
    {"Task": "read 3 papers", "Start": datetime(2024, 5, 13), "Finish": datetime(2024, 5, 19)},
    {"Task": "read 2 papers", "Start": datetime(2024, 5, 20), "Finish": datetime(2024, 5, 26)},
    {"Task": "read 3 papers", "Start": datetime(2024, 5, 27), "Finish": datetime(2024, 6, 2)},
    {"Task": "Outline project plan", "Start": datetime(2024, 4, 29), "Finish": datetime(2024, 5, 15)},
    {"Task": "write review and technical details", "Start": datetime(2024, 6, 10), "Finish": datetime(2024, 6, 16)},
    {"Task": "Data Acquisition and Preprocessing", "Start": datetime(2024, 6, 17), "Finish": datetime(2024, 6, 30)},
    {"Task": "Model Selection and Design", "Start": datetime(2024, 7, 1), "Finish": datetime(2024, 7, 14)},
    {"Task": "Dataset Splitting and Training", "Start": datetime(2024, 7, 15), "Finish": datetime(2024, 7, 28)},
    {"Task": "Model Evaluation", "Start": datetime(2024, 7, 29), "Finish": datetime(2024, 8, 11)},
    {"Task": "Results Interpretation and Analysis", "Start": datetime(2024, 8, 12), "Finish": datetime(2024, 8, 18)},
    {"Task": "write dissertation", "Start": datetime(2024, 8, 19), "Finish": datetime(2024, 9, 5)}
]

morandi_colors = [
    "rgb(255, 176, 122)",
    "rgb(255, 204, 170)",
    "rgb(255, 230, 180)",
    "rgb(255, 249, 196)",
    "rgb(195, 230, 203)",
    "rgb(159, 214, 213)",
    "rgb(130, 204, 221)",
    "rgb(99, 191, 219)",
    "rgb(66, 163, 220)",
    "rgb(49, 133, 214)",
    "rgb(34, 103, 190)",
    "rgb(31, 65, 109)",
    "rgb(127, 113, 109)",
    "rgb(127, 127, 127)"
]

# 使用figure_factory创建甘特图
fig = ff.create_gantt(tasks, index_col="Task", colors=morandi_colors,show_colorbar=True, group_tasks=True)




# 设置布局
fig.update_layout(
    title="SIQI BIAN_Gantt Chart",
    xaxis=dict(title="Date"),
    yaxis=dict(title="Tasks")
)

# 保存图形到本地
fig.write_image("gantt_chart_plotly.png", width=1000, height=600, scale=2)

# 显示图形
fig.show()
