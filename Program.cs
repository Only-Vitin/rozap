using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Rozap.Aplication.Services;

namespace Rozap
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var host = Startup.CreateHostBuilder(args).Build();

            using (var serviceScope = host.Services.CreateScope())
            {
                var services = serviceScope.ServiceProvider;

                var _windowService = services.GetRequiredService<WindowService>();
                var _chatService = services.GetRequiredService<ChatService>();
                _windowService.OpenByUrl("https://web.whatsapp.com/");
                _windowService.OpenNewWindow();
                _windowService.OpenNewWindow();
                _windowService.ChangeWindow(0);
                _chatService.OpenArchived();
                while(true)
                {
                    _chatService.OpenUnreadChat();
                }
            }
        }

    }
}
