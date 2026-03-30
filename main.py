from astrbot.api.all import *

@register("helloworld", "YourName", "一个简单的打招呼插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令：用户输入 /hello 时触发
    @command("hello")
    async def hello(self, event: CommandResult):
        '''打招呼指令'''
        yield event.plain_result(f"你好，{event.get_sender_name()}！")

    # 监听所有消息
    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: EventContext):
        # 可以在这里处理特定逻辑
        pass