import os
from dotenv import load_dotenv
from anthropic import Anthropic
from agentmail import AgentMail

load_dotenv()                     # reads .env into environment variables

claude = Anthropic()              # auto-reads ANTHROPIC_API_KEY
mail = AgentMail()                # auto-reads AGENTMAIL_API_KEY

# Verify current IDs at docs.claude.com/models
AGENT_MODEL = "claude-sonnet-5"   # strong tool use, agent brain
CHEAP_MODEL = "claude-haiku-4-5"  # fast + cheap, for eval detector

MY_EMAIL = "ssajjad.aakbari@gmail.com.com"   # test mail send to