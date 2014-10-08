from plugins.BasePlugin import BasePlugin


class HelloPlugin(BasePlugin):
        
        def __init__(self, twitchy):
                super(HelloPlugin, self).__init__(twitchy)
		
                self.registerCommand('hello', self.helloHandler) # respond when '!hello' is at beginning of message
                self.registerTrigger('hi there', self.heyHandler) # respond when 'hi' is anywhere in message
                self.registerForJoinPartNotifications(self.userJoinPart) # Greet a user, or say goodbye
                self.registerForModNotifications(self.modGivenTaken)

        def helloHandler(self, nick, commandArg):
                print("!hello called by "+nick)
                print(commandArg)
                if len(commandArg)>=2:
                        newword=""
                        for i in range(1, len(commandArg)):
                                if i==len(commandArg):
                                        newword+=(commandArg[i])
                                else:
                                        newword+=(commandArg[i]+" ")
                        if commandArg[1].lower()=="boulderbot":
                                self.sendMessage("Hello "+nick+"!")
                        else:
                                self.sendMessage("Hello "+newword+"!")
                else:
                        self.sendMessage("Hello "+ nick +"!")
        def heyHandler(self, nick, fullMsg):
                print("hey there called by " +nick)
                if nick=='tomdiamond':
                        self.sendMessage("Tom has visited your stream, how cool!")
                else:
                        self.sendMessage("Hi there, "+nick+". I'm Boulderbot.")
        
        def userJoinPart(self, nick, isJoining):
                if isJoining:
                        print(nick+" has joined")
                        #self.sendMessage("Welcome "+ nick +"!")
                else:
                        print(nick+" has left")
                        #self.sendMessage("See ya, "+ nick)

        def modGivenTaken(self, nick, modGiven):
                if modGiven:
                        print("Moderator status given to "+ nick)
                        if nick=="Sezco":
                                self.sezcopresent=True
                                print (str(sezcopresent))
                        #self.sendMessage("Run! "+ nick +" has been given moderator powers!")
                else:
                        print("Moderator status removed from "+ nick)
                        if nick=="Sezco":
                                self.sezcopresent=False
                                print (str(sezcopresent))
                        #self.sendMessage("Relax, "+ nick +" has lost moderator powers")
