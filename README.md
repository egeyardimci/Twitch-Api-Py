# **TwitchApiPython**

`TwitchApiPy` is a library that allow you to use the Twitch api easier.

# **Install Guide**
You can install this library by `pip install TwitchApiPy`.

# **Usage and an example**

```python
from TwitchApiPy import TwitchApiPy

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

This Project has only 3 functions for now you can use all of the commands on any channel i didn't add moderation commands yet.




