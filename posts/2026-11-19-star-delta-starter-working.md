---
title: How a Star-Delta Starter Works, and Why It Cuts Starting Current to a Third
date: 2026-11-19
category: learn
summary: A star-delta starter runs a motor up in star, at 58 % of the voltage, then switches to delta. Worked through on a 7.5 kW 4-pole motor: starting current falls from 93 A to 31 A, but starting torque falls by the same third.
seo_title: How a Star-Delta Starter Works: Current, Torque, Timer
seo_description: A star-delta starter cuts starting current and torque to one third. Worked example on a 7.5 kW motor, with timer and overload relay settings.
image: assets/2026-11-19-star-delta-starter.svg
image_alt: Diagram comparing star and delta connection of a 7.5 kW 400 V motor: in star each winding gets 230 V and the motor starts at 31 A and 36 Nm, in delta each winding gets 400 V and a direct start would take 93 A and 109 Nm
image_credit: Diagram: Engine-X
model: inductionmotor
keywords: star delta starter working, why star delta starter is used, star delta starting current, star delta timer setting, star delta overload relay setting
tldr: A star-delta starter starts the motor in star, so each winding gets 1/√3 of the line voltage and the motor draws a third of the direct-on-line current and torque, then switches to delta once the motor is near full speed.
takeaways:
- In star each winding gets 400 ÷ √3 = 230 V; in delta it gets the full 400 V.
- Starting current and starting torque both fall to about one third of a direct start.
- The motor must be rated for delta at the supply voltage (400 V Δ / 690 V Y on a 400 V supply) and have six terminals.
- Switch to delta at about 75–80 % of full speed, usually a timer of a few seconds.
- An overload relay in the delta loop is set to 0.58 × full-load current.
faq:
- Why is a star-delta starter used? | To cut the starting current. A direct-on-line start draws six to nine times full-load current, which dips the supply voltage. Starting in star cuts that to about a third, so a 7.5 kW motor starts at about 31 A instead of 93 A.
- What is the disadvantage of a star-delta starter? | Starting torque drops to a third as well, so the motor may not start a load that needs high torque from standstill. The switch to delta can also cause a short current and torque spike if the motor slows down during the change-over.
- What should the star-delta timer be set to? | Long enough for the motor to reach about 75–80 % of full speed before it changes to delta. For small pumps and fans this is often only a few seconds; check the motor and pump maker's limit, as some pump makers allow no more than 3 seconds in star.
- What is the overload relay setting in a star-delta starter? | When the relay sits in the motor lines, inside the delta loop, it carries the phase current, so set it to 0.58 × the motor's full-load current. For a 14.26 A motor that is about 8.3 A. A relay in the supply cable is set to the full-load current.
- Can any motor be started in star-delta? | No. It must be wound to run in delta at the supply voltage, with all six winding ends brought out to the terminal box. On a 400 V supply that means a motor marked 400 V Δ / 690 V Y.
sources:
- Bitzer — Star-delta start (Y/Δ) | https://www.bitzer.de/shared_media/html/at-330/en-GB/387365259387367051.html
- AuCom — Get your motor running: motor starting solutions | https://www.aucom.com/hubfs/Published%20Content/Get%20Your%20Motor%20Running/Whitepaper_3/GYMR_Motor_Starting_Solutions.pdf
- EEPower — Motor starters part 3: pros and cons of the star-delta configuration | https://eepower.com/technical-articles/motor-starters-part-3-pros-and-cons-of-the-star-delta-configuration/
- Schneider Electric — Overload selection on star-delta starters | https://www.se.com/uk/en/faqs/FA136856/
- Wilo — Star-delta activation | https://cms.media.wilo.com/dcianimpfinder/wilo532894/6520765/Flumen%20Excel%20Opti%2020-40/en-GB/114271499.html
- SEVA — MX3-132M1-4 7.5 kW 4-pole motor data sheet | https://www.seva-tec.de/media/pdf/91/f5/d7/SEVA-Datenblatt-MX3-132M1-4-7-5KW-4-polig-Bauform-B35-Drehstrommotor.pdf
- Engine-X — Induction motor 3D model | https://engx3d.com/3d-models/induction-motor
---
A star-delta starter starts a three-phase motor with its windings in star, so each winding gets only 58 % of the line voltage. That cuts the starting current and the starting torque to about a third. Once the motor is near full speed, a timer switches the windings to delta and the motor runs at full voltage.

The numbers below use the 7.5 kW 4-pole motor in the [Engine-X induction motor 3D model](https://engx3d.com/3d-models/induction-motor), the same one as in [how to read a motor nameplate](https://engx3d.com/blog/posts/2026-11-14-how-to-read-a-motor-nameplate.html). The [induction motor guide](https://engx3d.com/induction-motor) explains the stator, rotor cage and slip part by part.

## Why not just switch the motor straight on?

Because a motor at standstill draws a huge current. A direct-on-line (DOL) start typically takes 600 to 900 % of full-load current ([AuCom](https://www.aucom.com/hubfs/Published%20Content/Get%20Your%20Motor%20Running/Whitepaper_3/GYMR_Motor_Starting_Solutions.pdf)). On a weak supply, a generator or a long cable, that dips the voltage for everything else on the same board.

Our motor's data sheet gives 14.26 A full-load current and a starting current of 6.5 times that ([SEVA](https://www.seva-tec.de/media/pdf/91/f5/d7/SEVA-Datenblatt-MX3-132M1-4-7-5KW-4-polig-Bauform-B35-Drehstrommotor.pdf)):

**DOL starting current = 6.5 × 14.26 = 93 A**

## How does starting in star reduce the current?

In star, each winding sits between one line and the star point, so it gets the line voltage divided by √3. In delta, each winding sits between two lines and gets the full line voltage ([EEPower](https://eepower.com/technical-articles/motor-starters-part-3-pros-and-cons-of-the-star-delta-configuration/)). On a 400 V supply:

- **Star:** 400 ÷ √3 = **230 V** per winding
- **Delta:** **400 V** per winding

With 1/√3 of the voltage, each winding draws 1/√3 of the current. In delta the line current is also √3 times the winding current, while in star the two are the same. The two factors multiply, so the line current in star is one third of a direct start in delta ([Bitzer](https://www.bitzer.de/shared_media/html/at-330/en-GB/387365259387367051.html)):

**Star starting current ≈ 93 ÷ 3 = 31 A**

## What is the catch?

Torque. A motor's torque goes with the square of the voltage, so at 1/√3 of the voltage it falls to (1/√3)² = one third as well ([Bitzer](https://www.bitzer.de/shared_media/html/at-330/en-GB/387365259387367051.html)). The data sheet gives 49.4 Nm rated torque and a starting torque of 2.2 times that ([SEVA](https://www.seva-tec.de/media/pdf/91/f5/d7/SEVA-Datenblatt-MX3-132M1-4-7-5KW-4-polig-Bauform-B35-Drehstrommotor.pdf)):

| | Direct-on-line (delta) | Star-delta (in star) |
|---|---|---|
| Voltage per winding | 400 V | 230 V |
| Starting current | 93 A | 31 A |
| Starting torque | 109 Nm | 36 Nm |
| Torque vs rated 49.4 Nm | 2.2 × | 0.73 × |

In star the motor gives less than its rated torque at standstill. That is fine for a centrifugal pump or a fan, which need little torque until they speed up. It is not fine for a loaded conveyor, a crusher or a compressor starting against pressure; Bitzer notes that the load torque in star must stay under a third of the DOL torque, so compressors are usually started unloaded.

## Which motors can be started in star-delta?

The motor must run in delta at the supply voltage, and all six winding ends (U1, V1, W1, U2, V2, W2) must come out to the terminal box ([Bitzer](https://www.bitzer.de/shared_media/html/at-330/en-GB/387365259387367051.html), [EEPower](https://eepower.com/technical-articles/motor-starters-part-3-pros-and-cons-of-the-star-delta-configuration/)).

On a 400 V supply that means a nameplate marked **400 V Δ / 690 V Y**. A motor marked 230 V Δ / 400 V Y already runs in star on 400 V, so it cannot be started in star-delta there: switching it to delta would put 400 V on windings made for 230 V.

## How the starter switches over

A star-delta starter has three contactors, a timer and an overload relay:

1. **Main and star contactors close.** The motor starts in star at a third of the DOL current.
2. **The timer runs** while the motor speeds up. It should change over at about 75–80 % of full speed ([Bitzer](https://www.bitzer.de/shared_media/html/at-330/en-GB/387365259387367051.html)), about 1,150 rpm on this 4-pole motor.
3. **The star contactor opens.** The motor is off the supply for a moment, so the delta contactor cannot close while star is still in. This is called an open transition.
4. **The delta contactor closes.** The motor now runs at full voltage and full torque.

On small pumps the time in star is short. Wilo allows no more than 3 seconds in star for its Flumen pumps ([Wilo](https://cms.media.wilo.com/dcianimpfinder/wilo532894/6520765/Flumen%20Excel%20Opti%2020-40/en-GB/114271499.html)). Larger, heavier loads take longer, so follow the maker's figure.

## Why the change-over can still kick

In the short gap between star and delta the motor slows down a little, and its spinning rotor keeps a voltage of its own in the windings. If delta closes when that voltage is out of step with the supply, AuCom puts the spike at up to 200 % of the locked-rotor current and 400 % of the locked-rotor torque ([AuCom](https://www.aucom.com/hubfs/Published%20Content/Get%20Your%20Motor%20Running/Whitepaper_3/GYMR_Motor_Starting_Solutions.pdf)).

So a timer set too short, changing over before the motor is near speed, throws away most of the benefit. Closed-transition starters bridge the gap with resistors, but AuCom notes they are rarely used. Where a soft start matters more, a soft starter or a VFD is the usual answer.

## Setting the overload relay

The overload relay usually sits in the motor lines, after the main contactor, inside the delta loop. There it carries the winding current, not the line current, which is 1/√3 = 0.58 of it. Schneider's rule is to set it to **full-load current × 0.58** ([Schneider Electric](https://www.se.com/uk/en/faqs/FA136856/)):

**Overload setting = 14.26 × 0.58 ≈ 8.3 A**

If the relay is in the supply cable before the starter instead, set it to the full 14.26 A ([Wilo](https://cms.media.wilo.com/dcianimpfinder/wilo532894/6520765/Flumen%20Excel%20Opti%2020-40/en-GB/114271499.html)). Setting 14.26 A on a relay in the delta loop is a common mistake, and it leaves the motor almost unprotected.

## The engineering takeaway

Star-delta trades torque for current: a third of the current, a third of the torque. It suits pumps and fans that start light, needs a 400 V Δ motor with six terminals on a 400 V supply, and works only if the timer lets the motor reach near full speed before the change-over.
