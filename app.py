#Made by Pakhomov A.K. IKBO-17-22
from textual.app import App, ComposeResult
from textual.widgets import Button, TextArea
from textual import on

import asm
from asm import asm 
from interpreter import execute
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



DEMO = """
commands:
  - write_const:
    dest_addr: 0
    value: 10
  - write_const:
    dest_addr: 1
    value: 20
""".strip()

TEMPLATE = """
memory: %s
bytecode: %s
""".strip()


class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield TextArea(text=DEMO, id="input")
        yield Button(label="start", id="main")
        yield TextArea(id="output", text=" ")

    @on(Button.Pressed, "#main")
    def click(self) -> None:
        program = self.query_one("#input").text
        program = yaml.safe_load(program)  
        bytecode = asm(program)
        textcode = " ".join([hex(i) for i in bytecode])
        memory=execute(bytecode)
        self.query_one("#output").text = TEMPLATE % (memory, textcode)

if __name__ == "__main__":
    app = ClockApp()
    app.run()
