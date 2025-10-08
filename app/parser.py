# Placeholder parser module.
def parse_raw_match(raw):
    return {
        'match_id': raw.get('id') if isinstance(raw, dict) else None,
        'teams': raw.get('teams') if isinstance(raw, dict) else None,
        'odds': raw.get('odds') if isinstance(raw, dict) else None,
    }
