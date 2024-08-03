from datetime import datetime, timedelta
from time import gmtime, strftime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import random

from bot.config import IMG_PATH


def conv_str_to_datetime(full_date: str) -> str:
    _date = full_date[full_date.find('[') + 1:full_date.find(']')]
    _time = full_date[full_date.find(']') + 1:]
    _date = list(map(int, _date.split('-')))
    _time = list(map(int, _time.split(':')))

    utc_0 = list(map(int, strftime('%Y-%m-%d-%H-%M', gmtime()).split('-')))
    utc_x = list(map(int, datetime.now().strftime('%Y-%m-%d-%H-%M').split('-')))
    date_utc_0 = datetime(*utc_0)
    date_utc_x = datetime(*utc_x)
    utc_delta = date_utc_x - date_utc_0

    full_date = datetime(*_date, *_time)
    res_date = full_date - utc_delta
    res_date = f'{res_date.strftime("%Y-%m-%d")}T{res_date.strftime("%H:%M:%S")}.000Z'

    return res_date


def conv_str_to_seconds(time: str) -> int:
    hh, mm = list(map(int, time.split(':')))
    ss = mm * 60 + hh * 3600
    return ss


def create_plot(tg_id: int, events: list[dict]):
    colors = {}
    unique_events = list(set(event['title'] for event in events))
    for event in unique_events:
        colors[event] = "#%06x" % random.randint(0, 0xFFFFFF)

    fig, ax = plt.subplots(figsize=(12, 6))

    dates_sorted = sorted([event['date_start'] for event in events])
    dates_start = dates_sorted[0]
    dates_end = dates_sorted[-1]
    if (dates_end - dates_start).days < 10:
        dates_start = dates_end - timedelta(days=12)
    dates = list(map(lambda x: x.date(), pd.date_range(start=dates_start, end=dates_end)))

    date_to_index = {date: index for index, date in enumerate(dates)}

    bar_height = 0.95
    for event in events:
        start_time = event["date_start"]
        end_time = start_time + timedelta(seconds=event["duration"])

        date_index = date_to_index[start_time.date()]

        ax.barh(date_index, (end_time - start_time).total_seconds() / 3600,
                left=start_time.hour + start_time.minute / 60, align='center',
                edgecolor='black', color=colors[event["title"]], height=bar_height)

    ax.set_xlim(0, 24)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):02d}:00'))

    ax.set_yticks(list(date_to_index.values()))
    ax.set_yticklabels([date.strftime('%d-%m-%Y') for date in dates])

    ax.set_ylim(-0.5, len(dates) - 0.5)

    ax.set_xlabel('Время дня')
    ax.set_ylabel('Дата')
    ax.set_title('Диаграмма событий')

    legend_handles = [plt.Line2D([0], [0], color=colors[name], lw=4) for name in unique_events]
    ax.legend(legend_handles, unique_events, title="События")

    plt.xticks(rotation=45)

    ax.invert_yaxis()

    plt.grid(True, 'minor', 'both')
    plt.grid(True, 'major', 'x')
    ax.yaxis.set_minor_locator(mdates.HourLocator(byhour=None, interval=12, tz=None))

    plt.tight_layout()
    plt.savefig(f'{IMG_PATH}/{tg_id}.png')
