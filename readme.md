# Sync Ubuntu Screenshots to Imgur
(Tested on python3 and Ubuntu 18.04)
## Requirements
* Python3
* pyimgur (pip3 install pyimgur)

## Steps to use
* Login to imgur and create a new Album (aka post) and add it's id to sync.py file (all screenshots will be added to this album)
* Create an App on Imgur [Link here](https://api.imgur.com/oauth2/addclient)
* Choose without Redirect Url option
* Generate Access Tokens by choosing REQUESTED_RESPONSE_TYPE = token [Link here](https://apidocs.imgur.com/?version=latest#authorization-and-oauth)
* Copy these tokens and add them in sync.py file
* Setup Cron to run this python script everyday

## Note:
* Imgur has upload rate limits which might close the script when it exceeds that limit but for uploading screenshots it should be good enough

## Example image: 
![alt text](https://cdn.discordapp.com/attachments/604679204105355264/646047330105032742/unknown.png "Example image")
