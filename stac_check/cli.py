import click
from .lint import Linter

def link_asset_message(link_list:list, type: str, format: str):
    if len(link_list) > 0:
        click.secho(f"{type.upper()} {format} errors: ", fg="red")
        for asset in link_list:
            click.secho(f"    {asset}")
    else:
        click.secho(f"No {type.upper()} {format} errors!", fg="green")

def recursive_message(linter):
    click.secho(f"    Recursive: Validate all assets in a collection or catalog")
    click.secho()
    click.secho(f"Assets Validated: ")
    click.secho()
    for msg in linter.validate_all:
        click.secho(f"Version {msg['version']}")
        click.secho(f"Path {msg['path']}")
        click.secho(f"Schemas {msg['schema']}")
        if "asset_type" in msg:
            click.secho(f"Type {msg['asset_type']}")
        if "error_type" in msg:
            click.secho(f"Error Type {msg['error_type']}")
        if "error_message" in msg:
            click.secho(f"Error Type {msg['error_message']}")
        click.echo("Valid: ")
        if msg['valid_stac'] == True:
            click.secho(f"{msg['valid_stac']}", fg='green')
        else:
            click.secho(f"{msg['valid_stac']}", fg='red')
        click.secho()

def intro_message(linter):
    click.secho("""
 ____  ____  __    ___       ___  _  _  ____  ___  __ _ 
/ ___)(_  _)/ _\  / __)___  / __)/ )( \(  __)/ __)(  / )
\___ \  )( /    \( (__(___)( (__ ) __ ( ) _)( (__  )  ( 
(____/ (__)\_/\_/ \___)     \___)\_)(_/(____)\___)(__\_)
    """)

    click.secho("stac-check: STAC spec validaton and linting tool", bold=True)

    click.secho()

    if linter.version == "1.0.0":
        click.secho(linter.set_update_message(), fg='green')
    else:
        click.secho(linter.set_update_message(), fg='red')

    click.secho()

    click.secho(f"Validator: stac-validator {linter.validator_version}", bg="blue", fg="white")

    click.secho()

def cli_message(linter):
    ''' valid stac object message - true or false '''
    if linter.valid_stac == True:
        click.secho(f"Valid {linter.asset_type}: {linter.valid_stac}", fg='green')
    else:
        click.secho(f"Valid {linter.asset_type}: {linter.valid_stac}", fg='red')

    ''' schemas validated for core object '''
    click.secho()
    if len(linter.schema) > 0:
        click.secho("Schemas validated: ", fg="blue")
        for schema in linter.schema:
            click.secho(f"    {schema}")

    ''' best practices message'''
    click.secho()
    for message in linter.best_practices_msg:
        if message == linter.best_practices_msg[0]:
            click.secho(message, bg='blue')
        else:
            click.secho(message, fg='red')

    if linter.validate_all == True:
        click.secho()
        click.secho(f"Recursive validation has passed!", fg='blue')
    elif linter.validate_all == False and linter.recursive > 0:
        click.secho()
        click.secho(f"Recursive validation has failed!", fg='red')

    if linter.invalid_asset_format is not None:
        click.secho()
        link_asset_message(linter.invalid_asset_format, "asset", "format")

    if linter.invalid_asset_request is not None:
        click.secho()
        link_asset_message(linter.invalid_asset_request, "asset", "request")

    if linter.invalid_link_format is not None:
        click.secho()
        link_asset_message(linter.invalid_link_format, "link", "format")

    if linter.invalid_link_request is not None:
        click.secho()
        link_asset_message(linter.invalid_link_request, "link", "request")

    if linter.error_type != "":
        click.secho(f"Validation error type: ", fg="red")
        click.secho(f"    {linter.error_type}")

    if linter.error_msg != "":
        click.secho(f"Validation error message: ", fg='red')
        click.secho(f"    {linter.error_msg}")

    click.secho()

    click.secho(f"This object has {len(linter.data['links'])} links")

    click.secho()

    ### Stac validator response for reference
    # click.secho(json.dumps(linter.message, indent=4))

@click.option(
    "--recursive",
    "-r",
    type=int,
    default=0,
    help="Maximum depth to traverse when using recursion.",
)
@click.option(
    "-a", "--assets", is_flag=True, help="Validate assets for format and response."
)
@click.option(
    "-l", "--links", is_flag=True, help="Validate links for format and response."
)
@click.command()
@click.argument('file')
@click.version_option(version="1.2.0")
def main(file, recursive, assets, links):
    linter = Linter(file, assets=assets, links=links, recursive=recursive)
    intro_message(linter)
    if recursive > 0:
        recursive_message(linter)
    else:
        cli_message(linter)