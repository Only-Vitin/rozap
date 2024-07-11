using Rozap.Application.Gateway;

namespace Rozap.Application.Service;

public class StartService(IWindowGateway windowGateway, IClickGateway clickGateway)
{
    public void Execute()
    {
        windowGateway.OpenByUrl("https://web.whatsapp.com/");
        windowGateway.OpenNewWindow();
        windowGateway.OpenNewWindow();
        windowGateway.ChangeWindow(0);
        clickGateway.ClickOnArchived();
    }
}
