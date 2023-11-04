from briefcase.bootstraps import TogaGuiBootstrap


class TogaAutomationBootstrap(TogaGuiBootstrap):
    def app_source(self):
        return '''\
import asyncio

import toga


class {{ cookiecutter.class_name }}(toga.App):

    def startup(self):
        """Construct and show the Toga application."""
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.show()

        self.add_background_task(self.exit_soon)

    async def exit_soon(self, app: toga.App, **kwargs):
        """Background task that closes the app after a few seconds."""
        await asyncio.sleep(2)
        print(">>> successfully started...exiting <<<")
        print(">>>>>>>>>> EXIT 0 <<<<<<<<<<")
        self.exit()


def main():
    return {{ cookiecutter.class_name }}()
'''