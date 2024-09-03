const { Readability } = require('@mozilla/readability');
const { JSDOM } = require('jsdom');
const fetch = require('node-fetch');

async function extractContent(url, headers) {
    try {
        const response = await fetch(url, { headers });
        const html = await response.text();
        const doc = new JSDOM(html, { url });
        const reader = new Readability(doc.window.document);
        const article = reader.parse();
        
        return JSON.stringify({
            title: article.title,
            content: article.content,
            textContent: article.textContent,
            length: article.length,
            excerpt: article.excerpt
        });
    } catch (error) {
        return JSON.stringify({ error: error.message });
    }
}

const url = process.argv[2];
const headersJson = process.argv[3];

let headers = {};
if (headersJson) {
    try {
        headers = JSON.parse(headersJson);
    } catch (error) {
        console.error('Error parsing headers JSON:', error.message);
    }
}

extractContent(url, headers).then(result => console.log(result));