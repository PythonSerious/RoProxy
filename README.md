# RoProxy
## A Discord webhook proxy passthrough for roblox.


### Demo

Post to: `http://<your-server-ip>:<your-port (default: 80)>/webhook`

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
        ['content'] = "Cont Test",
        ['embeds'] = {
            ['fields'] = {
                {
                    ['name'] = 'Field name',
                    ['value'] = 'Field value',
                    ['inline'] = false
                }
            },
        },
    },
    ["payloadurl"] = 'YOUR-WEBHOOK-URL'
}
```
