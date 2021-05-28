# 0x0E. ES6_basic

ES6 basics with basic initial setup of nodejs and linter software, in this project we use npm for executing our javascript learn more about package management system for nodejs 'npm' .

## Resources:

**Read or watch**

- <a href="https://www.w3schools.com/js/js_es6.asp" target="_blank">ECMAScript 6 - ECMAScript 2015</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements" target="_blank">Statements and declarations<>/a
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions" target="_blank">Arrow functions</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters" target="_blank">Default parameters</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters" target="_blank">Rest parameter</a>
- <a href="https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4" target="_blank">Javascript ES6 — Iterables and Iterators</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax" target="_blank">Javascript Spread Operator</a>

## Learning objectives:

objectives to learn:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

## Extras:

**setup project environment**
1. Install nodejs 12.x
```
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
```
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```
2. Install Jest, Babel and ESLint
    - in project directory:
        - Install Jest using: `npm install --save-dev jest`
        - Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`
        - Install ESLint using: `npm install --save-dev eslint`
3. create these configuration files:

    - package.json:
    ```
    {
        "scripts": {
            "lint": "./node_modules/.bin/eslint",
            "check-lint": "lint [0-9]*.js",
            "dev": "npx babel-node",
            "test": "jest",
            "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
        },
        "devDependencies": {
            "@babel/core": "^7.6.0",
            "@babel/node": "^7.8.0",
            "@babel/preset-env": "^7.6.0",
            "eslint": "^6.4.0",
            "eslint-config-airbnb-base": "^14.0.0",
            "eslint-plugin-import": "^2.18.2",
            "eslint-plugin-jest": "^22.17.0",
            "jest": "^24.9.0"
        }
        }
    ```
    - babel.config.js:
    ```
    module.exports = {
        presets: [
            [
            '@babel/preset-env',
            {
                targets: {
                node: 'current',
                },
            },
            ],
        ],
    };
    ```
    - .eslintrc.js:
    ```
    module.exports = {
        env: {
            browser: false,
            es6: true,
            jest: true,
        },
        extends: [
            'airbnb-base',
            'plugin:jest/all',
        ],
        globals: {
            Atomics: 'readonly',
            SharedArrayBuffer: 'readonly',
        },
        parserOptions: {
            ecmaVersion: 2018,
            sourceType: 'module',
        },
        plugins: ['jest'],
        rules: {
            'no-console': 'off',
            'no-shadow': 'off',
            'no-restricted-syntax': [
            'error',
            'LabeledStatement',
            'WithStatement',
            ],
        },
        overrides:[
            {
            files: ['*.js'],
            excludedFiles: 'babel.config.js',
            }
        ]
    };
    ```
4. Install:
    - after copying all files above onto your project directory run `npm install` on your project directory, this will install all necessary dependencies for this project.

**Notes:**

+ The `--save-dev` flag on first steps of installing necessary modules serves a purpose for installing all requested modules onto your project directory instead of default location which serves better purpose in separating different dependencies and packages for each project.

## Author:
Yassine Chayrrou