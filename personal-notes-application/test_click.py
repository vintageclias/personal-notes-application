import click  

@click.command()  
def hello():  
    """A simple greeting command."""  
    click.echo("Hello, Click!")  

if __name__ == '__main__':  
    hello()  