from datetime import datetime
from time import gmtime, strftime


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
