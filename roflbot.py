from pyrcb import IRCBot


class MyBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        elif message == "!penis":
            self.send(channel, nickname + ": " + "penis command")
        elif message == "!hestepikk":
            self.send(channel, nickname + ": " + "hestepikk command")
        elif message == "!approves":
            if nickname == "kad" or "R0flcopt3r" or "moggy":
                self.send(channel, nickname + ": " + "kad-server.net/" +
                          nickname + "approves")
            else:
                self.send(channel, nickname + "kad-server.net/approves")

    def on_join(self, nickname, channel):
        if nickname != self.nickname:
            self.send(channel, nickname + " has joined " + channel)


def main():
    bot = MyBot()
    bot.connect("irc.snoonet.org", 6667)
    bot.register("Roflbot")
    bot.join("#dei3bukkenenoobs")
    bot.listen()


if __name__ == "__main__":
    main()
