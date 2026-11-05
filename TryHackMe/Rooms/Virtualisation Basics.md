#TryHackMe

What does virtualisation enable multiple applications to share?

Answer: `physical server`

What is the name of the software that manages the resources for each virtual machine?

In previous rooms, you learned what the components of a computer are and how they communicate with each other.
In this room, you will learn how companies have optimized these computer components to reduce costs and build flexible, scalable systems that power the modern internet through a concept known as virtualization.

Have you ever considered how expensive and inefficient it would be if every piece of software or every website required its own physical server?
Virtualization was created to solve exactly this problem.

Think of an apartment building:

- Building: The physical server.
- Apartments: The virtual machines.
- Building manager: The hypervisor.

Each VM operates as a separate system while sharing the underlying hardware.
The hypervisor manages those shared resources.

Multiple workloads can share one physical machine instead of requiring separate servers.
