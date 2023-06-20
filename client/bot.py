import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter


nonebot.init()


driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)


nonebot.load_builtin_plugins("echo")  # 内置插件
# nonebot.load_plugin("third_party_plugin")  # 第三方插件
# nonebot.load_plugins("awesome_bot/plugins")  # 本地插件


if __name__ == "__main__":
    nonebot.run()