

class Steamie:
    def __init__(self):
        # Log in
        self.r = praw.Reddit("SteamieBot for /r/Glasgow v2.0 by /u/timlardner")
        o = OAuth2Util(r)
        o.refresh()

        # Load from the configuration file
        self.config = ConfigParser.ConfigParser()
        self.config.read(configFile)
        
        # Check to see if we need to post a new thread or update an existing one
        self.hasPostedToday = self.alreadyPosted()  
        
    def alreadyPosted(self):
        # We want to find out here if we've posted a Steamie thread today.
        

if __name__ == "__main__":
    SteamieBot = Steamie()
