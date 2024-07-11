using Rozap.Application.Gateway;
using Rozap.Infrastructure.Selenium;

namespace Rozap.Infrastructure.Gateway;

public class WindowGateway(ISeleniumClient client) : IWindowGateway
{
    public void ChangeWindow(int index) =>
        client.ChangeWindow(index);

    public void OpenByUrl(string url) =>
        client.OpenByUrl(url);

    public void OpenNewWindow() =>
        client.OpenNewWindow();
}
