using Rozap.Application.Gateway;
using Rozap.Infrastructure.Selenium;

namespace Rozap.Infrastructure.Gateway;

public class ClickGateway(ISeleniumClient client) : IClickGateway
{
    public void ClickOnArchived() =>
        client.ClickByXPath("//div[text()=\"Arquivadas\"]");

    public void ClickUnreadChat() =>
        client.ClickOnLastByXPath("//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[2]/div/div[./div/div/div[2]/div[2]/div[2]/span[1]/div]");
}
