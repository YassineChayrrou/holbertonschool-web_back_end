export default function createReportObject(employeesList) {
  const emp = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return emp;
}
