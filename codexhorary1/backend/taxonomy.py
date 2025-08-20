from __future__ import annotations

import logging
from enum import Enum
from typing import Any, Dict, Optional

try:
    from .models import Planet
except ImportError:  # pragma: no cover - fallback when executed as script
    from models import Planet

logger = logging.getLogger(__name__)


class Category(str, Enum):
    """Central taxonomy of question categories."""

    GENERAL = "general"
    LOST_OBJECT = "lost_object"
    MARRIAGE = "marriage"
    PREGNANCY = "pregnancy"
    CHILDREN = "children"
    TRAVEL = "travel"
    GAMBLING = "gambling"
    FUNDING = "funding"
    MONEY = "money"
    CAREER = "career"
    HEALTH = "health"
    LAWSUIT = "lawsuit"
    RELATIONSHIP = "relationship"
    EDUCATION = "education"
    PARENT = "parent"
    SIBLING = "sibling"
    FRIEND_ENEMY = "friend_enemy"
    PROPERTY = "property"
    DEATH = "death"
    SPIRITUAL = "spiritual"

    # Possession sub‑categories
    VEHICLE = "vehicle"
    PRECIOUS = "precious"
    TECHNOLOGY = "technology"
    LIVESTOCK = "livestock"
    MARITIME = "maritime"


CATEGORY_DEFAULTS: Dict[Category, Dict[str, Any]] = {
    Category.GENERAL: {"houses": [1, 7], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.LOST_OBJECT: {"houses": [1, 2], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.MARRIAGE: {
        "houses": [1, 7],
        "significators": {"venus": "natural significator of love", "mars": "natural significator of men"},
        "natural_significators": {},
        "contract": {},
    },
    Category.PREGNANCY: {"houses": [1, 5], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.CHILDREN: {"houses": [1, 5], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.TRAVEL: {
        "houses": [1, 3, 6],
        "significators": {"mercury": "short journeys", "jupiter": "long journeys and foreign travel"},
        "natural_significators": {},
        "contract": {},
    },
    Category.GAMBLING: {
        "houses": [1, 5],
        "significators": {
            "jupiter": "natural significator of fortune and luck",
            "venus": "natural significator of pleasure and enjoyment",
        },
        "natural_significators": {},
        "contract": {},
    },
    Category.FUNDING: {
        "houses": [1, 2, 8],
        "significators": {
            "jupiter": "natural significator of abundance and investors",
            "venus": "natural significator of attraction and partnerships",
            "mercury": "natural significator of contracts and negotiations",
        },
        "natural_significators": {},
        "contract": {},
    },
    Category.MONEY: {
        "houses": [1, 2],
        "significators": {"jupiter": "greater fortune", "venus": "lesser fortune"},
        "natural_significators": {
            Category.VEHICLE: Planet.SUN,
            Category.PROPERTY: Planet.MOON,
            Category.PRECIOUS: Planet.VENUS,
            Category.TECHNOLOGY: Planet.MERCURY,
            Category.LIVESTOCK: Planet.MARS,
            Category.MARITIME: Planet.MOON,
        },
        "contract": {},
    },
    Category.CAREER: {
        "houses": [1, 10],
        "significators": {"sun": "honor and reputation", "jupiter": "success"},
        "natural_significators": {},
        "contract": {},
    },
    Category.HEALTH: {
        "houses": [1, 6],
        "significators": {"mars": "fever and inflammation", "saturn": "chronic illness"},
        "natural_significators": {},
        "contract": {},
    },
    Category.LAWSUIT: {"houses": [1, 7], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.RELATIONSHIP: {"houses": [1, 7], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.EDUCATION: {
        "houses": [1, 10, 9],
        "significators": {"mercury": "natural significator of learning and knowledge", "jupiter": "wisdom and higher learning"},
        "natural_significators": {},
        "contract": {"examiner": Planet.SUN},
    },
    Category.PARENT: {"houses": [1, 4], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.SIBLING: {"houses": [1, 3], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.FRIEND_ENEMY: {"houses": [1, 11], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.PROPERTY: {"houses": [1, 4], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.DEATH: {"houses": [1, 8], "significators": {}, "natural_significators": {}, "contract": {}},
    Category.SPIRITUAL: {"houses": [1, 9], "significators": {}, "natural_significators": {}, "contract": {}},
}


def resolve_category(value: Optional[str | Category]) -> Optional[Category]:
    """Resolve a category value to :class:`Category`.

    Accepts either a :class:`Category` instance or its string value. When a
    legacy string is provided, a deprecation warning is logged.
    """

    if value is None or value == "":
        return None
    if isinstance(value, Category):
        return value
    try:
        cat = Category(value)
    except ValueError as exc:  # pragma: no cover - defensive
        logger.warning("Unknown category '%s'", value)
        raise exc
    logger.warning("Legacy category string '%s' used; prefer Category.%s", value, cat.name)
    return cat


def get_defaults(category: str | Category) -> Dict[str, Any]:
    cat = resolve_category(category)
    return CATEGORY_DEFAULTS.get(cat, {})
