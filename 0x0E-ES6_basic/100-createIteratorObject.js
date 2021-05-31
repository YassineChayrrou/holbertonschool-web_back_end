export default function createIteratorObject(report) {
  let arr = [];
  for (const elem of Object.values(report.allEmployees)) {
    arr = [...arr, ...elem];
  }
  return arr;
}
