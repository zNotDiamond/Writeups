#TryHackMe


Task 1:
- Which of the following options better represents the process where you simulate a hacker’s actions to find vulnerabilities in a system?

Answer : `Offensive Security`

Task 2:
- Start the lab
- What is your bank account number in the FakeBank web application?
Answer : `8881` (visible on the app’s top-left corner)

- In this case it is being used without using a specified wordlist and using its own standard wordlist located at /usr/share/dirb/wordlists/common.txt (which may not be an effective one).
- Use it like so (via terminal): dirb http://fakebank.thm
- Two directories were found:
— http://fakebank.thm/bank-deposit
— http://fakebank.thm/images

Input the green words as the answer to this question (all in uppercase).
Answer : `BANK-HACKED`

DIRB is a tool used in cybersecurity to find hidden directories and files on a website.
