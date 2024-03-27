# event-driven-dms-failure-alerts
event-driven-dms-failure-alerts

![image](https://github.com/soumilshah1995/event-driven-dms-failure-alerts/assets/39345855/c1355ef2-c3c4-4398-b125-19464e846ba4)

# Steps to deploy 

#### Step 1: Edit ENV
```
ACCOUNT=XXXXX
TopicName=dms-status-topics


DEV_ACCESS_KEY=XXXXXXXXX
DEV_SECRET_KEY=XXX
DEV_REGION=us-east-1
```

### step 2: Edit Email Addrees in serverless.yml
```
    MySubscription:
      Type: AWS::SNS::Subscription
      Properties:
        Endpoint: <ADD EMAIL HERE>
        Protocol: email
        TopicArn: !Ref 'SNSTopic'
```

### Step 2 Deploy stack 
```
sls deploy
```

