Week 1 Deliverables

Overview: In this week, you have set-up your Python Environment. The Lab for this week demonstrates
your first use of this environment with a fairly simple Python application. You will also use pylint to
verify your code is using professional coding style and standards.

Submission requirements include 2 files. (Zipping them into one file is acceptable):
• Python Voter Registration Application Code (python code)
• Word or PDF file containing your test and pylint results

Python Applications for Lab1: (total 100 points):
This lab consists of two parts. The first exercise produces a voter registration application asking the user
a few simple questions followed by a confirmation of registration, provided the user is eligible. The
second part documents your testing and pylint analysis results.

1. Using your Python programming environment, write a Python application that supports voter
registration. The application will launch and run from the command line prompt. The application will
prompt the user for their first name, last name, age, country of citizenship, state of residence and
zipcode. To be a valid registration all fields must be entered. If they are at least 18 years old and a U.S
citizen, they can move forward and be prompted for the remaining questions and register to vote. If not,
they should not be presented with the additional questions. There should be some error checking logic
on the input statements to make sure the age numbers entered seem reasonable (e.g. a person is
probably not > 120 years) and states should be 2 letters representing only valid U.S. States. The
application should prompt the user for the needed questions to complete the registration and reprompt when data is invalid giving the user the opportunity to retry. The output should summarize the
input data and congratulate the user if they are eligible to vote and entered all of the data. The user
should be given options to exit the program at any time to cancel the registration process

Hints:
1. Be sure to add logic to test for continuing the registration process.
2. Validate data is valid on entry (e.g. all fields have input data, age seems correct, states seem
correct.)
3. Test with many combinations. For example, what happens if you enter invalid data? Exit the
application at any point, or aren’t 18 years old?
4. Use comments to document your code
5. Use pylint to verify the code style – the goal is a 10!

2. Document your test results for each application within your programming environment. You should
also include and discuss your pylint results for each application. The test document should include a test
table that includes the input values, the expected results and the actual results. A screen capture should
be included that shows the actual test results of running each test case found in the test table. Be sure
to include multiple test cases to provide full coverage for all code. For example, you should demonstrate
each set of logic in the code works as expected and every statement in the code is reached through the
test cases
