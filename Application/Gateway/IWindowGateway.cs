namespace Rozap.Application.Gateway;
public interface IWindowGateway
{
    void OpenByUrl(string url);
    void OpenNewWindow();
    void ChangeWindow(int index);
}
