using Microsoft.Extensions.DependencyInjection;
using Rozap.Config;
using Rozap.Aplication.Interfaces;
using Microsoft.Extensions.Hosting;
using Rozap.Aplication.Services;
using Rozap.Presentation;
using OpenQA.Selenium;


namespace Rozap
{
    public class Startup
    {
        public static IHostBuilder CreateHostBuilder(string[] args) => Host.CreateDefaultBuilder(args)
        .ConfigureServices((hostContext, services) =>
        {
            services.AddScoped<IBrowserConfig<IWebDriver>, SeleniumChromeBrowser>();
            services.AddScoped<IWindowDriver, WindowAdapter>();
            services.AddScoped<IChatDriver, ChatAdapter>();
            services.AddScoped(provider =>
            {
                var browser = provider.GetRequiredService<IBrowserConfig<IWebDriver>>();
                return browser.Configure();
            });

            services.AddScoped<WindowService>();
            services.AddScoped<ChatService>();
        });
    }
}
