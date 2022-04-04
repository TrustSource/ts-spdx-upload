import click

from ts_python_client.client import Client
from .importer import SPDXImporter

@click.command()
@click.option('--apiKey', default='', help='API Key.')
@click.option('--projectName', default='', help='Project name.')
@click.option('--skipTransfer', default=False, is_flag=True, help='Skip transfer of results to the application.')
@click.option('--settingsFile', default='', help='Path to a settings file.')
@click.option('--outputFile', default='', help='Path to an output file.')
@click.argument('path', required=True)
def main(apikey, projectname, skiptransfer, settingsfile, outputfile, path):
    tool = Client('ts-spdx-import', SPDXImporter())
    tool.run(path,
             apiKey=apikey,
             projectName=projectname,
             skipTransfer=skiptransfer,
             settingsFile=settingsfile,
             outputFile=outputfile)

if __name__ == '__main__':
    main()