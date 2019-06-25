# Multi-source Event Coalescing
-Event data coming from logs such as server logs, windows or linux logs etc are very common
in an infrastructure management world. Often multiple events across logs refer to the same problem.
Matching these events is key to reducing noise. Given a set of event data,
find events that are similar based on inherent patterns in them.
*similar based on inherent patterns*
-Events come from varying sources and have different structures of key:value pairs in a JSON format.
Given an incoming event, you are required to find other events that have occurred in the past
that this one is a close match to. In order to do this, you have to
generate a signature of events based on the key:value pairs within it.
Identifying these matches across 1000s of events is where the computational challenge is.
