using Rozap.Aplication.Interfaces;

namespace Rozap.Aplication.Services
{
    public class ChatService
    {
        private readonly IChatDriver _chatDriver;

        public ChatService(IChatDriver chatDriver)
        {
            _chatDriver = chatDriver;
        }

        public void OpenArchived()
        {
            _chatDriver.ClickOnArchived();
        }

        public void OpenUnreadChat()
        { 
            _chatDriver.ClickOnUnreadChat();
        }
    }
}
