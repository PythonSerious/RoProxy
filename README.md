# RoProxy
## A Discord webhook proxy passthrough for roblox.


### Demo

Your payload should look something like this:

  ```json
  {
    "payload": {
        "content": "test",
        "embeds":[
           {
               "title":"Test embed"
           }
       ]
    },

    "payloadurl": "YOUR-WEBHOOK-URL"
  }
