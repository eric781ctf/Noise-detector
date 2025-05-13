from rich.console import Console
from rich.table import Table

def print_report(analysis: dict):
    console = Console()
    table = Table(title="Noise Analysis Result")
    table.add_column("Metric")
    table.add_column("Value")
    for key, value in analysis.items():
        table.add_row(key, f"{value:.4f}")
    console.print(table)