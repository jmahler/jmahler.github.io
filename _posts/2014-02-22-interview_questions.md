---
layout: post
title: "Interview Questions"
date: 2014-02-22 1:00
category: Interview
tags: [Interview, Programming, Electrical Engineering]
---

# Introduction

This is a collection of questions that I have been asked,
and that have been asked of me, during job interviews.
The technical questions are mostly related to
Electrical Engineering and Programming.
Included are notes describing how I would answer a question as
well as what I am looking for in an answer.

# Questions From Managers

1. Where do you see yourself in 5 years?

  A person should have some sort of specific goal for the future.

1. Do you have any questions for me?

  Having lots of interesting questions helps to show interest.

# Questions For Managers

1. I have read several books related to managing projects which align
with my idea of an ideal workplace.  Tell me if you have read any of
the following:

  1. Peopleware by Tom DeMarco
  1. Drive by Daniel Pink
  1. Getting Things Done by David Allen
  1. The Mythical Man Month by Frederick P. Brooks

1. If you could implement a change which would significantly increase
productivity of your employees but which would also reduce the control
you have over them, would you do it?
  - [Peopleware] Using a gun to lead means you have to "lead" from behind.
  - A good manager could lead even without positional authority.
  - Poor managers tend to fear any loss of control or authority.

1. A project in development has two alternatives: A and B.
Alternative A has been in development for several months and is having
lots of problems.  And it has been decided by the managers that
B is a poor alternative.
An employee on the project has some free time and decides to try alternative
B to see if it is as bad as they say it is.
Surprisingly, alternative B is vastly superior to alternative A
in every respect.
He presents his results at the next weekly meeting and argues that
all development on A should cease in favor of B.<br>
How do you respond to this?

  A manager with a big ego and control issues will see this attack upon
  their authority.  And they will likely punish the employee.

  A good manager will thank the employee and switch development to B.

1. Your company uses Linux and other open source software.
What does it contribute back to the community?

  They should feel obligated to contribute back to the community.
  If their changes are not being made public this could be a licensing
  issue as well.

1. How much does turnover cost you?
  - [Peopleware] Those who try to ignore the problem or believe it is out
	of their control often have no idea how much losing an employee costs.
  - cost of lost work
  - cost of lost knowledge

1. Suppose you have a project that has been in development for over
a year and it looks like it could take another six months or more
to get something working.
And recently an alternative solution became available which was better in
every respect and could be put in to operation in less than a week.
But this new solution requires a one time fee of $10k for use in a
commercial project.
Would you continue development on the old project or switch to the new one?

  sunk costs - The decision should be based upon its value in todays
  market.  Investment costs should not be part of the decision.

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
  allocate memory and return a pointer.  This must be freed to avoid
  a leak.

  When using Gcc the Valgrind program is great for tracking down
  hard to find memory leaks.

1. Tell me about a challenging problem that kept you up at night.

1. Why did you choose Electrical Engineering?

  I chose Electrical Engineering because it was the most challenging
  among my interests (electronics and programming).  I like programming
  but Computer Science was not challenging enough.

1. Plot the magnitude of a 16-bit signed and unsigned number.

[Magnitude of Signed/Unsigned 16-bit](/programming/2014/01/17/sign_magnitude.html)

# Questions For Electrical Engineers and Programmers

1. Have you ever written good quality C code that used a goto statement?

  The general rule is to never use goto statements.
  But in Linux device drivers they are used to undo allocated resources
  during module insertion.
  This is the one place where a goto is acceptable.

# Questions, General

1. What surprised you the most about working here that you did
not anticipate before you were hired?

1. What is a typical day for you like?

1. Are you allowed any time to work on your own ideas?

  Google 20% time.  A great way to keep employees enthusiastic
  about the projects they are working on.  And the company often
  benefits from their good ideas.

