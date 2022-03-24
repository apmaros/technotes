# Interview Structure

## Timing
| Time (min) | Stage                                    |
| -----------| -----------------------------------------|
| 10 - 15    | Understand problem and establish a scope |
| 10 - 15    | Propose high level design and get buy in |
| 10 - 25    | Deep dive into interesting points        |
| 5 -10      | Wrap up                                  |
 
## Understand problem and establish a scope
When discussing initial requirements, it is important to take a deep breath and realize there is no need to rush for the answer.c

The interview is designed to give a specific set of signals at each stage.

### Functional Requirements
**Core Information**


- Ask what are the most important features of the system
	- clarify main properties e.g:
		- is fead reverse chronologically sorted?
		- single user vs group?
- (Reconsider) Demonstrate end-to-end transaction of given endpoints. 
	- what components would be required?

**Business Purpose**


Discussing business and revenue model can help to drive some design decisions. e.g. injecting adds into user twitter feed.

### Non Functional Requirements
- How many users
- Read vs Write heavy
- User interaction rate - e.g. a number of posts
- back of an envelope calculations

## High Level Design
- Come up with initial blueprint for design. This is an initial thought and can evolve as we go.
- Draw main components - Clients, APIs, Servers, Stores, Cache, CDN, message queue, etc
- Go trough few high level use cases
- Back of an envelope calculations
- Design API endpoints if necessary - no useful for high level problems e.g. design Google - this needs communication with the interviewer

**State**


- What state will need to be stored?
- What consistency requirements will be on the storage?
	- tweets, booking vs bank transactions
	- can you utilise a single data source?

**Domain Driven Design**


- Have you recognised any clear domain entities?
- Acknowladge blured domain boundaries if any
- Can this help with defining services?

**Authentication**


- How will user be authenticated?
- OAuth, in-house, external?

## Nonfunctional Requirements


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

