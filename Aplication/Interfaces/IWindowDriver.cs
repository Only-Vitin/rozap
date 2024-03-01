namespace Rozap.Aplication.Interfaces
{
    public interface IWindowDriver
    {
        void NavegateTo(string url);
        void OpenEmptyWindow();
        void ChangeWindow(int index);
    }
}
