---
title: Robots Are Taking Over Ship Inspection — Here's the Engineering Behind It
date: 2026-10-11
category: news
tag: automation
summary: Gecko Robotics is bringing robotic inspection to Anduril's new submarine factory. A look at why inspection slows shipbuilding down, and how a thickness check actually works.
seo_title: Robotic Ship Inspection: The Engineering Behind It
seo_description: Why inspection slows shipbuilding, how robots like Gecko's measure hull thickness, and what it means for submarine and ship factories.
image: assets/2026-10-11-ut-thickness.svg
image_alt: Diagram of an ultrasonic probe measuring steel plate thickness from the echo time
image_credit: Diagram: Engine-X
keywords: ship inspection robots, ultrasonic thickness gauging, non-destructive testing, NDT, dry dock
tldr: Inspection robots use the same ultrasonic physics as a hand probe, but they cover far more steel, more consistently, and turn hull inspection into data that helps plan dry-dock repairs early.
takeaways:
- Inspection is a bottleneck because hulls have huge areas of plate and weld, and qualified NDT technicians are scarce.
- Ultrasonic thickness gauging times a sound echo: thickness = speed of sound × time ÷ 2.
- Robots don't change the physics; they add continuous coverage, consistent probe contact and located data.
- Knowing which plates need renewal before a ship arrives saves days in dry dock.
faq:
- How does ultrasonic thickness gauging work? | A probe sends a short sound pulse into the steel, times the echo from the far side, and calculates thickness as speed of sound × time ÷ 2.
- Do inspection robots replace NDT engineers? | No. Robots collect more consistent data, but an engineer still decides what a thin reading means and how to repair it.
- Why does early inspection data matter for dry docking? | A ship in dry dock costs money every day, so knowing which plates need cutting out before it arrives avoids days of opening up and measuring.
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
