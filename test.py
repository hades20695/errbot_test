from errbot import BotPlugin, botcmd
import subprocess

class Hint(BotPlugin):
    @botcmd
    def exec(self, msg, args):
        """
        I will help you. usage: `!hint` or `!help`
        """
        process = subprocess.Popen(args.split(" "), stdout=subprocess.PIPE)
        ret = process.communicate()[0]
        self.send(msg.to, f"```{ret}```", in_reply_to=msg)
