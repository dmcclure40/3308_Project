# LeapArm
Group project for CSCI 3308

##Team Members:
* Adam Heaton - MonumentToAllYourSins
* Davis McClure - dmcclure40
* Nhi Nguyen - nhng5827
* Nicky Schardt - Ninjahampster611
* Tyler Lugger - tylu3495

##Description:

The Leap Motion controlled Robotic Arm will use the movements of a user's hand to move a robotic arm. The Leap motion detects hand movements in all directions that will be mapped to the three axis that a robotic arm will move. A Raspberry Pi will be used as the medium between the input device as the Leap Motion and the output device as the Arm. This could potentially be used for precise movements for people that do not have the strength, or ability to perform a task using their own arm. 

##Vision Statement:

Controlling an artificial limb in a natural way.

##Motivation:

This project would solve a problem that does not yet have an easy solution. Users will be able to control a non-natural robotic limb in a very natural way. This project could also be further developed and improved upon later in our college careers to do more and work better.

##Risks:
* Being new to working with Raspberry Pi.
* Timeline to finish working project may be too short.
* Expenses for a robotic arm may be difficult to invest in.

##Risk Mitigation Strategy:
* Read up on and become familiar with Raspberry Pi.
* Make sure we are communicating well and exchanging schedules.
* Use inexpensive arm parts such as legos.
* Leap Motion has provided a lot of documentation on how to use their device for projects: https://developer.leapmotion.com/documentation/python/index.html

##Requirements:

###User Requirements###

Requirement Number| Description|Size (hours)
---------|--------|------------
1.0 | As a User, I want to pick up and move an object | 8
2.0 | As a User, I want to be able to turn the device on and off | 1
3.0 | As a User, I want to be able to pick up a variety of objects | 8
4.0 | As a User, I want intuitive control so I don't need to learn new skills | 5

###Functional Requirements###

Requirement Number| Description | Size (hours)
---------|--------|-----------
1.0 | As a developer, the arm uses a Lead motion tracking device for input | 4
2.0 | As a developer, Leap input should communicate with arm quickly | 5
3.0 | As a developer, the arm must have 3 joints | 2
4.0 | As a developer, the end must have a grabber / pincer| 2
5.0 | As a developer, the arm should be able to pick objects up | 7
6.0 | As a developer, the arm should be able to rotate on 3 axis | 6
7.0 | As a developer, each limb/joint can move individually | 5
8.0 | As a developer, basic hand movements should translate to arm movements | 8

###Non-Functional Requirements###

Requirement Number| Description | Size (hours)
---------|--------|---------------
1.0 | As a developer, the arm must have fluid, non-abrupt motions | 4
2.0 | As a developer, latency between inputs and the arm must be short | 7

##Methodology

We'll start using Waterfall, then once we have basic functionaloity we'll use Agile to implement our remaining requirements

##Project Plan:

![leaparm](https://cloud.githubusercontent.com/assets/3279958/13099364/79832088-d4ee-11e5-8a92-9ff2ca5b5d4a.JPG)
