using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using Rozap.Aplication.Interfaces;
using System.Drawing;

namespace Rozap.Config
{
    public class SeleniumChromeBrowser : IBrowserConfig<IWebDriver>
    {
        public IWebDriver Configure()
        {
            var profilePath = Path.Combine(Directory.GetCurrentDirectory(), "profile", "wpp");

            var options = new ChromeOptions();
            //options.AddArgument("--headless");
            //options.AddArgument("--no-sandbox");
            options.AddArgument("--lang=pt");
            options.AddArgument(string.Format("user-data-dir={0}", profilePath));

            var driver = new ChromeDriver(options);
            driver.Manage().Window.Size = new Size(1024, 768);

            return driver;
        }
    }
}
