# **MoSCoW Prioritization: Bristol Regional Food Network**

**MoSCoW prioritization** is used as a strategic filter for the product backlog, dictating exactly which core multi-vendor features must be modeled in Camunda first to deliver a viable system before we focus on additional functions.

| **Priority** | **User Story** | **Acceptance criteria** |
| :--- | :--- | :--- |
| **MUST HAVE** | As a customer, I want to browse products organized by categories and use a search bar to find specific items | Features a category navigation menu and a keyword search bar |
| **MUST HAVE** | As the customer, I want to purchase items from multiple vendors with a single transaction | Shopping cart accepts items from various different vendors and processes a single payment for the total |
| **MUST HAVE** | As a customer, I want to see harvest dates, farm origins, organic certification and allergen warnings clearly for each item | Product detail pages display mandatory firlds for harvest date, origin, allergen info. and certification status |
| **MUST HAVE** | As a customer, I want clear instructions on delivery and collection for each vendor in my multi-vendor order so I know how to get my items | The checkout confirmation screen and data flow clearly split the order by supplier and detail specific delivery/collection arrangements for each. |
| **MUST HAVE** | As a customer, I want my multi-vendor checkout to process securely while automatically handling the network's 5% commission in the background. | The Camunda checkout process successfully routes the transaction through a mock payment gateway and automatically calculates the 5% network deduction. |
| **MUST HAVE** | As a customer, I want my order to proceed even if one vendor in my multi-vendor cart rejects their portion, so I receive the rest of my groceries and an automatic partial refund. | The Camunda process utilizes boundary error events to catch a single vendor's rejection, issues a partial refund for that specific amount, and allows the remaining vendors' fulfillment processes to continue. |
| **SHOULD HAVE** | As a customer, I want access to rapid communication channels on the storefront in case I have food safety or quality concerns. | A contact or report feature is integrated into the operational process, directly linking the customer's order to the specific producer. |
| **SHOULD HAVE** | As a customer ordering from three different farms, I want the system to calculate a single, synchronized delivery window so I do not receive three separate drop-offs at different times. | The process engine holds the customer's delivery notification until all individual vendor preparation timers (minimum 48 hours) have elapsed, calculating the latest possible dispatch time for a consolidated route |
| **COULD HAVE** | As a customer, I want to see the "food miles" for my local produce delivery to understand the environmental impact. | The checkout process includes a step that calculates the physical distance between the customer's entered postcode and the farm's origin postcode. |
| **COULD HAVE** | As a customer browsing late in the day, I want to see discounted surplus items so I can purchase affordable food while helping producers reduce waste. |The Camunda process incorporates a timer event that automatically applies a set discount percentage to remaining perishable stock in the system. |

