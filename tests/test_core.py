import numpy as np
import pandas as pd
import pytest

from travel_map import core


@pytest.fixture
def csvfile_example(tmp_path):
    records = pd.DataFrame({
        '城市': ['北京', '上海', '武汉', '香港'], '组': ['旅行', '旅行', '居住', '中转']
    })
    csvpath = tmp_path / 'travelled_cities.csv'
    records.to_csv(csvpath)
    yield csvpath
    csvpath.unlink()


def test_parse_groups_from_csv(csvfile_example):
    expect = ['中转', '居住', '旅行']
    assert np.array_equal(core.parse_groups_from_csv(csvfile_example), expect)


def test_create_tooltip_formatter_code(csvfile_example):
    groups = core.parse_groups_from_csv(csvfile_example)
    expect = """
    function(params){
        const convert = new Map([[0, '中转'], [1, '居住'], [2, '旅行']]);
        if (isNaN(params.value)) {
            return params.name;
        }
        return params.name + ': ' + convert.get(params.value);
    }
    """
    assert core.create_tooltip_formatter_code(groups) == expect


def test_parse_data_pairs_from_csv(csvfile_example):
    data_pairs = core.parse_data_pairs_from_csv(csvfile_example)
    assert data_pairs[0].opts['name'] == '北京'
    assert data_pairs[0].opts['value'] == 2
    assert data_pairs[1].opts['name'] == '上海'
    assert data_pairs[1].opts['value'] == 2
    assert data_pairs[2].opts['name'] == '武汉'
    assert data_pairs[2].opts['value'] == 1
    assert data_pairs[3].opts['name'] == '香港'
    assert data_pairs[3].opts['value'] == 0


def test_render_travel_map(csvfile_example):
    output = csvfile_example.with_name('travel_map.html')
    travel_map_option = core.TravelMapOption(title='Travel Map', output=output)
    core.render_travel_map(csvfile_example, travel_map_option)
    assert output.exists()
    output.unlink()
