Use this image to generate [Let's Encrypt](https://letsencrypt.org) certificates for your applications on Openshfit.

___Warning: Keep an eye on [rate limits](https://letsencrypt.org/docs/rate-limits/) imposed by Let's Encrypt.___

From within your project, create a new application named `ssl`. If you'd like to suppress certificate for `www`, add `--env=INCLUDE_WWW=false` to command below.

```
$ DOMAIN_NAME=example.com

$ oc run ssl --image=caruccio/letsencrypt \
    --env=DOMAIN_NAME=$DOMAIN_NAME \
    --labels="app=ssl,domain=example.com" \
    --replicas=0
```

Create a Service and Route in order to Letencrypt ACME process reach your new app:

```
$ oc expose --port=8080 dc/ssl
$ oc expose --port=8080 svc/ssl --path=/.well-known --hostname=$DOMAIN_NAME
```

Start the container to initiate the request and validation process:

```
$ oc scale --replicas=1 dc/ssl
$ oc logs -f dc/letsenc
```

If everything goes fine, the `logs` command above presents the newly generated Certificate, Certificate Chain, CSR and Key files. Copy it and save in a safe place because after the pod is destroyed there is no way to retrieve it again other than requesting a new certificate.

Profit!

Clean up
--------

```
$ oc delete {route,svc,dc}/ssl
```

TODO (anyone?)
--------------
- allow testing on stage servers
- automatic route creation and resource cleanup
- auto renew (maybe using {Scheduled|Cron}Jobs)
