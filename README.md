[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Kf5HLjuv)

# Ping-Pong Game

A classic two-player pong game built with Python and Pygame.

## Features

- **Game Environment**: Playing field, two paddles, and a ball
- **Player Input**: Player 1 (W/S), Player 2 (↑/↓) to move paddles
- **Ball Physics**: Bounces off walls and paddles with angle-based deflection
- **Score Keeping**: First to 5 points wins

## Setup

```bash
cd ping-pong
pip install -r requirements.txt
```

## Run

```bash
python pong.py
```

## Controls

| Player   | Up      | Down    |
|----------|---------|---------|
| Player 1 | W       | S       |
| Player 2 | ↑ (Up)  | ↓ (Down)|

## Configuration

Edit constants at the top of `pong.py` to customize:

- `WIDTH`, `HEIGHT` – Window size
- `PADDLE_SPEED` – Paddle movement speed
- `BALL_SPEED_INITIAL` – Starting ball speed
- `WINNING_SCORE` – Points needed to win (default: 5)
