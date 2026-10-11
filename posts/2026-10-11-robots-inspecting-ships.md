---
title: Robots Are Taking Over Ship Inspection — Here's the Engineering Behind It
date: 2026-10-11
category: news
tag: automation
summary: Gecko Robotics is bringing robotic inspection to Anduril's new submarine factory. A look at why inspection slows shipbuilding down, and how a thickness check actually works.
image: assets/2026-10-11-ut-thickness.svg
image_alt: Diagram of an ultrasonic probe measuring steel plate thickness from the echo time
image_credit: Diagram: Engine-X
sources:
- MarineLink — Gecko Robotics, Anduril to accelerate American shipbuilding (8 Oct 2026) | https://www.marinelink.com/news/gecko-robotics-anduril-accelerate-543578
- Ocean News — Gecko Robotics and Anduril partner to accelerate submarine production | https://oceannews.com/news/milestones/gecko-robotics-and-anduril-partner-to-accelerate-submarine-production/
- The Next Web — Gecko Robotics lands $71M Navy deal (Mar 2026) | https://thenextweb.com/news/gecko-robotics-navy-contract-ship-digital-twins
---
This week, inspection-robot company **Gecko Robotics** announced it is partnering with defence manufacturer **Anduril** to speed up US submarine production. Gecko's robots and software will be used at Anduril's new 160,000 sq ft factory in California, where key submarine components will be made. Anduril has tied the work to a $3.7 billion investment in Virginia-class submarine production, including a new shipyard in Maryland.

The headline number: on forged components for other defence customers, Gecko says its system has cut **inspection time by up to 90%**, and that workers with no prior non-destructive testing (NDT) experience can be productive after about an hour of training.

As someone who works in a dry dock, that second claim is the interesting one. Here's why.

## Why inspection is a bottleneck

Every critical steel part on a ship — plates, welds, forgings, tanks — has to be checked before it goes into service and again throughout its life. The checks are **non-destructive**: you test the part without cutting it open.

The problem isn't the physics. It's people and time:

- A large hull has thousands of square metres of plate and kilometres of weld.
- Manual inspection means an inspector, a hand probe and a grid drawn on the steel, point by point.
- Qualified NDT technicians take a long time to train and certify, and there aren't enough of them.

If inspection can't keep up with fabrication, the whole yard waits.

## How a thickness check actually works

The most common check on a hull is **ultrasonic thickness gauging** — and it's simple physics:

1. A probe (transducer) is placed on the steel with a gel or water film called *couplant* so the sound can get in.
2. It sends a very short, high-frequency sound pulse into the plate.
3. The pulse reflects off the far side (the "back wall") and returns to the probe.
4. The instrument times the round trip. Since sound travels through steel at roughly 5,900 m/s, **thickness = speed × time ÷ 2** (÷ 2 because the pulse goes there and back).

When corrosion eats the inside of a tank or the outside of the hull, the back wall moves closer. The echo comes back sooner, and the reading drops. Compare that to the original plate thickness and you know how much metal has been lost — and whether the plate needs renewing.

## What robots change

A robot doesn't change the physics. It changes **how much steel you can cover and how consistently**:

- **Coverage.** Instead of spot readings on a grid, a crawler can take continuous readings along a surface, so a small thin patch between grid points isn't missed.
- **Consistency.** The robot holds the probe at the same angle and pressure every time, which removes a lot of operator variation.
- **Data, not paper.** Every reading is stored with its exact location. Gecko feeds this into what it calls a "digital thread" that follows a part from manufacture through decades of service.
- **Planning repairs early.** In its US Navy work, Gecko builds digital models of a ship's structural condition so repairs can be planned and parts ordered *before* the ship arrives in dry dock.

That last point matters a lot in my world. A ship in dry dock is costing money every day. Knowing which plates need cutting out before the ship arrives saves days of opening up and measuring.

## The engineering takeaway

NDT is one of the least glamorous parts of building and maintaining ships, but it's often the slowest. Automating it doesn't replace the engineer's judgement — someone still has to decide what a thin reading means and how to repair it — but it turns inspection from a manual bottleneck into a data stream. For yards facing a shortage of skilled workers, that's the real story.
