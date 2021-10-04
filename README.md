# RoProxy
## A Discord webhook proxy passthrough for roblox.


# Setup

Your port and endpoint are in the config.json, make sure both app.py and config.json are in the same folder.
```json
{
  "port": 80,
  "endpoint": "webhook"
}
```
If you want just to post directly to the ip and port with no ``/webhook`` or any other endpoint leave no text in the quotes for endpoint.

***DO NOT INCLUDE A `/` IN THE ENDPOINT CONFIG.***

### Demo

Post to: `http://<your-server-ip>:<your-port (default: 80)>/<your endpoint>`

Your payload should look something like this:

  ```json
  {
    "payload": {
        "content": "Cont Test",
        "embeds":[
           {
               "fields": [
                   {
                      "name": "Field name.",
                      "value": "Field value.",
                      "inline": false
                   }
               ]
           }
       ]
    },

    "payloadurl": "YOUR-WEBHOOK-URL"
  }
  ```

### Lua Demo
```lua
local Data = {
    ["payload"] = {
        ["content"] = "Cont Test",
        ["embeds"] = {
            ["fields"] = {
                {
                    ["name"] = "Field name",
                    ["value"] = "Field value",
                    ["inline"] = false
                }
            },
        },
    },
    ["payloadurl"] = "YOUR-WEBHOOK-URL"
}
```
