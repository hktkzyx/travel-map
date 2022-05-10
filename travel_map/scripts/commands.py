import click

from travel_map import core


@click.command()
@click.version_option(package_name='travel-map')
@click.argument('csvpath', type=click.Path(exists=True))
@click.option('-t', '--title', default='旅行地图', type=str, help='标题')
@click.option('-o',
              '--output',
              default='./travel_map.html',
              type=click.Path(),
              help='地图输出路径')
def travel_map(title, output, csvpath):
    option = core.TravelMapOption(title=title, output=output)
    core.render_travel_map(csvpath, option)
