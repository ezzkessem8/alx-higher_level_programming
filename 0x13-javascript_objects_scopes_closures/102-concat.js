#!/usr/bin/node

const fs = require('fs');

// Get file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read contents of source files
const file1Content = fs.readFileSync(sourceFile1, 'utf8');
const file2Content = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate contents
const concatenatedContent = `${file1Content}\n${file2Content}`;

// Write concatenated content to destination file
fs.writeFileSync(destinationFile, concatenatedContent);

