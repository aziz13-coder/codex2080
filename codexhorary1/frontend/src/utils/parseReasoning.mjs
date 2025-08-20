export function parseReasoningEntry(text) {
  if (typeof text !== 'string') {
    return { rule: '', weight: 0 };
  }

  // Match a trailing weight in parentheses, e.g. (12) or (-5%)
  const parenMatch = text.match(/\(([+-]?\d+%?)\)\s*$/);
  if (parenMatch) {
    const weight = parseInt(parenMatch[1], 10) || 0;
    const rule = text.slice(0, parenMatch.index).trim();
    return { rule, weight };
  }

  // Match a trailing signed weight token, e.g. +3 or -5%
  const tokenMatch = text.match(/([+-]\d+%?)\s*$/);
  if (tokenMatch) {
    const weight = parseInt(tokenMatch[1], 10) || 0;
    const rule = text.slice(0, tokenMatch.index).trim();
    return { rule, weight };
  }

  return { rule: text.trim(), weight: 0 };
}
