# clickhouse-tracker

Event example

```json
{
  "$type": "login",
  "$ip": "114.122.71.102",
  "$os": "Android",
  "$lib": "web",
  "$host": "dashboard.mantap.id",
  "$time": 1612242493.864,
  "token": "YV6_jFlg7VwAQZPKkIKT_zU6K8LWjfhFIPj_8ixFvfs",
  "$device": "Android",
  "$browser": "Chrome",
  "$pathname": "/masuk",
  "$referrer": "https://www.mantap.id/",
  "$device_id": "1775b4c6d27106-016e1e87e9d9fd-3b0d3c17-3f480-1775b4c6d289e",
  "$current_url": "https://dashboard.mantap.id/masuk",
  "$lib_version": "1.8.3",
  "$screen_width": 360,
  "$screen_height": 720,
  "$search_engine": "google",
  "$browser_version": 87,
  "$initial_referrer": "https://www.google.com/",
  "$referring_domain": "www.mantap.id",
  "$initial_referring_domain": "www.google.com"
}
```

TODO:

- [ ] server implementation

- [ ] client implementation

- [ ] client security

# server

## endpoints

### POST /init

….

### POST /capture

….

## limitations

clickhouse doesn’t support small inserts. so inserts need to be batched/buffered somewhere minimal 1000 rows.

normally people use kafka, but I intend to use redis or buffered table for lesser complexity

# client:

### init

`client.init("<api_key>", {api_host: '<instance_address>'});`

desugars to

`requests.post('<instance_address>/init?api_key=api_key')`

returns

token yang dipegang client

### capture

`client.capture(user_id, '[event-name]', {property1: 'value', property2: 'another value'});`

desugars to

`requests.post('<instance_address>/capture', {"$type": "event-name", })`

states

-
