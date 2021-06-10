export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  static displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
