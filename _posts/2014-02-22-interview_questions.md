---
layout: post
title: "Interview Questions"
date: 2014-02-22 1:00
category: Interview
tags: [Interview, Programming, Electrical Engineering]
---

# Introduction

This is a collection of questions that I have been asked, or have asked,
during job interviews.
The technical questions are related to Electrical Engineering and Programming.
And included are notes describing how I would answer a question as
well as what I am looking for in an answer.

# Questions For Managers

In general I am looking for a manager who leads has employees and gives
them the freedom to do their best work.

1. If I was hired for this position what would be the first project that
I would work on?

1. What are your favorite books that have influenced your management style?
  1. [Peopleware][pw] by Tom DeMarco
  1. [Drive][drv] by Daniel Pink
  1. Getting Things Done by David Allen
  1. The Mythical Man Month by Frederick P. Brooks

  [pw]: http://books.google.com/books?id=TVQUAAAAQBAJ
  [drv]: http://books.google.com/books?id=A-agLi2ldB4C

1. Tell me about a time when there was a disagreement among your employees.
  - Was he able to convince them without asserting his authority?

1. Tell me about a time when one of your employees disagreed with you.
  - Was he able to convince them without asserting his authority?

1. (similar) Have you ever had to tell an employee to do something that
they disagreed with you about?

1. If an employee did something different than what you told them to do,
how would you respond?
  - Does he trust his employees?
  - Or is he threatened by a loss of control?

1. (follow up) What if the solution they came up with was significantly better?

1. If you had no authority over your employees would they still do what
you ask?
  - A boss or a leader?
  - A boss leverages his authority to force employees to do what he wants.
  - People will follow a leader even if they have no authority.

1. Tell me about a situation when you were wrong.

# Questions From Managers

1. Where do you see yourself in 5 years?
  - Should have a specific goal that they are trying to achieve.  And
    the position being sought should aligh with that goal.

1. Do you have any questions for me?
  - Should have lots of questions which shows an interest in the company
    and the position.  (see "Questions For Managers" section)

1. Why would you be a good candidate?

  There are many reasons why I would be a good candidate.
  But there are probably only a few that you are interested in.
  Describe to me your ideal candidate and I will tell you if I have
  anything in common.

# Questions From Electrical Engineers and Programmers

1. What is your favorite programming language?

  My favorite language is Lisp because it changed the way I think
  about programming.
  Things such as: Prefix notation, anonymous functions, tail recursion,
  functional programming, macros, linked lists, etc.

1. What is a memory leak?

  A memory leak occurs when memory is allocated but is not freed.
  If this leak occurs inside a loop it can quickly consume all the
  memory in the system.

  Most often this occurs in C when a malloc is performed without a
  corresponding free.  There are also functions which internally
  allocate memory and return a pointer.  These must be freed to avoid
  a leak.

  A good tool for finding memory leaks when using Gcc is Valgrind.

1. Tell me about a challenging problem that kept you up at night.

1. Why did you choose Electrical Engineering?

  I considered several degrees which were of interest to me: Computer
  Science, Computer Engineering and Electrical Engineering.  I already had
  a lot of experience programming so Computer Science would have been the
  least challenging.  However the low level hardware and circuitry was
  interesting to me as well.  I chose EE because it was the most challenging
  degree that was of interest to me.

1. Plot the magnitude of a 16-bit signed and unsigned number.

[Magnitude of Signed/Unsigned 16-bit](/programming/2014/01/17/sign_magnitude.html)

# Questions For Electrical Engineers and Programmers

1. Have you ever written good quality C code that used a goto statement?

  The general rule is to never use goto statements.
  But in Linux device drivers they are used to undo allocated resources
  during module insertion.
  This is the one place where a goto is acceptable.

1. If your manager had no authority to fire you would you still do what he
asks?
  - A boss or a leader?

1. Tell me about a time when you disagreed with your manager.
  - Did his manager assert his authority to get him to do something he
  did not agree with?

# Questions For Others, General

1. What is a typical day for you like?

1. What surprised you the most about working here that you did
not anticipate before you were hired?

1. Are you allowed any time to work on your own ideas?

  Google 20% time.  A great way to keep employees enthusiastic
  about the projects they are working on.  And the company often
  benefits from their good ideas.

1. Tell me about some of the projects you have worked on here.

# Questions From Recruiters

1. Why do you want to work for this company?  Why not competitor X or Y?

  (Tesla)
  The benefits of the electric car on our society is obvious
  (cleaner air, reduced dependence on foreign oil,  more efficient, etc).
  And yet most manufacturers choose not to develop an electric car even though
  they have more than enough resources to do so.
  I don't want to work for any manufacturer where profit is the primary
  goal and the long term health of our society is secondary.

1. Why do you think you would be a good candidate at this company?

