"""Core chatbot wrapper around the AIML kernel."""
import os
import aiml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BRAIN_FILE = os.path.join(BASE_DIR, "bot_brain.brn")
STARTUP_FILE = os.path.join(BASE_DIR, "aiml_files", "startup.xml")


def create_bot():
    """Create and train the AIML kernel. Uses a cached brain file for faster startup."""
    kernel = aiml.Kernel()
    kernel.verbose(False)

    # Bot predicates (used by <bot name="..."/>)
    kernel.setBotPredicate("name", "AIMLBot")
    kernel.setBotPredicate("master", "Developer")

    os.chdir(BASE_DIR)  # AIML <learn> paths are relative
    if os.path.exists(BRAIN_FILE):
        kernel.bootstrap(brainFile=BRAIN_FILE)
    else:
        kernel.bootstrap(learnFiles=STARTUP_FILE, commands="LOAD AIML B")
        kernel.saveBrain(BRAIN_FILE)
    return kernel


def reply(kernel, message, session_id="default"):
    return kernel.respond(message, session_id) or "..."
