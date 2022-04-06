# News Feed

## Functional Requirements

### Questions

- Q: What platform is this build for desktop, or mobile?
  A: Both

- Q: What are the key features?
  A: Be able to post a news and read a feed of news

- Q: How many connections can user have?
  A: 5000

- Q: What is the traffic volume?
  A: 10mil DAU

## Design

There are 2 user flows we will discuss:

- Feed publishing
- Feed building - posts in the feed need to be ordered in reverse chronological order

## Feed publishing flow

API: `POST /api/v1/user/feed`

### Fanout on Write

Push the post to all followers feeds

### Fanout on Read

On each read, user pulls new posts from the users they follow

### Combination Fanout on Write and Read

Design priority is to be able to retrieve posts fast and thats why we choose fanout on write.
There are following inefficiencies that we need to address:
  
- popular users with too many followers create hotposts and high load on the system. Fanning out their post on write would be unefficient and would not scale well
- there is little value in updating newsfeeds of inactive users.

For these usecases we use fanout on read. This information will be defined in the User database.

### Key Components

#### feed-api

- expose a public api used by mobile and desktop clients
- provides basic validation
- dispatch to the right backend

##### API

- `POST /user/feed`
  - parameters:
    - media-type: string enum (text/bytes/...)
    - content: text/image-jpg/video/...
  - header:
    - Authorization: token
- `GET /user/feed`
  - header:
    - Authorization: token

#### post-service

- stores the post to post database
- fetches user information:
  - who are the followers
  - what privacy settings has the users
- applies post privacy settings
- fans out the post to given follwers
  - 1 post -> n user-id:post-id

#### newsfeed-fanout-worker

- pushes the post to the newsfeed-cache

##### Example of the cache

Bob sends message "hello world" with id IDX and Bob has followers John and Alice:

(Alice) 0001: [IDX, IDA]
(John)  0002: [IDX, IDB, IDC]

![news feed system design](../_assets/news-feed/news-feed-system-design.png)
