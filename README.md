# Bowling Game Kata

A game of bowling has 10 rounds or frames. During each frame, a player is given 2 opportunities to knock down all 10 pins. The score for the frame is the number of pins knocked down in addition to any bonuses for *strikes* and *spares*.

- **Spare**: a player knocked down all 10 pins in the 2 tries given during the frame (*roll 1 can be 5 pins knocked down and the 2nd roll can be the 5 remaining pins*).
  - **Spare Bonus**: the number of pins knocked down in the frame after the spare was scored.
- **Strike**: a player knocks down all 10 pins on the first roll in a frame.
  - **Strike Bonus**: The number of pins knocked down in the subsequent 2 rolls.

During the last frame (the 10th round), if a player rolls a spare or a strike, the player is then allowed to roll up to 3 balls to complete the frame.