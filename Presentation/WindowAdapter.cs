using OpenQA.Selenium;
using Rozap.Aplication.Interfaces;

namespace Rozap.Presentation
{
    public class WindowAdapter : IWindowDriver
    {
        private readonly IWebDriver _driver;

        public WindowAdapter(IWebDriver driver)
        {
            _driver = driver;
        }
        public void ChangeWindow(int index)
        {
            _driver.SwitchTo().Window(_driver.WindowHandles[index]);
        }

        public void NavegateTo(string url)
        {
            _driver.Navigate().GoToUrl(url);
        }

        public void OpenEmptyWindow()
        {
            ((IJavaScriptExecutor)_driver).ExecuteScript("window.open()");
        }
    }
}
