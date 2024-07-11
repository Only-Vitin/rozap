namespace Rozap.Infrastructure.Selenium;

public interface ISeleniumClient
{
    void OpenByUrl(string url);
    void OpenNewWindow();
    void ChangeWindow(int index);
    void ClickByXPath(string xpath);
    void ClickOnLastByXPath(string xpath);
}