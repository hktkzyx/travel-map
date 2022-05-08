import pandas as pd
import pytest


@pytest.fixture
def csvfile_example(tmp_path):
    records = pd.DataFrame({
        '城市': ['北京', '上海', '武汉', '香港'], '组': ['旅行', '旅行', '居住', '中转']
    })
    csvpath = tmp_path / 'travelled_cities.csv'
    records.to_csv(csvpath)
    yield csvpath
    csvpath.unlink()
