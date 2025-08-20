import assert from 'assert';
import { parseReasoningEntry } from '../src/utils/parseReasoning.mjs';

function test(name, fn) {
  try {
    fn();
    console.log(`\u2714\ufe0f ${name}`);
  } catch (err) {
    console.error(`\u274c ${name}`);
    console.error(err);
    process.exitCode = 1;
  }
}

test('parses negative percentages', () => {
  const { rule, weight } = parseReasoningEntry('Loss of power -5%');
  assert.strictEqual(weight, -5);
  assert.strictEqual(rule, 'Loss of power');
});

test('parses trailing unsigned parenthetical', () => {
  const { rule, weight } = parseReasoningEntry('Good fortune (12)');
  assert.strictEqual(weight, 12);
  assert.strictEqual(rule, 'Good fortune');
});

test('uses last numeric token when multiple present', () => {
  const { rule, weight } = parseReasoningEntry('Mixed signals (+3) (-4)');
  assert.strictEqual(weight, -4);
  assert.strictEqual(rule, 'Mixed signals (+3)');
});
