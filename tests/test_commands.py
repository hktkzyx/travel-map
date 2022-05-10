from click import testing

from travel_map.scripts import commands


def test_travel_map(csvfile_example, tmp_path):
    runner = testing.CliRunner()
    output = tmp_path / 'renderred_travel_map.html'
    result = runner.invoke(
        commands.travel_map,
        ['-t', 'travel_map', '-o', f'{output}', f'{csvfile_example}'])
    assert result.exit_code == 0
    assert output.exists()
    output.unlink()
