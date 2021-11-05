# RoProxy

<img width=200px height=200px align="right" src="https://github.com/PythonSerious/RoProxy/blob/main/image.png?raw=true">

![Build Passing](https://app.travis-ci.com/PythonSerious/RoProxy.svg?branch=main&status=passed)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FPythonSerious%2FRoProxy)

## A simple Discord webhook proxy passthrough for roblox.


# Setup

To install on your own server: `git clone https://github.com/PythonSerious/RoProxy.git`


Your port and endpoint are in the config.json, make sure both app.py and config.json are in the same folder.
```json
{
  "port": 80,
  "endpoint": "webhook"
}
```
If you want just to post directly to the ip and port with no ``/webhook`` or any other endpoint leave no text in the quotes for endpoint.

***DO NOT INCLUDE A `/` AT THE BEGINNING OF THE ENDPOINT CONFIG.***

YES: `"webhook"`, `"subdirectory/webhook"`

NO: `"/webhook"`, `"/subdirectory/webhook"`

### Demo

Post to: `http://<your-server-ip>:<your-port (default: 80)>/<your-endpoint (default: webhook)>`

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



