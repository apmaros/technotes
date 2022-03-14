# Interview Structure
## Functional Requirements
**API**
- Define core API endpoints
	- use different methods - GET, POST, PUT
- Demonstrate end-to-end transaction of given endpoints. 
	- what components would be required? 
	- is state required?

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

**Consistency**
Evaluate consistency requirements for different parts of the system. Does everyting require to be synchronous and strongly consistent?

**Failure Tolerance**
 *tbd*


*Update system diagram with components adapted for scale*