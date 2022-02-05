# **TwitchApiPython**

`TwitchApiPy` is a library that allow you to use the Twitch API easier.

# **Install Guide**
You can install this library by `pip install TwitchApiPy`.

# **Usage and an example**

```python
from TwitchApiPy.TwitchApiPy import TwitchApiPy

#Configration
api = TwitchApiPy()
api.ClientID = "YOURCLIENTID"
api.OAuth = "YOUROAUTH"

#Example Commands
FollowerCount = api.GetFollowerCount("Channel Name")

#This returns a dictionary you can use the data you want from there
ChannelStatus = api.GetChannelStatus("Channel Name")

#This returns a dictionary you can use the data you want from there
ChannelInfo = api.GetChannelInfo("Channel Name")
```

# **Contributing The Project**

You can always pull request to this repo, if you report or fix a bug or if you add more functions to project i'll be happy, enjoy.

# **Note**

This Project have only 3 functions for now, you can use all the 3 commands on any channel because i didn't add any command that needs moderater permissions.




