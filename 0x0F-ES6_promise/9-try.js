export default function guardrail(mathFunction) {
  const  queue = [];
  let res;
  try {
    res = mathFunction();
  } catch (err) {
    res = err.toString();
  }
  queue.push(res, 'Guardrail was processed')
  return queue;
}
