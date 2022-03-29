# Notification System
## Functional Requirements
- What type of notifications does the system supports?
- What is the latency for a message delivery?
- What are the supported devices?
- What triggers the notifications?
- How many notifications are sent daily?

## Simplified Design

Following Diagram demonstrates simple implementation of the notification system
![notification system](../_assets/notification-system/notification-system-simplified-design.png)

### Architecture Problems
- **Single point of failure** - if notification service was to be down, sending notification would not be possible
	- Notification server should be deployed as a cluster with horizontal scaling
- **Performance bottleneck** - processing notifications can be resource intensive on CPU
	- introduce message queue to decouple the system components 
- Uneven spread of the load - different components might be growing in different speed. For example, we might be sending high number of push notifications but only few text messages as they are more expensive.
	- decouple sending notifications to different workers.

## System Design

### API
`[POST] /v1.notifications.mycompany.io/send`

```
{
  "from": { "email": "no-reply@myemail.com" },
  "to": ["email": "bob@myemail.com"],
  "subject": "Hello World!"
  "content": [{
    "type": "text/plain",
    "value": "Hello World"
  }]
}
```

![notification system](../_assets/notification-system/notification-system-system-design-highlevel.png)
