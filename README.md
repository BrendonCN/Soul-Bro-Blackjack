# Soul-Bro-Blackjack
A idea game come from my cousin

# Background:
The player and his friends should act as adventurers in another world, each player with a unique class (Fighter, Mage, Archer, Rogue). The story happens after you defeat the Demon King; the Demon King's body has been destroyed, but his soul has not. Now he spoke to the players, turning the players' souls into chips(soul chips) and shuffling them. Only players with a complete soul can defeat the Demon King's soul, and to achieve that, players have to gamble with Demon Kings to win back their souls.

# Core Rules:
4 players start with equal soul chips (e.g., 10 each). Standard deck (52 cards, but suits are irrelevant; only ranks A-K matter for specials). No jokers.

# Gameplay Loop:
- Rotate Demon King role each round.
- Demon King deals cards: Themselves (one up, one down) and players (two up).
- Players bet soul chips (min 1, max half their stack).
- Standard blackjack: Hit/Stand, aim for 21 without busting. Aces = 1 or 11.
- Twist: Drawing a card triggers its rank's special event (only once per draw, player's choice to activate).
- Demon King wins ties. If Demon King wins, they take bets as soul chips. If players win, they gain soul chips from Demon King.
- Special events can steal soul chips directly or alter hands.

# Winning:
- Collect all soul chips to "complete your soul" and defeat the Demon King permanently.

# Goal:
Each round, each player will take turns to play the role of the Demon King. The Demon King is trying to win all non-Demon King players collect their 'soul chips'; the adventurers have to collect all their own 'soul chips'.

# Features: 
Blackjack, 13 poker cards excluding type[spades: ♠️, hearts: ♥️, diamonds: ♦️, clubs: ♣️] each have a special event(e.g., A can D20 with the current Demon King, the largest number wins, the winner can take one 'soul chips' from the loser.)

# Requirements:
  - The UI should be colorful and cartoonish, the actwork should be close to an adventure in another world, with One-handed operation(The player can peek at their own hand by turning over a corner of the card).
  - The characters should look cartoonish, cute, have a three-headed body and be fun to watch.
  - Multiplayer: Local multiplayer (pass-and-play) for mobile, or online if expanded.(4-player for now).
  - One-Handed UI: Swipe to peek (drag corner to reveal card), tap to hit/stand/bet.

# Remark (Card Event):
- A (Ace of Souls): Roll a D20 with the current Demon King, the largest number wins, winner can take one soul chip from the loser.
- A（靈魂的王牌）：與目前的惡魔王一起滾動D20，贏得了最多的勝利，獲勝者可以從失敗者那裡獲得一個靈魂籌碼。

- 2 (Duo of Destiny): Summon a magical pistol. Roll a D20; if 10 or higher, hit the Demon King and take one soul chip.
- 2（命運二人組）：召喚一隻神奇的手槍。滾動D20；如果10歲或更高，請擊中惡魔之王，然後拿一個靈魂籌碼。

- 3 (Triad of Thorns): Summon entangling plants. Roll a D20; if 12 or higher, bind the Demon King, forcing them to stand on their current hand, and take one soul chip if you win the round.
- 3（荊棘三合會）：召喚糾纏植物。滾動D20；如果12歲或更高，請綁定惡魔之王，強迫他們站在他們目前的手上，如果您贏得了一輪，則拿起一個靈魂芯片。
  
- 4 (Quartet of Winds): Manipulate winds to reshuffle. Replace one card in your hand with the top card from the deck.
- 4（風四重奏）：操縱風以改組。用甲板上的頂部卡中的一張卡片中的一張卡片替換。

- 5 (Pentad of Renewal): Burn inner energy to heal. If your hand busts, roll a D20; if 15 or higher, treat the bust as 20 instead.
- 5（更新的重音）：燃燒內部能量以治愈。如果您的手摔傷，請滾動D20；如果15或更高，則將胸圍視為20。

- 6 (Hex of Tides): Manipulate water to flood. Force the Demon King to draw an extra card, potentially causing them to bust.
- 6（潮汐十六進制）：操縱水氾濫。強迫惡魔王畫一張額外的卡，有可能導致他們破產。

- 7 (Sept of Shadows): Become invisible like a chameleon. Peek at the Demon King's hole card without them knowing.
- 7（陰影9月）：像變色龍一樣變得隱形。窺視惡魔國王的孔卡，不知道。

- 8 (Octad of Explosions): Summon an explosive trap. Choose a player (including Demon King); if their hand is 17 or less, force them to hit again.
- 8（爆炸的ictad）：召喚一個爆炸性陷阱。選擇一個球員（包括惡魔王）；如果他們的手是17歲以下的，請迫使他們再次擊中。

- 9 (Ennead of Insight): Enhance your genius. Calculate and know the exact probability of busting if you hit.
- 9（洞察力）：增強您的天才。計算並知道擊打的確切可能性。

- 10 (Decade of Senses): Heighten your senses. Peek at the next card in the deck before deciding your action.
- 10（感官十年）：增強感官。在決定您的動作之前，請窺視甲板上的下一張卡片。

- J (Jack of Tricks): Fly like a sky dancer. If you would lose the round, roll a D20; if 16 or higher, evade the loss and keep your bet.
- J（傑克的傑克）：像天空舞者一樣飛。如果您會輸掉這一回合，請滾動D20；如果16歲或更高，請逃避損失並保持下注。

- Q (Queen of Velocity): Move at sonic speeds. Take an extra hit without the risk of busting (if over 21, subtract 10).
- Q（速度女王）：以聲音速度移動。額外的打擊而沒有破壞風險（如果超過21，則減去10）。

- K (King of Might): Enhance physical prowess. Add 5 to your hand total for this round (cannot exceed 21).
- K（可能的國王）：增強身體能力。在這一輪中加5（不能超過21）。
