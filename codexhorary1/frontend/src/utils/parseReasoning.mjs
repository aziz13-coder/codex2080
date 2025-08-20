export function parseReasoningEntry(text) {
  if (typeof text !== 'string') {
    return { rule: '', weight: 0 };
  }
  const parenMatch = text.match(/\(([-+]?\d+)\s*%?\)\s*$/);
  if (parenMatch) {
    return { rule: text.slice(0, parenMatch.index).trim(), weight: parseInt(parenMatch[1], 10) || 0 };
  }
  const signedMatch = text.match(/([-+]\d+)\s*%?\s*$/);
  if (signedMatch) {
    return { rule: text.slice(0, signedMatch.index).trim(), weight: parseInt(signedMatch[1], 10) || 0 };
  }
  return { rule: text.trim(), weight: 0 };
}
