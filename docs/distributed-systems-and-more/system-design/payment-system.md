# Payment System

## Functional Requirements

## System Design

### API

`POST /v1/payment`

parameters:

| field | type | note |
| -------| ---- | -----|
| sender | json | information about the buyer |
| orders | [json] | list of orders |
| payment_id | string/bytes | for payment |
| payment_method | json | information about the payment method e.g. credit card details |

orders:

|  field | type | note  |
| -------| ---- | ----- |
| receiver | json | describes the receiver of given order |
| order_item | json | describes the purchased item |
| amount | string |
| currency | string |

![payment sstem system design diagram](../_assets/payment-system/payment-system.png)