import pandas as pd
import pyfiglet as tit
import random
import time
import platform
import os
import _pickle
from pickle import dump, load
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table
from rich import print as rprint


init()

console = Console()


def pont(ch):
    return sum(1 for i in range(len(ch)) if ch[i] == ".")


def DatetimeForma(ch):
    if (
        len(ch) == 16
        and ch[4] == "-"
        and ch[7] == "-"
        and ch[10] == " "
        and ch[13] == ":"
    ):
        year = ch[:4]
        month = ch[5:7]
        day = ch[8:10]
        hour = ch[11:13]
        minute = ch[14:16]
        if (
            year.isdigit()
            and month.isdigit()
            and day.isdigit()
            and hour.isdigit()
            and minute.isdigit()
        ):
            return True
    return False


def IpForma(ch):
    if pont(ch) == 3:
        x, y, z, w = ch.split(".")
        if len(x) > 3 or len(y) > 3 or len(z) > 3 or len(w) > 3:
            return False
        elif not (
            x.isdigit() and y.isdigit() and z.isdigit() and w.isdigit() and w.isdigit()
        ):
            return False
        else:
            return True
    else:
        return False


def search(df, ip, type):
    return df.loc[df[type] == ip]


def felter():
    global df
    df = df.replace("0", None)
    df = df.replace(0, None)
    df.dropna(inplace=True)
    df = df.sort_values(by=["datetime"], ascending=False)
    df = df.drop_duplicates(subset=["ip", "user", "passwd"], keep="last")
    df = df[df["ip"].apply(lambda x: IpForma(x) if isinstance(x, str) else False)]
    df = df[
        df["datetime"].apply(
            lambda x: DatetimeForma(x) if isinstance(x, str) else False
        )
    ]
    df = df[["ip", "user", "passwd", "datetime", "type"]]


def UpdateUserData(ip, type):
    global df
    Target = search(df, ip, type)
    if not Target.empty:
        Target = list(Target.iloc[0])
        console.print(
            "[bold yellow]Modifying record - Press Enter to keep current value[/bold yellow]"
        )
        for i in range(len(Target)):
            current_value = Target[i]
            console.print(
                f"[bold MAGENTA]--------------Update {df.columns[i]}--------------[/bold MAGENTA]"
            )
            new_value = input(
                Fore.CYAN
                + f"Current {df.columns[i]}: {current_value}\nNew value (or Enter to keep current): "
                + Style.RESET_ALL
            ).strip()
            if df.columns[i] == "ip":
                while not (IpForma(new_value) or new_value == ""):
                    console.print("[red][!]Format: xxx.yyy.zzz.www[red]")
                    new_value = input(
                        Fore.CYAN
                        + f"Current {df.columns[i]}: {current_value}\nNew value (or Enter to keep current): "
                        + Style.RESET_ALL
                    ).strip()
            elif df.columns[i] == "datetime":
                while not (DatetimeForma(new_value) or new_value == ""):
                    console.print("[red][!]Format: yyyy-mm-dd hh:mm[red]")
                    new_value = input(
                        Fore.CYAN
                        + f"Current {df.columns[i]}: {current_value}\nNew value (or Enter to keep current): "
                        + Style.RESET_ALL
                    ).strip()
            Target[i] = new_value if new_value else current_value
        df = df[df[type] != ip]
        df = pd.concat(
            [df, pd.DataFrame([Target], columns=df.columns)], ignore_index=True
        )
        console.print(
            "[bold green]✓ Record modified successfully! Use -s to save changes.[/bold green]"
        )
    else:
        console.print("[red]Record not found! Please check your search criteria.[/red]")


def resetuser():
    global df
    console.print(
        "[bold yellow]Please select which field to use for deletion:[/bold yellow]"
    )
    console.print(f"[cyan]Available fields:[/cyan] {', '.join(df.columns)}")
    type = input(Fore.CYAN + "Enter field name: " + Style.RESET_ALL).strip()
    while type not in list(df.columns):
        if type == "-q":
            break
        console.print("[red]Invalid field! Please choose from available fields.[/red]")
        type = input(
            Fore.CYAN + f"Enter field name [-q to cancel]: " + Style.RESET_ALL
        ).strip()
    if type != "-q":
        ip = input(
            Fore.CYAN + f"Enter {type} value to delete: " + Style.RESET_ALL
        ).strip()
        df = df[df[type] != ip]
        console.print(
            "[bold green]✓ Record deleted successfully! Use -s to save changes.[/bold green]"
        )


def adduser():
    global df
    new_user = {}
    console.print(
        "[bold cyan]Please enter the following information for the new record:[/bold cyan]"
    )
    for col in df.columns:
        new_user[col] = input(Fore.YELLOW + f"Enter {col}: " + Style.RESET_ALL).strip()
        if col == "ip":
            while not (IpForma(new_user[col])):
                console.print("[red][!]Format: xxx.yyy.zzz.www[red]")
                new_user[col] = input(
                    Fore.YELLOW + f"Enter {col} again: " + Style.RESET_ALL
                ).strip()
        elif col == "datetime":
            while not (DatetimeForma(new_user[col])):
                console.print("[red][!]Format: yyyy-mm-dd hh:mm[red]")
                new_user[col] = input(
                    Fore.YELLOW + f"Enter {col} again: " + Style.RESET_ALL
                ).strip()
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    console.print(
        "[bold green]✓ Record added successfully! Use -s to save changes.[/bold green]"
    )


def deleteType(url="typesPages.dat"):
    types = ListeTypePages(url)
    if types == []:
        console.print("[bold red]Error: No types found ![/bold red]")
        exit(1)
    try:
        type = input(Fore.YELLOW + f"Enter type of Page to delete: " + Style.RESET_ALL)
        while type not in types:
            if type == "-q":
                break
            console.print(f"[red]Invalid type! Choose from: {types}[/red]")
            type = input(
                Fore.YELLOW
                + f"Enter type of Page to delete [-q quit]: "
                + Style.RESET_ALL
            ).strip()
        if type != "-q":
            f = open(url, "rb")
            l = []
            while True:
                try:
                    data = load(f)
                    if data["type"] != type:
                        l.append(data)
                except EOFError:
                    break
            f.close()
            f = open(url, "wb")
            for i in l:
                dump(i, f)
            f.close()
            console.print("[bold green]✓ Page deleted successfully![/bold green]")
    except FileNotFoundError:
        console.print(
            "[bold red]Error: 'typesPages.dat' file not found! Please check the file path.[/bold red]"
        )
        console.print(
            "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
        )
        exit(1)


def ListeTypePages(url="typesPages.dat"):
    try:
        f = open(url, "rb")
        l = []
        while True:
            try:
                data = load(f)
                l.append(data["type"])
            except EOFError:
                break
            except (_pickle.UnpicklingError, UnicodeDecodeError) as e:
                console.print(
                    f"[bold red]Warning: Corrupted data found in {url}![/bold red]"
                )
                console.print(
                    "[yellow]The file might be corrupted or in wrong format.[/yellow]"
                )
                console.print(
                    "[yellow]Please ensure the file was created properly.[/yellow]"
                )
                return []
        f.close()
    except EOFError:
        console.print("[bold red]Error: No data found in file![/bold red]")
        return []
    except FileNotFoundError:
        console.print(
            "[bold red]Error: 'typesPages.dat' file not found! Please check the file path.[/bold red]"
        )
        console.print(
            "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
        )
        return []
    return l


def changePage(data, index):
    type = input(Fore.YELLOW + f"Enter type of Page to change: " + Style.RESET_ALL)
    while type not in ListeTypePages(data):
        if type == "-q":
            break
        console.print(f"[red]Invalid type! Choose from: {ListeTypePages(data)}[/red]")
        type = input(
            Fore.YELLOW + f"Enter type of Page to change [-q quit]: " + Style.RESET_ALL
        ).strip()
    if type != "-q":
        try:
            f = open(data, "rb")
            e = load(f)
            while e["type"] != type:
                try:
                    e = load(f)
                except EOFError:
                    console.print("[bold red]Error: Type not found in file![/bold red]")
                    break
            f.close()
        except FileNotFoundError:
            console.print(
                "[bold red]Error: 'typesPages.dat' file not found! Please check the file path.[/bold red]"
            )
            console.print(
                "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
            )
            exit(1)
        try:
            f = open(index, "w", encoding="utf-8")
            with console.status(
                "[bold green]Changing HTML page content...[/bold green]"
            ) as status:
                time.sleep(random.uniform(0.5, 1))
                f.write(e["content"])
            console.print(
                "[bold green]✓ HTML page content changed successfully![bold green]"
            )
            f.close()
        except FileNotFoundError:
            console.print(
                "[bold red]Error: 'index.html' file not found! Please check the file path.[/bold red]"
            )
            console.print(
                "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
            )
            exit(1)
        except UnicodeEncodeError:
            console.print(
                "[bold red]Error: Unable to write content to file. Please check the encoding.[/bold red]"
            )
            console.print(
                "[bold green]Make sure the content is properly encoded.[/bold green]"
            )
            exit(1)


def addPage(url="typesPages.dat"):
    try:
        type = input(Fore.YELLOW + f"Enter type of Page: " + Style.RESET_ALL).strip()
        while type in ListeTypePages(url):
            if type == "-q":
                break
            console.print(f"[red]Type already exists! Choose a different type.[/red]")
            type = input(
                Fore.YELLOW + f"Enter type of Page [-q quit]: " + Style.RESET_ALL
            ).strip()
        if type == "-q":
            return
        console.print(
            "[red]The code must be vaccinated here first.< https://codebeautify.org/minify-html >[/red]"
        )
        content = input(
            Fore.YELLOW + f"Enter content of Page: " + Style.RESET_ALL
        ).strip()
        f = open(url, "ab+")
        e = {"type": type, "content": content}
        dump(e, f)
        f.close()
        console.print("[bold green]✓ Page added successfully![/bold green]")
    except:
        console.print(
            "[bold red]Error: Unable to add page. Please check the file path.[/bold red]"
        )
        console.print(
            "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
        )
        exit(1)


def helpcmd(cmds):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="yellow")
    for k, v in cmds.items():
        table.add_row(k, v)
    console.print(table)


def print_header():
    os.system(clear)
    console.print(
        "[bold yellow]"
        + tit.figlet_format("PhishSense", font="slant")
        + "[/bold yellow]"
    )
    console.print(f"[cyan]Author:[/cyan] [green]PUTIN[/green]")
    console.print(f"[cyan]Platform:[/cyan] [green]{plat}[/green]")
    console.print(f"[cyan]Working Directory:[/cyan] [green]{os.getcwd()}[/green]")
    console.print(f"[cyan]Current User:[/cyan] [green]{os.getlogin()}[/green]")
    console.print(
        f"[cyan]Python Version:[/cyan] [green]{platform.python_version()}[/green]"
    )


def display_dataframe(df):
    table = Table(show_header=True, header_style="bold magenta")
    for col in df.columns:
        table.add_column(col)
    for _, row in df.iterrows():
        table.add_row(*[str(x) for x in row])
    console.print(table)


cmds = {
    "-RE": "Restart application and reload data",
    "-a": "Display all records in database",
    "-s": "Save changes to database",
    "-r": "Search for a record using any field",
    "-S": "Remove a specific record from database",
    "-c": "Clear screen",
    "-A": "Add new record to database",
    "-M": "Modify existing record using IP address",
    "-Sa": "Reset entire database (Warning: removes all data)",
    "-h": "Show this help message",
    "-f": "Filter and clean database records",
    "-q": "Exit application",
    "-Cp": "Change HTML page content",
    "-Ap": "Add a new HTML page",
    "-ap": "Display all Pages Types",
    "-Sap": "Remove page content from index.html",
    "-Sp": "Remove a specific Page Type ",
}

plat = platform.system()
if plat == "Windows":
    clear = "cls"
else:
    clear = "clear"
print_header()
url = os.getcwd() + "/result.csv"
try:
    df = pd.read_csv(url, dtype=str, encoding="utf-8")
    df = df[["ip", "user", "passwd", "datetime", "type"]]
except FileNotFoundError:
    console.print(
        "[bold red]Error: 'result.csv' file not found! Please check the file path.[/bold red]"
    )
    console.print(
        "[bold green]Make sure the file is in the same directory as this script.[/bold green]"
    )
    exit(1)
console.print(
    "[bold cyan]Enter command [bold cyan]([green]'-h'[green][bold cyan] for help):[bold cyan]"
)
cmd = input(Fore.GREEN + "> " + Style.RESET_ALL).strip()
while cmd != "-q":
    if cmd not in cmds.keys():
        console.print("[bold red]Command not found![/bold red]")
        helpcmd(cmds)
    else:
        match cmd:
            case "-a":
                display_dataframe(df)
            case "-ap":
                print(ListeTypePages(os.getcwd() + "/typesPages.dat"))
            case "-A":
                console.print("[bold yellow]Adding new user...[/bold yellow]")
                adduser()
            case "-S":
                console.print("[bold yellow]Resetting user...[/bold yellow]")
                resetuser()
            case "-RE":
                print_header()
                df = pd.read_csv(url, dtype=str, encoding="utf-8")
                df = df[["ip", "user", "passwd", "datetime", "type"]]
            case "-f":
                with console.status(
                    "[bold green]Filtering data...[/bold green]"
                ) as status:
                    felter()
                    time.sleep(random.uniform(0.5, 1))
                console.print("[bold green]Filter completed successfully![bold green]")
            case "-r":
                console.print("[bold yellow]Search Mode[bold yellow]")
                type = input(
                    Fore.CYAN + f"Type to find {list(df.columns)} >> " + Style.RESET_ALL
                ).strip()
                while type not in list(df.columns):
                    if type == "-q":
                        break
                    console.print(
                        f"[red]Invalid type! Choose from: {list(df.columns)}[/red]"
                    )
                    type = input(
                        Fore.CYAN + "Type to find [-q quit] >> " + Style.RESET_ALL
                    ).strip()
                if type != "-q":
                    ip = input(
                        Fore.CYAN + f"Enter The {type} >>> " + Style.RESET_ALL
                    ).strip()
                    result = search(df, ip, type)
                    if result.empty:
                        console.print("[red]No results found![red]")
                    else:
                        display_dataframe(result)
            case "-s":
                with console.status(
                    "[bold green]Saving changes...[/bold green]"
                ) as status:
                    df.to_csv(url, encoding="utf-8")
                    time.sleep(random.uniform(0.5, 1))
                console.print("[bold green]✓ Changes saved successfully![bold green]")
            case "-Sa":
                console.print("[bold red]Warning: Resetting all data![bold red]")
                df = pd.DataFrame(columns=df.columns)
                display_dataframe(df)
                console.print("[yellow]Use -s to save changes[yellow]")
            case "-M":
                console.print("[bold yellow]Modification Mode[bold yellow]")
                type = "ip"
                ip = input(Fore.CYAN + "Target IP >>> " + Style.RESET_ALL).strip()
                while not (len(ip) > 5 and len(ip) <= 15 and (IpForma(ip))):
                    if ip == "-q":
                        break
                    console.print("[red][!]Format: xxx.yyy.zzz.www[red]")
                    ip = input(
                        Fore.CYAN + "Target IP [-q quit] >>> " + Style.RESET_ALL
                    ).strip()
                try:
                    if ip != "-q":
                        UpdateUserData(ip, type)
                except NameError:
                    console.print("[red]Modification cancelled[red]")
            case "-c":
                print_header()
            case "-h":
                helpcmd(cmds)
            case "-Cp":
                changePage(os.getcwd() + "/typesPages.dat", os.getcwd() + "/index.html")
            case "-Ap":
                addPage(os.getcwd() + "/typesPages.dat")
            case "-Sap":
                try:
                    open(os.getcwd() + "/index.html", "w", encoding="utf-8").close()
                except FileNotFoundError:
                    console.print("[bold red]File not found![bold red]")
                    console.print(
                        "[bold green]Make sure the file is in the same directory as this script.[bold green]"
                    )
                console.print(
                    "[bold green]✓ HTML page cleared successfully![bold green]"
                )
            case "-Sp":
                deleteType(os.getcwd() + "/typesPages.dat")
            case "_":
                console.print("[bold red]Command not found![bold red]")

    console.print(
        "[bold cyan]Enter command [bold cyan]([green]'-h'[green][bold cyan] for help):[bold cyan]"
    )
    cmd = input(Fore.GREEN + "> " + Style.RESET_ALL).strip()

os.system(clear)
