from collections.abc import Iterable
from collections.abc import Sequence
import pathlib
from typing import NamedTuple

import numpy as np
import pandas as pd
from pyecharts import charts
from pyecharts import options
from pyecharts.commons import utils


def parse_groups_from_csv(path):
    """Return groups.

    Parameters
    ----------
    path : path_like
        CSV path.

    Returns
    -------
    groups : np.ndarray of str
        Groups name.
    """
    filepath = pathlib.Path(path)
    data = pd.read_csv(filepath,
                       usecols=['城市', '组'],
                       index_col=False,
                       dtype=str)
    return np.unique(data.loc[:, '组'].to_numpy())


def create_tooltip_formatter_code(groups: Iterable[str]) -> str:
    """Return tooltip formatter code.

    Parameters
    ----------
    groups : iterable of str
        Groups.

    Returns
    -------
    str
    """
    map_str = ', '.join(
        [f'[{index}, {group!r}]' for index, group in enumerate(groups)])
    return f"""
    function(params){{
        const convert = new Map([{map_str}]);
        if (isNaN(params.value)) {{
            return params.name;
        }}
        return params.name + ': ' + convert.get(params.value);
    }}
    """


def create_visualmap_pieces(groups: Iterable[str]) -> list[dict]:
    """Return tooltip formatter code.

    Parameters
    ----------
    groups : iterable of str
        Groups.

    Returns
    -------
    list of dict

    Examples
    --------
    >>> create_visualmap_pieces(['travel', 'live'])
    [{'value': 0, 'label': 'travel'}, {'value': 1, 'label': 'live'}]
    """
    return [{
        'value': index, 'label': group
    } for (index, group) in enumerate(groups)]


def parse_data_pairs_from_csv(path) -> Sequence[options.MapItem]:
    """Return data pairs required for `pyecharts` `Map` instance.

    Parameters
    ----------
    path : path_like
        CSV file path.

    Returns
    -------
    data_pairs : list of options.MapItem
        Data pairs.
    """
    groups = parse_groups_from_csv(path)
    group_value = {group: index for index, group in enumerate(groups)}
    data = pd.read_csv(path, usecols=['城市', '组'], index_col=False, dtype=str)
    return [
        options.MapItem(item['城市'], group_value[item['组']])
        for (_, item) in data.iterrows()
    ]


class TravelMapOption(NamedTuple):
    """Travel map options.

    Attributes
    ----------
    title : str
        Travel map title.
    output : str
        Output file path.
    """
    title: str
    output: str


def render_travel_map(csvpath, travel_map_option: TravelMapOption):
    """Render travel map.

    Parameters
    ----------
    csvpath : path_like
        CSV file path.
    travel_map_option : TravelMapOption
        Travel map options.
    """
    groups = parse_groups_from_csv(csvpath)
    toolbox_feature = options.ToolBoxFeatureOpts(
        options.ToolBoxFeatureSaveAsImageOpts(),
        options.ToolBoxFeatureRestoreOpts(),
        options.ToolBoxFeatureDataViewOpts(is_show=False),
        options.ToolBoxFeatureDataZoomOpts(is_show=False),
        options.ToolBoxFeatureMagicTypeOpts(is_show=False),
        options.ToolBoxFeatureBrushOpts(type_=[]))
    visualmap_option = options.VisualMapOpts(
        is_piecewise=True, pieces=create_visualmap_pieces(groups))
    tooltip_option = options.TooltipOpts(
        formatter=utils.JsCode(create_tooltip_formatter_code(groups)))
    figure = charts.Map()
    figure.add('Travel Map',
               parse_data_pairs_from_csv(csvpath),
               maptype='china-cities',
               label_opts=options.LabelOpts(is_show=False),
               is_map_symbol_show=False)
    figure.set_global_opts(
        visualmap_opts=visualmap_option,
        tooltip_opts=tooltip_option,
        title_opts=options.TitleOpts(travel_map_option.title),
        toolbox_opts=options.ToolboxOpts(feature=toolbox_feature),
        legend_opts=options.LegendOpts(is_show=False))
    figure.render(travel_map_option.output)
