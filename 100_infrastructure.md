---
aliases: [Infrastructure]
---

<br/>
<br/>

# Infrastructure


- **Dev** 
	- The development environment is the location of the main branch of a software application. 
	- Testing levels and types: unit testing.
- **UAT / Testing - app.website.com**
	- Dedicated environment that is used primarily for manual testing.e
	- Testing levels and types: Integration, UAT, Exploratory, E2E, Regression, Acceptance, Security, Adhoc. 
- **Staging - app.website.com**
	- Simulates production as much as possible. The staging environment is restricted to a few select people. 
	- Testing levels and types: acceptance testing some of features, migration testing.
- **Production - website.com**
	- An environment where the application is available for business use by clients. 
	- Testing levels and types: unit testing, acceptance testing some of features, migration testing. Feature flags are used to show a few specific users a feature or version of an application.

<br/>
<br/>

___

links: [Test Plan Contents](000_test_plan_contents.md)
created: 2021-04-25
updated: 2021-06-12
