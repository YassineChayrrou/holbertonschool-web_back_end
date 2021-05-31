# 0x0F. ES6_promise

JavaScript ES6 promises

## Resources:

**Read or watch:**

- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise" target="_blank">Promise</a>
- <a href="https://web.dev/promises/" target="_blank">JavaScript Promise: An introduction</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await" target="_blank">Await</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function" target="_blank">Async</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw" target="_blank">Throw / Try</a>


## Learning Objectives:

- Promises (how, why, and what)
- How to use the then, resolve, catch methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an async function

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
    - utils.js:
    ```
    export function uploadPhoto() {
      return Promise.resolve({
        status: 200,
        body: 'photo-profile-1',
      });
    }


    export function createUser() {
      return Promise.resolve({
        firstName: 'Guillaume',
        lastName: 'Salva',
      });
    }
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
