---
layout: post
title: "Interview Questions"
date: 2014-02-22 1:00
category: Interview
tags: [Interview, Programming, Electrical Engineering]
---

# Introduction

This is a collection of questions that I have encountered during job interviews.
The technical questions are related to Electrical Engineering and Programming.
And included are notes describing how I would answer a question as
well as what I am looking for in an answer.

# Questions For Managers

1. I have read several books related to project management which align
with my idea of an ideal workplace.  Tell me if you have read any of
the following:
  1. Peopleware by Tom DeMarco
  1. Drive by Daniel Pink
  1. Getting Things Done by David Allen
  1. The Mythical Man Month by Frederick P. Brooks

1. If you could implement a change which would significantly increase
productivity of your employees but which would also limit the control
you have over them, would you do it?
  - Poor managers tend to fear any loss of control or authority.
  - Good managers cultivate an environment where their employees can
    succeed and do not fear of a loss of control.
  - (See Peopleware by Tom DeMarco for a detailed discussion)

1. A project in development has two alternatives: A and B.
Alternative A has been in development for several months and is having
lots of problems.  It has been decided by you and several other
managers that B is a poor alternative that all development should proceed on A.
One of the employees on the project is skeptical and decides to try out
B in his spare time.
Surprisingly, he determines that B is vastly superior to A in every respect.
He presents his findings at the next weekly meeting
where he argues that the decision made by you and the other
managers was flawed and that all development on A should
cease in favor of B.<br>
How do you respond to this?

  A manager with a big ego and control issues will see this as an attack
  upon their authority.  And they will likely punish the employee.

  A good manager will thank the employee and switch development to B.

1. Your company uses Linux and other open source software.
Does it contribute anything back to the community?

  They should feel obligated to contribute back to the community.
  If their changes are used in a product and not being made public this
  could be a licensing issue as well.

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
  market.  Past expenses should not influence the decision.

# Questions From Managers

1. Where do you see yourself in 5 years?

  (A person should have some specific goal for the future.)

1. Do you have any questions for me?

  (Having lots of questions helps to show interest.)

  (see Questions For Managers section)

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

  When using Gcc the Valgrind program is great for tracking down
  hard to find memory leaks.

1. Tell me about a challenging problem that kept you up at night.

1. Why did you choose Electrical Engineering?

  I chose Electrical Engineering because it was the most challenging
  degree among the areas I was interested in (electronics and programming).
  I enjoy programming but Computer Science was not challenging enough.

1. Plot the magnitude of a 16-bit signed and unsigned number.

[Magnitude of Signed/Unsigned 16-bit](/programming/2014/01/17/sign_magnitude.html)

# Questions For Electrical Engineers and Programmers

1. Have you ever written good quality C code that used a goto statement?

  The general rule is to never use goto statements.
  But in Linux device drivers they are used to undo allocated resources
  during module insertion.
  This is the one place where a goto is acceptable.

1. You are writing a program to interface the PCIe bus and you have two
design alternatives.  The first transfers the data to a shared
buffer in memory.  The second uses a file and data is read in from a
file handle.  The fastest solution is the preferred one.  Which do you choose?

  "Premature optimization is the root of all evil." - Donald Knuth

  Without profiling the program it is unknown whether either of these
  choices would make any difference.  The bottle neck might be somewhere
  else entirely in which case this optimization would be a waste to time.

  Programs should be written to maximize maintainability first.
  Then, only after profiling the code, should optimization be performed.

# Questions For Others, General

1. What surprised you the most about working here that you did
not anticipate before you were hired?

1. What is a typical day for you like?

1. Are you allowed any time to work on your own ideas?

  Google 20% time.  A great way to keep employees enthusiastic
  about the projects they are working on.  And the company often
  benefits from their good ideas.

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

