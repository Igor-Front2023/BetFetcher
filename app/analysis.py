# Placeholder analysis module.
def evaluate_match(normalized_match):
    odds = normalized_match.get('odds') or {}
    try:
        inv = {k: (1.0/float(v) if v else 0.0) for k,v in odds.items()}
        s = sum(inv.values()) or 1e-9
        norm = {k: (v/s)*100.0 for k,v in inv.items()}
        best = max(norm.items(), key=lambda kv: kv[1])
        return {'pass': 75.0 <= best[1] <= 95.0, 'best_outcome': best[0], 'prob': best[1], 'norm': norm}
    except Exception:
        return {'pass': False}
