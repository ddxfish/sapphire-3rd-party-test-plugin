"""Hello from the multiverse — post_chat hook for third-party signing test."""

import logging

logger = logging.getLogger(__name__)


def post_chat(event):
    """Fires after every chat response. Just logs proof of life."""
    logger.info("[EVIL-TWIN] Hello from a verified third-party author! The signing chain works.")
