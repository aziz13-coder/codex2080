# Backend Overview

This backend uses a central taxonomy defined in `taxonomy.py` to manage
question categories and their defaults. Modules such as
`question_analyzer`, `category_router` and the horary engine import the
`Category` enum instead of hard coded strings. Legacy string values are
still accepted but will emit a warning.
