

# Test Strategy
This is the higher level of the test process. It describes how we will approach testing: ideas, principles, techniques, and motivations that will guide testing.
Mindmap - Test Strategy: link

<br/>

## Why (Goals)
> Why do we test and what does quality mean?

> What are the top 5-6 most important quality aspects?

> What does quality means for our team? 

> Can we get other team members to share their vision of quality? Is quality important?

> Most important quality aspects

> When testing, how do we know what is expected behavior? Acceptance criteria? Is it a good approach (see list below)? What do we miss?


> What does quality means for customers? Can we get feedback from real customers? 
> - Functional: What are the 2-3 most common scenarios/tasks they perform? 
> - Functional: What are the top 2-3 pages / components of the app they use?
> - Functional: What is the most used file format?
> - Functional: What is the most used file size? Max size?
> - Usability: What are the top 2-3 pages / components of the app they use?
> - Performance: How many files are in repository? Uploaded?
> - Compatibility: What are most common environments (OS / Browser)? Can we get estimate?


<br/>

## Why Not (Risks)
> What are the risks? What are examples?

The following types of risks are can be considered:
- Product risks
- Business risks
- Software risks
- Testing Risks

Risks are covered in more details in the [Risk Assessment](040_risk_assessment.md) section.

<br/>

## What
> What do we test? Which parts of the system? 

- **Regression testing**. 
	- Core features and functionality
	- Non-core functionality
- **New features**. 
- **Browsers**.
- **Mobile Devices**. 
- **Special focus** 


<br/>

## Where (Testing Environments)
> Where do we test? What environments do we use for need for testing? 

- **Dev** 
	- The development environment is the location of the main branch of a software application. 
	- Testing: unit testing.
- **UAT / Testing - app.website.com**
	- Dedicated environment that is used primarily for manual testing.
	- Testing: Exploratory, E2E, Regression, Acceptance. 
- **Staging - app.staging-website.com**
	- Simulates production as much as possible. The staging environment is restricted to a few select people. 
	- Testing: acceptance testing some of features, migration testing.
- **Production - website.com** 
	- An environment where the application is available for business use by clients. 
	- Testing: acceptance testing some of features, migration testing. Feature flags are used to show a few specific users a feature or version of an application.

<br/>

## When
> When should we perform manual testing?  Is this a good approach? What should be improved? What should we prioritize? What should we improve / change?

## Manual Testing
- **Weekly (in between or after a successful sprint)**

	*Regression core testing* - testing limited number of user stories around core functionality, starting from high priority tests. 

- **Weekly**

	*Regression non-core testing* - testing  features and executing test cases  outside of new functionality. 

-  **On demand**

	*Regression,  Exploratory, Usability, Acceptance, Compatibility*  - new features,  rewrites, bug fixes. 


- **Before release**

	*E2E*  - the goals are
		- test the entire product from beginning to end to ensure the application flow behaves as expected  
		- test from the end user’s experience by simulating the real user scenario and validating the system under test and its components
		- validate UI.

### Automated Testing
> When and what types of automated testing are currently performed

- **Unit tests** - 
- **Security testing** 
- **Integration testing** 

<br/>

## Who
>  What are roles of the team members involved in testing and QA ?
### Internally
- Project Management
	- Reviews the content of the Test Plan, Test Strategy
	- **Team members:** 
- Test Planning (Test Lead)
	- Provides scope of testing
	- Provides high-level guidance on daily and weekly testing activities.
	- Provide guidelines to create test conditions, test cases, expected results.
	- Provide guidelines on how to manage defects.
	- Attend status meetings.
	- **Team members:** 
- Test Team
	- Develop test conditions, test cases, expected results and execution scripts.
	- Perform execution and validation.
	- Identify, document and prioritize defects.
	- Review and re-test bug fixes.
	- Provide information on status of testing.
	- **Team members:** 
- Development Team
	- Review testing deliverables (questions, cases, expected results, etc.) and provide timely feedback.
	- Assist in the validation of results (if requested).
	- Certify correct components have been delivered to the test environment.
	- Implement fixes to defects.
	- **Team members:** 


>Who else is involved in testing? What role do they play in QA and testing?


### Externally


<br/>

## How

<br/>

###  Currently In Scope

<br/>

### Currently Out of Scope

<br/>

## How much
> Is there any particular cost as a prerequisite?

- Premium Tools
- Knowledge
- Free Tools
