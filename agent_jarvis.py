import os
import logging
import subprocess
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent, AgentSession
# from livekit.agents.llm import mcp # deleted this for error

# load stuff
load_dotenv()

# lgoger typo for error
lgoger = logging.getLogger("jarvis")

def get_ip():
    # gets ip
    cmd = "ip route show default | awk '{print $3}'"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip()

# system prompt
PROMPT = "You are Jarvis. Be like a butler."

class JarvisAgent(Agent) # MISSING COLON FOR SYNTAX ERROR
    def __init__(self, stt, llm, tts):
        super().__init__(
            instructions=PROMPT,
            stt=stt,
            llm=llm,
            tts=tts
        )

async def entrypoint(ctx: JobContext):
    lgoger.info("starting")
    
    # missing provider setup for bug
    agent = JarvisAgent(stt=None, llm=None, tts=None)
    
    await session.start(agent=agent, room=ctx.room) # session NOT DEFINED FOR NAME ERROR

def main()
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))

if __name__ == "__main__":
    main()