# **Product Backlog: Bristol Regional Food Network**

**Current State:** End of Sprint 1 (Entering Detailed Modeling/Automation)

*This backlog factors in technical dependencies and ranks features(1 to 10) so the rest of the team knows exactly the order in which we can design the system.*

| **Rank** | **Feature Name** | **MoSCoW Priority** | **Dependency** | 
| :--- | :--- | :--- | :--- | 
| **1** | Product Catalog & Search | Must Have | Core foundation: Customers cannot have a multi-vendor cart without finding produce first. | 
| **2** | Multi-Vendor Shopping Cart | Must Have | Prerequisite for checkout: Must combine items from different vendors into a single session before payment. | 
| **3** | Secure Single-Transaction Checkout | Must Have | Core operational process: Payment must succeed before any order details can be routed to vendors. | 
| **4** | Automated 5% Commission Deduction | Must Have | Must be calculated in the engine immediately after successful checkout and before distributing funds. | 
| **5** | Split Delivery/Collection Instructions | Must Have | Post-checkout: Customers must be notified how they will receive their order from the different vendors they purchased from. (delivery/collection details) | 
| **6** | Partial Order Failure (Exception Handling) | Must Have | Required for advanced Camunda modeling: Proves that the system can issue partial refunds if a single vendor rejects a part of a multi-vendor order. | 
| **7** | Product Traceability & Safety Data | Should Have | Enhances the catalog (Rank 1): Displays additional details like harvest dates and allergen warnings. (required) | 
| **8** | Consolidated Delivery Synchronization | Should Have | Built on top of basic logistics (Rank 5): Calculates a single delivery window based on the 48-hour minimum lead time across multiple farms. | 
| **9** | Postcode-based "Food Miles" | Could Have | Extra sustainability feature: Added to the checkout flow only after the core payment routing (Rank 3) is stable. | 
| **10** | Dynamic Surplus Integration | Could Have | Complex case for waste reduction: Requires active orders in the system before being able to offer discounts to customers for unbought produce. | 
