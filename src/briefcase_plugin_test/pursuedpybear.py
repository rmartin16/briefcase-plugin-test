import toml

from briefcase.bootstraps import PursuedPyBearGuiBootstrap


class PursuedPyBearAutomationBootstrap(PursuedPyBearGuiBootstrap):
    def app_source(self):
        return """\
import importlib.metadata
import os
import sys

import ppb


class {{ cookiecutter.class_name }}(ppb.Scene):
    def __init__(self, **props):
        super().__init__(**props)
        self.updates: int = 0

        self.add(
            ppb.Sprite(
                image=ppb.Image("{{ cookiecutter.module_name }}/resources/{{ cookiecutter.app_name }}.png"),
            )
        )

    def on_update(self, event, signal):
        self.updates += 1
        # quit after 2 seconds since on_update is run 60 times/second
        if self.updates > 120:
            print(">>> successfully started...exiting <<<")
            print(">>>>>>>>>> EXIT 0 <<<<<<<<<<")
            signal(ppb.events.Quit())


def main():
    app_module = sys.modules["__main__"].__package__
    metadata = importlib.metadata.metadata(app_module)

    os.environ["SDL_VIDEO_X11_WMCLASS"] = metadata["Formal-Name"]

    ppb.run(
        starting_scene={{ cookiecutter.class_name }},
        title=metadata["Formal-Name"],
    )
"""

    def pyproject_table_linux_flatpak(self):
        table = toml.loads(super().pyproject_table_linux_flatpak())
        table.setdefault("requires", []).append("pysdl2-dll==2.0.22")
        return f"\n{toml.dumps(table)}"

    def pyproject_table_windows(self):
        table = toml.loads(super().pyproject_table_windows())
        table.setdefault("requires", []).append("pysdl2-dll==2.0.22")
        return f"\n{toml.dumps(table)}"

    def pyproject_table_macOS(self):
        table = toml.loads(super().pyproject_table_macOS())
        table.setdefault("requires", []).append("pysdl2-dll==2.0.22")
        return f"\n{toml.dumps(table)}"
