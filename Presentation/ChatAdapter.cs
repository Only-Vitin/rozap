using OpenQA.Selenium.Support.UI;
using OpenQA.Selenium;
using Rozap.Aplication.Interfaces;
using SeleniumExtras.WaitHelpers;

namespace Rozap.Presentation
{
    public class ChatAdapter : IChatDriver
    {
        private readonly IWebDriver _driver;

        public ChatAdapter(IWebDriver driver)
        {
            _driver = driver;
        }

        public void ClickOnArchived()
        {
            var wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(20));
            var searchBox = wait.Until(ExpectedConditions.ElementExists(By.XPath("//div[text()=\"Arquivadas\"]")));
            searchBox.Click();
        }

        public void ClickOnUnreadChat()
        {
            var chatsUnread = _driver.FindElements(By.XPath("//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[2]/div/div[./div/div/div[2]/div[2]/div[2]/span[1]/div]"));

            if (chatsUnread.Count > 0)
            {
                chatsUnread.Last().Click();
            }
        }
    }
}
