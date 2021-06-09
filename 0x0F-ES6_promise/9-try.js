export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const value = mathFunction();
    queue.push(value, 'Guardrail was processed');
  } catch (err) {
    queue.push(`Error: ${error.message}`, 'Guardrail was processed');
  }
  return queue;
}
