import os; from dotenv import load_dotenv; from agentmail import AgentMail
   load_dotenv()
   client = AgentMail()  # reads AGENTMAIL_API_KEY from env
   inbox = client.inboxes.create(username="inboxguard", client_id="ig-main")  # idempotent
   print("Inbox:", inbox.inbox_id)
   client.inboxes.messages.send(
       inbox_id=inbox.inbox_id, to="YOUR_PERSONAL_EMAIL@gmail.com",
       subject="InboxGuard is alive", text="First email from my agent's inbox.")
   print("Sent — check your inbox.")