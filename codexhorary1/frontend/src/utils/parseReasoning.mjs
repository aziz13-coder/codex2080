export function parseReasoningEntry(text) {
  if (typeof text !== 'string') {
    return { rule: '', weight: 0 };
  }
  const matches = [...text.matchAll(/[-+]?\d+%?/g)];
  if (matches.length === 0) {
    return { rule: text.trim(), weight: 0 };
  }
  const last = matches[matches.length - 1];
  const token = last[0];
  let weight = parseInt(token, 10) || 0;
  let start = last.index;
  let end = start + token.length;

  let before = text.slice(0, start);
  let after = text.slice(end);

  const beforeParen = before.match(/\(\s*$/);
  const afterParen = after.match(/^\s*\)/);
  if (beforeParen && afterParen) {
    start -= beforeParen[0].length;
    end += afterParen[0].length;
    before = text.slice(0, start);
    after = text.slice(end);
  }

  before = before.replace(/\s+$/, '');
  after = after.replace(/^\s+/, '');
  const rule = `${before}${before && after ? ' ' : ''}${after}`.trim();
  return { rule, weight };
}
