---
aliases: Measuring Progress, Reporting
---

links: [000_test_plan_contents](000_test_plan_contents.md)
<br><br>

# 14. Measuring Progress and Reporting

> Which test monitoring metrics  will be used for exploratory, regression, E2E testing?

> What types of reports will be helpful and informative for PM, Test Lead, other testers and stakeholders?

> What kind of information will be useful to track overall progress? Can we show  more detailed information on exploratory testing?

> How can we perform on-going comparison of actual progress against the test plan using any test monitoring metrics defined in the test plan?

Below are some  suggestion on how reporting and measuring  progress of testing can be implemented.

## Regression Testing, End-to-End Testing
Reports on regression testing may include:
- **Test session notes**
- **Daily summary.** 
- **Test Run reports** in [Test Management Software](090_test_management.md).
- **Standard monthly regression log**.


## Exploratory Testing, New Functionality, Ad Hoc Testing
Reports related to regression testing may include:
- **Daily summary.** Short summary sent via Slack #testing channel or email  by the end of the day highlighting what features, requirements, functionalities, risks have been covered, has not been covered, any other comments and highlights..
- **Per-feature exploratory testing reports**. Stored  in "features/" folder 
- **Test session reports**. Stored  in  "sessions" folder and based on [Session Based Test Management (SBTM)](https://www.satisfice.com/download/session-based-test-management) approach. Test session is usually between 20-150 min. Test session report may include test charter (mission), start time, duration, testing notes, attached min dmaps, test data. Metadata can be used to utilize scripts and automated reports. 


<br/>
<br/>
___

- links: [Test Plan Contents](000_test_plan_contents.md)
- created: 2021-04-25
- updated: 2021-06-27
