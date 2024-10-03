'use strict';
import data from './x.json' assert { type: 'json' };
import { writeFile } from 'fs/promises';
//Важно указывать тип и не забывай указывать type="module" при подключении скрипта
let product_obj = Object.values(data);
//const codes = product_obj.map(product_obj => parseInt(product_obj['Код товара'])); // числовые значения кодов
const codesString = product_obj.map(obj => `${obj['Код товара']}`).join('","');
// Если надо вывести результат в консоль
// console.log(codesString);

// Если надо в отдельный файл завернуть создаем объект для записи в файл
const outputData = { codes: codesString }; // Если вы хотите сохранить как строку, оберните в объект
// Записываем результат в output.json
writeFile('output.json', JSON.stringify(outputData, null, 2))
    .then(() => {
        console.log('Файл output.json успешно создан!');
    })
    .catch((error) => {
        console.error('Ошибка при записи в файл:', error);
    });
