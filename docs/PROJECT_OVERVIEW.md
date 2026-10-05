# Project Overview

## Problem

The project explores how structured social-network data can be cleaned and used for simple recommendation tasks.

## Data Model

Each user contains:
- `id`
- `name`
- `friends`
- `liked_pages`

Each page contains:
- `id`
- `name`

## Recommendation Logic

### People You May Know
The implementation uses a friends-of-friends approach and ranks candidates by the number of mutual connections.

### Pages You Might Like
The implementation compares liked-page sets across users and assigns a score based on shared interests.

## Data Quality Examples

The intentionally messy dataset includes examples such as:
- A missing user name
- Duplicate friend IDs
- Duplicate page IDs
- A user with no friends and no liked pages

The cleaning notebook addresses these issues before recommendation analysis.

## Important Note

This is a **rule-based recommendation project**, not a machine-learning model. It is best presented as a Python data-processing and recommendation-logic project.
