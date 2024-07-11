using Rozap.Application.Service;
using Rozap.Infrastructure.Gateway;
using Rozap.Infrastructure.Selenium;

namespace Rozap;

public class Program
{
    public static void Main()
    {
        var seleniumClient = new SeleniumClient();
        var clickGateway = new ClickGateway(seleniumClient);
        var windowGateway = new WindowGateway(seleniumClient);
        var startService = new StartService(windowGateway, clickGateway);
        startService.Execute();

        var openUnreadService = new OpenUnreadChatService(clickGateway);
        while (true)
        {
            openUnreadService.Execute();
        }
    }
}