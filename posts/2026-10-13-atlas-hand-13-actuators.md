---
title: Why Boston Dynamics Gave Atlas a Four-Finger Hand With No Pinky
date: 2026-10-13
updated: 2026-10-26
category: news
tag: automation
summary: Atlas's new hand has 13 identical sealed actuators and no cables across the joints. Here is how direct, backdrivable actuation works, and why dropping the pinky was an engineering decision.
seo_title: Atlas Robot Hand: 13 Actuators, Four Fingers, No Pinky
seo_description: Boston Dynamics' new Atlas hand uses 13 sealed backdrivable actuators and no cables. How direct actuation works and why the pinky was dropped.
image: assets/2026-10-13-atlas-hand-actuation.svg
image_alt: Diagram comparing a cable-driven finger with fragile cables across joints to a directly actuated finger with an encapsulated actuator in each joint, plus the 13 degrees of freedom split of thumb and three fingers
image_credit: Diagram: Engine-X
keywords: humanoid robot hand, backdrivable actuator, degrees of freedom, direct drive robot finger, Atlas robot hand, tendon-driven vs direct actuation
tldr: Boston Dynamics chose 13 identical sealed actuators and no pinky to make Atlas's hand simpler, repairable and easy to simulate, trading a little human-likeness for reliability.
takeaways:
- The new Atlas hand has four fingers and 13 degrees of freedom, up from 7 in the previous hand.
- Every joint is driven directly by the same type of fully enclosed actuator, so no fragile cables cross the joints.
- Backdrivable actuators let the hand feel contact through its own motors and make simulation more accurate for reinforcement learning.
- A pinky would have needed three more actuators, so the team judged it not worth the cost, size and power.
faq:
- What does "degrees of freedom" mean for a robot hand? | It is the number of independent ways the hand can move, usually one per powered joint axis. The new Atlas hand has 13: four in the thumb and three in each of the other three fingers.
- What is a backdrivable actuator? | One where an outside force can push the output and move the motor, so the joint gives way instead of locking. This lets the robot sense and absorb contact through the actuator itself.
- Why did Boston Dynamics leave out the pinky? | The team said a pinky would add three more actuators plus size, cost and power draw, and tests showed the hand did not need it for tool tasks.
sources:
- The Robot Report — Boston Dynamics drops the pinkie on new humanoid hand (1 Oct 2026) | https://www.therobotreport.com/boston-dynamics-drops-pinkie-on-new-humanoid-hand/
- The Robot Report — Boston Dynamics gives more insight into its redesigned humanoid hand (9 Oct 2026) | https://www.therobotreport.com/boston-dynamics-gives-more-insight-into-its-redesigned-humanoid-hand/
- Interesting Engineering — Boston Dynamics 13-DOF robot hand (2 Oct 2026) | https://interestingengineering.com/ai-robotics/boston-dynamics-13-dof-robot-hand
- Robotics & Automation News — Boston Dynamics unveils new four-finger hand for Atlas (2 Oct 2026) | https://roboticsandautomationnews.com/2026/10/02/boston-dynamics-unveils-new-four-finger-hand-for-atlas-humanoid-robot/105440/
- Robotics 24/7 — Boston Dynamics unveils new dexterous hands for Atlas (2 Oct 2026) | https://www.robotics247.com/article/boston-dynamics-unveils-new-dexterous-hands-for-atlas-humanoid-robot
---
Boston Dynamics has shown a redesigned hand for its Atlas humanoid, and the headline detail is what is missing: [the hand has four fingers and no pinky](https://www.therobotreport.com/boston-dynamics-drops-pinkie-on-new-humanoid-hand/). It has 13 degrees of freedom, up from seven before, and in a [follow-up interview](https://www.therobotreport.com/boston-dynamics-gives-more-insight-into-its-redesigned-humanoid-hand/) the Atlas behaviour lead explained the thinking behind it.

The story is less about robot fingers and more about a classic mechanical trade-off: how many moving parts can you afford, and where do you put them?

## What do 13 degrees of freedom mean in a robot hand?

A degree of freedom (DOF) is one independent way a mechanism can move. In a robot hand that is usually one powered joint axis. According to the reporting, the thumb has four DOF and each of the three fingers has three, which lets the fingers splay sideways and lets the thumb slide along the other fingers. Those motions allow pinch grasps, three-finger grasps and holding a triggered tool such as a drill or grinder.

Every extra DOF needs an actuator, wiring, sensing and space. [Boston Dynamics said](https://roboticsandautomationnews.com/2026/10/02/boston-dynamics-unveils-new-four-finger-hand-for-atlas-humanoid-robot/105440/) a pinky would have needed three more actuators. The hand is about the size of a large human hand, so there is simply no room to keep adding motors.

## Why does the Atlas hand avoid cables?

The Atlas hand avoids cables because they stretch, fray and loosen; each joint gets its own sealed actuator instead. Many robot hands copy the human arrangement: motors sit in the forearm and pull cables (tendons) that run through the finger to bend each joint. It is compact at the fingertip, but cables stretch, fray, rub and loosen, and every joint they cross changes the tension on the others.

Atlas takes the opposite route. Each joint is driven by its own actuator, and the reporting says all 13 are the same type and [completely encapsulated](https://www.robotics247.com/article/boston-dynamics-unveils-new-dexterous-hands-for-atlas-humanoid-robot), with no cables crossing joints. The result is:

1. **Fewer failure points.** A sealed actuator is one part to swap, rather than a bundle of cables to re-tension.
2. **One part number.** Thirteen identical actuators simplify manufacturing and spares.
3. **A cleaner force path.** The torque at the joint is what the motor makes, minus a known amount of friction, instead of a number blurred by cable stretch.

The strength target stayed roughly the same as the previous hand, which belongs to a robot that carried a loaded mini-fridge of over 100 lb.

## What is a backdrivable actuator, and why does it matter?

A backdrivable actuator is one where an outside push on the output can turn the motor back. Think of a self-locking worm gear on a valve operator: it holds position and the handwheel cannot be driven from the stem side. That is exactly what you do *not* want in a finger. A backdrivable joint gives way when it hits something, and the controller can read that push from the motor itself.

Boston Dynamics says the actuation and transmission are designed for this transparency, with control software compensating for friction and cogging that remain. Two benefits follow. The hand can sense contact through its own joints, and the actuator behaves predictably enough to simulate accurately, which the team says makes reinforcement-learning training for dexterous tasks more effective. The company has also described dense pressure sensors on the fingertips and palm, though sources differ on how much detail was disclosed.

## Why does the Atlas robot hand have no pinky?

The Atlas hand has no pinky because Boston Dynamics found the robot's tasks did not need one. Rodriguez's team tested the question rather than guessing. Reports say the chief product and technology officer had engineers tape two fingers together for a day, and the team concluded a pinky was not needed for the tasks Atlas does, such as handling cables, "fishing" for screws and using power tools. Dropping it saves actuators, mass and power. A two-thumb design, which would have allowed one assembly line for both hands, was also rejected for adding DOF, cost and volume.

The hand is being used extensively at the company's headquarters but, per the same interview, [is not yet on the whole fleet](https://www.therobotreport.com/boston-dynamics-gives-more-insight-into-its-redesigned-humanoid-hand/). No production figures or durability data have been published, so long-term reliability is still unproven.

## The engineering takeaway

This is design-for-manufacture and design-for-maintenance thinking applied to a hand. In my work with valves and piping, a component that looks clever but cannot be reached or replaced quickly tends to become the problem. Boston Dynamics chose identical, sealed, replaceable modules and accepted a hand that is less human, because it is easier to build, repair and simulate. For related reading on how automation is spreading into inspection work, see [robots inspecting ships](https://engx3d.com/blog/posts/2026-10-11-robots-inspecting-ships.html).
