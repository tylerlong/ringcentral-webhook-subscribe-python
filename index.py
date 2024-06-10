from ringcentral import SDK
import os

sdk = SDK(os.environ['RINGCENTRAL_CLIENT_ID'],
        os.environ["RINGCENTRAL_CLIENT_SECRET"],
        os.environ["RINGCENTRAL_SERVER_URL"],)
platform = sdk.platform()
platform.login(jwt=os.environ["RINGCENTRAL_JWT_TOKEN"])

eventFilters = ['/restapi/v1.0/account/~/extension/~/message-store/instant?type=SMS']
bodyParams = {
    'eventFilters' : eventFilters,
    'deliveryMode': {
        'transportType': 'WebHook',
        'address': 'https://75c7-67-160-244-146.ngrok-free.app'
    },
    'expiresIn': 3600
}
endpoint = "/restapi/v1.0/subscription"
resp = platform.post(endpoint, bodyParams)
jsonObj = resp.json()
print (f"Subscription id: {jsonObj.id}")
print ("Ready to receive incoming SMS via WebHook.")
