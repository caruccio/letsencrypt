Example usage

```
$ oc -n mateus run letsenc --image=caruccio/letsencrypt \
    --env=DOMAIN_NAME=php.caruccio.com \
    --env=INCLUDE_WWW=false \
    --labels="app=letsenc,domain=php.caruccio.com" \
    --replicas=0

$ oc -n mateus expose --port=8080 dc/letsenc
$ oc -n mateus expose --port=8080 svc/letsenc --path=/.well-known --hostname=php.caruccio.com
$ oc -n mateus scale --replicas=1 dc/letsenc
$ oc logs -f dc/letsenc
```

Clean up

```
$ oc -n mateus delete route/letsenc svc/letsenc dc/letsenc
```

TODO: automatic route creation
