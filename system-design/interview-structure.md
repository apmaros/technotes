# Interview Structure
## Functional Requirements
**API Modeling**
- Define core API endpoints
	- use different methods - GET, POST, PUT
- Demonstrate end-to-end transaction of given endpoints. 
	- what components would be required? 

**State**
- What state will need to be stored?
- What consistency requirements will be on the storage?
	- tweets, booking vs bank transactions
	- can you utilise a single data source?

**Domain Driven Design**
- Have you recognised any clear domain entities?
- Acknowladge blured domain boundaries if any
- Can this help with defining services?

*this is opportunity to introduce core components and simplistic architecture*

**Business Purpose**
Discussing business and revenue model can help to drive some design decisions. e.g. injecting adds into user twitter feed.

**Authentication**
- How will user be authenticated?
- OAuth, in-house, external?

## Nonfunctional Requirements
**Scale**
- How many users
- Read vs Write heavy
- User interaction rate - e.g. a number of posts
- back of an envelope calculations

*Update system diagram with components adapted for scale*

**Consistency**
Evaluate consistency requirements for different parts of the system. Does everyting require to be synchronous and strongly consistent?

**Failure Tolerance**
- is there a single point of failure?

**Tracing, Monitoring and Alerting**
- as progressing system design keep:
  - describing custom system metrics
  - describing custom business metrics

- what metrics are measured for every component
- touch on alerting

**Extra**
- CI/CD:
  - every release is automatically deployed
- Software security monitoring:
  - code dependencies are periodically analysed for vulnerabilityies
- Dependency freshness:
  - sourcode will be periodically checked for updates

At the end summarise best practices for monitoring and alerting
