import requests
import json
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt


API_URL = "https://api.gatecore.xyz"
API_KEY = "Your API key"

console = Console()

def print_header():
    console.print(Panel.fit(
        "[bold cyan]GateCore API Terminal Tester[/bold cyan]\n"
        "[white]Interactive API verification tool[/white]",
        border_style="blue"
    ))

def make_request(endpoint, method="POST", data=None):
    headers = {"X-API-Key": API_KEY}
    url = f"{API_URL}{endpoint}"
    
    with console.status(f"[bold yellow]Requesting {endpoint}...[/bold yellow]"):
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=30)
            else:
                response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                console.print(f"[bold red]Error {response.status_code}:[/bold red] {response.text}")
                return None
        except Exception as e:
            console.print(f"[bold red]Connection Error:[/bold red] {str(e)}")
            return None

def test_phone():
    phone = Prompt.ask("[bold green]Enter phone number[/bold green]")
    result = make_request("/api/phone", data={"phone": phone})
    if result:
        console.print_json(data=result)

def test_telegram():
    username = Prompt.ask("[bold green]Enter Telegram Username (without @)[/bold green]")
    result = make_request("/api/telegram", data={"username": username})
    if result:
        console.print_json(data=result)

def test_username():
    username = Prompt.ask("[bold green]Enter Username for cross-platform search[/bold green]")
    result = make_request("/api/username", data={"username": username})
    if result:
        console.print_json(data=result)

def test_domain():
    domain = Prompt.ask("[bold green]Enter domain for reconnaissance (e.g., google.com)[/bold green]")
    result = make_request("/api/domain", data={"domain": domain})
    if result:
        console.print_json(data=result)

def test_discord():
    discord_id = Prompt.ask("[bold green]Enter Discord User ID[/bold green]")
    result = make_request("/api/discord", data={"id": discord_id})
    if result:
        console.print_json(data=result)

def test_ip_mac():
    console.print("\n1. IP Lookup\n2. MAC Lookup")
    choice = Prompt.ask("Select sub-function", choices=["1", "2"])
    if choice == "1":
        ip = Prompt.ask("[bold green]Enter IP address[/bold green]")
        result = make_request("/api/ip", data={"ip": ip})
    else:
        mac = Prompt.ask("[bold green]Enter MAC address[/bold green]")
        result = make_request("/api/mac", data={"mac": mac})
    
    if result:
        console.print_json(data=result)

def test_temp_mail():
    console.print("\n1. Generate new email\n2. Check messages")
    choice = Prompt.ask("Select sub-function", choices=["1", "2"])
    if choice == "1":
        result = make_request("/api/temp-mail/generate", method="GET")
        if result:
            console.print(f"[bold cyan]Your new email:[/bold cyan] {result}")
    else:
        email = Prompt.ask("[bold green]Enter email to check[/bold green]")
        result = make_request(f"/api/temp-mail/messages/{email}", method="GET")
        if result:
            console.print_json(data=result)

def test_balance():
    result = make_request("/api/balance", method="GET")
    if result:
        console.print(Panel(
            f"[bold white]User:[/bold white] {result.get('username')}\n"
            f"[bold green]Balance:[/bold green] ${result.get('balance'):.2f}",
            title="Account Info", border_style="green"
        ))

def main_menu():
    while True:
        console.print("\n")
        table = Table(title="API Tester Main Menu", show_header=True, header_style="bold magenta")
        table.add_column("No", style="dim", width=4)
        table.add_column("Function", min_width=20)
        table.add_column("Description")

        table.add_row("1", "Phone Search", "Phone number intelligence")
        table.add_row("2", "Telegram Search", "Telegram profile analysis")
        table.add_row("3", "Username Search", "Search across 500+ sites (Maigret)")
        table.add_row("4", "Domain Recon", "Passive domain data collection")
        table.add_row("5", "Discord Lookup", "Discord User ID information")
        table.add_row("6", "IP/MAC Lookup", "Network reconnaissance")
        table.add_row("7", "Temp Mail", "Disposable email management")
        table.add_row("8", "Balance", "Check API account balance")
        table.add_row("0", "Exit", "Close the script")

        console.print(table)
        
        choice = Prompt.ask("Select an action", choices=["1", "2", "3", "4", "5", "6", "7", "8", "0"])

        if choice == "1": test_phone()
        elif choice == "2": test_telegram()
        elif choice == "3": test_username()
        elif choice == "4": test_domain()
        elif choice == "5": test_discord()
        elif choice == "6": test_ip_mac()
        elif choice == "7": test_temp_mail()
        elif choice == "8": test_balance()
        elif choice == "0": 
            console.print("[bold cyan]Goodbye![/bold cyan]")
            break
        
        Prompt.ask("\nPress Enter to return to menu...")

if __name__ == "__main__":
    print_header()
    main_menu()
