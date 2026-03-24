const fs = require('fs');
const path = require('path');

const dir = 'e:\\\\Insurance Websites';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const addressesToReplace = [
    // Matches the standard footer address
    {
        regex: /Headquarters,\s*Suite 500\s*<br>\s*123 Business Rd,\s*Suite 100,?\s*/g,
        replacement: '4421 Broadway Industrial Park<br>Apt 821 Detroit 99045'
    },
    // Matches the inline privacy policy address
    {
        regex: /123 Business Rd,\s*Suite 100\s*<br>\s*/g,
        replacement: '4421 Broadway Industrial Park, Apt 821, Detroit 99045<br>'
    }
];

for (const file of files) {
    const filepath = path.join(dir, file);
    let content = fs.readFileSync(filepath, 'utf8');

    for (const rule of addressesToReplace) {
        content = content.replace(rule.regex, rule.replacement);
    }

    fs.writeFileSync(filepath, content, 'utf8');
}

console.log(`Successfully processed ${files.length} HTML files and updated the address.`);
