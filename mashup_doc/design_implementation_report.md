# Design and Implementation Report

## Design

According to the schematic given in teacher's requirements, the app should be a mashup of an city's information from multiple perspectives.

### Perspectives

What perspectives exactly is needed in a mashup application like this? The schematic teacher provided includes the following:

* City Brief Information
* Economy
* Environment
* Society
* Technology
* City Data
* Map

From these I refined my design and provide the following:

* City Brief Information
* GDP
* Weather and AQI
* City News
* City Position on Map

## Implementation

I use `flask` as my backend framework, partly because I worked with it few times earlier and it's light-weight enough to describe just a few APIs.

For frontend, I have no choice but to use `Vue` and `Element UI` as I'm totally inexperienced in frontend developmenting field.

In backend, I try to scrap information from Baidu as I can't find APIs that fulfill my needs. (That's also why sometimes all the things go wrong :>)

In frontend, I implemented loading animation and error handling when things goes wrong. :/ pops up if you did bad things.
