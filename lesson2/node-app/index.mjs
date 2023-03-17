import fs from 'fs'

fs.appendFile('my-file', 'Файл создан Node.js', (err) => {
    if (err) throw err
    console.log('Файл сохранён')
});