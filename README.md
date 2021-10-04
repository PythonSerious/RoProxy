# RoProxy
## A Discord webhook proxy passthrough for roblox.


### Demo

Post to: `http://<your-server-ip>:<your-port (default: 80)>/webhook`

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
  ```

### Lua Demo
```lua
local data = {
    ["payload"] = {
        ["content"] = "Test Content.",
        ["embeds"] = {
            {
            ["title"] = "Test Title.",
                        
            }
                        
        }
    },
    ["payloadurl"] = "WEBHOOK-URL-HERE"
    }
```
