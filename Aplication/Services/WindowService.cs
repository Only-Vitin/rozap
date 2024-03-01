using Rozap.Aplication.Interfaces;

namespace Rozap.Aplication.Services
{
    public class WindowService
    {
        private readonly IWindowDriver _windowDriver;

        public WindowService(IWindowDriver driver)
        {
            _windowDriver = driver;
        }

        public void OpenByUrl(string url)
        {
            _windowDriver.NavegateTo(url);
        }

        public void OpenNewWindow()
        {
            _windowDriver.OpenEmptyWindow();
        }

        public void ChangeWindow(int index)
        {
            _windowDriver.ChangeWindow(index);
        }
    }
}
