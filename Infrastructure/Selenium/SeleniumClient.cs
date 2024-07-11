using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;

namespace Rozap.Infrastructure.Selenium;

public class SeleniumClient : ISeleniumClient
{
    private readonly IWebDriver webDriver = SeleniumChromeBrowser.Configure();

    public void ChangeWindow(int index) =>
        webDriver.SwitchTo().Window(webDriver.WindowHandles[index]);

    public void OpenByUrl(string url) =>
        webDriver.Navigate().GoToUrl(url);

    public void OpenNewWindow() =>
        ((IJavaScriptExecutor)webDriver).ExecuteScript("window.open()");

    public void ClickByXPath(string xpath)
    {
        var wait = new WebDriverWait(webDriver, TimeSpan.FromSeconds(20));
        var searchBox = wait.Until(ExpectedConditions.ElementExists(By.XPath(xpath)));
        searchBox.Click();
    }

    public void ClickOnLastByXPath(string xpath)
    {
        var chatsUnread = webDriver.FindElements(By.XPath(xpath));

        if (chatsUnread.Count > 0)
            chatsUnread.Last().Click();
    }
}
