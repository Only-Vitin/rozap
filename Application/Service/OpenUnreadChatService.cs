using Rozap.Application.Gateway;

namespace Rozap.Application.Service;

public class OpenUnreadChatService(IClickGateway clickGateway)
{
    public void Execute()
    {
        clickGateway.ClickUnreadChat();
    }
}
